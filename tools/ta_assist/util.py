"""Shared helpers: paths, YAML fences, markdown tables."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

YAML_FENCE = re.compile(r"```yaml\s*\n(.*?)\n```", re.DOTALL | re.IGNORECASE)
EVIDENCE_ID = re.compile(r"EVID-[A-Z0-9]+-\d{4}-\d{2}-\d{2}-\d{3}")
MATURITY_R = re.compile(r"^R[0-5]$")
MATURITY_W = re.compile(r"^W[0-5]$")
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VALID_STATUS = {"candidate", "observed", "documented", "applied", "transferred"}
VALID_COVERAGE = {"none", "partial", "full"}
VALID_EPISTEMIC = {
    "FACT",
    "MEASURED",
    "INFERRED",
    "HYPOTHESIS",
    "UNKNOWN",
    "REJECTED",
}


def repo_root(path: Path | None = None) -> Path:
    p = (path or Path.cwd()).resolve()
    for cand in [p, *p.parents]:
        if (cand / "docs" / "DOCUMENT-STANDARD.md").is_file():
            return cand
    return p


def is_native(root: Path) -> bool:
    return (root / "docs" / "DOCUMENT-STANDARD.md").is_file()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_yaml_blocks(text: str) -> list[dict[str, Any]]:
    """Parse simple key: value / nested maturity YAML from fenced blocks."""
    out: list[dict[str, Any]] = []
    for m in YAML_FENCE.finditer(text):
        out.append(parse_simple_yaml(m.group(1)))
    return out


def parse_simple_yaml(raw: str) -> dict[str, Any]:
    """Minimal YAML subset: scalars, lists [a, b], nested indent one level."""
    data: dict[str, Any] = {}
    current_map: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        # nested under maturity: etc.
        if line.startswith("  ") and current_map:
            nested = line.strip()
            if ":" not in nested:
                continue
            k, v = nested.split(":", 1)
            k, v = k.strip(), v.strip()
            if not isinstance(data.get(current_map), dict):
                data[current_map] = {}
            data[current_map][k] = _scalar(v)
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key, val = key.strip(), val.strip()
        if val == "" or val.startswith("#"):
            current_map = key
            data[key] = {}
            continue
        current_map = None
        data[key] = _scalar(val)
    return data


def _scalar(v: str) -> Any:
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [x.strip().strip("'\"") for x in inner.split(",")]
    if v.lower() in {"null", "none", "~"}:
        return None
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v.strip("'\"")


def parse_md_tables(text: str) -> list[list[list[str]]]:
    """Return list of tables; each table is list of rows; row is list of cells."""
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
                continue  # separator
            current.append(cells)
        else:
            if current:
                tables.append(current)
                current = []
    if current:
        tables.append(current)
    return tables


def today() -> str:
    from datetime import date

    return date.today().isoformat()


def slugify_repo_name(name: str) -> str:
    name = name.lower().replace("_", "-").replace(".", "-")
    name = re.sub(r"[^a-z0-9-]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name or "project"
