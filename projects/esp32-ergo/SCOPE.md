# Project Scope: esp32.ergo

```yaml
project_id: esp32-ergo
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.ergo
reviewed_commit: edaeb19
```

## Grenzen

| | |
|--|--|
| **In scope** | Firmware `src/`, `platformio.ini`, `docs/ergometer/*`, `STATE.md`, `CHANGELOG.md`, Bridge/Coach-Verhalten, Hub-IO `fwType=ergo` |
| **Nicht in scope** | Internals von iobroker.esp-hub; MyWhoosh-Quellcode; medizinische Claims; vollständige Trainingsplan-Generatorik |
| **Hardware** | ESP32-S3 (`env:ergo`); Bike Hammer Varon XTR II; Puls via Gurt / [esp32.heartrate](https://github.com/MPunktBPunkt/esp32.heartrate)-Relay / Bike-IBD |
| **Version** | Badge/README teils 0.3.23-dev · `FW_VERSION` in `platformio.ini` = `0.3.24-dev` |

## Systeme

```text
Varon XTR II ──BLE Central (FTMS)──┐
                                   ├──▶ ESP32-S3 ──WiFi──▶ WebUI/SSE + ESP-Hub
HR-Relay / Polar H9 ──0x180D───────┘         │
                                             └──BLE Peripheral (FTMS Bridge)──▶ MyWhoosh
```

## Ziel dieses Audit-Laufs

Desk-Inventar + priorisierte Sheets/Applications: FTMS (neu), Geräteprofil Varon, Wiederverwendung/Wachstum der Heartrate-Sheets (HR, Relay, Hub, Web/SSE). Offene Feldpunkte (Nachtest 6, Bridge-Abnahme) bleiben als Exit-Kriterien.
