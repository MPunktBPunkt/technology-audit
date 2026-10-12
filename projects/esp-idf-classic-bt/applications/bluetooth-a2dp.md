# Project Application: bluetooth-a2dp in esp-idf-classic-bt

```yaml
project_id: esp-idf-classic-bt
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/esp-idf-classic-bt-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

Offizielle Bluedroid-Beispiele: `a2dp_sink_stream` / `_aac` und `a2dp_source` / `_aac` unter `examples/bluetooth/bluedroid/classic_bt/`. Shared utils in `common/a2dp_utils/`.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `.../classic_bt/a2dp_sink_stream/` | Sink (ersetzt älteren `a2dp_sink`-Namen) |
| `.../classic_bt/a2dp_source/` | Source |
| `.../classic_bt/common/a2dp_utils/` | Shared sink/source helpers |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Official sink/source examples on ESP32 (+S31 defaults) | `EVID-IDF-A2DP-2026-10-12-001` | `FACT` |
| Cover-art example requires SPIRAM with A2DP | `EVID-IDF-A2DP-2026-10-12-002` | `FACT` |
