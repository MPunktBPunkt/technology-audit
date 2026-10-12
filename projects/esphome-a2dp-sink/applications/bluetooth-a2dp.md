# Project Application: bluetooth-a2dp in esphome-a2dp-sink

```yaml
project_id: esphome-a2dp-sink
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/esphome-a2dp-sink-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

ESPHome `A2DPSinkHub`: Classic ESP32 Sink; `minimal_bluetooth` spart BLE; Entities für Connection/RSSI/Sample-Rate.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Classic ESP32 only (pschatzmann note) | `EVID-ESPHOME-A2DP-2026-10-12-001` | `FACT` |
| Hub + media_source architecture | `EVID-ESPHOME-A2DP-2026-10-12-002` | `FACT` |
