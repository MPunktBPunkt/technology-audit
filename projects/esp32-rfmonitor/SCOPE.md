# Project Scope: esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.rfmonitor
reviewed_commit: 95314cd
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `src/` (RfScanner, BleTracker, RfAnalyzer, Hub, Web), `docs/RF_SCORE.md`, `docs/PFLICHTENHEFT.md`, `platformio.ini` |
| **Nicht in scope** | Spektrumanalyse; toolnode; Presence-Genauigkeit; Hub-Internals |
| **Hardware** | `rfmonitor-mini` (D1 Mini) · `rfmonitor-s3` |
| **Version** | `FW_VERSION` 1.1.0 |

## Systeme

```text
WLAN APs / BLE Adv ──Scan (sequentiell)──▶ ESP32 RF-Monitor ──WiFi──▶ WebUI/SSE + ESP-Hub
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.0** (inkl. `standard_version`, Reuse-Match, Profil). Neues Pattern-Sheet RF-Monitor; Hub/Web wiederverwenden.
