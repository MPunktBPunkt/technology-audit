"""Scan a technology-audit (native) or foreign (bootstrap) repository."""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .util import (
    VALID_COVERAGE,
    VALID_STATUS,
    extract_yaml_blocks,
    is_native,
    parse_md_tables,
    read_text,
    slugify_repo_name,
)


@dataclass
class Finding:
    level: str  # error | warning | info
    code: str
    message: str
    path: str = ""


@dataclass
class InventoryItem:
    slug: str
    name: str = ""
    primary: str = ""
    tags: str = ""
    status: str = ""
    coverage: str = ""
    sheet_link: str = ""
    app_link: str = ""
    sheet_exists: bool = False
    app_exists: bool = False


@dataclass
class ScanResult:
    root: Path
    native: bool
    projects: list[str] = field(default_factory=list)
    inventory: list[InventoryItem] = field(default_factory=list)
    sheets: list[str] = field(default_factory=list)
    applications: list[str] = field(default_factory=list)
    audits: list[dict[str, Any]] = field(default_factory=list)
    evidence_ids: list[str] = field(default_factory=list)
    bootstrap: dict[str, Any] = field(default_factory=dict)
    findings_raw: list[str] = field(default_factory=list)

    def status_text(self) -> str:
        lines = [
            f"root: {self.root}",
            f"mode: {'native' if self.native else 'bootstrap'}",
            f"projects: {', '.join(self.projects) or '(none)'}",
            f"sheets: {len(self.sheets)}",
            f"applications: {len(self.applications)}",
            f"audits: {len(self.audits)}",
            f"inventory_items: {len(self.inventory)}",
            f"evidence_ids: {len(self.evidence_ids)}",
        ]
        active = [a for a in self.audits if a.get("status") == "active"]
        closed = [a for a in self.audits if a.get("status") == "closed"]
        lines.append(f"audits_active: {[a.get('id') for a in active]}")
        lines.append(f"audits_closed: {[a.get('id') for a in closed]}")
        for item in self.inventory:
            lines.append(
                f"inv {item.slug}: status={item.status} coverage={item.coverage} "
                f"sheet={'yes' if item.sheet_exists else 'no'} "
                f"app={'yes' if item.app_exists else 'no'}"
            )
        if self.findings_raw:
            lines.append("scan_notes:")
            lines.extend(f"  - {x}" for x in self.findings_raw)
        return "\n".join(lines)


def scan_native(root: Path) -> ScanResult:
    result = ScanResult(root=root, native=True)
    projects_dir = root / "projects"
    if projects_dir.is_dir():
        result.projects = sorted(
            p.name for p in projects_dir.iterdir() if p.is_dir() and not p.name.startswith(".")
        )

    tech_dir = root / "technologies"
    if tech_dir.is_dir():
        for p in sorted(tech_dir.iterdir()):
            sheet = p / "SHEET.md"
            if sheet.is_file():
                result.sheets.append(str(sheet.relative_to(root)))

    for proj in result.projects:
        app_dir = root / "projects" / proj / "applications"
        if app_dir.is_dir():
            for f in sorted(app_dir.glob("*.md")):
                result.applications.append(str(f.relative_to(root)))
        inv = root / "projects" / proj / "INVENTORY.md"
        if inv.is_file():
            result.inventory.extend(_parse_inventory(root, proj, inv))

    audits_dir = root / "audits"
    if audits_dir.is_dir():
        for d in sorted(audits_dir.iterdir()):
            if not d.is_dir() or d.name.startswith("."):
                continue
            readme = d / "README.md"
            meta: dict[str, Any] = {"id": d.name, "path": str(d.relative_to(root))}
            if readme.is_file():
                blocks = extract_yaml_blocks(read_text(readme))
                if blocks:
                    meta.update(blocks[0])
            evid = d / "evidence.md"
            if evid.is_file():
                text = read_text(evid)
                ids = re.findall(r"EVID-[A-Z0-9]+-\d{4}-\d{2}-\d{2}-\d{3}", text)
                result.evidence_ids.extend(ids)
                meta["evidence_count"] = len(ids)
                meta["evidence_path"] = str(evid.relative_to(root))
            result.audits.append(meta)

    return result


def _parse_inventory(root: Path, project_id: str, path: Path) -> list[InventoryItem]:
    text = read_text(path)
    items: list[InventoryItem] = []
    tables = parse_md_tables(text)
    for table in tables:
        if not table:
            continue
        header = [h.lower() for h in table[0]]
        if "slug" not in header:
            continue
        idx = {name: i for i, name in enumerate(header)}
        for row in table[1:]:
            if len(row) < len(header):
                row = row + [""] * (len(header) - len(row))
            slug = _strip_md(row[idx["slug"]])
            if not slug or slug == "—" or slug.startswith("`") and len(slug) < 3:
                slug = slug.strip("`")
            slug = slug.strip("`")
            if not slug or slug.lower() == "slug":
                continue
            item = InventoryItem(slug=slug)
            if "name" in idx:
                item.name = _strip_md(row[idx["name"]])
            if "primary" in idx:
                item.primary = _strip_md(row[idx["primary"]])
            if "tags" in idx:
                item.tags = _strip_md(row[idx["tags"]])
            if "status" in idx:
                item.status = _strip_md(row[idx["status"]]).strip("`")
            if "coverage" in idx:
                item.coverage = _strip_md(row[idx["coverage"]]).strip("`")
            sheet_path = root / "technologies" / slug / "SHEET.md"
            app_path = root / "projects" / project_id / "applications" / f"{slug}.md"
            item.sheet_exists = sheet_path.is_file()
            item.app_exists = app_path.is_file()
            if "sheet" in idx:
                item.sheet_link = row[idx["sheet"]]
            if "application" in idx:
                item.app_link = row[idx["application"]]
            items.append(item)
    return items


def _strip_md(s: str) -> str:
    s = s.strip()
    # [text](url) or `code`
    m = re.match(r"\[([^\]]+)\]\([^)]+\)", s)
    if m:
        return m.group(1).strip("`")
    return s.strip("`")


def scan_bootstrap(source: str, work_dir: Path | None = None) -> ScanResult:
    """Scan foreign repo by URL or local path."""
    local: Path | None = None
    url = source.strip()
    if Path(url).exists():
        local = Path(url).resolve()
        result = ScanResult(root=local, native=is_native(local))
        result.bootstrap = {
            "source": str(local),
            "suggested_project_id": slugify_repo_name(local.name),
        }
        result.findings_raw = _local_tree_notes(local)
        return result

    # Remote: prefer gh api
    owner_repo = _parse_github(url)
    findings: list[str] = []
    suggested = "project"
    if owner_repo:
        owner, repo = owner_repo
        suggested = slugify_repo_name(repo)
        findings.append(f"github: {owner}/{repo}")
        meta = _gh_json(f"repos/{owner}/{repo}")
        if meta:
            findings.append(f"description: {meta.get('description')}")
            findings.append(f"language: {meta.get('language')}")
            findings.append(f"pushed_at: {meta.get('pushed_at')}")
            findings.append(f"default_branch: {meta.get('default_branch')}")
        listing = _gh_json(f"repos/{owner}/{repo}/contents/")
        if isinstance(listing, list):
            names = [x.get("name") for x in listing if isinstance(x, dict)]
            findings.append(f"top_level: {', '.join(str(n) for n in names)}")
            if "docs/DOCUMENT-STANDARD.md" in names or "DOCUMENT-STANDARD.md" in names:
                findings.append("note: may already be audit-native — verify")
        readme = _gh_readme(owner, repo)
        if readme:
            findings.append("README excerpt:")
            for line in readme.splitlines()[:40]:
                findings.append(f"  {line}")
            # signal heuristics
            blob = readme.lower()
            for token, label in [
                ("esp32", "signal: esp32"),
                ("ftms", "signal: ftms"),
                ("gatt", "signal: gatt/ble"),
                ("bluetooth", "signal: bluetooth"),
                ("ble", "signal: ble"),
                ("platformio", "signal: platformio"),
                ("msc", "signal: usb-msc"),
                ("avrcp", "signal: avrcp"),
            ]:
                if token in blob:
                    findings.append(label)
    else:
        findings.append(f"non-github or unparsed URL: {url}")
        findings.append("Provide a local clone path for deeper scan.")

    root = work_dir or Path.cwd()
    result = ScanResult(root=root, native=False)
    result.bootstrap = {"source": url, "suggested_project_id": suggested, "github": owner_repo}
    result.findings_raw = findings
    return result


def _parse_github(url: str) -> tuple[str, str] | None:
    # https://github.com/owner/repo(.git)?
    m = re.match(
        r"https?://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$",
        url.strip(),
    )
    if m:
        return m.group(1), m.group(2)
    m = re.match(r"git@github\.com:([^/]+)/([^/]+?)(?:\.git)?$", url.strip())
    if m:
        return m.group(1), m.group(2)
    path = urlparse(url).path.strip("/")
    parts = path.split("/")
    if len(parts) >= 2 and "github.com" in url:
        return parts[0], parts[1].removesuffix(".git")
    return None


def _gh_json(path: str) -> Any:
    try:
        proc = subprocess.run(
            ["gh", "api", path],
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def _gh_readme(owner: str, repo: str) -> str | None:
    try:
        proc = subprocess.run(
            ["gh", "api", f"repos/{owner}/{repo}/readme", "--jq", ".content"],
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0 or not proc.stdout.strip():
        return None
    import base64

    try:
        # gh --jq may return quoted JSON string
        content = proc.stdout.strip().strip('"')
        # if jq returns raw base64 without quotes
        return base64.b64decode(content).decode("utf-8", errors="replace")
    except Exception:
        return None


def _local_tree_notes(root: Path) -> list[str]:
    notes = [f"local_path: {root}"]
    names = sorted(p.name for p in root.iterdir() if not p.name.startswith("."))
    notes.append(f"top_level: {', '.join(names)}")
    readme = root / "README.md"
    if readme.is_file():
        notes.append("README excerpt:")
        for line in read_text(readme).splitlines()[:40]:
            notes.append(f"  {line}")
    return notes
