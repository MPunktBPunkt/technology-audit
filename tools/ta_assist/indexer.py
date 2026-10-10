"""Generate technology + project catalogs from Sheet/Project YAML.

Sources of truth:
  technologies/*/SHEET.md
  projects/*/SCOPE.md (+ INVENTORY for app counts)
  technologies/_planned.txt

Run: python3 tools/ta-assist index
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .util import KEBAB, extract_yaml_blocks, read_text, repo_root, today

PRIMARY_LABELS = {
    "A": "Empfang",
    "B": "Audio",
    "C": "Protokolle",
    "D": "Embedded",
    "E": "Speicher / Formate",
    "F": "Systemintegration",
    "G": "Steuerung / UI",
    "H": "Test / Analyse",
    "I": "Fahrzeug / Geräte",
    "J": "Architektur",
}
VALID_PRIMARY = set(PRIMARY_LABELS)

DEFAULT_PLANNED = [
    "pipewire",
    "scsi",
    "esp32",
    "fat",
    "systemd",
    "mpris2",
    "webradio (Pi-Stack; ESP hat webradio-browser-host)",
]


@dataclass
class SheetEntry:
    slug: str
    title: str
    primary: str
    reusability: str
    seen_in: list[str] = field(default_factory=list)
    path: str = ""
    errors: list[str] = field(default_factory=list)


@dataclass
class ProjectEntry:
    project_id: str
    title: str = ""
    profile: str = ""
    status: str = ""
    app_count: int = 0
    path: str = ""


def yaml_scalar(value: Any) -> str:
    """Quote YAML scalars that would break naive dumps."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    s = str(value)
    if s == "":
        return '""'
    needs = (
        s != s.strip()
        or any(c in s for c in ":#{}[]&*!|>'\"%@`,\n\t")
        or s.lower() in {"true", "false", "null", "yes", "no", "on", "off"}
        or s.startswith(("-", "?", "*", "&", "!", "|", ">", "%", "@", "`"))
    )
    if needs:
        esc = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{esc}"'
    return s


def yaml_list(items: list[str]) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(yaml_scalar(x) for x in items) + "]"


def md_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def canonicalize_project_id(raw: str) -> str:
    s = str(raw).strip().strip("'\"")
    if s.startswith("projects/"):
        s = s[len("projects/") :]
    return s.strip("/")


def collect_sheets(root: Path) -> list[SheetEntry]:
    tech = root / "technologies"
    entries: list[SheetEntry] = []
    if not tech.is_dir():
        return entries
    for d in sorted(tech.iterdir()):
        if not d.is_dir() or d.name.startswith(".") or d.name.startswith("_"):
            continue
        sheet = d / "SHEET.md"
        if not sheet.is_file():
            continue
        blocks = extract_yaml_blocks(read_text(sheet))
        errors: list[str] = []
        if not blocks:
            errors.append("missing YAML")
            entries.append(
                SheetEntry(
                    slug=d.name,
                    title=d.name,
                    primary="?",
                    reusability="W?",
                    path=f"technologies/{d.name}/SHEET.md",
                    errors=errors,
                )
            )
            continue
        meta = blocks[0]
        slug = str(meta.get("slug") or d.name).strip()
        if slug != d.name:
            errors.append(f"slug '{slug}' ≠ directory '{d.name}'")
        if not KEBAB.match(slug):
            errors.append(f"slug not kebab-case: {slug}")
        title = str(meta.get("title") or slug).strip()
        primary = str(meta.get("primary") or "?").strip().upper()[:1]
        if primary not in VALID_PRIMARY:
            errors.append(f"invalid primary '{primary}'")
        maturity = meta.get("maturity") if isinstance(meta.get("maturity"), dict) else {}
        reus = str(maturity.get("reusability") or "W?").split()[0]
        seen_raw = meta.get("seen_in") or []
        if isinstance(seen_raw, str):
            seen_raw = [seen_raw]
        if not isinstance(seen_raw, list):
            seen_raw = []
        seen: list[str] = []
        for item in seen_raw:
            canon = canonicalize_project_id(item)
            if str(item).strip().startswith("projects/"):
                errors.append(f"seen_in uses path form '{item}' — use '{canon}'")
            if canon and canon not in seen:
                seen.append(canon)
        entries.append(
            SheetEntry(
                slug=slug,
                title=title,
                primary=primary or "?",
                reusability=reus,
                seen_in=seen,
                path=f"technologies/{d.name}/SHEET.md",
                errors=errors,
            )
        )
    return entries


def collect_projects(root: Path) -> list[ProjectEntry]:
    projects_dir = root / "projects"
    out: list[ProjectEntry] = []
    if not projects_dir.is_dir():
        return out
    for d in sorted(projects_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        scope = d / "SCOPE.md"
        title = d.name
        profile = ""
        status = ""
        project_id = d.name
        if scope.is_file():
            blocks = extract_yaml_blocks(read_text(scope))
            if blocks:
                meta = blocks[0]
                project_id = str(meta.get("project_id") or d.name).strip()
                title = str(meta.get("title") or project_id).strip()
                profile = str(
                    meta.get("profile") or meta.get("profile_hint") or ""
                ).strip()
                status = str(meta.get("status") or "").strip()
        apps = d / "applications"
        app_count = len(list(apps.glob("*.md"))) if apps.is_dir() else 0
        out.append(
            ProjectEntry(
                project_id=project_id,
                title=title,
                profile=profile or "—",
                status=status or "—",
                app_count=app_count,
                path=f"projects/{d.name}/",
            )
        )
    return out


def load_planned(root: Path) -> list[str]:
    planned_path = root / "technologies" / "_planned.txt"
    if planned_path.is_file():
        lines = []
        for line in read_text(planned_path).splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
        return lines
    return list(DEFAULT_PLANNED)


def write_tech_index_yaml(root: Path, entries: list[SheetEntry], planned: list[str]) -> Path:
    out = root / "technologies" / "index.yaml"
    lines = [
        f"# Generated by ta-assist index — {today()}",
        "# Source of truth: technologies/*/SHEET.md",
        "# Regenerate: python3 tools/ta-assist index",
        "# Do not hand-edit sheet rows.",
        "",
        f"generated: {today()}",
        f"sheet_count: {len(entries)}",
        "sheets:",
    ]
    for e in entries:
        lines.append(f"  - slug: {yaml_scalar(e.slug)}")
        lines.append(f"    title: {yaml_scalar(e.title)}")
        lines.append(f"    primary: {yaml_scalar(e.primary)}")
        lines.append(f"    reusability: {yaml_scalar(e.reusability)}")
        lines.append(f"    seen_in: {yaml_list(e.seen_in)}")
        lines.append(f"    path: {yaml_scalar(e.path)}")
    lines.append("planned:")
    for p in planned:
        lines.append(f"  - {yaml_scalar(p)}")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_tech_readme(root: Path, entries: list[SheetEntry], planned: list[str]) -> Path:
    out = root / "technologies" / "README.md"
    by_primary: dict[str, list[SheetEntry]] = {}
    for e in entries:
        by_primary.setdefault(e.primary, []).append(e)

    lines = [
        "# technologies/",
        "",
        "Wiederverwendbare Technology Sheets.",
        "",
        "**Reuse:** [`docs/REUSE.md`](../docs/REUSE.md) · **Neustart:** [`docs/PROJECT-START.md`](../docs/PROJECT-START.md) · "
        "**Familien:** [`docs/FAMILIES.md`](../docs/FAMILIES.md) · **Standard:** [`VERSION`](../VERSION)",
        "",
        f"**Maschinenindex:** [`index.yaml`](index.yaml) (generiert — `{today()}`, {len(entries)} Sheets). "
        "Neu generieren: `python3 tools/ta-assist index`",
        "",
        "## Index nach Primary (TAXONOMY)",
        "",
    ]
    for letter in list("ABCDEFGHIJ") + sorted(
        k for k in by_primary if k not in set("ABCDEFGHIJ")
    ):
        group = by_primary.get(letter)
        if not group:
            continue
        label = PRIMARY_LABELS.get(letter, letter)
        lines.append(f"### {letter} — {label}")
        lines.append("")
        lines.append("| Slug | Title | Reuse | Gesehen in |")
        lines.append("|------|-------|-------|------------|")
        for e in sorted(group, key=lambda x: x.slug):
            seen = ", ".join(f"`{s}`" for s in e.seen_in) if e.seen_in else "—"
            lines.append(
                f"| [`{md_cell(e.slug)}`]({e.slug}/SHEET.md) | {md_cell(e.title)} | "
                f"{md_cell(e.reusability)} | {md_cell(seen)} |"
            )
        lines.append("")

    lines.append("## Geplant (ohne Sheet)")
    lines.append("")
    lines.append("Pflege: [`_planned.txt`](_planned.txt) · dann `ta-assist index`.")
    lines.append("")
    lines.append(" · ".join(f"`{p}`" for p in planned))
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_projects_index_yaml(root: Path, projects: list[ProjectEntry]) -> Path:
    out = root / "projects" / "index.yaml"
    lines = [
        f"# Generated by ta-assist index — {today()}",
        "# Source of truth: projects/*/SCOPE.md",
        "# Regenerate: python3 tools/ta-assist index",
        "",
        f"generated: {today()}",
        f"project_count: {len(projects)}",
        "projects:",
    ]
    for p in projects:
        lines.append(f"  - id: {yaml_scalar(p.project_id)}")
        lines.append(f"    title: {yaml_scalar(p.title)}")
        lines.append(f"    profile: {yaml_scalar(p.profile)}")
        lines.append(f"    status: {yaml_scalar(p.status)}")
        lines.append(f"    applications: {p.app_count}")
        lines.append(f"    path: {yaml_scalar(p.path)}")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_projects_readme(root: Path, projects: list[ProjectEntry]) -> Path:
    out = root / "projects" / "README.md"
    lines = [
        "# projects/",
        "",
        "Projektkontext: Scope, Inventar, Applications. Technologie-Wissen → [`technologies/`](../technologies/).",
        "",
        f"**Maschinenindex:** [`index.yaml`](index.yaml) (generiert — `{today()}`, {len(projects)} Projekte). "
        "`python3 tools/ta-assist index`",
        "",
        "| Projekt | Titel | Profil | Status | Apps |",
        "|---------|-------|--------|--------|------|",
    ]
    for p in projects:
        lines.append(
            f"| [`{md_cell(p.project_id)}`]({p.project_id}/) | {md_cell(p.title)} | "
            f"{md_cell(p.profile)} | {md_cell(p.status)} | {p.app_count} |"
        )
    lines.extend(
        [
            "",
            "Neues Projekt: [`REUSE.md`](../docs/REUSE.md) · [`AUDIT-PROFILES.md`](../docs/AUDIT-PROFILES.md) · "
            "[`MAINTENANCE.md`](../docs/MAINTENANCE.md).",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def ensure_planned_file(root: Path, planned: list[str]) -> Path:
    path = root / "technologies" / "_planned.txt"
    if not path.is_file():
        body = (
            "# Observed/planned slugs without SHEET.md yet.\n"
            "# One entry per line. Regenerates into technologies/README.md via `ta-assist index`.\n"
            + "\n".join(planned)
            + "\n"
        )
        path.write_text(body, encoding="utf-8")
    return path


def regenerate(root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    entries = collect_sheets(root)
    hard = [e for e in entries if e.errors]
    if hard:
        # Still write catalogs, but surface errors to caller
        pass
    planned = load_planned(root)
    ensure_planned_file(root, planned)
    planned = load_planned(root)
    projects = collect_projects(root)
    tech_yml = write_tech_index_yaml(root, entries, planned)
    tech_md = write_tech_readme(root, entries, planned)
    proj_yml = write_projects_index_yaml(root, projects)
    proj_md = write_projects_readme(root, projects)
    return {
        "sheet_count": len(entries),
        "project_count": len(projects),
        "index_yaml": str(tech_yml.relative_to(root)),
        "readme": str(tech_md.relative_to(root)),
        "projects_index": str(proj_yml.relative_to(root)),
        "projects_readme": str(proj_md.relative_to(root)),
        "planned": len(planned),
        "sheet_errors": sum(len(e.errors) for e in entries),
    }


def index_slugs_from_yaml(root: Path) -> set[str]:
    path = root / "technologies" / "index.yaml"
    if not path.is_file():
        return set()
    slugs: set[str] = set()
    for line in read_text(path).splitlines():
        line = line.strip()
        if line.startswith("- slug:"):
            val = line.split(":", 1)[1].strip().strip("'\"")
            slugs.add(val)
    return slugs


def project_ids_from_yaml(root: Path) -> set[str]:
    path = root / "projects" / "index.yaml"
    if not path.is_file():
        return set()
    ids: set[str] = set()
    for line in read_text(path).splitlines():
        line = line.strip()
        if line.startswith("- id:"):
            ids.add(line.split(":", 1)[1].strip().strip("'\""))
    return ids
