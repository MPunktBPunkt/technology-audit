"""Structure and consistency checks (PROMPT-CONTRACT / REVIEW-CHECKS)."""

from __future__ import annotations

import re
from pathlib import Path

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
    "README.md",
    "VERSION",
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
        # look for next pilot avrcp
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
        for a in active:
            out.append(
                Finding(
                    "info",
                    "PILOT",
                    f"active campaign {a.get('id')} — prefer evidence-update before new pilot",
                    str(a.get("path")),
                )
            )
    return out


def summarize(findings: list[Finding]) -> tuple[int, int, int]:
    e = sum(1 for f in findings if f.level == "error")
    w = sum(1 for f in findings if f.level == "warning")
    i = sum(1 for f in findings if f.level == "info")
    return e, w, i


def format_report(findings: list[Finding]) -> str:
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
