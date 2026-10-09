# Project Inventory: esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
updated: 2026-10-09
reviewed_commit: 95314cd
profile: firmware
pilot_order: [rf-environment-monitor, esp-hub-telemetry, esp-embedded-web-sse]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.0](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| RF-/WLAN-/BLE-Scan + Score | `rf-environment-monitor` | **neu** |
| Hub Heartbeat `fwType=rfmonitor` | `esp-hub-telemetry` | wachsen (`seen_in`) |
| Lab-Web + SSE | `esp-embedded-web-sse` | wachsen |
| WiFiManager | `wifi-manager-captive` | observed |
| NimBLE Adv-Scan only | unter RF-Monitor | kein Fork von `ble-hrm-gatt` |

Ursprung: [esp32.rfmonitor](https://github.com/MPunktBPunkt/esp32.rfmonitor).  
Kampagne: [esp32-rfmonitor-2026-pilot](../../audits/esp32-rfmonitor-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `rf-environment-monitor` | RF Environment Monitor | H | `esp-idf`, `lab-only` | applied | partial | [SHEET](../../technologies/rf-environment-monitor/SHEET.md) | [app](applications/rf-environment-monitor.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | applied | partial | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | [app](applications/esp-embedded-web-sse.md) |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |
| `esp32-arduino-pio` | PlatformIO ESP32 | D | `esp-idf` | observed | none | — | — |
| `nvs-config-store` | NVS ConfigStore | E | — | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| RF-Score Kalibrierung | Heuristik v1, standortabhängig | Feldserie + Evidence |
| BLE Beacon-Taxonomie | iBeacon/Eddystone skizziert | mehr Geräteklassen |

## Signale ohne Eintrag

- EventLog / HistoryStore — Teil RF-Monitor-Application
- Betriebsmodi Live/Normal/Diagnose — Application B
