# Project Application: avrcp in esp32.bt-gateway

```yaml
project_id: esp32-bt-gateway
tech_slug: avrcp
status: draft
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/esp32-bt-gateway-2026-planning/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt (Design-B)

ESP als **AVRCP Target** (Pass-Through, Meta, optional Browsing S3). Semantik des Menüs bleibt PiDrive; ESP transportiert generischen Baum. Observe-first vor Mapping.

## Architektur

```text
BMW Controller ──AVRCP──▶ ESP Target ──PDAP events──▶ Pi map_event()
Pi Menübaum ──PDAP──▶ ESP Browse responses ──▶ BMW
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `docs/planung/AVRCP-MOEGLICHKEITEN.md` | Stufen S1–S3 |
| `docs/planung/PHASE-0-MESSPLAN.md` | Phase −1 Messung |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| NBT: welche Tasten als AVRCP ankommen | — | `UNKNOWN` (Phase −1) |
| Browsing S3 machbar am Ziel-Stack | — | `UNKNOWN` |
| Skip=Cursor Ist-Workaround am Pi | `EVID-AVRCP-2026-10-09-001` | `INFERRED` (Planungsdoku / PiDrive-Referenz) |

## Offene Fragen

- Browse-Befehlssubset NBT?
- Menübaum ~98 KB ohne Paging (P-F5) — Transport-Limit?

## Verwandte

- [bmw-nbt-evo](bmw-nbt-evo.md) · Sheet `avrcp`
