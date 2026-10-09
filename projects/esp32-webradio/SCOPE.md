# Project Scope: esp32.webradio

```yaml
project_id: esp32-webradio
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.webradio
reviewed_commit: caee2f8
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `esp32.webradio.ino`, README (API, Hub-IO, radio-browser) |
| **Nicht in scope** | A2DP-Audio; PipeWire-/Pi-Webradio; DAB+; On-Device-I2S-Player |
| **Hardware** | ESP32 / ESP32-S3 (Bins) |
| **Version** | 2.4.0 |

## Systeme

```text
Browser HTML5 Audio ◀── ESP Web-UI/API (stations, nowplaying, proxy)
ESP ──Hub /api/register──▶ esp-hub (nowStation/nowTitle, kein fwType)
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.2** (Hub ohne fwType, Scan-Schichten, Reuse).
