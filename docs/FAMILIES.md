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
| `esp32-msc-gadget-refs` | Desk: Fremd-MSC-Gadgets (IDF/Arduino/Adafruit/EspTinyUSB, aoscarius, atomic14) |
| `esp32-bt-gateway` | Planung A2DP/AVRCP (auch ESP-Hub-Familie) |

MSC/FAT: `usb-msc`, `virtual-fat`; Host: `bmw-nbt-evo`. Methods: `msc-lba-timing-instrument`, `msc-trace-correlation`.  
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

## Lab / Fremd — On-Device ML / Graph

| Projekt-ID | Rolle |
|------------|-------|
| `esp32-ai` | Desk: [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) — PLE-LLM + Fly-Connectome auf S3 N16R8 |

Sheets: `mcu-ple-inference`, `mcu-connectome-graph`; Reuse `esp32-s3-silicon`, `ssd1306-oled-ui`. Keine Weight-/Graph-Spiegelung.

## Lab / Fremd — BLE GATT Bridge / Dual-Role

| Projekt-ID | Rolle |
|------------|-------|
| `ble-gatt-bridge-refs` | Desk: ChimeraBLE, iFitnessProxy, ifit, esp32-ble2mqtt, BleRemoteBrideg, esp32-ble-uart-mx, btlejuice — Pattern-Extraktion |

Sheets: `ble-gatt-dual-role`, `ble-gatt-transparent-bridge`, `ble-gatt-semantic-bridge`. Kontrast/Reuse: `ble-hr-relay`, `bluetooth-ftms`. Offensive MITM nur Inventar — keine Attack-How-tos. Kampagne: [`ble-gatt-bridge-refs-2026-foreign`](../audits/ble-gatt-bridge-refs-2026-foreign/).

## Lab / Fremd — Bluetooth Classic Gaps (HFP/SPP/HID/Coex)

| Projekt-ID | Rolle |
|------------|-------|
| `bt-classic-profile-refs` | Desk: a2dpSinkHfpClient, EspBle, esp32-hsp-hf, esp32-bthidbridge, BTClassicSPP, IDF classic_bt, btstack |

Sheets: `bluetooth-hfp`, `bluetooth-spp`, `bluetooth-hid`, `bt-dual-mode-coex`, `hid-cross-transport-bridge`. Kontrast: `bluetooth-a2dp` / `avrcp`. Kampagne: [`bt-classic-gaps-2026-foreign`](../audits/bt-classic-gaps-2026-foreign/).

## Lab / Fremd — Bluetooth Analyse-Relais / Device-Understanding

| Projekt-ID | Rolle |
|------------|-------|
| `bt-analysis-relay-refs` | Desk: Observe-Proxy vs Endpoint vs Host-Sniffer (Phone↔Uhr/Soundbar/Auto/HID) |
| `bt-sniffing-capture-refs` | Desk: Capture-Pipelines ESP→Host (JSONL/TCP) vs nRF/HCI/PCAP |

Sheets: `ble-gatt-observe-proxy`, `bt-analysis-endpoint`, `bt-endpoint-event-stream`. Method: `bt-passive-host-sniff`. Kampagnen: [`bt-analysis-relay-2026-foreign`](../audits/bt-analysis-relay-2026-foreign/), [`bt-sniffing-capture-2026-foreign`](../audits/bt-sniffing-capture-2026-foreign/). Regel: ESP App-Level; nRF/HCI Funk/Stack; Debian wertet aus.

## Lab / Fremd — WiFi/BLE Capture Toolkit

| Projekt-ID | Rolle |
|------------|-------|
| `esp32-marauder` | Desk: [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder) — Promiscuous/PCAP; Offensive TX nur Inventar |

Sheet: `esp-wifi-promiscuous-pcap`. Kontrast: `rf-environment-monitor`. Keine Attack-How-tos in der KB.

## Lab / Fremd — Wi-Fi Sensing (CSI)

| Projekt-ID | Rolle |
|------------|-------|
| `espectre` | Desk: [francescopace/espectre](https://github.com/francescopace/espectre) — CSI Motion, Temporal Admission, on-device Detectors |
| `esp32-rf-sensing` | Planung: Messvertrag CSI/Promiscuous/RX-meta/CCA-Gate — Kampagne [`esp32-rf-sensing-2026-desk`](../audits/esp32-rf-sensing-2026-desk/); **kein** rfmonitor-Umbau |

Sheet: `wifi-csi-motion`. Kontrast: `esp-wifi-promiscuous-pcap`, `rf-environment-monitor`. Keine Dataset-Spiegelung. Planung reuse-first (Phase 0), dann IDF-Gate.

## Lab / Fremd — Heavy PSRAM Ports

| Projekt-ID | Rolle |
|------------|-------|
| `esp32-doom` | Desk: [espressif/esp32-doom](https://github.com/espressif/esp32-doom) — PrBoom PoC, Classic+PSRAM (historisch) |

Sheet: `esp-psram-heavy-port`. Kontrast: `esp32-s3-silicon`, `ssd1306-oled-ui`. Unsupported PoC.

## Lab / Fremd — Ham SSTV / AF TX

| Projekt-ID | Rolle |
|------------|-------|
| `tinysstv` | Desk: [JO3ALT/TinySSTV](https://github.com/JO3ALT/TinySSTV) — Martin M1 AF SSTV auf ESP32-C3 |

Sheet: `sstv-martin-m1`. Kontrast: `esp32-apll-fm-tx` (RF ≠ AF).

## Lab / Fremd — LMS / Multi-Room Audio

| Projekt-ID | Rolle |
|------------|-------|
| `squeezelite-esp32` | Desk: [sle118/squeezelite-esp32](https://github.com/sle118/squeezelite-esp32) — LMS/Squeezelite (+ AirPlay/BT/Spotify Add-ons) |

Sheet: `lms-squeezelite`; Reuse `esp-i2s-audio`, `esp-psram-heavy-port`, `bluetooth-a2dp`. Kontrast: `webradio-browser-host`, `spotify-web-api-remote`.

## Lab / Fremd — Spotify Web-API Remote

| Projekt-ID | Rolle |
|------------|-------|
| `esp32-spotify-remote` | Desk: [seichris/esp32-spotify-remote](https://github.com/seichris/esp32-spotify-remote) — Web API + PKCE Remote (kein Connect-Decode) |

Sheet: `spotify-web-api-remote`. Kontrast: `lms-squeezelite` (Connect/Decode ≠ Remote).

## Lab / Fremd — Ride BLE Display / Proximity

| Projekt-ID | Rolle |
|------------|-------|
| `open-bike-computer` | Desk: [seichris/open-bike-computer](https://github.com/seichris/open-bike-computer) — Custom BLE Ride/Nav Display + Ownership |
| `esp-ble-finder` | Desk: [khlebobul/esp_ble_finder](https://github.com/khlebobul/esp_ble_finder) — BLE Adv RSSI Proximity Hunt |

Sheets: `ride-ble-display`, `ble-rssi-proximity`. Kontrast: `bluetooth-ftms`, `ble-hrm-gatt`, `rf-environment-monitor`.

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
