# Project Application: mqtt-node-telemetry in esp32.toolnode

```yaml
project_id: esp32-toolnode
tech_slug: mqtt-node-telemetry
status: active
sheet: ../../../technologies/mqtt-node-telemetry/SHEET.md
audit: ../../../audits/esp32-toolnode-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R1
  reusability: W2
```

## Rolle im Projekt

Optional (`TOOLNODE_ENABLE_MQTT`): Topics `esphub/toolnode/<device>/…` Status/Events/cmd; Reconnect ohne Delay in Hauptschleife.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/core/MqttClientWrapper.*` | Client |
| README MQTT / ARCHITECTURE | Schema |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| MQTT optional + Topic-Namespace | `EVID-MQTT-2026-10-09-001` | `FACT` |
