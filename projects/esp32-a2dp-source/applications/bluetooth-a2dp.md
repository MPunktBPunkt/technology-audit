# Project Application: bluetooth-a2dp in esp32-a2dp-source

```yaml
project_id: esp32-a2dp-source
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/esp32-a2dp-source-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W1
```

## Rolle

A2DP Source: PCM/Wellenform → Classic Sink (Speaker). Älteres Standalone-Projekt; Gateway sollte neuere Referenzen bevorzugen.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Source-oriented repo with esp_a2dp APIs | `EVID-SRC-2026-10-12-001` | `FACT` |
| Stale vs. current IDF best practice | `INFERRED` | age 2023 |
