# Project Scope: esp32.io-control

```yaml
project_id: esp32-io-control
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.io-control
reviewed_commit: c79dd3a
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `esp32.io-control.ino`, README (Pin-API, SSE, Hub ios) |
| **Nicht in scope** | Sensor-Produkt-Firmware; RF-/LAN-Scanner; toolnode-Host-Internals |
| **Hardware** | Wemos D1 Mini ESP32 / ESP32-S3 |
| **Version** | 1.6.1 |

## Systeme

```text
Browser Pinout/GPIO/I2C/SPI/PWM ◀── REST+SSE
ESP ──Hub ios (aktive Pins)──▶ esp-hub
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.2** (Hub ohne fwType, Scan-Schichten, Reuse).
