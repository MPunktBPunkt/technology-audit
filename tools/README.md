# tools/

Assistenz für `technology-audit`: Strukturprüfung, Prompt-Vorbereitung, **Katalog-Index**.

Schreibt **keine** Sheet-/Application-/Evidence-Inhalte. Erlaubt ist nur die Regenerierung von `technologies/index.yaml` + `technologies/README.md` aus Sheet-YAML (`ta-assist index`).

Vertrag: [`docs/PROMPT-CONTRACT.md`](../docs/PROMPT-CONTRACT.md) · Prüfliste: [`docs/REVIEW-CHECKS.md`](../docs/REVIEW-CHECKS.md) · Pflege: [`docs/MAINTENANCE.md`](../docs/MAINTENANCE.md)

## Versionierung

| Was | Wo | Bedeutung |
|-----|-----|-----------|
| **Framework** | [`VERSION`](../VERSION) | Dokumentenstandard (z. B. 0.6.4) |
| **CLI** | `tools/ta_assist/__init__.py` → `__version__` | Assistenz-Tool (z. B. 0.1.5) |

### CLI 0.1.6

- Indexer: YAML/MD-Escaping; Projektkatalog `projects/index.yaml`
- Checks S9/S10/G2 bidirektional, RT1 retrieval-fixtures, R5 maturity hint

### CLI 0.1.5

- `ta-assist index` — Primary-gruppierte README + `index.yaml`
- Checks NAV1–NAV4, S8, C8 patch-lag info

### CLI 0.1.4

- Audit YAML: `standard_version` (C7–C9)

### CLI 0.1.3

- Bootstrap: `{{existing_sheets}}`

## Schnellstart

```bash
python3 tools/ta-assist index
python3 tools/ta-assist check
python3 tools/ta-assist prepare next
python3 tools/ta-assist prepare bootstrap https://github.com/example/repo
python3 tools/ta-assist scan
```

## Befehle

| Befehl | Zweck |
|--------|--------|
| `index` | Regeneriert Sheet-Katalog (Primary A–J) |
| `check` | Structure/Consistency → Exit 1 bei Errors |
| `scan` | Repo-Befund + Vorschlag nächster Prompt |
| `prepare next` / `bootstrap` | Prompt-Packs |
| `prompt <type>` | expliziter Prompt-Typ |

## Checker ↔ REVIEW-CHECKS

`checker.py` bildet einen **Teil** der REVIEW-CHECKS ab (Parität, Frontmatter, Evidence-IDs, Index). Semantik von Claims bleibt manuell/KI.

## GitHub Actions

- `audit-structure-check` — `index` (Diff-Exit) + `check`
- `audit-prompt-pack` — manuell
