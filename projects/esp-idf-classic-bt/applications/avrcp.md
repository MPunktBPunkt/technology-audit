# Project Application: avrcp in esp-idf-classic-bt

```yaml
project_id: esp-idf-classic-bt
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/esp-idf-classic-bt-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

Vendor-Referenz für AVRCP-Features:

| Example | Fokus |
|---------|-------|
| `avrcp_ct_metadata` | CT → Title/Artist/Album… |
| `avrcp_ct_cover_art` | AVRCP 1.6 Cover Art + LCD; menuconfig Cover Art; **PSRAM** |
| `avrcp_absolute_volume` | Absolute Volume CT↔TG |

Shared: `common/avrcp_utils/` (metadata, cover_art, abs_vol).

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| CT metadata example exists | `EVID-IDF-AVRCP-2026-10-12-001` | `FACT` |
| Cover Art example + SPIRAM defaults | `EVID-IDF-AVRCP-2026-10-12-002` | `FACT` |
| Absolute volume example | `EVID-IDF-AVRCP-2026-10-12-003` | `FACT` |
| Targets ESP32 / ESP32-S31 in READMEs | `EVID-IDF-AVRCP-2026-10-12-004` | `FACT` |
