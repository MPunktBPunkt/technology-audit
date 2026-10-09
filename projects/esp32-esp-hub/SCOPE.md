# Project Scope: ESP32.esp-hub

```yaml
project_id: esp32-esp-hub
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/ESP32.esp-hub
reviewed_commit: a03400a
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `esp-hub-base.ino`, README (Familie, Heartbeat, Ableiten), docs/hardware |
| **Nicht in scope** | Adapter-Internals; Fachmodule abgeleiteter Repos |
| **Hardware / Runtime** | ESP32 / ESP32-S3 |
| **Version** | 1.7.0 |

## Systeme

```text
esp-hub-base ──WiFiManager──▶ STA
         ──POST /api/register──▶ iobroker.esp-hub :8093
         ──Web Status+SSE + /ota──▶ Browser
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.3** (sprachneutraler Contract, Adapter-Profil, Navigations-Einstieg).
