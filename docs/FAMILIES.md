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

Radio-Sheets (Empfang): `dab-plus`, `rtl-sdr`, `pmr446`, `airband-am`, `sdr-spectrum-fft`.

## Lab / Fremd — Radio (RX/TX)

| Projekt-ID | Rolle |
|------------|-------|
| `welle-io` | Desk: AlbrechtL/welle.io — Upstream DAB/DAB+ SDR (welle-cli/gui) |
| `pi-fm-tx` | Desk: pifm, PiFmRds, markondej/fm_transmitter, zoroxide, pi-fm-player, F5OEO/rpitx |
| `esp-fm-tx` | Desk: Alexxdal/ESP32FMRadio, hiperiondev/esp32_fm_radio — Classic ESP32 APLL/MCLK-FM |
| `esp32-sdr-trx` | Desk: jochenhammes/esp32-sdr-trx (+ eSpDR) — S3 narrowband RX + polar PHY TX (13 cm) |
| `esp32sdr` | Desk: lozaning/ESP32SDR — S3 burst RX + Wi-Fi tone keying TX (DAC-I/Q `REJECTED`) |
| `esp-sdr-bridge` | Desk: z2labs/esp-sdr-bridge — IQS USB → SpyServer/rtl_tcp |
| `espargos-espsdr` | Desk: ESPARGOS/esp-sdr + SoapyESPSDR (+ Cardputer-Port) — Multi-Chip Undoc I/Q Matrix |
| `c5vrx` | Desk: Twotoz/C5VRX — C5 continuous 5.8 GHz FPV → CVBS |
| `esp32-a2dp` | Desk: pschatzmann/ESP32-A2DP — Arduino Bluedroid A2DP/AVRCP (Kern-Library) |
| `espble` | Desk: tanakamasayuki/EspBle — NimBLE + Classic CT/TG AVRCP |
| `a2dpsinkhfpclient` | Desk: walinsky/a2dpSinkHfpClient — Sink+HFP+explizite AVRC-API |
| `esp-idf-classic-bt` | Desk: Espressif classic_bt examples — Metadata/CoverArt/AbsVol SoT |
| `esp32-a2dp-codecs` | Desk: cfint + WillyBilly06 multi-codec sinks |
| `esp32-a2dp-source` | Desk: schreibfaul1 Source (historisch/dünn AVRCP) |
| `esp32-bt-iap` | Desk: fanthos IAP (historisch; stale metadata folklore) |
| `esphome-a2dp-sink` | Desk: PxPert ESPHome A2DP Sink entities |
| `bluetooth-stack` | Desk: sj15712795029/bluetooth_stack — HCI-Host-Stack (Kontrast) |
| `espusbhost` | Desk: tanakamasayuki/EspUsbHost — USB Host S2/S3/P4 |

RX-Reuse: `dab-plus`, `rtl-sdr`, `esp32-undoc-iq-rx` (nicht mit TX vermischen).  
TX-Sheets: `rpi-gpio-fm-tx`, `fm-rds`, `rpitx`, `esp32-apll-fm-tx` (Classic only; S3-UKW = Gate), `esp32-polar-phy-tx` (S3 13 cm polar), `esp32-wifi-tone-tx` (S3 2.4 GHz channel-grid keying). Kein Antennen-Sendepfad in der KB.  
BT/USB: `bluetooth-a2dp` / `avrcp` stack-neutral; Standalone-AVRCP Praxis `REJECTED`; Cover Art IDF≥5.4+PSRAM; `esp-usb-host` ≠ `usb-msc`.

## Lab / Fremd — sekundäre Web-Kataloge

| Projekt-ID | Rolle |
|------------|-------|
| `rnt-esp32` | Desk: [RNT ESP32 Projects Index](https://randomnerdtutorials.com/projects-esp32/) — Match gegen Sheet-Katalog; **kein** Tutorial-Text; Snapshot statt Commit |

Quellenart **sekundär**. Reuse/Signale nur; `seen_in` erst mit Application. Chip-Scope: Arduino-„ESP32“ ≠ S3/C3 automatisch.

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
