"""Generate technology + project catalogs from Sheet/Project YAML.

Sources of truth:
  technologies/*/SHEET.md
  projects/*/SCOPE.md (+ applications for evidence aggregation)
  technologies/_planned.txt

Run: python3 tools/ta-assist index

Also writes docs/KNOWLEDGE-MATURITY.md — W (reusability) vs R (evidence)
aggregated across Sheets + Applications. Does not invent a parallel E-scale.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .util import (
    KEBAB,
    VALID_EVIDENCE_SCOPE,
    extract_yaml_blocks,
    maturity_rank,
    max_maturity,
    read_text,
    repo_root,
    today,
)

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

SCOPE_ORDER = ("LAB", "FIELD", "HOST-SPECIFIC", "DEVICE-SPECIFIC", "GENERAL")


@dataclass
class SheetEntry:
    slug: str
    title: str
    primary: str
    reusability: str
    technology: str = "R?"
    field_evidence_sheet: str = "R?"
    evidence_max: str = "R0"
    evidence_scope: list[str] = field(default_factory=list)
    evidence_scope_source: str = "derived"
    tags: list[str] = field(default_factory=list)
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


def _as_str_list(raw: Any) -> list[str]:
    if raw is None:
        return []
    if isinstance(raw, str):
        return [raw] if raw.strip() else []
    if isinstance(raw, list):
        return [str(x).strip() for x in raw if str(x).strip()]
    return []


def collect_app_evidence_max(root: Path) -> dict[str, str]:
    """Per tech slug: max Application maturity.field_evidence (R0–R5)."""
    out: dict[str, str] = {}
    projects = root / "projects"
    if not projects.is_dir():
        return out
    for proj in projects.iterdir():
        apps = proj / "applications"
        if not apps.is_dir():
            continue
        for path in apps.glob("*.md"):
            blocks = extract_yaml_blocks(read_text(path))
            if not blocks:
                continue
            meta = blocks[0]
            slug = str(meta.get("tech_slug") or meta.get("slug") or path.stem).strip()
            maturity = meta.get("maturity") if isinstance(meta.get("maturity"), dict) else {}
            fe = str(maturity.get("field_evidence") or "R0").split()[0]
            if not fe.startswith("R"):
                continue
            out[slug] = max_maturity(out.get(slug, "R0"), fe, prefix="R")
    return out


def normalize_evidence_scope(raw: Any) -> list[str]:
    items = _as_str_list(raw)
    seen: list[str] = []
    for item in items:
        key = item.upper().replace("_", "-")
        if key in VALID_EVIDENCE_SCOPE and key not in seen:
            seen.append(key)
    return [s for s in SCOPE_ORDER if s in seen]


def derive_evidence_scope(
    *,
    primary: str,
    tags: list[str],
    reusability: str,
    evidence_max: str,
) -> list[str]:
    """Infer scope from ranks + host/device hints when Sheet omits evidence_scope.

    LAB/FIELD follow evidence_max only (R3+/R4+) — never from tags like lab-only.
    Tags describe intent; inventing LAB without R3 would reintroduce false evidence.
    Explicit Sheet evidence_scope remains the override for host/device/field nuance.
    """
    tags_l = {t.lower() for t in tags}
    scopes: set[str] = set()
    er = maturity_rank(evidence_max)
    wr = maturity_rank(reusability)

    if er >= 3:
        scopes.add("LAB")
    if er >= 4:
        scopes.add("FIELD")

    if "automotive" in tags_l and primary == "I":
        scopes.add("HOST-SPECIFIC")
    elif primary == "I":
        scopes.add("DEVICE-SPECIFIC")

    # GENERAL: reusable A-pattern with lab+ evidence, not host/device-locked
    if (
        wr >= 3
        and er >= 3
        and "HOST-SPECIFIC" not in scopes
        and "DEVICE-SPECIFIC" not in scopes
    ):
        scopes.add("GENERAL")

    return [s for s in SCOPE_ORDER if s in scopes]


def collect_sheets(root: Path) -> list[SheetEntry]:
    tech = root / "technologies"
    entries: list[SheetEntry] = []
    app_fe = collect_app_evidence_max(root)
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
        tech_r = str(maturity.get("technology") or "R?").split()[0]
        sheet_fe = str(maturity.get("field_evidence") or "R?").split()[0]
        tags = _as_str_list(meta.get("tags"))
        evidence_max = max_maturity(
            sheet_fe if sheet_fe.startswith("R") else "R0",
            app_fe.get(slug, "R0"),
            prefix="R",
        )
        explicit_scope = normalize_evidence_scope(maturity.get("evidence_scope"))
        if explicit_scope:
            scope = explicit_scope
            scope_src = "sheet"
            for bad in _as_str_list(maturity.get("evidence_scope")):
                key = bad.upper().replace("_", "-")
                if key not in VALID_EVIDENCE_SCOPE:
                    errors.append(f"invalid evidence_scope '{bad}'")
        else:
            scope = derive_evidence_scope(
                primary=primary or "?",
                tags=tags,
                reusability=reus,
                evidence_max=evidence_max,
            )
            scope_src = "derived"
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
                technology=tech_r,
                field_evidence_sheet=sheet_fe,
                evidence_max=evidence_max,
                evidence_scope=scope,
                evidence_scope_source=scope_src,
                tags=tags,
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
        "# Source of truth: technologies/*/SHEET.md (+ app field_evidence → evidence_max)",
        "# Regenerate: python3 tools/ta-assist index",
        "# Do not hand-edit sheet rows.",
        "# reusability=W* (transfer); evidence_max=R* = max declared field_evidence (sheet∪apps);",
        "# evidence_max ≠ 'all A-claims validated'; always read with evidence_scope.",
        "# evidence_scope=LAB|FIELD|HOST-SPECIFIC|DEVICE-SPECIFIC|GENERAL",
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
        lines.append(f"    technology: {yaml_scalar(e.technology)}")
        lines.append(f"    field_evidence_sheet: {yaml_scalar(e.field_evidence_sheet)}")
        lines.append(f"    evidence_max: {yaml_scalar(e.evidence_max)}")
        lines.append(f"    evidence_scope: {yaml_list(e.evidence_scope)}")
        lines.append(f"    evidence_scope_source: {yaml_scalar(e.evidence_scope_source)}")
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
        "**Familien:** [`docs/FAMILIES.md`](../docs/FAMILIES.md) · **Standard:** [`VERSION`](../VERSION) · "
        "**Maturity:** [`docs/KNOWLEDGE-MATURITY.md`](../docs/KNOWLEDGE-MATURITY.md)",
        "",
        f"**Maschinenindex:** [`index.yaml`](index.yaml) (generiert — `{today()}`, {len(entries)} Sheets). "
        "Neu generieren: `python3 tools/ta-assist index`",
        "",
        "Spalten: **W** = Reusability · **Evid** = `evidence_max` (stärkste Lab/Feld-Belege aus Sheet∪Applications) · "
        "nicht verwechseln mit Projekt-Status (Prototype/Pilot).",
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
        lines.append("| Slug | Title | W | Evid | Scope | Gesehen in |")
        lines.append("|------|-------|---|------|-------|------------|")
        for e in sorted(group, key=lambda x: x.slug):
            seen = ", ".join(f"`{s}`" for s in e.seen_in) if e.seen_in else "—"
            scope = ", ".join(e.evidence_scope) if e.evidence_scope else "—"
            lines.append(
                f"| [`{md_cell(e.slug)}`]({e.slug}/SHEET.md) | {md_cell(e.title)} | "
                f"{md_cell(e.reusability)} | {md_cell(e.evidence_max)} | {md_cell(scope)} | "
                f"{md_cell(seen)} |"
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


def _count_prefix(entries: list[SheetEntry], attr: str, prefix: str) -> dict[str, int]:
    c: Counter[str] = Counter()
    for e in entries:
        val = str(getattr(e, attr) or "").split()[0]
        if val.startswith(prefix):
            c[val] += 1
        else:
            c["?"] += 1
    return dict(sorted(c.items(), key=lambda kv: (kv[0][0], maturity_rank(kv[0]))))


def write_knowledge_maturity(root: Path, entries: list[SheetEntry]) -> Path:
    """Machine-oriented maturity overview — generated, do not hand-edit."""
    out = root / "docs" / "KNOWLEDGE-MATURITY.md"
    w_dist = _count_prefix(entries, "reusability", "W")
    e_dist = _count_prefix(entries, "evidence_max", "R")
    scope_c: Counter[str] = Counter()
    for e in entries:
        if e.evidence_scope:
            for s in e.evidence_scope:
                scope_c[s] += 1
        else:
            scope_c["(none)"] += 1

    strong = [
        e
        for e in entries
        if maturity_rank(e.evidence_max) >= 3 and maturity_rank(e.reusability) >= 3
    ]
    strong.sort(key=lambda x: (-maturity_rank(x.evidence_max), -maturity_rank(x.reusability), x.slug))

    weak_w = [
        e
        for e in entries
        if maturity_rank(e.reusability) >= 3 and maturity_rank(e.evidence_max) <= 1
    ]
    weak_w.sort(key=lambda x: (x.reusability, x.slug))

    limited = [
        e
        for e in entries
        if maturity_rank(e.evidence_max) >= 3
        and (
            maturity_rank(e.reusability) <= 2
            or "HOST-SPECIFIC" in e.evidence_scope
            or "DEVICE-SPECIFIC" in e.evidence_scope
        )
    ]
    limited.sort(key=lambda x: (-maturity_rank(x.evidence_max), x.slug))

    def dist_table(d: dict[str, int]) -> list[str]:
        rows = ["| Stufe | Anzahl |", "|-------|--------|"]
        for k, v in d.items():
            rows.append(f"| {k} | {v} |")
        return rows

    lines = [
        "# Knowledge Maturity (generated)",
        "",
        f"Generated by `ta-assist index` — `{today()}`. **Do not hand-edit.**",
        "",
        "Source: Sheet YAML + max `maturity.field_evidence` across Applications.",
        "",
        "## Do not confuse these axes",
        "",
        "| Axis | Scale | Means | Does **not** mean |",
        "|------|-------|-------|-------------------|",
        "| **Reusability** | W0–W5 | How transferable the *technology sheet* is | How well it was measured |",
        "| **Evidence** | R0–R5 (`evidence_max`) | Max *declared* `field_evidence` over Sheet∪Applications | Universal tech validation / every A-claim proven |",
        "| **Evidence scope** | LAB / FIELD / HOST-SPECIFIC / DEVICE-SPECIFIC / GENERAL | Context + generalization bound for that evidence | Same as a high R alone |",
        "| **Project status** | SCOPE / audits | Lifecycle of one repo/campaign | KB technology maturity |",
        "",
        "**Reading rule:** `HOST-SPECIFIC R3` ≠ `GENERAL R3`. Same R, different transfer rights.",
        "",
        "Sheet `field_evidence` is often **R0 by design** (details live in Applications).",
        "Always read **`evidence_max`**, not only the Sheet row. Missing/invalid app R → ignored (treated as absent).",
        "",
        "Derived LAB/FIELD require `evidence_max` ≥ R3 / ≥ R4. Tags like `lab-only` do **not** invent LAB.",
        "Explicit Sheet `evidence_scope` may still mark FIELD at R3 when field *context* exists but strength stays R3.",
        "",
        "There is **no E0–E4 scale** here — that would collide with Review-Check IDs (E1–E4)",
        "and duplicate `field_evidence` R0–R5. Map “evidence strength” → **R**.",
        "",
        f"**Sheets:** {len(entries)} · Detail index: [`technologies/index.yaml`](../technologies/index.yaml)",
        "",
        "## Distribution — Reusability (W)",
        "",
        *dist_table(w_dist),
        "",
        "## Distribution — Evidence (`evidence_max` R)",
        "",
        *dist_table(e_dist),
        "",
        "## Distribution — Evidence scope (multi-label)",
        "",
        "| Scope | Sheets (count) |",
        "|-------|----------------|",
    ]
    for s in list(SCOPE_ORDER) + ["(none)"]:
        if s in scope_c:
            lines.append(f"| {s} | {scope_c[s]} |")
    for s, n in sorted(scope_c.items()):
        if s not in SCOPE_ORDER and s != "(none)":
            lines.append(f"| {s} | {n} |")

    lines.extend(
        [
            "",
            "## Strong reuse + strong evidence (W≥3 and evidence_max≥R3)",
            "",
            "| Slug | W | Evid | Scope | seen_in |",
            "|------|---|------|-------|---------|",
        ]
    )
    if strong:
        for e in strong:
            scope = ", ".join(e.evidence_scope) or "—"
            seen = ", ".join(f"`{s}`" for s in e.seen_in) or "—"
            lines.append(
                f"| [`{e.slug}`](../{e.path}) | {e.reusability} | {e.evidence_max} | "
                f"{scope} | {seen} |"
            )
    else:
        lines.append("| — | — | — | — | — |")

    lines.extend(
        [
            "",
            "## W3/W4 with weak evidence (evidence_max≤R1)",
            "",
            "Reusable on paper; do **not** treat as empirically settled.",
            "",
            "| Slug | W | Evid | Scope |",
            "|------|---|------|-------|",
        ]
    )
    if weak_w:
        for e in weak_w:
            scope = ", ".join(e.evidence_scope) or "—"
            lines.append(
                f"| [`{e.slug}`](../{e.path}) | {e.reusability} | {e.evidence_max} | {scope} |"
            )
    else:
        lines.append("| — | — | — | — |")

    lines.extend(
        [
            "",
            "## Strong evidence, limited generalizability",
            "",
            "High `evidence_max`, but W≤W2 and/or HOST-/DEVICE-SPECIFIC scope.",
            "",
            "| Slug | W | Evid | Scope | Why limited |",
            "|------|---|------|-------|-------------|",
        ]
    )
    if limited:
        for e in limited:
            scope = ", ".join(e.evidence_scope) or "—"
            reasons = []
            if maturity_rank(e.reusability) <= 2:
                reasons.append(f"reusability {e.reusability}")
            for tag in ("HOST-SPECIFIC", "DEVICE-SPECIFIC"):
                if tag in e.evidence_scope:
                    reasons.append(tag)
            lines.append(
                f"| [`{e.slug}`](../{e.path}) | {e.reusability} | {e.evidence_max} | "
                f"{scope} | {'; '.join(reasons) or '—'} |"
            )
    else:
        lines.append("| — | — | — | — | — |")

    lines.extend(
        [
            "",
            "## How to read this as an AI reviewer",
            "",
            "1. Open [`technologies/index.yaml`](../technologies/index.yaml) — not only `projects/`.",
            "2. Judge **W** and **evidence_max** separately; never infer KB maturity from Pilot/Prototype labels.",
            "3. Pair every R with `evidence_scope` — `W1/R3 HOST-SPECIFIC` is not `W3/R3 GENERAL`.",
            "4. Sheet `field_evidence: R0` + Application R3 is normal — use `evidence_max`.",
            "5. `evidence_max` is a ceiling of declared labels, not proof that all Sheet A-claims hold.",
            "6. Epistemic claim tags stay FACT / MEASURED / INFERENCE / HYPOTHESIS / UNKNOWN / REJECTED.",
            "",
            "Regenerate: `python3 tools/ta-assist index`",
            "",
        ]
    )
    out.parent.mkdir(parents=True, exist_ok=True)
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
    maturity_md = write_knowledge_maturity(root, entries)
    proj_yml = write_projects_index_yaml(root, projects)
    proj_md = write_projects_readme(root, projects)
    return {
        "sheet_count": len(entries),
        "project_count": len(projects),
        "index_yaml": str(tech_yml.relative_to(root)),
        "readme": str(tech_md.relative_to(root)),
        "knowledge_maturity": str(maturity_md.relative_to(root)),
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
