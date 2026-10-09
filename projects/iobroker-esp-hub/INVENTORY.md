# Project Inventory: iobroker.esp-hub

```yaml
project_id: iobroker-esp-hub
updated: 2026-10-09
reviewed_commit: 8d3853c
profile: adapter
pilot_order: [iobroker-esp-hub-adapter, esp-hub-telemetry]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.3](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Adapter-Produkt USB/OTA/Compile/States/WebRTC | `iobroker-esp-hub-adapter` | **neu** |
| HTTP Register/otaUrl Spec | `esp-hub-telemetry` | **wachsen** (Server-Seite, gleicher Slug — Sprache egal) |
| WebRTC Signaling Relay | `hub-webrtc-signaling` | observed (jetzt im Adapter belegt) |
| Simple-API | `iobroker-simple-api` | **kein Match** (anderer Adapter) |

Ursprung: [iobroker.esp-hub](https://github.com/MPunktBPunkt/iobroker.esp-hub).  
Kampagne: [iobroker-esp-hub-2026-pilot](../../audits/iobroker-esp-hub-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `iobroker-esp-hub-adapter` | ioBroker ESP-Hub Adapter | F | `iobroker`,`nodejs` | applied | partial | [SHEET](../../technologies/iobroker-esp-hub-adapter/SHEET.md) | [app](applications/iobroker-esp-hub-adapter.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry Contract | F | `iobroker` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `hub-webrtc-signaling` | Hub WebRTC Signaling | F | — | observed | none | — | — |
| `esptool-usb-flash` | esptool USB Flash | D | — | observed | none | — | — |
| `arduino-cli-host` | arduino-cli im Adapter | D | — | observed | none | — | — |
