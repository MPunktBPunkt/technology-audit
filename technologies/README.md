# technologies/

Wiederverwendbare Technology Sheets.

**Reuse:** [`docs/REUSE.md`](../docs/REUSE.md) · **Neustart:** [`docs/PROJECT-START.md`](../docs/PROJECT-START.md) · **Familien:** [`docs/FAMILIES.md`](../docs/FAMILIES.md) · **Standard:** [`VERSION`](../VERSION)

**Maschinenindex:** [`index.yaml`](index.yaml) (generiert — `2026-10-10`, 41 Sheets). Neu generieren: `python3 tools/ta-assist index`

## Index nach Primary (TAXONOMY)

### A — Empfang

| Slug | Title | Reuse | Gesehen in |
|------|-------|-------|------------|
| [`airband-am`](airband-am/SHEET.md) | VHF Airband AM Reception | W2 | `pidrive` |
| [`dab-plus`](dab-plus/SHEET.md) | DAB+ Digital Audio Broadcasting | W2 | `pidrive` |
| [`pmr446`](pmr446/SHEET.md) | PMR446 (EU License-Free UHF) | W2 | `pidrive` |
| [`rtl-sdr`](rtl-sdr/SHEET.md) | RTL-SDR (RTL2832U Host Stack) | W3 | `pidrive` |

### C — Protokolle

| Slug | Title | Reuse | Gesehen in |
|------|-------|-------|------------|
| [`avrcp`](avrcp/SHEET.md) | AVRCP | W2 | `pidrive`, `esp32-bt-gateway` |
| [`ble-hr-relay`](ble-hr-relay/SHEET.md) | BLE HR-Relay (Peripheral Bridge) | W3 | `esp32-heartrate`, `esp32-ergo` |
| [`ble-hrm-gatt`](ble-hrm-gatt/SHEET.md) | BLE Heart Rate GATT (Central) | W3 | `esp32-heartrate`, `esp32-ergo`, `esp32-ftmsprobe` |
| [`bluetooth-a2dp`](bluetooth-a2dp/SHEET.md) | Bluetooth A2DP | W2 | `pidrive`, `esp32-bt-gateway` |
| [`bluetooth-ftms`](bluetooth-ftms/SHEET.md) | Bluetooth FTMS (Fitness Machine) | W3 | `esp32-ftmsprobe`, `esp32-ergo` |
| [`esp-now-messaging`](esp-now-messaging/SHEET.md) | ESP-NOW Messaging | W2 | `esp32-communicator` |
| [`fm-rds`](fm-rds/SHEET.md) | FM-RDS (Radio Data System) | W2 | `pi-fm-tx` |
| [`kostal-piko-http`](kostal-piko-http/SHEET.md) | Kostal PIKO Local HTTP Interface | W2 | `iobroker-kostalpiko` |
| [`pump-control-link`](pump-control-link/SHEET.md) | PUMP Control Link | W2 | `esp32-pidrive` |
| [`usb-msc`](usb-msc/SHEET.md) | USB Mass Storage Class | W2 | `projects/pidrive`, `esp32-pidrive` |

### D — Embedded

| Slug | Title | Reuse | Gesehen in |
|------|-------|-------|------------|
| [`rpi-gpio-fm-tx`](rpi-gpio-fm-tx/SHEET.md) | Raspberry Pi GPIO / Clock FM Transmit | W3 | `pi-fm-tx` |
| [`rpitx`](rpitx/SHEET.md) | rpitx — Raspberry Pi Software RF Transmit Platform | W2 | `pi-fm-tx` |

### F — Systemintegration

| Slug | Title | Reuse | Gesehen in |
|------|-------|-------|------------|
| [`esp-hub-telemetry`](esp-hub-telemetry/SHEET.md) | ESP-Hub Node Telemetry | W4 | `esp32-heartrate`, `esp32-ergo`, `esp32-ftmsprobe`, `esp32-bt-gateway`, `esp32-rfmonitor`, `esp32-toolnode`, `esp32-metermaster`, `esp32-webradio`, `esp32-io-control`, `esp32-communicator`, `esp32-network`, `esp32-esp-hub`, `iobroker-esp-hub`, `esp32-pidrive` |
| [`freeair-connect-portal`](freeair-connect-portal/SHEET.md) | bluMartin freeAir Connect Portal | W1 | `iobroker-freeair100` |
| [`fritzbox-tr064`](fritzbox-tr064/SHEET.md) | FritzBox TR-064 Hostlist | W2 | `esp32-network`, `iobroker-fritzwireguard` |
| [`iobroker-esp-hub-adapter`](iobroker-esp-hub-adapter/SHEET.md) | ioBroker ESP-Hub Adapter | W3 | `iobroker-esp-hub` |
| [`iobroker-fritzwireguard-adapter`](iobroker-fritzwireguard-adapter/SHEET.md) | ioBroker FritzWireguard Adapter | W2 | `iobroker-fritzwireguard` |
| [`iobroker-kalender-adapter`](iobroker-kalender-adapter/SHEET.md) | ioBroker Calendar Adapter | W2 | `iobroker-kalender` |
| [`iobroker-linuxdashboard-adapter`](iobroker-linuxdashboard-adapter/SHEET.md) | ioBroker Linux Dashboard Adapter | W2 | `iobroker-linuxdashboard` |
| [`iobroker-mbrepository-adapter`](iobroker-mbrepository-adapter/SHEET.md) | ioBroker MB Repository Manager | W2 | `iobroker-mbrepository` |
| [`iobroker-metermaster-adapter`](iobroker-metermaster-adapter/SHEET.md) | ioBroker MeterMaster Adapter | W2 | `iobroker-metermaster`, `esp32-metermaster`, `metermaster-app` |
| [`iobroker-simple-api`](iobroker-simple-api/SHEET.md) | ioBroker Simple-API Client | W2 | `esp32-metermaster` |
| [`mqtt-node-telemetry`](mqtt-node-telemetry/SHEET.md) | MQTT Node Telemetry | W2 | `esp32-toolnode` |

### G — Steuerung / UI

| Slug | Title | Reuse | Gesehen in |
|------|-------|-------|------------|
| [`esp-embedded-web-sse`](esp-embedded-web-sse/SHEET.md) | Embedded Web REST + SSE | W3 | `esp32-heartrate`, `esp32-ergo`, `esp32-ftmsprobe`, `esp32-rfmonitor`, `esp32-toolnode`, `esp32-io-control`, `esp32-communicator`, `esp32-network`, `esp32-esp-hub` |
| [`metermaster-android-app`](metermaster-android-app/SHEET.md) | MeterMaster Android App | W2 | `metermaster-app` |
| [`ssd1306-oled-ui`](ssd1306-oled-ui/SHEET.md) | SSD1306 OLED UI (small) | W2 | `esp32-metermaster` |
| [`webradio-browser-host`](webradio-browser-host/SHEET.md) | Web-Radio Browser Host (ESP) | W2 | `esp32-webradio` |

### H — Test / Analyse

| Slug | Title | Reuse | Gesehen in |
|------|-------|-------|------------|
| [`ble-http-gatt-probe`](ble-http-gatt-probe/SHEET.md) | HTTP-gesteuerte BLE-GATT-Sonde | W2 | `esp32-ftmsprobe` |
| [`esp-lab-bus-tools`](esp-lab-bus-tools/SHEET.md) | ESP Lab Bus / GPIO Tools | W3 | `esp32-io-control`, `esp32-toolnode` |
| [`lan-device-inventory`](lan-device-inventory/SHEET.md) | LAN Device Inventory Scan | W2 | `esp32-network` |
| [`rf-environment-monitor`](rf-environment-monitor/SHEET.md) | RF Environment Monitor | W3 | `esp32-rfmonitor`, `esp32-toolnode` |
| [`sdr-spectrum-fft`](sdr-spectrum-fft/SHEET.md) | SDR Spectrum / FFT Analysis | W3 | `pidrive` |

### I — Fahrzeug / Geräte

| Slug | Title | Reuse | Gesehen in |
|------|-------|-------|------------|
| [`bmw-nbt-evo`](bmw-nbt-evo/SHEET.md) | BMW NBT Evo Head Unit — Host-Plattform | W1 | `projects/pidrive`, `esp32-bt-gateway` |
| [`hammer-varon-xtr`](hammer-varon-xtr/SHEET.md) | Hammer Varon XTR II (FTMS Host) | W2 | `esp32-ftmsprobe`, `esp32-ergo` |

### J — Architektur

| Slug | Title | Reuse | Gesehen in |
|------|-------|-------|------------|
| [`esp-hub-base-template`](esp-hub-base-template/SHEET.md) | ESP-Hub Base Firmware Template | W3 | `esp32-esp-hub` |
| [`esp-module-host`](esp-module-host/SHEET.md) | ESP Modular Tool Firmware | W2 | `esp32-toolnode` |
| [`pdap`](pdap/SHEET.md) | PDAP (PCM + Control over WiFi) | W1 | `esp32-bt-gateway` |

## Geplant (ohne Sheet)

Pflege: [`_planned.txt`](_planned.txt) · dann `ta-assist index`.

`pipewire` · `scsi` · `esp32` · `fat` · `systemd` · `mpris2` · `webradio (Pi-Stack; ESP hat webradio-browser-host)`
