# Produktfamilien (Orientierung)

Nicht jeder Sheet gehört zu jeder Familie. Beim Projektstart zuerst die Familie wählen, dann den Sheet-Index filtern.

## ESP-Hub-Familie

Zentrale: **iobroker.esp-hub** (:8093) · Vorlage: **ESP32.esp-hub** (`esp-hub-base`)

| Projekt-ID | Rolle |
|------------|-------|
| `iobroker-esp-hub` | Adapter (States, OTA, USB, Compiler, WebRTC-Signaling) |
| `esp32-esp-hub` | Basis-Firmware / Ableitungsvorlage |
| `esp32-network` | LAN-Inventar |
| `esp32-webradio` | Browser-Radio-Host |
| `esp32-io-control` | Lab GPIO/Bus |
| `esp32-communicator` | ESP-NOW Messenger |
| `esp32-metermaster` | OLED + Triple-HTTP (Hub optional) |
| `esp32-rfmonitor` | RF-Environment |
| `esp32-toolnode` | Modular (RF+Lab+MQTT) |
| `esp32-heartrate` / `ergo` / `ftmsprobe` | BLE-Training / Sonde (Hub-Client) |
| `esp32-bt-gateway` | A2DP/AVRCP (planning) |

Gemeinsame Sheets: `esp-hub-telemetry`, oft `esp-embedded-web-sse`.

## PiDrive / Infotainment

| Projekt-ID | Rolle |
|------------|-------|
| `pidrive` | Ops/Feld: USB-MSC, BMW HU, DAB+/SDR/PMR/Airband/FFT, A2DP/AVRCP |
| `esp32-pidrive` | Firmware: TinyUSB MSC-Gadget + PUMP + HubClient |
| `esp32-bt-gateway` | Planung A2DP/AVRCP (auch ESP-Hub-Familie) |

Radio-Sheets: `dab-plus`, `rtl-sdr`, `pmr446`, `airband-am`, `sdr-spectrum-fft`.

## ioBroker-Adapter (Produkt)

| Projekt-ID | Rolle |
|------------|-------|
| `iobroker-esp-hub` | ESP-Hub-Zentrale :8093 |
| `iobroker-metermaster` | Zähler-App + ESP-OLED-Nodes :8089 |
| `iobroker-kostalpiko` | Kostal PIKO lokal HTTP |
| `iobroker-fritzwireguard` | WireGuard + TCP-Tunnel zur Remote-FritzBox |
| `iobroker-freeair100` | bluMartin freeAir Cloud-Portal |
| `iobroker-kalender` | Kalender / Trigger / ICS / Alexa |
| `iobroker-linuxdashboard` | Linux Host-Ops Dashboard |
| `iobroker-mbrepository` | GitHub-Adapter Install-Manager |
| `metermaster-app` | Android-App Ökosystem (Submodule) |
| `iobroker-repositories` | Catalog-Fork (Ops, kein Produktcode) |

## Querschnitt (nicht familiegebunden)

`bluetooth-*`, `ble-*`, `usb-msc`, `iobroker-simple-api`, `kostal-piko-http`, `fritzbox-tr064`, …

## Pflege

Neue Repos: Zeile in der passenden Familie + Inventar-Reuse. Familienkarte absichtlich **kurz** halten.
