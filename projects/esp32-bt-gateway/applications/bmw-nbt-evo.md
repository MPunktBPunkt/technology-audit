# Project Application: bmw-nbt-evo in esp32.bt-gateway

```yaml
project_id: esp32-bt-gateway
tech_slug: bmw-nbt-evo
status: draft
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../../audits/esp32-bt-gateway-2026-planning/
maturity:
  technology: R3
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt (Design-B)

Erste Ziel-Sink/Controller-Kombination. Gateway bewusst **nicht** bmw-benannt; Host-Quirks bleiben hier / im Host-Sheet. Observe-first AVRCP/Meta.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Gateway-Pfad NBT Feld-PASS | — | `UNKNOWN` |
| Gegenbefunde P-F1–P-F5 aus PiDrive-Mapping | `EVID-BTGW-2026-10-09-001` | `INFERRED` (STATE / Auftrag-4) |

## Verwandte

- PiDrive [bmw-nbt-evo](../../pidrive/applications/bmw-nbt-evo.md) (USB-MSC-C) — anderes Medium, gleiches Host-Sheet
