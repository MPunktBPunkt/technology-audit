"""Structure and consistency checks (PROMPT-CONTRACT / REVIEW-CHECKS)."""

from __future__ import annotations

import re
from pathlib import Path

from .indexer import collect_sheets, index_slugs_from_yaml
from .scanner import Finding, ScanResult, scan_native
from .util import (
    EVIDENCE_ID,
    KEBAB,
    MATURITY_R,
    MATURITY_W,
    VALID_COVERAGE,
    VALID_EPISTEMIC,
    VALID_STATUS,
    extract_yaml_blocks,
    is_native,
    read_text,
    repo_root,
)


REQUIRED_DOCS = [
    "docs/DOCUMENT-STANDARD.md",
    "docs/METHODOLOGY.md",
    "docs/TAXONOMY.md",
    "docs/PROMPT-CONTRACT.md",
    "docs/REVIEW-CHECKS.md",
    "docs/REUSE.md",
    "docs/AUDIT-PROFILES.md",
    "docs/STANDARD-CHANGELOG.md",
    "docs/MAINTENANCE.md",
    "docs/KB-FIT.md",
    "README.md",
    "VERSION",
    "LICENSE",
]


def run_checks(root: Path | None = None) -> list[Finding]:
    root = repo_root(root)
    findings: list[Finding] = []
    if not is_native(root):
        findings.append(
            Finding(
                "error",
                "NATIVE01",
                "docs/DOCUMENT-STANDARD.md missing — not a native technology-audit repo",
                str(root),
            )
        )
        return findings

    for rel in REQUIRED_DOCS:
        if not (root / rel).is_file():
            findings.append(Finding("error", "DOC01", f"missing required file: {rel}", rel))

    for rel in [
        "templates/prompts/bootstrap-repo.md",
        "templates/prompts/next-step.md",
        "templates/prompts/README.md",
        "artifacts/prompts/README.md",
    ]:
        if not (root / rel).is_file():
            findings.append(Finding("warning", "DOC02", f"missing assist file: {rel}", rel))

    scan = scan_native(root)
    findings.extend(_check_inventory(root, scan))
    findings.extend(_check_sheets(root, scan))
    findings.extend(_check_applications(root, scan))
    findings.extend(_check_audits(root, scan))
    findings.extend(_check_evidence(root, scan))
    findings.extend(_check_pilot_hints(scan))
    findings.extend(_check_tech_index(root, scan))
    findings.extend(_check_seen_in_apps(root, scan))
    return findings


def _check_inventory(root: Path, scan: ScanResult) -> list[Finding]:
    out: list[Finding] = []
    for proj in scan.projects:
        inv = root / "projects" / proj / "INVENTORY.md"
        if not inv.is_file():
            out.append(Finding("warning", "I0", f"project has no INVENTORY.md", f"projects/{proj}"))
            continue
        if not (root / "projects" / proj / "SCOPE.md").is_file():
            out.append(Finding("warning", "P1", "SCOPE.md missing", f"projects/{proj}/SCOPE.md"))
        inv_text = read_text(inv)
        if scan.sheets and not any(
            t in inv_text for t in ("Reuse", "Match", "Wissenswachstum", "REUSE")
        ):
            out.append(
                Finding(
                    "warning",
                    "G7",
                    "INVENTORY missing Reuse/Match note",
                    f"projects/{proj}/INVENTORY.md",
                )
            )

    for item in scan.inventory:
        path = f"inventory:{item.slug}"
        if item.status and item.status not in VALID_STATUS:
            out.append(
                Finding("error", "I2", f"invalid status '{item.status}'", path)
            )
        if item.coverage and item.coverage not in VALID_COVERAGE:
            out.append(
                Finding("error", "I3", f"invalid coverage '{item.coverage}'", path)
            )
        if not KEBAB.match(item.slug):
            out.append(Finding("warning", "SLUG", f"slug not kebab-case: {item.slug}", path))

        if item.status in {"documented", "applied"} and not item.sheet_exists:
            out.append(
                Finding(
                    "error",
                    "I4",
                    f"status {item.status} but sheet missing: technologies/{item.slug}/SHEET.md",
                    path,
                )
            )
        if item.status == "applied" and not item.app_exists:
            out.append(
                Finding(
                    "error",
                    "I5",
                    f"status applied but application missing: applications/{item.slug}.md",
                    path,
                )
            )
        if item.status in {"observed", "candidate"} and not item.sheet_exists:
            out.append(
                Finding(
                    "warning",
                    "I6",
                    f"no sheet yet for {item.status} slug (zielpfad ok)",
                    path,
                )
            )
        if item.coverage == "full":
            out.append(
                Finding(
                    "info",
                    "R4",
                    f"{item.slug}: coverage=full — verify open questions / evidence",
                    path,
                )
            )
    return out


def _check_sheets(root: Path, scan: ScanResult) -> list[Finding]:
    out: list[Finding] = []
    for rel in scan.sheets:
        path = root / rel
        text = read_text(path)
        blocks = extract_yaml_blocks(text)
        if not blocks:
            out.append(Finding("error", "S1", "missing YAML frontmatter", rel))
            continue
        meta = blocks[0]
        for key in ("slug", "primary", "status"):
            if key not in meta or meta[key] in (None, ""):
                out.append(Finding("error", "S1", f"YAML missing '{key}'", rel))
        maturity = meta.get("maturity")
        if not isinstance(maturity, dict):
            out.append(Finding("error", "S1", "YAML missing maturity map", rel))
        else:
            for dim, rx in (
                ("technology", MATURITY_R),
                ("implementation", MATURITY_R),
                ("field_evidence", MATURITY_R),
                ("reusability", MATURITY_W),
            ):
                val = str(maturity.get(dim, ""))
                # allow inline comments after value
                val = val.split()[0] if val else ""
                if not rx.match(val):
                    out.append(
                        Finding(
                            "error",
                            "S1",
                            f"invalid maturity.{dim}='{maturity.get(dim)}'",
                            rel,
                        )
                    )
        # A/B/C heuristic — warn only on heavy project/field token mix
        lowered = text.lower()
        proj_hits = sum(
            1
            for t in ("pidrive", "msc-aktuell", "feld-session", "bmw nbt")
            if t in lowered
        )
        if proj_hits >= 3:
            out.append(
                Finding(
                    "warning",
                    "S4",
                    "sheet mentions multiple project/field tokens — check A-only rule",
                    rel,
                )
            )
        if "Projektstart-Checkliste" not in text:
            out.append(
                Finding(
                    "warning",
                    "G6",
                    "sheet missing Projektstart-Checkliste (reuse)",
                    rel,
                )
            )
    return out


def _check_applications(root: Path, scan: ScanResult) -> list[Finding]:
    out: list[Finding] = []
    for rel in scan.applications:
        path = root / rel
        text = read_text(path)
        blocks = extract_yaml_blocks(text)
        if not blocks:
            out.append(Finding("error", "A0", "missing YAML frontmatter", rel))
            continue
        meta = blocks[0]
        sheet = meta.get("sheet")
        if sheet:
            # resolve relative to application file
            target = (path.parent / str(sheet)).resolve()
            if not target.is_file():
                out.append(
                    Finding("error", "A1", f"sheet path does not exist: {sheet}", rel)
                )
        else:
            out.append(Finding("error", "A1", "YAML missing sheet:", rel))

        maturity = meta.get("maturity")
        if isinstance(maturity, dict):
            for dim, rx in (
                ("technology", MATURITY_R),
                ("implementation", MATURITY_R),
                ("field_evidence", MATURITY_R),
                ("reusability", MATURITY_W),
            ):
                raw = str(maturity.get(dim, ""))
                val = raw.split()[0] if raw else ""
                if not rx.match(val):
                    out.append(
                        Finding(
                            "warning",
                            "A6",
                            f"invalid maturity.{dim}='{maturity.get(dim)}'",
                            rel,
                        )
                    )
            fe = str(maturity.get("field_evidence", "")).split()[0]
            if fe in {"R4", "R5"}:
                # check if any active audit still has open field exit — soft
                out.append(
                    Finding(
                        "info",
                        "R1",
                        f"field_evidence={fe} — confirm documented field PASS exists",
                        rel,
                    )
                )

        if "Ebene C" in text or "Ebene **C**" in text or "Host" in text:
            if "EVID-" not in text and "Evidence" not in text and "evidence" not in text.lower():
                out.append(
                    Finding(
                        "warning",
                        "A3",
                        "C/host section present but no Evidence-ID mention",
                        rel,
                    )
                )
    return out


def _check_audits(root: Path, scan: ScanResult) -> list[Finding]:
    out: list[Finding] = []
    for audit in scan.audits:
        rel = f"{audit.get('path')}/README.md"
        path = root / rel
        if not path.is_file():
            out.append(Finding("error", "C1", "audit README missing", rel))
            continue
        text = read_text(path)
        blocks = extract_yaml_blocks(text)
        if not blocks:
            out.append(Finding("error", "C1", "audit YAML missing", rel))
            continue
        meta = blocks[0]
        for key in ("id", "project_id", "status", "started"):
            if key not in meta or meta[key] in (None, ""):
                out.append(Finding("error", "C1", f"audit YAML missing '{key}'", rel))
        if "Exit-Kriterien" not in text and "Exit" not in text and "| # |" not in text:
            out.append(Finding("error", "C2", "exit criteria table not found", rel))
        std = str(meta.get("standard_version") or "").strip().strip('"').strip("'")
        if not std:
            out.append(
                Finding(
                    "error",
                    "C7",
                    "audit YAML missing standard_version (see VERSION / STANDARD-CHANGELOG)",
                    rel,
                )
            )
        else:
            if not re.match(r"^\d+\.\d+\.\d+$", std):
                out.append(
                    Finding(
                        "error",
                        "C7",
                        f"standard_version '{std}' is not semver X.Y.Z",
                        rel,
                    )
                )
            else:
                current = read_text(root / "VERSION").strip()
                if current and std != current and not meta.get("standard_gaps"):

                    def _semver(s: str) -> tuple[int, int, int] | None:
                        m = re.match(r"^(\d+)\.(\d+)\.(\d+)$", s.strip())
                        return (int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None

                    cur_t, std_t = _semver(current), _semver(std)
                    if cur_t and std_t and std_t[:2] < cur_t[:2]:
                        out.append(
                            Finding(
                                "warning",
                                "C8",
                                f"standard_version {std} behind major.minor of repo {current} — list standard_gaps or refresh",
                                rel,
                            )
                        )
                    elif cur_t and std_t and std_t < cur_t:
                        # Collect later as one PILOT-style info — mark via code C8p
                        out.append(
                            Finding(
                                "info",
                                "C8p",
                                f"{std}",
                                rel,
                            )
                        )
                    elif std != current:
                        out.append(
                            Finding(
                                "warning",
                                "C8",
                                f"standard_version {std} ≠ repo VERSION {current} and no standard_gaps listed",
                                rel,
                            )
                        )
        if not meta.get("profile"):
            out.append(Finding("warning", "C9", "audit YAML missing profile", rel))
        status = meta.get("status")
        if status == "closed":
            if "Lessons" not in text and "Lessons Learned" not in text:
                out.append(Finding("warning", "C5", "closed audit without Lessons section", rel))
            # open markers in exit table
            if re.search(r"\|\s*\d+\s*\|[^|\n]+\|\s*\*\*nicht erfüllt\*\*", text) or re.search(
                r"\|\s*\d+\s*\|[^|\n]+\|\s*offen\b", text, re.I
            ):
                out.append(
                    Finding(
                        "warning",
                        "C3",
                        "closed audit still shows open/unmet exit rows — document deviation",
                        rel,
                    )
                )
        if status == "active" and "evidence" not in audit:
            evid = root / str(audit.get("path")) / "evidence.md"
            if not evid.is_file():
                out.append(
                    Finding("warning", "C4", "active audit has no evidence.md", rel)
                )
    return out


def _check_evidence(root: Path, scan: ScanResult) -> list[Finding]:
    out: list[Finding] = []
    for audit in scan.audits:
        evid_rel = audit.get("evidence_path")
        if not evid_rel:
            continue
        text = read_text(root / evid_rel)
        for line in text.splitlines():
            if "EVID-" not in line:
                continue
            if "*" in line and "`EVID-" in line:
                continue  # prose wildcard, e.g. EVID-USBMSC-*
            for bad in re.findall(
                r"EVID-[A-Z0-9]+-\d{4}-\d{2}-\d{2}-\d{3,}", line
            ):
                if not EVIDENCE_ID.fullmatch(bad):
                    out.append(
                        Finding(
                            "error",
                            "E1",
                            f"invalid evidence id format: {bad}",
                            evid_rel,
                        )
                    )
            for m in EVIDENCE_ID.finditer(line):
                if not m.group(0):
                    continue
            # status tokens in table rows
            if line.strip().startswith("|") and "EVID-" in line:
                cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
                for cell in cells:
                    if cell in VALID_EPISTEMIC or cell.startswith("EVID-"):
                        continue
                # soft: look for known bad
                for cell in cells:
                    if cell.startswith("`") and cell.endswith("`"):
                        cell = cell.strip("`")
                    if cell in {
                        "PASS",
                        "FAIL",
                        "TODO",
                        "WIP",
                    }:
                        out.append(
                            Finding(
                                "warning",
                                "E3",
                                f"non-epistemic status token in evidence row: {cell}",
                                evid_rel,
                            )
                        )
    return out


def _check_pilot_hints(scan: ScanResult) -> list[Finding]:
    out: list[Finding] = []
    active = [a for a in scan.audits if a.get("status") == "active"]
    if not active:
        for item in scan.inventory:
            if item.slug == "avrcp" and item.status == "observed" and not item.sheet_exists:
                out.append(
                    Finding(
                        "info",
                        "PILOT",
                        "no active audit; avrcp observed without sheet — candidate for pilot-prep",
                        "inventory:avrcp",
                    )
                )
    else:
        ids = [str(a.get("id")) for a in active]
        sample = ", ".join(ids[:5])
        more = f" (+{len(ids) - 5} more)" if len(ids) > 5 else ""
        out.append(
            Finding(
                "info",
                "PILOT",
                f"{len(ids)} active campaign(s) — prefer evidence-update / close desk-complete before new pilots: {sample}{more}",
                "audits/",
            )
        )
    return out


def _check_tech_index(root: Path, scan: ScanResult) -> list[Finding]:
    """NAV: Sheet dirs ↔ index.yaml ↔ README (generated catalog)."""
    out: list[Finding] = []
    index_path = root / "technologies" / "index.yaml"
    readme_path = root / "technologies" / "README.md"
    disk_slugs = {Path(s).parent.name for s in scan.sheets}
    if not index_path.is_file():
        out.append(
            Finding(
                "warning",
                "NAV1",
                "technologies/index.yaml missing — run `python3 tools/ta-assist index`",
                "technologies/",
            )
        )
        return out
    indexed = index_slugs_from_yaml(root)
    missing_in_index = sorted(disk_slugs - indexed)
    extra_in_index = sorted(indexed - disk_slugs)
    for slug in missing_in_index:
        out.append(
            Finding(
                "error",
                "NAV2",
                f"sheet on disk not in index.yaml — run `ta-assist index`: {slug}",
                f"technologies/{slug}/SHEET.md",
            )
        )
    for slug in extra_in_index:
        out.append(
            Finding(
                "error",
                "NAV3",
                f"index.yaml lists slug without SHEET.md — run `ta-assist index`: {slug}",
                "technologies/index.yaml",
            )
        )
    if readme_path.is_file():
        readme = read_text(readme_path)
        for slug in sorted(disk_slugs):
            if f"`{slug}`" not in readme and f"]({slug}/SHEET.md)" not in readme:
                out.append(
                    Finding(
                        "warning",
                        "NAV4",
                        f"technologies/README.md missing link for {slug} — run `ta-assist index`",
                        "technologies/README.md",
                    )
                )
    # Soft: index.yaml generated date lag (info only if parseable)
    entries = collect_sheets(root)
    if indexed and len(entries) != len(indexed) and not missing_in_index and not extra_in_index:
        out.append(
            Finding(
                "info",
                "NAV5",
                "index sheet_count mismatch vs collect_sheets — re-run index",
                "technologies/index.yaml",
            )
        )
    return out


def _check_seen_in_apps(root: Path, scan: ScanResult) -> list[Finding]:
    """G2 soft: sheet seen_in should have Application when project exists."""
    out: list[Finding] = []
    app_pairs = set()
    for rel in scan.applications:
        # projects/<id>/applications/<slug>.md
        parts = Path(rel).parts
        if len(parts) >= 4 and parts[0] == "projects":
            app_pairs.add((parts[1], Path(parts[-1]).stem))
    for rel in scan.sheets:
        text = read_text(root / rel)
        blocks = extract_yaml_blocks(text)
        if not blocks:
            continue
        meta = blocks[0]
        slug = str(meta.get("slug") or Path(rel).parent.name)
        seen = meta.get("seen_in") or []
        if isinstance(seen, str):
            seen = [seen]
        if not isinstance(seen, list):
            continue
        for proj in seen:
            proj = str(proj).strip().replace("projects/", "")
            if not proj or proj not in scan.projects:
                continue
            if (proj, slug) not in app_pairs:
                out.append(
                    Finding(
                        "warning",
                        "S8",
                        f"sheet seen_in has `{proj}` but no applications/{slug}.md",
                        rel,
                    )
                )
    return out


def summarize(findings: list[Finding]) -> tuple[int, int, int]:
    e = sum(1 for f in findings if f.level == "error")
    w = sum(1 for f in findings if f.level == "warning")
    i = sum(1 for f in findings if f.level == "info")
    return e, w, i


def _collapse_findings(findings: list[Finding]) -> list[Finding]:
    """Reduce duplicate noise (I6, C8p) while keeping one actionable line."""
    c8p = [f for f in findings if f.code == "C8p"]
    i6 = [f for f in findings if f.code == "I6"]
    other = [f for f in findings if f.code not in {"C8p", "I6"}]
    if i6:
        slugs = sorted({f.path.replace("inventory:", "") for f in i6})
        sample = ", ".join(slugs[:8])
        more = f" (+{len(slugs) - 8} more)" if len(slugs) > 8 else ""
        other.append(
            Finding(
                "warning",
                "I6",
                f"{len(i6)} observed/candidate row(s) without sheet ({len(slugs)} unique) — ok until triage: {sample}{more}",
                "projects/*/INVENTORY.md",
            )
        )
    if c8p:
        vers = sorted({f.message for f in c8p})
        other.append(
            Finding(
                "info",
                "C8p",
                f"{len(c8p)} campaign(s) on patch-lag vs VERSION ({', '.join(vers)}) — ok for docs/nav bumps",
                "audits/",
            )
        )
    return other


def format_report(findings: list[Finding]) -> str:
    findings = _collapse_findings(findings)
    e, w, i = summarize(findings)
    lines = [
        "## technology-audit check",
        "",
        f"**Errors:** {e} · **Warnings:** {w} · **Info:** {i}",
        "",
    ]
    for level in ("error", "warning", "info"):
        group = [f for f in findings if f.level == level]
        if not group:
            continue
        lines.append(f"### {level.capitalize()}s")
        for f in group:
            loc = f" (`{f.path}`)" if f.path else ""
            lines.append(f"- `{f.code}` {f.message}{loc}")
        lines.append("")
    return "\n".join(lines)
