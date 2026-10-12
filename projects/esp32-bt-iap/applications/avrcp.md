# Project Application: avrcp in esp32-bt-iap

```yaml
project_id: esp32-bt-iap
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/esp32-bt-iap-2026-foreign/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W1
```

## Rolle

Code registriert `ESP_AVRC_CT_METADATA_RSP_EVT` und sendet Metadata-Cmds — Community-README-Folklore „metadata not supported by esp-idf“ war schon damals ungenau und ist **heute falsch** (siehe IDF `avrcp_ct_metadata`).

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| CT metadata event handling in code | `EVID-IAP-AVRCP-2026-10-12-001` | `FACT` |
| Folklore claim as current truth | `REJECTED` | Sheet Fallstrick |
