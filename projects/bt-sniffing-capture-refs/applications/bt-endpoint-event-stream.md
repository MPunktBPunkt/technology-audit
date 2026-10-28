# Project Application: bt-endpoint-event-stream in bt-sniffing-capture-refs

```yaml
project_id: bt-sniffing-capture-refs
tech_slug: bt-endpoint-event-stream
status: active
sheet: ../../../technologies/bt-endpoint-event-stream/SHEET.md
audit: ../../../audits/bt-sniffing-capture-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| scan-mqtt: Adv JSON + MQTT/Serial queues + dropped_* | `EVID-BTSC-2026-10-28-001` | `FACT` |
| ble2mqtt: GATT values → MQTT topics | `EVID-BTSC-2026-10-28-010` | `FACT` |
| BLESniffer: Adv → SD PCAP synth (kein TCP) | `EVID-BTSC-2026-10-28-020` | `FACT` |
| classic_sniffer: UART binary → Host PCAPNG | `EVID-BTSC-2026-10-28-030` | `FACT` |
| bsniffhub: Host Serial→PCAP/pipe (kein ESP) | `EVID-BTSC-2026-10-28-040` | `FACT` |
| Eidolon HFP TCP öffentlich | — | `UNKNOWN` / nicht gefunden |
