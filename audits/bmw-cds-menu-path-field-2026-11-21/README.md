# Audit: CDS Menu Path Field (B3)

```yaml
id: bmw-cds-menu-path-field-2026-11-21
project_id: esp32-bt-analyzer
started: 2026-11-21
ended: 2026-11-23
status: closed
profile: ops-field
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits: [bmw-etch-rpc-binary-reassembly-2026-11-21, bmw-rhmi-music-handle23-field-2026-11-21]
reuse_outcomes:
  reused: [technologies/bmw-etch-rpc]
  new: []
  not_helped: []
  process: "Document CDS create/handler/get-set + Media/Radio→visibleContext 50034; reject CDS-as-track-bus."
```

## Ziel

CDS Property-Events und den beobachteten Menü-Pfad (Media/Radio → listIndex → visibleContext **50034**) als FIELD FACT festhalten; Track-Metadaten-Bus explizit **NOT PROVEN**.

## Scope

- Im Scope: `cds_create` / PropertyChangedHandler / get|setPropertyAsync; Property-Namen; Menu-Pfad FACT; Abgrenzung zu RHMI Track-Models.
- Nicht im Scope: vollständige Property-Semantik; Navigation/Vehicle Deep-Dive.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | CDS API-Präsenz FIELD FACT in etch-rpc Sheet | erfüllt |
| 2 | Menu-Pfad 50034 dokumentiert | erfüllt |
| 3 | Track-Bus NOT PROVEN | erfüllt |

## Claim-Level-Tabelle

| Claim | Level | Evidence |
|-------|-------|----------|
| `cds_create` + handlers + get/setPropertyAsync im Wire | **FIELD FACT** | method histogram / CDS_EVENTS |
| Properties u. a. `entertainment.multimedia`, `hmi.graphicalContext`, VIN/units/… | **FIELD FACT** | CDS_PROPERTY_COUNTS / ADDENDUM |
| Menu-Pfad Media/Radio → listIndex → visibleContext **50034** | **FIELD FACT** | EVAL Music section |
| CDS = Track-Metadaten-Bus (Artist/Title/Cover) | **NOT PROVEN** | EVAL; Track via RHMI H23 |
| Home Entry Object-ID via CDS | **NOT OBSERVED** | EVAL |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Track-Metadata wo suchen? | CDS oder RHMI? | H23 setData | RHMI; CDS nicht als Bus annehmen |

## Kill-Kriterien

**Hypothese:** CDS liefert in B3 Menü-/Fahrzeugkontext, nicht Now-Playing-Text.

| # | Kill | Status |
|---|------|--------|
| 1 | Artist/Title ausschließlich als CDS property values ohne RHMI setData | nicht eingetreten |

## Knowledge Feedback

| Evidence-ID | Zurück in |
|-------------|-----------|
| `EVID-B3-CDS-API` | `technologies/bmw-etch-rpc/SHEET.md` |
| `EVID-B3-CDS-VISCTX-50034` | same |
| `EVID-B3-CDS-NOT-TRACK-BUS` | same + `bmw-rhmi` |

## Offene Punkte

- Semantik `entertainment.multimedia` Payload
- `hmi.graphicalContext` ↔ RHMI Focus korrelieren
