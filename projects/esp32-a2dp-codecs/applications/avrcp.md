# Project Application: avrcp in esp32-a2dp-codecs

```yaml
project_id: esp32-a2dp-codecs
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/esp32-a2dp-codecs-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle

AVRCP läuft parallel zum Multi-Codec-Sink (WillyBilly: „native A2DP/AVRCP wrapper“). Desk vertieft keine Cover-Art/Browse-Claims — Fokus Codec-Pfad.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| AVRCP present alongside codecs (WillyBilly README) | `EVID-CODEC-AVRCP-2026-10-12-001` | `FACT` |
| Feature-Tiefe vs. IDF avrcp_* examples | — | `UNKNOWN` |
