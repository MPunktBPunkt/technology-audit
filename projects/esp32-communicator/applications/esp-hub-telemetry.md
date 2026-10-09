# Project Application: esp-hub-telemetry in esp32.communicator

```yaml
project_id: esp32-communicator
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-communicator-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

ios: peers, sent, recv, unread, channel. Kein fwType. Hub auch WebRTC-Signaling-Endpoint (observed).

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Hub ios Komms-Stats | `EVID-HUB-2026-10-09-050` | `FACT` |
| Kein fwType | `EVID-HUB-2026-10-09-051` | `FACT` |
