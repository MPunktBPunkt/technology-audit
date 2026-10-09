"""Generate prompt packs from templates (no knowledge-file writes)."""

from __future__ import annotations

import re
from pathlib import Path

from .scanner import ScanResult, scan_bootstrap, scan_native
from .util import extract_yaml_blocks, read_text, repo_root, today


PROMPT_TYPES = {
    "bootstrap-repo",
    "next-step",
    "new-tech-sheet",
    "new-application",
    "evidence-update",
    "pilot-prep",
    "quality-review",
}


def template_path(root: Path, prompt_type: str) -> Path:
    return root / "templates" / "prompts" / f"{prompt_type}.md"


def _existing_sheets_catalog(root: Path) -> str:
    """Compact list of technology sheets for bootstrap reuse matching."""
    tech = root / "technologies"
    if not tech.is_dir():
        return "(no technologies/ directory)"
    lines: list[str] = []
    for p in sorted(tech.iterdir()):
        sheet = p / "SHEET.md"
        if not sheet.is_file():
            continue
        primary = ""
        title = p.name
        text = read_text(sheet)
        for block in extract_yaml_blocks(text):
            if "slug" in block or "primary" in block:
                primary = str(block.get("primary", ""))
                title = str(block.get("title", title))
                break
        seen = ""
        m = re.search(r"seen_in:\s*\[([^\]]*)\]", text)
        if m:
            seen = m.group(1).strip()
        lines.append(
            f"- {p.name}: primary={primary or '?'} title={title}"
            + (f" seen_in=[{seen}]" if seen else "")
        )
    return "\n".join(lines) or "(no sheets yet)"


def render(template: str, variables: dict[str, str]) -> str:
    out = template
    for key, value in variables.items():
        out = out.replace("{{" + key + "}}", value)
    # leave unknown placeholders visible
    return out


def suggest_next(scan: ScanResult) -> tuple[str, dict[str, str]]:
    """Return (prompt_type, params) for the next sensible step."""
    active = [a for a in scan.audits if a.get("status") == "active"]
    if active:
        a = active[0]
        slug = str(a.get("tech_slug") or "")
        if not slug:
            # guess from audit id
            aid = str(a.get("id", ""))
            if "bmw" in aid or "hu" in aid:
                slug = "bmw-nbt-evo"
            elif "msc" in aid:
                slug = "usb-msc"
        return "evidence-update", {
            "project_id": str(a.get("project_id") or (scan.projects[0] if scan.projects else "pidrive")),
            "audit_id": str(a.get("id")),
            "slug": slug or "unknown",
        }

    # pilot order hint: avrcp
    for item in scan.inventory:
        if item.slug == "avrcp" and not item.sheet_exists:
            return "pilot-prep", {
                "project_id": scan.projects[0] if scan.projects else "pidrive",
                "slug": "avrcp",
                "suggested_audit_id": f"{scan.projects[0] if scan.projects else 'pidrive'}-2026-avrcp",
            }

    for item in scan.inventory:
        if item.status in {"observed", "candidate"} and not item.sheet_exists:
            return "new-tech-sheet", {
                "project_id": scan.projects[0] if scan.projects else "project",
                "slug": item.slug,
            }

    return "quality-review", {
        "project_id": scan.projects[0] if scan.projects else "project",
        "doc_types": "all",
        "target_paths": "projects/ technologies/ audits/",
    }


def build_variables(
    root: Path,
    prompt_type: str,
    *,
    project_id: str = "",
    slug: str = "",
    audit_id: str = "",
    source_repo: str = "",
    scan: ScanResult | None = None,
    bootstrap: ScanResult | None = None,
) -> dict[str, str]:
    d = today()
    vars: dict[str, str] = {
        "today": d,
        "project_id": project_id,
        "slug": slug,
        "audit_id": audit_id,
        "source_repo": source_repo,
        "suggested_project_id": "",
        "scan_findings": "",
        "existing_sheets": _existing_sheets_catalog(root),
        "repo_status": "",
        "inventory_excerpt": "",
        "prior_audits": "",
        "suggested_audit_id": "",
        "sheet_path": f"technologies/{slug}/SHEET.md" if slug else "",
        "upstream_pointers": "(provide MSC-AKTUELL / session links when running evidence-update)",
        "evidence_excerpt": "",
        "target_paths": "",
        "doc_types": "sheet,application,audit,evidence,inventory",
    }

    if bootstrap is not None:
        vars["source_repo"] = str(bootstrap.bootstrap.get("source", source_repo))
        vars["suggested_project_id"] = str(
            bootstrap.bootstrap.get("suggested_project_id", "")
        )
        vars["scan_findings"] = "\n".join(bootstrap.findings_raw) or "(no findings)"

    if scan is not None:
        vars["repo_status"] = scan.status_text()
        if not project_id and scan.projects:
            vars["project_id"] = scan.projects[0]
            project_id = vars["project_id"]
        # inventory excerpt
        lines = []
        for item in scan.inventory:
            if slug and item.slug != slug:
                continue
            lines.append(
                f"- {item.slug}: status={item.status} coverage={item.coverage} "
                f"sheet={'yes' if item.sheet_exists else 'no'} "
                f"app={'yes' if item.app_exists else 'no'} primary={item.primary}"
            )
        vars["inventory_excerpt"] = "\n".join(lines) or "(no inventory rows matched)"
        vars["prior_audits"] = "\n".join(
            f"- {a.get('id')}: status={a.get('status')} tech={a.get('tech_slug')}"
            for a in scan.audits
        ) or "(none)"
        if not vars["suggested_audit_id"] and project_id and slug:
            vars["suggested_audit_id"] = f"{project_id}-{d[:4]}-{slug}"

        if audit_id:
            evid = root / "audits" / audit_id / "evidence.md"
            if evid.is_file():
                text = read_text(evid)
                vars["evidence_excerpt"] = "\n".join(text.splitlines()[:80])
            readme = root / "audits" / audit_id / "README.md"
            if readme.is_file() and "upstream" not in vars["upstream_pointers"].lower():
                # keep default; user can enrich
                pass

        if prompt_type == "quality-review":
            targets = []
            if project_id:
                targets.append(f"projects/{project_id}/")
            if slug:
                targets.append(f"technologies/{slug}/SHEET.md")
                targets.append(f"projects/{project_id}/applications/{slug}.md")
            if audit_id:
                targets.append(f"audits/{audit_id}/")
            if not targets:
                targets = ["projects/", "technologies/", "audits/", "docs/"]
            vars["target_paths"] = "\n".join(targets)

    return vars


def generate_prompt(
    prompt_type: str,
    *,
    root: Path | None = None,
    project_id: str = "",
    slug: str = "",
    audit_id: str = "",
    source_repo: str = "",
    write: bool = True,
) -> tuple[Path | None, str]:
    if prompt_type not in PROMPT_TYPES:
        raise ValueError(f"unknown prompt type: {prompt_type}")

    root = repo_root(root)
    tpl = template_path(root, prompt_type)
    if not tpl.is_file():
        raise FileNotFoundError(f"template missing: {tpl}")

    scan = scan_native(root) if (root / "docs" / "DOCUMENT-STANDARD.md").is_file() else None
    bootstrap = scan_bootstrap(source_repo) if source_repo else None

    # bootstrap prompts should not inherit native project naming
    if prompt_type == "bootstrap-repo":
        scan_for_vars = None
    else:
        scan_for_vars = scan

    if prompt_type == "next-step" and scan is not None and not slug and not audit_id:
        suggested_type, params = suggest_next(scan)
        # still emit next-step prompt, but enrich repo_status with suggestion
        extra = (
            f"\n\nsuggested_followup_type: {suggested_type}\n"
            + "\n".join(f"suggested_param_{k}: {v}" for k, v in params.items())
        )
        variables = build_variables(
            root,
            prompt_type,
            project_id=project_id or params.get("project_id", ""),
            slug=slug or params.get("slug", ""),
            audit_id=audit_id or params.get("audit_id", ""),
            scan=scan,
        )
        variables["repo_status"] = variables["repo_status"] + extra
    else:
        variables = build_variables(
            root,
            prompt_type,
            project_id=project_id if prompt_type != "bootstrap-repo" else "",
            slug=slug,
            audit_id=audit_id,
            source_repo=source_repo,
            scan=scan_for_vars,
            bootstrap=bootstrap,
        )

    body = render(read_text(tpl), variables)
    # Strip the template header metadata note lines about placeholders? Keep full template.

    out_path: Path | None = None
    if write:
        out_dir = root / "artifacts" / "prompts"
        out_dir.mkdir(parents=True, exist_ok=True)
        stamp = today().replace("-", "")
        parts = [prompt_type]
        pid = project_id or variables.get("project_id") or variables.get("suggested_project_id") or ""
        if pid:
            parts.append(pid)
        sid = slug or variables.get("slug") or ""
        aid = audit_id or variables.get("audit_id") or ""
        if sid:
            parts.append(sid)
        elif aid:
            parts.append(aid)
        name = "-".join(parts) + f"-{stamp}.md"
        # sanitize
        name = re.sub(r"[^a-zA-Z0-9._-]+", "-", name)
        out_path = out_dir / name
        header = (
            f"<!-- generated by ta-assist · {prompt_type} · {today()} · "
            f"do not treat as knowledge source -->\n\n"
        )
        out_path.write_text(header + body, encoding="utf-8")
    return out_path, body
