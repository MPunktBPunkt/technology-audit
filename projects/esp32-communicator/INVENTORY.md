# Project Inventory: esp32.communicator

```yaml
project_id: esp32-communicator
updated: 2026-10-09
reviewed_commit: 429f20e
profile: firmware
pilot_order: [esp-now-messaging, esp-embedded-web-sse, esp-hub-telemetry]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.2](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| ESP-NOW Chat/Discovery | `esp-now-messaging` | **neu** |
| SSE `/api/sse` | `esp-embedded-web-sse` | wachsen |
| Hub Heartbeat ohne fwType | `esp-hub-telemetry` | wachsen |
| WebRTC via Hub-Signaling | `hub-webrtc-signaling` | observed |
| WiFi+ESP-NOW gleicher Kanal | `unter esp-now-messaging` | Fallstrick |

Ursprung: [esp32.communicator](https://github.com/MPunktBPunkt/esp32.communicator).  
Kampagne: [esp32-communicator-2026-pilot](../../audits/esp32-communicator-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp-now-messaging` | ESP-NOW Messaging | C | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-now-messaging/SHEET.md) | [app](applications/esp-now-messaging.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | applied | partial | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | [app](applications/esp-embedded-web-sse.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `hub-webrtc-signaling` | Hub WebRTC Signaling | F | — | observed | none | — | — |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |
| `mdns-discovery` | mDNS | F | — | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Feldserie | Desk-Audit | Evidence nachziehen |

## Signale ohne Eintrag

- WiFiManager / NVS — observed-Familie
