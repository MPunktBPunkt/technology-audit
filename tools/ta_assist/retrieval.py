"""Generate audit INDEX + retrieval bundles from existing SoT (not a second truth)."""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .util import (
    extract_yaml_blocks,
    parse_md_tables,
    parse_simple_yaml,
    read_text,
    today,
    yaml_scalar,
)

# Broader than historic EVID-…-YYYY-MM-DD-NNN
EVIDENCE_ID_RE = re.compile(r"\bEVID-[A-Z0-9]+(?:-[A-Z0-9]+)+\b")
STATUS_RE = re.compile(
    r"`?(FACT|MEASURED|FIELD FACT|LAB FACT|DESK FACT|INFERENCE|INFERRED|"
    r"HYPOTHESIS|UNKNOWN|REJECTED|NOT PROVEN|NOT_PROVEN|NOT OBSERVED|NOT_OBSERVED|"
    r"OPEN|SUPERSEDED|STRONG|PARTIAL)[`\s]*",
    re.I,
)

EPISTEMIC_BUCKET = {
    "FACT": "facts",
    "MEASURED": "facts",
    "FIELD FACT": "facts",
    "LAB FACT": "facts",
    "DESK FACT": "facts",
    "STRONG": "facts",
    "INFERENCE": "inferences",
    "INFERRED": "inferences",
    "HYPOTHESIS": "hypotheses",
    "UNKNOWN": "unknowns",
    "OPEN": "unknowns",
    "PARTIAL": "unknowns",
    "NOT PROVEN": "unknowns",
    "NOT_PROVEN": "unknowns",
    "NOT OBSERVED": "unknowns",
    "NOT_OBSERVED": "unknowns",
    "REJECTED": "rejected",
    "SUPERSEDED": "rejected",
}


@dataclass
class AuditRecord:
    directory: str
    audit_id: str = ""
    id: str = ""
    project_id: str = ""
    status: str = ""
    profile: str = ""
    started: str = ""
    ended: str = ""
    standard_version: str = ""
    display_name: str = ""
    technologies: list[str] = field(default_factory=list)
    environment: str = ""
    evidence_ids: list[str] = field(default_factory=list)
    claims: list[dict[str, Any]] = field(default_factory=list)
    path: str = ""


def _norm_status(raw: str) -> str:
    s = raw.strip().strip("`").upper().replace("_", " ")
    s = re.sub(r"\s+", " ", s)
    aliases = {
        "FIELD FACT": "FACT",
        "LAB FACT": "FACT",
        "DESK FACT": "FACT",
        "MEASURED": "FACT",
        "STRONG": "FACT",
        "INFERRED": "INFERENCE",
        "NOT PROVEN": "NOT_PROVEN",
        "NOT OBSERVED": "NOT_OBSERVED",
    }
    return aliases.get(s, s.replace(" ", "_") if s in {"NOT PROVEN", "NOT OBSERVED"} else s)


def _bucket_for(status: str) -> str:
    key = status.upper().replace("_", " ")
    if status.upper() in EPISTEMIC_BUCKET:
        return EPISTEMIC_BUCKET[status.upper()]
    return EPISTEMIC_BUCKET.get(key, "unknowns")


def _infer_environment(profile: str, text: str) -> str:
    p = (profile or "").lower()
    t = text.lower()
    if "ops-field" in p or "field fact" in t or "field_" in t:
        if "lab" in t and "field" in t:
            return "mixed"
        return "field"
    if "lab-tool" in p or "lab fact" in t:
        return "lab"
    if "planning" in p or "desk" in t:
        return "desk"
    return "mixed"


def _infer_technologies(text: str, known: set[str]) -> list[str]:
    found: list[str] = []
    # prefer longer slugs first
    for slug in sorted(known, key=len, reverse=True):
        if re.search(rf"(?<![a-z0-9-]){re.escape(slug)}(?![a-z0-9-])", text, re.I):
            found.append(slug)
    return found[:12]


def _extract_fallstricke(text: str) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for table in parse_md_tables(text):
        if len(table) < 2:
            continue
        header = [h.lower() for h in table[0]]
        if not any("claim" in h or "aussage" in h for h in header):
            continue
        claim_i = next((i for i, h in enumerate(header) if "claim" in h or "aussage" in h), 0)
        status_i = next((i for i, h in enumerate(header) if "status" in h), 1)
        note_i = next(
            (i for i, h in enumerate(header) if "hinweis" in h or "note" in h or "evidence" in h),
            None,
        )
        for row in table[1:]:
            if claim_i >= len(row) or status_i >= len(row):
                continue
            claim = row[claim_i].strip()
            status_cell = row[status_i].strip()
            m = STATUS_RE.search(status_cell)
            if not claim or not m:
                continue
            st = _norm_status(m.group(1))
            note = row[note_i].strip() if note_i is not None and note_i < len(row) else status_cell
            out.append({"statement": claim, "status": st, "note": note})
    return out


def _load_claims_yaml(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    text = read_text(path)
    # allow fenced or raw yaml
    blocks = extract_yaml_blocks(text)
    if blocks and "claims" in blocks[0]:
        # simple parser may not parse list-of-maps; fall through to line scan
        pass
    # Prefer full parse via naive split on "- id:"
    claims: list[dict[str, Any]] = []
    if "claims:" not in text:
        return claims
    chunks = re.split(r"\n\s*-\s+id:\s*", "\n" + text)
    for chunk in chunks[1:]:
        lines = chunk.splitlines()
        if not lines:
            continue
        cid = lines[0].strip().strip("'\"")
        body = "id: " + cid + "\n" + "\n".join(lines[1:])
        # Take until next top-level key that isn't indented claim fields — parse_simple works for flat
        data = parse_simple_yaml(body)
        # lists in supported_by etc.
        claim = {
            "id": cid,
            "statement": str(data.get("statement") or "").strip(),
            "status": _norm_status(str(data.get("status") or "UNKNOWN")),
            "supported_by": data.get("supported_by") if isinstance(data.get("supported_by"), list) else [],
            "contradicted_by": data.get("contradicted_by")
            if isinstance(data.get("contradicted_by"), list)
            else [],
            "transfer_limits": data.get("transfer_limits")
            if isinstance(data.get("transfer_limits"), list)
            else [],
            "unknown_reason": data.get("unknown_reason"),
            "environment": data.get("environment"),
        }
        scope = data.get("scope") if isinstance(data.get("scope"), dict) else {}
        if scope:
            claim["scope"] = scope
        # Fix list fields if scalars were empty
        for key in ("supported_by", "contradicted_by", "transfer_limits"):
            if not isinstance(claim[key], list):
                claim[key] = []
        # Re-read list lines manually for reliability
        for key in ("supported_by", "contradicted_by", "transfer_limits", "limited_by"):
            m = re.search(rf"{key}:\s*\[(.*?)\]", body, re.S)
            if m:
                inner = m.group(1).strip()
                claim[key] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()] if inner else []
        if claim["statement"]:
            claims.append(claim)
    return claims


def collect_audits(root: Path, known_slugs: set[str]) -> list[AuditRecord]:
    audits_dir = root / "audits"
    records: list[AuditRecord] = []
    if not audits_dir.is_dir():
        return records
    for d in sorted(audits_dir.iterdir()):
        if not d.is_dir() or d.name.startswith(".") or d.name.startswith("_"):
            continue
        readme = d / "README.md"
        if not readme.is_file():
            continue
        text = read_text(readme)
        blocks = extract_yaml_blocks(text)
        meta = blocks[0] if blocks else {}
        # display name = first markdown H1
        display = d.name
        for line in text.splitlines():
            if line.startswith("# "):
                display = line[2:].strip()
                break
        evid = sorted(set(EVIDENCE_ID_RE.findall(text)))
        claims_path = d / "claims.yaml"
        claims = _load_claims_yaml(claims_path)
        for c in claims:
            for e in c.get("supported_by") or []:
                if e not in evid:
                    evid.append(e)
        techs = meta.get("technologies") if isinstance(meta.get("technologies"), list) else []
        if not techs:
            techs = _infer_technologies(text, known_slugs)
        # related from YAML related_audits unused for tech
        rec = AuditRecord(
            directory=d.name,
            id=str(meta.get("id") or d.name),
            project_id=str(meta.get("project_id") or ""),
            status=str(meta.get("status") or ""),
            profile=str(meta.get("profile") or ""),
            started=str(meta.get("started") or ""),
            ended="" if meta.get("ended") in (None, "null") else str(meta.get("ended") or ""),
            standard_version=str(meta.get("standard_version") or "").strip().strip("\"'"),
            display_name=display,
            technologies=list(techs),
            environment=_infer_environment(str(meta.get("profile") or ""), text),
            evidence_ids=evid,
            claims=claims,
            path=f"audits/{d.name}",
        )
        # optional explicit audit_id in YAML
        if meta.get("audit_id"):
            rec.audit_id = str(meta.get("audit_id")).strip()
        records.append(rec)
    _assign_audit_ids(records)
    return records


def _assign_audit_ids(records: list[AuditRecord]) -> None:
    """Deterministic A-YYYY-NNN from started date + directory (immutable across regenerations)."""
    by_year: dict[str, list[AuditRecord]] = defaultdict(list)
    for r in records:
        year = "0000"
        if re.match(r"^\d{4}-\d{2}-\d{2}", r.started or ""):
            year = r.started[:4]
        else:
            m = re.search(r"(20\d{2})", r.directory)
            if m:
                year = m.group(1)
        by_year[year].append(r)
    for year, group in by_year.items():
        group.sort(key=lambda r: (r.started or "9999", r.directory))
        for i, r in enumerate(group, start=1):
            if not r.audit_id:
                r.audit_id = f"A-{year}-{i:03d}"


def load_retrieval_topics(root: Path) -> list[dict[str, Any]]:
    path = root / "docs" / "retrieval-topics.yaml"
    if not path.is_file():
        return []
    text = read_text(path)
    topics: list[dict[str, Any]] = []
    # split on "- id:"
    parts = re.split(r"\n\s*-\s+id:\s*", "\n" + text)
    for part in parts[1:]:
        lines = part.splitlines()
        tid = lines[0].strip().strip("'\"")
        body = "id: " + tid + "\n" + "\n".join(lines[1:])
        data = parse_simple_yaml(body)
        topic = {"id": tid, **{k: v for k, v in data.items() if k != "id"}}
        for key in ("technologies", "audits", "methods", "applications", "transfer_limits", "keywords"):
            m = re.search(rf"{key}:\s*\[(.*?)\]", body, re.S)
            if m:
                inner = m.group(1).strip()
                topic[key] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()] if inner else []
        topics.append(topic)
    return topics


def _apps_for_slug(root: Path, slug: str) -> list[str]:
    out: list[str] = []
    projects = root / "projects"
    if not projects.is_dir():
        return out
    for p in sorted(projects.iterdir()):
        app = p / "applications" / f"{slug}.md"
        if app.is_file():
            out.append(f"projects/{p.name}/applications/{slug}.md")
    return out


def _methods_mentioned(text: str, root: Path) -> list[str]:
    methods_dir = root / "methods"
    if not methods_dir.is_dir():
        return []
    names = [p.stem for p in methods_dir.glob("*.md") if p.name != "README.md"]
    found = []
    for name in sorted(names, key=len, reverse=True):
        if name in text or f"methods/{name}" in text:
            found.append(f"methods/{name}.md")
    return found[:8]


def build_bundle_for_slug(
    root: Path,
    slug: str,
    sheet_text: str,
    sheet_meta: dict[str, Any],
    audits: list[AuditRecord],
) -> dict[str, Any]:
    fall = _extract_fallstricke(sheet_text)
    facts, inferences, hypotheses, unknowns, rejected = [], [], [], [], []
    for item in fall:
        entry = {
            "statement": item["statement"],
            "status": item["status"],
            "source": f"technologies/{slug}/SHEET.md",
        }
        bucket = _bucket_for(item["status"])
        {
            "facts": facts,
            "inferences": inferences,
            "hypotheses": hypotheses,
            "unknowns": unknowns,
            "rejected": rejected,
        }[bucket].append(entry)

    related_audits = [a for a in audits if slug in a.technologies or slug in a.directory]
    # also match if sheet slug in audit evidence path mentions
    for a in audits:
        if a in related_audits:
            continue
        if slug.replace("-", "") in a.directory.replace("-", ""):
            related_audits.append(a)

    for a in related_audits:
        for c in a.claims:
            entry = {
                "id": c.get("id"),
                "statement": c.get("statement"),
                "status": c.get("status"),
                "source": f"{a.path}/claims.yaml",
                "supported_by": c.get("supported_by") or [],
                "transfer_limits": c.get("transfer_limits") or [],
                "unknown_reason": c.get("unknown_reason"),
                "scope": c.get("scope") or {},
                "audit_id": a.audit_id,
            }
            bucket = _bucket_for(str(c.get("status") or "UNKNOWN"))
            {
                "facts": facts,
                "inferences": inferences,
                "hypotheses": hypotheses,
                "unknowns": unknowns,
                "rejected": rejected,
            }[bucket].append(entry)

    maturity = sheet_meta.get("maturity") if isinstance(sheet_meta.get("maturity"), dict) else {}
    transfer_limits: list[str] = []
    scope_list = maturity.get("evidence_scope") if isinstance(maturity.get("evidence_scope"), list) else []
    if "HOST-SPECIFIC" in [str(x).upper() for x in scope_list]:
        transfer_limits.append("host_specific")
    if "DEVICE-SPECIFIC" in [str(x).upper() for x in scope_list]:
        transfer_limits.append("device_specific")
    if any("nicht" in (x.get("statement") or "").lower() for x in rejected):
        transfer_limits.append("see_rejected_claims")

    # Abgrenzung bullets as soft transfer limits
    if "## Abgrenzung" in sheet_text:
        section = sheet_text.split("## Abgrenzung", 1)[1].split("\n## ", 1)[0]
        for line in section.splitlines():
            if line.strip().startswith("- **Ist nicht:**"):
                transfer_limits.append("sheet_abgrenzung_ist_nicht")
                break

    evid = sorted({e for a in related_audits for e in a.evidence_ids})
    methods = _methods_mentioned(sheet_text, root)
    for a in related_audits:
        methods.extend(_methods_mentioned(read_text(root / a.path / "README.md"), root))
    methods = sorted(set(methods))

    return {
        "topic": slug,
        "generated": today(),
        "source_of_truth": [
            f"technologies/{slug}/SHEET.md",
            *[f"{a.path}/README.md" for a in related_audits[:20]],
        ],
        "primary": [slug],
        "maturity": {
            "technology": maturity.get("technology"),
            "field_evidence": maturity.get("field_evidence"),
            "reusability": maturity.get("reusability"),
            "evidence_scope": scope_list,
        },
        "applications": _apps_for_slug(root, slug),
        "audits": [
            {
                "audit_id": a.audit_id,
                "directory": a.directory,
                "status": a.status,
                "environment": a.environment,
                "path": a.path,
            }
            for a in sorted(related_audits, key=lambda x: x.audit_id)
        ],
        "methods": methods,
        "evidence_ids": evid,
        "facts": facts[:80],
        "inferences": inferences[:40],
        "hypotheses": hypotheses[:40],
        "unknowns": unknowns[:40],
        "rejected": rejected[:40],
        "transfer_limits": sorted(set(transfer_limits)),
        "note": "GENERATED — do not hand-edit; regenerate via ta-assist index",
    }


def build_topic_bundle(
    root: Path,
    topic: dict[str, Any],
    audits: list[AuditRecord],
    sheet_bundles: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    tid = topic["id"]
    techs = topic.get("technologies") or []
    facts, rejected, unknowns, inferences = [], [], [], []
    evid: list[str] = []
    audit_refs = []
    apps: list[str] = []
    methods: list[str] = []
    transfer = list(topic.get("transfer_limits") or [])

    for slug in techs:
        b = sheet_bundles.get(slug)
        if not b:
            continue
        facts.extend(b.get("facts") or [])
        rejected.extend(b.get("rejected") or [])
        unknowns.extend(b.get("unknowns") or [])
        inferences.extend(b.get("inferences") or [])
        evid.extend(b.get("evidence_ids") or [])
        apps.extend(b.get("applications") or [])
        methods.extend(b.get("methods") or [])
        transfer.extend(b.get("transfer_limits") or [])
        audit_refs.extend(b.get("audits") or [])

    # explicit audit dirs from topic
    dir_set = set(topic.get("audits") or [])
    for a in audits:
        if a.directory in dir_set or a.audit_id in dir_set:
            audit_refs.append(
                {
                    "audit_id": a.audit_id,
                    "directory": a.directory,
                    "status": a.status,
                    "environment": a.environment,
                    "path": a.path,
                }
            )
            evid.extend(a.evidence_ids)
            for c in a.claims:
                entry = {
                    "id": c.get("id"),
                    "statement": c.get("statement"),
                    "status": c.get("status"),
                    "source": f"{a.path}/claims.yaml",
                    "supported_by": c.get("supported_by") or [],
                    "transfer_limits": c.get("transfer_limits") or [],
                    "audit_id": a.audit_id,
                }
                bucket = _bucket_for(str(c.get("status") or "UNKNOWN"))
                {
                    "facts": facts,
                    "inferences": inferences,
                    "hypotheses": [],
                    "unknowns": unknowns,
                    "rejected": rejected,
                }.get(bucket, unknowns).append(entry)

    # dedupe audits by directory
    seen_a = set()
    audits_out = []
    for a in audit_refs:
        key = a.get("directory") or a.get("audit_id")
        if key in seen_a:
            continue
        seen_a.add(key)
        audits_out.append(a)

    return {
        "topic": tid,
        "title": topic.get("title") or tid,
        "question": topic.get("question") or "",
        "generated": today(),
        "primary": techs,
        "applications": sorted(set(apps)),
        "audits": audits_out,
        "methods": sorted(set(methods + (topic.get("methods") or []))),
        "evidence_ids": sorted(set(evid)),
        "facts": facts[:100],
        "inferences": inferences[:50],
        "unknowns": unknowns[:50],
        "rejected": rejected[:50],
        "transfer_limits": sorted(set(transfer)),
        "note": "GENERATED from docs/retrieval-topics.yaml + SoT — do not hand-edit",
    }


def _emit_yaml_value(v: Any, indent: int = 0) -> list[str]:
    sp = "  " * indent
    if isinstance(v, dict):
        if not v:
            return ["{}"]
        lines = []
        for k, val in v.items():
            if isinstance(val, (dict, list)):
                if not val:
                    lines.append(f"{sp}{k}: []" if isinstance(val, list) else f"{sp}{k}: {{}}")
                else:
                    lines.append(f"{sp}{k}:")
                    nested = _emit_yaml_value(val, indent + 1)
                    if isinstance(val, dict):
                        lines.extend(nested)
                    else:
                        lines.extend(nested)
            else:
                lines.append(f"{sp}{k}: {yaml_scalar(val)}")
        return lines
    if isinstance(v, list):
        if not v:
            return [f"{sp}[]"]
        lines = []
        for item in v:
            if isinstance(item, dict):
                lines.append(f"{sp}-")
                for k, val in item.items():
                    if isinstance(val, (dict, list)) and val:
                        lines.append(f"{sp}  {k}:")
                        for nl in _emit_yaml_value(val, indent + 2):
                            lines.append(nl)
                    elif isinstance(val, list) and not val:
                        lines.append(f"{sp}  {k}: []")
                    else:
                        lines.append(f"{sp}  {k}: {yaml_scalar(val)}")
            else:
                lines.append(f"{sp}- {yaml_scalar(item)}")
        return lines
    return [f"{sp}{yaml_scalar(v)}"]


def write_yaml_doc(path: Path, header_comment: str, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {header_comment}", f"# generated: {today()}", ""]
    for k, v in data.items():
        if isinstance(v, (dict, list)):
            if not v:
                lines.append(f"{k}: []" if isinstance(v, list) else f"{k}: {{}}")
            else:
                lines.append(f"{k}:")
                for nl in _emit_yaml_value(v, 1):
                    lines.append(nl)
        else:
            lines.append(f"{k}: {yaml_scalar(v)}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def regenerate_retrieval(root: Path) -> dict[str, Any]:
    from .indexer import collect_sheets

    sheets = collect_sheets(root)
    known = {e.slug for e in sheets if not e.errors}
    audits = collect_audits(root, known)

    # audits/INDEX.yaml
    audit_index = {
        "schema": "technology-audit.audits-index.v1",
        "generated": today(),
        "count": len(audits),
        "note": "GENERATED by ta-assist — directory names unchanged; audit_id is stable",
        "audits": [
            {
                "audit_id": a.audit_id,
                "directory": a.directory,
                "id": a.id,
                "display_name": a.display_name,
                "project_id": a.project_id,
                "status": a.status,
                "profile": a.profile,
                "environment": a.environment,
                "started": a.started,
                "ended": a.ended or None,
                "standard_version": a.standard_version,
                "technologies": a.technologies,
                "evidence_count": len(a.evidence_ids),
                "claims_count": len(a.claims),
                "path": a.path,
            }
            for a in sorted(audits, key=lambda x: x.audit_id)
        ],
    }
    write_yaml_doc(
        root / "audits" / "INDEX.yaml",
        "GENERATED — do not hand-edit. Source: audits/*/README.md YAML",
        audit_index,
    )

    out_dir = root / "generated" / "retrieval"
    bundles_dir = out_dir / "bundles"
    bundles_dir.mkdir(parents=True, exist_ok=True)

    # Prefer sheets with field evidence or any fallstricke / related audits
    sheet_bundles: dict[str, dict[str, Any]] = {}
    for e in sheets:
        if e.errors:
            continue
        sheet_path = root / e.path
        text = read_text(sheet_path)
        blocks = extract_yaml_blocks(text)
        meta = blocks[0] if blocks else {}
        related = [a for a in audits if e.slug in a.technologies]
        fall = _extract_fallstricke(text)
        fe = str((meta.get("maturity") or {}).get("field_evidence") or e.field_evidence_sheet or "R0")
        if not fall and not related and not fe.startswith(("R2", "R3", "R4", "R5")):
            # still emit thin bundle for navigability of all active sheets? keep lean: only if useful
            if not e.seen_in:
                continue
        bundle = build_bundle_for_slug(root, e.slug, text, meta, audits)
        sheet_bundles[e.slug] = bundle
        write_yaml_doc(
            bundles_dir / f"{e.slug}.yaml",
            f"GENERATED retrieval bundle for {e.slug}",
            bundle,
        )

    topics = load_retrieval_topics(root)
    topic_ids = []
    for topic in topics:
        tid = topic["id"]
        topic_ids.append(tid)
        tb = build_topic_bundle(root, topic, audits, sheet_bundles)
        write_yaml_doc(
            bundles_dir / f"topic-{tid}.yaml",
            f"GENERATED topic bundle {tid}",
            tb,
        )

    master = {
        "schema": "technology-audit.retrieval-index.v1",
        "generated": today(),
        "model_doc": "docs/EVIDENCE-CLAIM-MODEL.md",
        "audit_index": "audits/INDEX.yaml",
        "bundle_count": len(sheet_bundles) + len(topic_ids),
        "tech_bundles": sorted(sheet_bundles.keys()),
        "topic_bundles": [f"topic-{t}" for t in topic_ids],
        "ai_entry": [
            "generated/retrieval/index.yaml",
            "audits/INDEX.yaml",
            "docs/EVIDENCE-CLAIM-MODEL.md",
            "docs/retrieval-topics.yaml",
            "docs/retrieval-tests.yaml",
        ],
        "rules": [
            "Bundles are derived views — Sheets/Audits remain SoT",
            "Always read rejected + transfer_limits + unknowns",
            "Do not invent a parallel AI_KNOWLEDGE.md",
        ],
    }
    write_yaml_doc(out_dir / "index.yaml", "GENERATED retrieval master index", master)

    readme = out_dir / "README.md"
    readme.write_text(
        "\n".join(
            [
                "# generated/retrieval/",
                "",
                "**GENERATED** by `python3 tools/ta-assist index`. Do not hand-edit.",
                "",
                "SoT remains `technologies/`, `projects/`, `audits/`.",
                "Model: [`docs/EVIDENCE-CLAIM-MODEL.md`](../../docs/EVIDENCE-CLAIM-MODEL.md).",
                "",
                "## Layout",
                "",
                "| Path | Role |",
                "|------|------|",
                "| `index.yaml` | Master retrieval index |",
                "| `bundles/<slug>.yaml` | Per-technology evidence bundle |",
                "| `bundles/topic-*.yaml` | Cross-cutting topic bundles |",
                "| `../../audits/INDEX.yaml` | Stable audit_id ↔ directory map |",
                "",
                "## AI usage",
                "",
                "1. Open `index.yaml` or a topic/tech bundle.",
                "2. Honor `rejected`, `unknowns`, `transfer_limits`.",
                "3. Follow `source_of_truth` / audit paths for depth.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    return {
        "audits_indexed": len(audits),
        "tech_bundles": len(sheet_bundles),
        "topic_bundles": len(topic_ids),
        "audit_index": "audits/INDEX.yaml",
        "retrieval_index": "generated/retrieval/index.yaml",
    }
