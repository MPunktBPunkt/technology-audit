# Project Application: avrcp in esphome-a2dp-sink

```yaml
project_id: esphome-a2dp-sink
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/esphome-a2dp-sink-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Triggers: `on_metadata`, `on_volume_change`, `on_avrcp_connection_state`, playback status/position — Metadata/Volume als ESPHome text_sensor/number.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Metadata/volume/AVRCP entity triggers documented | `EVID-ESPHOME-AVRCP-2026-10-12-001` | `FACT` |
