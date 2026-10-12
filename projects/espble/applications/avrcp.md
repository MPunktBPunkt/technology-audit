# Project Application: avrcp in espble

```yaml
project_id: espble
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/espble-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

`EspBleClassicAvrcp`: explizite **Controller- und Target**-API (Pass-Through, Metadata, Notifications, Volume). Wichtiger Upstream-Hinweis: bundled Classic host erlaubt Target-Notifications weitgehend nur für **Volume** — Play-Status/Track als TG nicht erreichbar ohne anderen Host.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/EspBleClassicAvrcp.cpp` / `EspBleClassic.h` (`EspBleClassicAvrcp`) | CT/TG API |
| README Classic feature notes | Dual-host / limits |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Explicit CT + TG API surface | `EVID-ESPBLE-AVRCP-2026-10-12-001` | `FACT` |
| TG notifications mostly volume-only (bundled host) | `EVID-ESPBLE-AVRCP-2026-10-12-002` | `FACT` (header comments) |
| CT side unrestricted vs that limit | `EVID-ESPBLE-AVRCP-2026-10-12-003` | `FACT` |
