# Project Scope: esp32.toolnode

```yaml
project_id: esp32-toolnode
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.toolnode
reviewed_commit: af4d973
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `src/core` (ModuleManager, Hub, MQTT, Setup), `src/modules` (Scanner, RfHealth, Lab), `src/web`, `docs/ARCHITECTURE.md`, `platformio.ini` / `BuildFlags.h` |
| **Nicht in scope** | Presence-Genauigkeit (Phase 2); Spektrumanalyse; Hub-Internals; I²C/UART-Labor-Tiefenespezifikation |
| **Hardware** | `toolnode-mini` (D1 Mini) · ESP32-S3-Env |
| **Version** | README Badge 1.1.0 |

## Systeme

```text
WLAN APs ──Scan──▶ Scanner/RfHealth Module ──▶ History/Events
Lab-Bus (I²C/UART/OW/Signal) ──▶ Lab-Module
AppCore ──Web REST/SSE + Wizard──▶ Browser
       ──Hub Heartbeat fwType=toolnode──▶ esp-hub
       ──MQTT (optional)──▶ Broker
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.1**: Geschwister-Reuse von `rf-environment-monitor` (kein Fork), plus neue Sheets Modular-Host / MQTT; Hub/Web wachsen.
