# Project Inventory: esp32.toolnode

```yaml
project_id: esp32-toolnode
updated: 2026-10-09
reviewed_commit: af4d973
profile: firmware
pilot_order: [esp-module-host, rf-environment-monitor, esp-hub-telemetry, esp-embedded-web-sse, mqtt-node-telemetry]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Modular Core + `TOOLNODE_ENABLE_*` | `esp-module-host` | **neu** |
| WLAN-Scan + RF-Score (Modul, BLE default aus) | `rf-environment-monitor` | **wachsen** (Geschwister zu rfmonitor) |
| Hub `fwType=toolnode` | `esp-hub-telemetry` | wachsen |
| Web REST + SSE + Wizard | `esp-embedded-web-sse` | wachsen |
| MQTT `esphub/toolnode/<device>/…` | `mqtt-node-telemetry` | **neu** |
| I²C/UART/OW/Signal Lab | `esp-lab-bus-tools` | observed |
| WiFiManager | `wifi-manager-captive` | observed |

Ursprung: [esp32.toolnode](https://github.com/MPunktBPunkt/esp32.toolnode).  
Kampagne: [esp32-toolnode-2026-pilot](../../audits/esp32-toolnode-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp-module-host` | ESP Modular Tool Firmware | J | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-module-host/SHEET.md) | [app](applications/esp-module-host.md) |
| `rf-environment-monitor` | RF Environment Monitor | H | `esp-idf`, `lab-only` | applied | partial | [SHEET](../../technologies/rf-environment-monitor/SHEET.md) | [app](applications/rf-environment-monitor.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | applied | partial | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | [app](applications/esp-embedded-web-sse.md) |
| `mqtt-node-telemetry` | MQTT Node Telemetry | F | `streaming` | applied | partial | [SHEET](../../technologies/mqtt-node-telemetry/SHEET.md) | [app](applications/mqtt-node-telemetry.md) |
| `esp-lab-bus-tools` | I²C/UART/OW/Signal Lab | H | `lab-only` | observed | none | — | — |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |
| `esp32-arduino-pio` | PlatformIO ESP32 | D | `esp-idf` | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| RF-Score vs. rfmonitor-Formel | getrennte Heuristiken möglich | Formel vergleichen / Evidence |
| Lab-Bus-Tools | nur observed | eigenes Sheet wenn ≥2 Projekte |
| Presence Phase 2 | Spez skizziert | planning nachziehen wenn FW |

## Signale ohne Eintrag

- PinGuard / SetupCatalog — Teil `esp-module-host` Application
- EventBus / HistoryStore — Core-Details Application B
