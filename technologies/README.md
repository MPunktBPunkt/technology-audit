# technologies/

Wiederverwendbare Technology Sheets.

**Reuse:** [`docs/REUSE.md`](../docs/REUSE.md) · **Neustart:** [`docs/PROJECT-START.md`](../docs/PROJECT-START.md) · **Familien:** [`docs/FAMILIES.md`](../docs/FAMILIES.md) · **Standard:** [`VERSION`](../VERSION) · **Maturity:** [`docs/KNOWLEDGE-MATURITY.md`](../docs/KNOWLEDGE-MATURITY.md)

**Maschinenindex:** [`index.yaml`](index.yaml) (generiert — `2026-10-28`, 72 Sheets). Neu generieren: `python3 tools/ta-assist index`

Spalten: **W** = Reusability · **Evid** = `evidence_max` (stärkste Lab/Feld-Belege aus Sheet∪Applications) · nicht verwechseln mit Projekt-Status (Prototype/Pilot).

## Index nach Primary (TAXONOMY)

### A — Empfang

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`airband-am`](airband-am/SHEET.md) | VHF Airband AM Reception | W2 | R2 | — | `pidrive` |
| [`dab-plus`](dab-plus/SHEET.md) | DAB+ Digital Audio Broadcasting | W3 | R2 | — | `pidrive`, `welle-io` |
| [`esp32-undoc-iq-rx`](esp32-undoc-iq-rx/SHEET.md) | ESP32 Undocumented I/Q RX Dump | W2 | R0 | — | `espargos-espsdr`, `c5vrx`, `esp32-sdr-trx`, `esp32sdr`, `esp-sdr-bridge` |
| [`pmr446`](pmr446/SHEET.md) | PMR446 (EU License-Free UHF) | W2 | R2 | — | `pidrive` |
| [`rtl-sdr`](rtl-sdr/SHEET.md) | RTL-SDR (RTL2832U Host Stack) | W3 | R2 | — | `pidrive`, `welle-io` |
| [`sstv-martin-m1`](sstv-martin-m1/SHEET.md) | Martin M1 SSTV Tone Transmit (AF) | W1 | R0 | — | `tinysstv` |

### B — Audio

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`esp-i2s-audio`](esp-i2s-audio/SHEET.md) | ESP I2S Audio Path | W2 | R0 | — | `esp32-audioi2s`, `esp-usb-audio-example`, `esp32-i2s-ble`, `esp-fm-rds-node`, `esp-network-pcm-clock`, `squeezelite-esp32` |

### C — Protokolle

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`avrcp`](avrcp/SHEET.md) | AVRCP | W3 | R2 | — | `pidrive`, `esp32-bt-gateway`, `esp32-a2dp`, `bluetooth-stack`, `espble`, `a2dpsinkhfpclient`, `esp-idf-classic-bt`, `esp32-a2dp-codecs`, `esp32-a2dp-source`, `esp32-bt-iap`, `esphome-a2dp-sink` |
| [`ble-gatt-dual-role`](ble-gatt-dual-role/SHEET.md) | BLE GATT Dual-Role (Central + Peripheral) | W3 | R2 | — | `ble-gatt-bridge-refs` |
| [`ble-gatt-observe-proxy`](ble-gatt-observe-proxy/SHEET.md) | BLE GATT Observe Proxy (Analysis Dual-Role) | W3 | R2 | — | `bt-analysis-relay-refs` |
| [`ble-gatt-semantic-bridge`](ble-gatt-semantic-bridge/SHEET.md) | Semantic GATT Bridge (Profile A → B) | W3 | R2 | — | `ble-gatt-bridge-refs` |
| [`ble-gatt-transparent-bridge`](ble-gatt-transparent-bridge/SHEET.md) | Transparent GATT Bridge (Byte Passthrough) | W3 | R2 | — | `ble-gatt-bridge-refs` |
| [`ble-hr-relay`](ble-hr-relay/SHEET.md) | BLE HR-Relay (Peripheral Bridge) | W3 | R2 | — | `esp32-heartrate`, `esp32-ergo` |
| [`ble-hrm-gatt`](ble-hrm-gatt/SHEET.md) | BLE Heart Rate GATT (Central) | W3 | R3 | LAB, GENERAL | `esp32-heartrate`, `esp32-ergo`, `esp32-ftmsprobe` |
| [`ble-pcm-notify-stream`](ble-pcm-notify-stream/SHEET.md) | BLE PCM Notify Stream (Custom GATT) | W1 | R0 | — | `esp32-i2s-ble` |
| [`bluetooth-a2dp`](bluetooth-a2dp/SHEET.md) | Bluetooth A2DP | W3 | R2 | — | `pidrive`, `esp32-bt-gateway`, `esp32-a2dp`, `bluetooth-stack`, `espble`, `a2dpsinkhfpclient`, `esp-idf-classic-bt`, `esp32-a2dp-codecs`, `esp32-a2dp-source`, `esp32-bt-iap`, `esphome-a2dp-sink`, `squeezelite-esp32` |
| [`bluetooth-ftms`](bluetooth-ftms/SHEET.md) | Bluetooth FTMS (Fitness Machine) | W3 | R3 | LAB, GENERAL | `esp32-ftmsprobe`, `esp32-ergo` |
| [`bluetooth-hfp`](bluetooth-hfp/SHEET.md) | Bluetooth HFP (Hands-Free Profile) | W3 | R2 | — | `bt-classic-profile-refs` |
| [`bluetooth-hid`](bluetooth-hid/SHEET.md) | Bluetooth HID (Classic Device/Host) | W3 | R2 | — | `bt-classic-profile-refs` |
| [`bluetooth-spp`](bluetooth-spp/SHEET.md) | Bluetooth SPP (Serial Port Profile) | W3 | R2 | — | `bt-classic-profile-refs` |
| [`bt-analysis-endpoint`](bt-analysis-endpoint/SHEET.md) | BT Analysis Endpoint (Role Impersonation) | W3 | R2 | — | `bt-analysis-relay-refs` |
| [`bt-dual-mode-coex`](bt-dual-mode-coex/SHEET.md) | BT Dual-Mode Coexistence (Classic + BLE) | W3 | R2 | — | `bt-classic-profile-refs` |
| [`esp-now-messaging`](esp-now-messaging/SHEET.md) | ESP-NOW Messaging | W2 | R1 | — | `esp32-communicator` |
| [`esp-usb-audio-uac`](esp-usb-audio-uac/SHEET.md) | ESP USB Audio (UAC Device) | W2 | R0 | — | `esp-iot-solution`, `esp-usb-audio-example` |
| [`esp-usb-host`](esp-usb-host/SHEET.md) | ESP32 USB Host (OTG) | W2 | R0 | — | `espusbhost`, `esp-iot-solution` |
| [`fm-rds`](fm-rds/SHEET.md) | FM-RDS (Radio Data System) | W2 | R0 | — | `pi-fm-tx`, `esp-fm-rds-node` |
| [`hid-cross-transport-bridge`](hid-cross-transport-bridge/SHEET.md) | HID Cross-Transport Bridge (HOGP ↔ Classic) | W2 | R2 | — | `bt-classic-profile-refs` |
| [`kostal-piko-http`](kostal-piko-http/SHEET.md) | Kostal PIKO Local HTTP Interface | W2 | R2 | — | `iobroker-kostalpiko` |
| [`pump-control-link`](pump-control-link/SHEET.md) | PUMP Control Link | W2 | R2 | — | `esp32-pidrive` |
| [`ride-ble-display`](ride-ble-display/SHEET.md) | Ride BLE Display (Custom GATT) | W1 | R0 | — | `open-bike-computer` |
| [`usb-msc`](usb-msc/SHEET.md) | USB Mass Storage Class | W3 | R3 | LAB, GENERAL | `pidrive`, `esp32-pidrive`, `esp32-msc-gadget-refs`, `usb-bot-observation`, `hu-probe` |

### D — Embedded

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`esp-psram-heavy-port`](esp-psram-heavy-port/SHEET.md) | ESP PSRAM Heavy App / Legacy Port | W1 | R0 | — | `esp32-doom`, `squeezelite-esp32` |
| [`esp32-apll-fm-tx`](esp32-apll-fm-tx/SHEET.md) | ESP32 APLL / MCLK FM Transmit | W2 | R0 | — | `esp-fm-tx` |
| [`esp32-polar-phy-tx`](esp32-polar-phy-tx/SHEET.md) | ESP32-S3 Polar PHY Test-Tone TX | W2 | R0 | — | `esp32-sdr-trx` |
| [`esp32-s3-silicon`](esp32-s3-silicon/SHEET.md) | ESP32-S3 Silicon Errata & Hardware Limits | W2 | R1 | — | `esp32-pidrive`, `hu-probe`, `pidrive`, `esp32-ai` |
| [`esp32-s3-usb-wifi-coex`](esp32-s3-usb-wifi-coex/SHEET.md) | ESP32-S3 USB ↔ WiFi Coexistence (OTG Device + STA) | W2 | R1 | — | `hu-probe` |
| [`esp32-wifi-tone-tx`](esp32-wifi-tone-tx/SHEET.md) | ESP32-S3 Wi-Fi PHY CW Tone Keying TX | W2 | R0 | — | `esp32sdr` |
| [`mcu-connectome-graph`](mcu-connectome-graph/SHEET.md) | MCU Connectome / Sparse Neural Graph | W1 | R0 | — | `esp32-ai` |
| [`mcu-ple-inference`](mcu-ple-inference/SHEET.md) | MCU PLE / Memory-Tiered LLM Inference | W1 | R0 | — | `esp32-ai` |
| [`rpi-gpio-fm-tx`](rpi-gpio-fm-tx/SHEET.md) | Raspberry Pi GPIO / Clock FM Transmit | W3 | R0 | — | `pi-fm-tx` |
| [`rpitx`](rpitx/SHEET.md) | rpitx — Raspberry Pi Software RF Transmit Platform | W2 | R0 | — | `pi-fm-tx` |

### E — Speicher / Formate

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`virtual-fat`](virtual-fat/SHEET.md) | Virtual FAT Disk (Synthetic Geometry) | W3 | R2 | — | `esp32-msc-gadget-refs`, `pidrive`, `esp32-pidrive` |

### F — Systemintegration

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`esp-hub-telemetry`](esp-hub-telemetry/SHEET.md) | ESP-Hub Node Telemetry | W4 | R3 | LAB, GENERAL | `esp32-heartrate`, `esp32-ergo`, `esp32-ftmsprobe`, `esp32-bt-gateway`, `esp32-rfmonitor`, `esp32-toolnode`, `esp32-metermaster`, `esp32-webradio`, `esp32-io-control`, `esp32-communicator`, `esp32-network`, `esp32-esp-hub`, `iobroker-esp-hub`, `esp32-pidrive` |
| [`freeair-connect-portal`](freeair-connect-portal/SHEET.md) | bluMartin freeAir Connect Portal | W1 | R1 | — | `iobroker-freeair100` |
| [`fritzbox-tr064`](fritzbox-tr064/SHEET.md) | FritzBox TR-064 Hostlist | W2 | R2 | — | `esp32-network`, `iobroker-fritzwireguard` |
| [`iobroker-esp-hub-adapter`](iobroker-esp-hub-adapter/SHEET.md) | ioBroker ESP-Hub Adapter | W3 | R2 | — | `iobroker-esp-hub` |
| [`iobroker-fritzwireguard-adapter`](iobroker-fritzwireguard-adapter/SHEET.md) | ioBroker FritzWireguard Adapter | W2 | R2 | — | `iobroker-fritzwireguard` |
| [`iobroker-kalender-adapter`](iobroker-kalender-adapter/SHEET.md) | ioBroker Calendar Adapter | W2 | R1 | — | `iobroker-kalender` |
| [`iobroker-linuxdashboard-adapter`](iobroker-linuxdashboard-adapter/SHEET.md) | ioBroker Linux Dashboard Adapter | W2 | R1 | — | `iobroker-linuxdashboard` |
| [`iobroker-mbrepository-adapter`](iobroker-mbrepository-adapter/SHEET.md) | ioBroker MB Repository Manager | W2 | R1 | — | `iobroker-mbrepository` |
| [`iobroker-metermaster-adapter`](iobroker-metermaster-adapter/SHEET.md) | ioBroker MeterMaster Adapter | W2 | R2 | — | `iobroker-metermaster`, `esp32-metermaster`, `metermaster-app` |
| [`iobroker-simple-api`](iobroker-simple-api/SHEET.md) | ioBroker Simple-API Client | W2 | R1 | — | `esp32-metermaster` |
| [`lms-squeezelite`](lms-squeezelite/SHEET.md) | LMS / Squeezelite Multi-Room Player | W1 | R0 | — | `squeezelite-esp32` |
| [`mqtt-node-telemetry`](mqtt-node-telemetry/SHEET.md) | MQTT Node Telemetry | W2 | R1 | — | `esp32-toolnode` |
| [`spotify-web-api-remote`](spotify-web-api-remote/SHEET.md) | Spotify Web API Remote (PKCE) | W1 | R0 | — | `esp32-spotify-remote` |

### G — Steuerung / UI

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`esp-embedded-web-sse`](esp-embedded-web-sse/SHEET.md) | Embedded Web REST + SSE | W3 | R3 | LAB, GENERAL | `esp32-heartrate`, `esp32-ergo`, `esp32-ftmsprobe`, `esp32-rfmonitor`, `esp32-toolnode`, `esp32-io-control`, `esp32-communicator`, `esp32-network`, `esp32-esp-hub` |
| [`metermaster-android-app`](metermaster-android-app/SHEET.md) | MeterMaster Android App | W2 | R2 | — | `metermaster-app` |
| [`ssd1306-oled-ui`](ssd1306-oled-ui/SHEET.md) | SSD1306 OLED UI (small) | W2 | R2 | — | `esp32-metermaster`, `esp32-ai` |
| [`webradio-browser-host`](webradio-browser-host/SHEET.md) | Web-Radio Browser Host (ESP) | W2 | R1 | — | `esp32-webradio` |

### H — Test / Analyse

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`ble-http-gatt-probe`](ble-http-gatt-probe/SHEET.md) | HTTP-gesteuerte BLE-GATT-Sonde | W2 | R3 | LAB | `esp32-ftmsprobe` |
| [`ble-rssi-proximity`](ble-rssi-proximity/SHEET.md) | BLE RSSI Proximity Hunt | W1 | R0 | — | `esp-ble-finder` |
| [`esp-lab-bus-tools`](esp-lab-bus-tools/SHEET.md) | ESP Lab Bus / GPIO Tools | W3 | R1 | — | `esp32-io-control`, `esp32-toolnode` |
| [`esp-wifi-promiscuous-pcap`](esp-wifi-promiscuous-pcap/SHEET.md) | ESP WiFi Promiscuous Sniff + PCAP Capture | W1 | R0 | — | `esp32-marauder` |
| [`lan-device-inventory`](lan-device-inventory/SHEET.md) | LAN Device Inventory Scan | W2 | R1 | — | `esp32-network` |
| [`rf-environment-monitor`](rf-environment-monitor/SHEET.md) | RF Environment Monitor | W3 | R3 | LAB, GENERAL | `esp32-rfmonitor`, `esp32-toolnode` |
| [`sdr-spectrum-fft`](sdr-spectrum-fft/SHEET.md) | SDR Spectrum / FFT Analysis | W3 | R2 | — | `pidrive` |
| [`wifi-csi-motion`](wifi-csi-motion/SHEET.md) | Wi-Fi CSI Motion Sensing | W1 | R0 | — | `espectre` |

### I — Fahrzeug / Geräte

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`bmw-nbt-evo`](bmw-nbt-evo/SHEET.md) | BMW NBT Evo Head Unit — Host-Plattform | W1 | R3 | LAB, FIELD, HOST-SPECIFIC | `pidrive`, `esp32-bt-gateway`, `bmw-nbt-media-index`, `hu-probe` |
| [`hammer-varon-xtr`](hammer-varon-xtr/SHEET.md) | Hammer Varon XTR II (FTMS Host) | W2 | R3 | LAB, FIELD, DEVICE-SPECIFIC | `esp32-ftmsprobe`, `esp32-ergo` |

### J — Architektur

| Slug | Title | W | Evid | Scope | Gesehen in |
|------|-------|---|------|-------|------------|
| [`esp-hub-base-template`](esp-hub-base-template/SHEET.md) | ESP-Hub Base Firmware Template | W4 | R3 | LAB, GENERAL | `esp32-esp-hub` |
| [`esp-module-host`](esp-module-host/SHEET.md) | ESP Modular Tool Firmware | W2 | R1 | — | `esp32-toolnode` |
| [`pdap`](pdap/SHEET.md) | PDAP (PCM + Control over WiFi) | W1 | R0 | — | `esp32-bt-gateway`, `esp-network-pcm-clock` |

## Geplant (ohne Sheet)

Pflege: [`_planned.txt`](_planned.txt) · dann `ta-assist index`.

`pipewire` · `scsi` · `esp32` · `fat` · `systemd` · `mpris2` · `webradio (Pi-Stack; ESP hat webradio-browser-host)`
