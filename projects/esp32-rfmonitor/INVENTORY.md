# Project Inventory: esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
updated: 2026-10-26
reviewed_commit: afcd137
profile: firmware
pilot_order: [rf-environment-monitor, esp-hub-telemetry, esp-embedded-web-sse]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| RF-/WLAN-/BLE-Scan + Score v1∥v2 + Observation + Motion Own-Link | `rf-environment-monitor` | **wachsen** (Session-Profile, History, Motion≠Presence) |
| Hub Heartbeat `fwType=rfmonitor` + Contract v2 | `esp-hub-telemetry` | stabil (Adapter Exit offen) |
| Lab-Web + SSE + Operator Timeline + Own-Link-Chart | `esp-embedded-web-sse` | Application nachziehen |
| WiFiManager | `wifi-manager-captive` | observed |
| NimBLE Adv-Scan only | unter RF-Monitor | kein Fork von `ble-hrm-gatt` |
| Location/Session/Snapshot/Motion | unter RF-Monitor | kein neues Sheet (Application B + Method) |
| Own-Link Walk-by | Method `own-link-motion-sensitivity` | **kein** Fork zu `ble-rssi-proximity` / `wifi-csi-motion` |

Ursprung: [esp32.rfmonitor](https://github.com/MPunktBPunkt/esp32.rfmonitor) @ `afcd137`.  
Kampagne: [esp32-rfmonitor-2026-motion-delta](../../audits/esp32-rfmonitor-2026-motion-delta/) · Prior: [v2-validation](../../audits/esp32-rfmonitor-2026-v2-validation/) · [pilot](../../audits/esp32-rfmonitor-2026-pilot/).

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
| Motion-Transfer anderer Raum | Küche FACT; Geometrie `UNKNOWN` | Exit #5 Rest |
| Hub-Adapter Contract v2 | Device-Doku FACT; Adapter UNKNOWN | Exit #6 ioBroker.esp-hub |
| Mini↔S3 Score-Drift | Upstream Next | optional Nachlauf |
| Score-v2 langer Dump | Baseline unter 1.3 / scoreVersion 1 | optional Replay ≥1.4 |

## Signale ohne Eintrag

- EventLog / HistoryStore / MeasSession / Motion-Ring — RF-Monitor-Application
- Betriebsmodi Live/Normal/Diagnose — Application B
- Operator Timeline / WLAN-Filter / Own-Link-Chart — Web-Application
- Characterization A–G Host-Tools — Method/Application, kein Sheet-Fork
