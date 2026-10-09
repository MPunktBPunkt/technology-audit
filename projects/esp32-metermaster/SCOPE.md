# Project Scope: esp32.MeterMaster

```yaml
project_id: esp32-metermaster
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.MeterMaster
reviewed_commit: 60fa14b
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `esp32.MeterMaster.ino`, `docs/DATENAUSTAUSCH.md`, `docs/CODING-RULES.md`, Hardware-Docs OLED |
| **Nicht in scope** | iobroker.metermaster Adapter-Internals; Zähler-Backend; Spektrum/RF |
| **Hardware** | ESP32 D1 Mini + 0.66″ OLED 64×48 SSD1306 (EastRising) |
| **Version** | 0.4.3 |

## Systeme

```text
ioBroker States ──Simple-API :8087──▶ ESP poll values ──▶ OLED UI
ESP ──Adapter HTTP :8089──▶ register / config / cmd
ESP ──ESP-Hub :8093──▶ optional Dashboard Heartbeat
Browser ──Web UI──▶ ESP (Config, OTA)
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **0.6.1**: Drei HTTP-Rollen trennen (Simple-API / Produkt-Adapter / Hub); neue Sheets Simple-API + OLED; Hub wachsen; kein SSE-Sheet für reine Poll-Web-UI.
