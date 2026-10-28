# Project Application: usb-aoa in pidrive

```yaml
project_id: pidrive
tech_slug: usb-aoa
status: active
sheet: ../../../technologies/usb-aoa/SHEET.md
audit: ../../../audits/usb-aoa-bmw-connected-2026-desk/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

PiDrive nutzt heute **USB-MSC** (+ separat BT A2DP/AVRCP) an NBT Evo. AOA ist hier nur
als **möglicher Alternativ-Transport** für eine Connected-App-Control-Plane notiert —
nicht als Ersatz für den MSC-Medienpfad und ohne Architekturentscheid.

```text
MSC gadget  → Host Storage / Prefetch   (bestehend, SoT Host-C)
AOA bulk?   → Bytes an BclFramer        (HYPOTHESIS / UNKNOWN C)
BT SPP?     → Bytes an BclFramer        (BG Code-Pfad; Kontrast)
```

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| MSC-Host-Verhalten NBT Evo | eigene PiDrive/hu-probe Kampagnen | unverändert |
| AOA/BCL USB Wire | `EVID-AOA-2026-10-28-025/026` | `UNKNOWN` |
| Connected USB laut AAIdrive Doc | `EVID-AOA-2026-10-28-014`…`019` | fremd B |

## Nicht tun

- PiDrive auf AOA/RHMI umbauen ohne C1b
- MSC-FACTS mit AOA-Desk vermischen
- AOAv2 Audio als Medienstrategie planen (deprecated)
