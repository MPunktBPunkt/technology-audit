# Project Scope: esp32.pidrive

```yaml
project_id: esp32-pidrive
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.pidrive
reviewed_commit: b00e453
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | PlatformIO-Firmware (`src/`), SoftAP-WebUI, PUMP, HubClient, Dist-Artefakte, Planungsdocs im Repo |
| **Nicht in scope** | PiDrive-Userspace-Betrieb / Feldberichte (→ [`pidrive`](../pidrive/)); BMW-Host-C als Primärziel (→ `bmw-nbt-evo` / Pilot 2); Classic-BT (→ `esp32-bt-gateway`) |
| **Hardware** | ESP32-S3 (USB-OTG + UART-Bridge), `ARDUINO_USB_MODE=0` |
| **Version** | README-Phase 0.4.5-dev; Build-Flags u. a. `0.4.36-dev` / Lab-Envs `0.4.40+` (`STATE.md`) |

## Systeme

```text
PiDrive (Pi) ──PUMP (UART/CDC oder TCP :9090)──▶ esp32.pidrive
esp32.pidrive ──TinyUSB MSC Device──▶ BMW / Lab USB-Host
Browser ──SoftAP/STA REST WebUI──▶ esp32.pidrive
esp32.pidrive ──POST /api/register──▶ iobroker.esp-hub :8093
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.3**: MSC/PUMP/Hub als Firmware-Anwendungen, Reuse mit bestehendem `usb-msc` und Hub-Familie; Host-C nicht verdoppeln.
