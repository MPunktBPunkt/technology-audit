# Project Inventory: esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
updated: 2026-10-25
reviewed_commit: 739c67a
profile: firmware
pilot_order: [rf-environment-monitor, esp-hub-telemetry, esp-embedded-web-sse]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| RF-/WLAN-/BLE-Scan + Score v1∥v2 + Observation | `rf-environment-monitor` | **wachsen** (Schichten, Location-Achse) |
| Hub Heartbeat `fwType=rfmonitor` + Contract v2 | `esp-hub-telemetry` | wachsen (Fallstrick nested domain contract) |
| Lab-Web + SSE + Operator Timeline | `esp-embedded-web-sse` | Application nachziehen |
| WiFiManager | `wifi-manager-captive` | observed |
| NimBLE Adv-Scan only | unter RF-Monitor | kein Fork von `ble-hrm-gatt` |
| Location/Session/Snapshot | unter RF-Monitor | kein neues Sheet (Application B) |

Ursprung: [esp32.rfmonitor](https://github.com/MPunktBPunkt/esp32.rfmonitor) @ `739c67a`.  
Kampagne: [esp32-rfmonitor-2026-v2-validation](../../audits/esp32-rfmonitor-2026-v2-validation/) · Prior: [pilot](../../audits/esp32-rfmonitor-2026-pilot/).

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
| Zweiter Feldstandort | Lab-Baseline nur ein Standort | Exit #5 Feldserie |
| Hub-Adapter Contract v2 | Device-Doku FACT; Adapter UNKNOWN | Exit #6 ioBroker.esp-hub |
| Score-v2 langer Dump | 600 s-Baseline unter FW 1.3 / scoreVersion 1 | optional Replay-Session ≥1.4 |

## Signale ohne Eintrag

- EventLog / HistoryStore / MeasSession — RF-Monitor-Application
- Betriebsmodi Live/Normal/Diagnose — Application B
- Operator Timeline / WLAN-Filter — Web-Application
