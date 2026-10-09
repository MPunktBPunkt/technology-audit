# Project Application: esp-now-messaging in esp32.communicator

```yaml
project_id: esp32-communicator
tech_slug: esp-now-messaging
status: active
sheet: ../../../technologies/esp-now-messaging/SHEET.md
audit: ../../../audits/esp32-communicator-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R1
  reusability: W2
```

## Rolle im Projekt

Messenger: Broadcast/Unicast, Hello-Discovery 5 s, Call-Signale (ring/accept/end). Packet ~243 B. WiFi parallel; Kanal = STA.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| ESP-NOW + WiFi parallel dokumentiert | `EVID-NOW-2026-10-09-001` | `FACT` |
| Call nur Signal, Media Browser/WebRTC | `EVID-NOW-2026-10-09-002` | `FACT` |
