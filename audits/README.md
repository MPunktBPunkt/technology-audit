# audits/

Zeitlich begrenzte Analyse-Kampagnen. Jede Kampagne: `standard_version` (= [`VERSION`](../VERSION) / [`STANDARD-CHANGELOG`](../docs/STANDARD-CHANGELOG.md)). `audits/<id>/README.md` · Profile: [`AUDIT-PROFILES.md`](../docs/AUDIT-PROFILES.md).

## Index

| ID | Status | Profil | Fokus |
|----|--------|--------|-------|
| [`pidrive-2026-msc`](pidrive-2026-msc/) | closed | ops-field | Pilot 1 — USB-MSC |
| [`pidrive-2026-bmw-hu`](pidrive-2026-bmw-hu/) | active | ops-field | Pilot 2 — BMW NBT Evo · Busy-Pacing Feld 2026-10-12 · **0.7.1** Method-/Gate-Nachzug |
| [`pidrive-2026-10-17-prefetch-livelock`](pidrive-2026-10-17-prefetch-livelock/) | active | ops-field | Abend-Feld 2026-10-17 — Quiet/Storm-Muster, 167/136-Plateau, Guess-im-Storm · **0.7.1** |
| [`pidrive-2026-storm-capture-tooling`](pidrive-2026-storm-capture-tooling/) | closed | lab-tool | Desk-Fitness M30–M32: eigene MessCapture/Band-Report vs. Fremd-FAT/USB-Tools · **0.7.1** |
| [`prefetch-livelock-public-gap-2026`](prefetch-livelock-public-gap-2026/) | closed | lab-tool | Public Gap: Boot/Dump/KeenLab/Generic-MSC ≠ Storm/Q; eigene Instrumentierung P0 · **0.7.1** |
| [`pidrive-2026-radio-bt`](pidrive-2026-radio-bt/) | active | ops-field | DAB+/PMR/Airband/FFT + A2DP/AVRCP · **0.6.6** revalidated (from 0.6.3) |
| [`pi-fm-tx-2026-foreign`](pi-fm-tx-2026-foreign/) | active | lab-tool | Fremd: pifm + PiFmRds (GPIO-FM/RDS) · **0.6.6** revalidated (from 0.6.3) |
| [`esp-fm-tx-2026-foreign`](esp-fm-tx-2026-foreign/) | active | lab-tool | Fremd: ESP32 APLL/MCLK-FM (Alexxdal + hiperiondev) · **0.6.6** |
| [`esp-fm-rds-node-2026-foreign`](esp-fm-rds-node-2026-foreign/) | closed | lab-tool | Fremd: S3-I2S-MPX + QN8027/Si4713 · **0.7.1** |
| [`esp-network-pcm-clock-2026-foreign`](esp-network-pcm-clock-2026-foreign/) | active | lab-tool | Fremd: RTP/TCP PCM, Jitterbuffer und Clockdrift · **0.7.1** |
| [`bmw-nbt-media-index-2026-foreign`](bmw-nbt-media-index-2026-foreign/) | closed | lab-tool | Fremd: BMW Offline-Medien-/Forensikkontext · **0.7.1** |
| [`usb-bot-observation-2026-foreign`](usb-bot-observation-2026-foreign/) | closed | lab-tool | Fremd: BOT-Command-Beobachtung und Capture-Grenzen · **0.7.1** |
| [`usb-bot-observation-2026-instrument-sources`](usb-bot-observation-2026-instrument-sources/) | closed | lab-tool | Fremd: TinyUSB-Hooks, usbsnoop, BOT-Schema · **0.7.1** |
| [`usb-control-stall-recovery-2026`](usb-control-stall-recovery-2026/) | closed | lab-tool | Follow-on: usbd Control/Enum/STALL, esp_tinyusb, EspUsbDevice · **0.7.1** |
| [`esp32-s3-usb-wifi-coexistence-2026`](esp32-s3-usb-wifi-coexistence-2026/) | closed | lab-tool | S3 USB OTG Device ↔ WiFi Coex-Karte (hu-probe) · **0.7.1** |
| [`esp32-s3-hw-limits-2026`](esp32-s3-hw-limits-2026/) | closed | lab-tool | S3 Chip-Errata + HW-Limits (CACHE/ANALOG/USB-OTG/RTC) für MSC/Storm · **0.7.1** |
| [`msc-host-read-semantics-s1s2s3-2026`](msc-host-read-semantics-s1s2s3-2026/) | closed | lab-tool | hu-probe S1–S3 Messplan (Eager/Prefetch/Cache); PiDrive-Claims ≠ FACT · **0.7.1** |
| [`hu-probe-bmw-s0s2-field-2026`](hu-probe-bmw-s0s2-field-2026/) | closed | lab-tool | hu-probe BMW S0/S2 Transport-Feld + Lab Offline; Semantik INFERENCE · **0.7.1** |
| [`hu-probe-bmw-s2-abend-offline-2026-10-18`](hu-probe-bmw-s2-abend-offline-2026-10-18/) | closed | lab-tool | hu-probe BMW S2 Abend Offline; CBW-Atom 240+69 · **0.7.1** |
| [`hu-probe-psram-board-free-2026-10-21`](hu-probe-psram-board-free-2026-10-21/) | closed | lab-tool | PSRAM N8R2 + free Offline Grammar demo_v1 · **0.7.1** |
| [`hu-probe-media-ladder-2026-10-22`](hu-probe-media-ladder-2026-10-22/) | closed | lab-tool | Media-Leiter Live: Head 32+128, Tail-Prefetch, Elevator, PiDrive-Vertrag · **0.7.1** |
| [`hu-probe-heimfahrt-2026-10-22`](hu-probe-heimfahrt-2026-10-22/) | closed | lab-tool | Heimfahrt Offline: Remount≠Cold Start, LBA-Scheduler, Eager≠Play, Lead kontextabhängig · **0.7.1** |
| [`technology-audit-2026-kb-measured`](technology-audit-2026-kb-measured/) | closed | ops-field | Meta: MEASURED-Corpus vs. Desk-FACT · **0.7.1** |
| [`esp32-sdr-trx-2026-foreign`](esp32-sdr-trx-2026-foreign/) | active | lab-tool | Fremd: S3 polar PHY TX + narrowband RX · **0.6.6** |
| [`espargos-espsdr-2026-foreign`](espargos-espsdr-2026-foreign/) | active | lab-tool | Fremd: ESPARGOS Undoc I/Q Chip-Matrix · **0.6.6** |
| [`c5vrx-2026-foreign`](c5vrx-2026-foreign/) | active | lab-tool | Fremd: C5VRX C5 FPV continuous I/Q · **0.6.6** |
| [`welle-io-2026-foreign`](welle-io-2026-foreign/) | active | lab-tool | Fremd: AlbrechtL/welle.io DAB+ Upstream · **0.6.6** revalidated (from 0.6.5) |
| [`rnt-esp32-2026-foreign`](rnt-esp32-2026-foreign/) | active | lab-tool | Fremd: RNT ESP32 Tutorial-Index (sekundär) · **0.6.6** |
| [`esp32-a2dp-2026-foreign`](esp32-a2dp-2026-foreign/) | active | lab-tool | Fremd: pschatzmann/ESP32-A2DP Classic A2DP/AVRCP · **0.6.6** |
| [`espble-2026-foreign`](espble-2026-foreign/) | active | lab-tool | Fremd: EspBle Classic A2DP + AVRCP CT/TG · **0.6.6** |
| [`a2dpsinkhfpclient-2026-foreign`](a2dpsinkhfpclient-2026-foreign/) | active | lab-tool | Fremd: A2DP Sink+HFP+AVRC API · **0.6.6** |
| [`esp-idf-classic-bt-2026-foreign`](esp-idf-classic-bt-2026-foreign/) | active | lab-tool | Fremd: IDF classic_bt AVRCP/A2DP examples · **0.6.6** |
| [`esp32-a2dp-codecs-2026-foreign`](esp32-a2dp-codecs-2026-foreign/) | active | lab-tool | Fremd: multi-codec A2DP sinks · **0.6.6** |
| [`esp32-a2dp-source-2026-foreign`](esp32-a2dp-source-2026-foreign/) | active | lab-tool | Fremd: schreibfaul1 A2DP Source · **0.6.6** |
| [`esp32-bt-iap-2026-foreign`](esp32-bt-iap-2026-foreign/) | active | lab-tool | Fremd: fanthos bt-iap (historisch) · **0.6.6** |
| [`esphome-a2dp-sink-2026-foreign`](esphome-a2dp-sink-2026-foreign/) | active | lab-tool | Fremd: ESPHome a2dp_sink entities · **0.6.6** |
| [`esp32sdr-2026-foreign`](esp32sdr-2026-foreign/) | active | lab-tool | Fremd: lozaning/ESP32SDR tone-TX + burst RX · **0.6.6** |
| [`espusbhost-2026-foreign`](espusbhost-2026-foreign/) | active | lab-tool | Fremd: EspUsbHost USB Host S2/S3/P4 · **0.6.6** |
| [`esp-iot-solution-2026-foreign`](esp-iot-solution-2026-foreign/) | active | lab-tool | Fremd: Espressif IoT Solution USB UAC/Host-Stream · **0.7.1** |
| [`esp32-audioi2s-2026-foreign`](esp32-audioi2s-2026-foreign/) | active | lab-tool | Fremd: schreibfaul1 ESP32-audioI2S Decode→I2S · **0.7.1** |
| [`esp-usb-audio-example-2026-foreign`](esp-usb-audio-example-2026-foreign/) | active | lab-tool | Fremd: finger563 S3-BOX USB Headset · **0.7.1** |
| [`esp32-ai-2026-foreign`](esp32-ai-2026-foreign/) | active | lab-tool | Fremd: slvDev esp32-ai PLE-LLM + Fly-Connectome · **0.7.1** |
| [`esp32-marauder-2026-foreign`](esp32-marauder-2026-foreign/) | active | lab-tool | Fremd: ESP32Marauder Promiscuous/PCAP (keine Attack-How-tos) · **0.7.1** |
| [`espectre-2026-foreign`](espectre-2026-foreign/) | active | lab-tool | Fremd: ESPectre Wi-Fi CSI Motion Sensing · **0.7.1** |
| [`esp32-doom-2026-foreign`](esp32-doom-2026-foreign/) | active | lab-tool | Fremd: ESP32-DOOM PrBoom + PSRAM Heavy Port · **0.7.1** |
| [`tinysstv-2026-foreign`](tinysstv-2026-foreign/) | active | lab-tool | Fremd: TinySSTV Martin M1 AF SSTV · **0.7.1** |
| [`squeezelite-esp32-2026-foreign`](squeezelite-esp32-2026-foreign/) | active | lab-tool | Fremd: Squeezelite-ESP32 LMS Multi-Room · **0.7.1** |
| [`esp32-spotify-remote-2026-foreign`](esp32-spotify-remote-2026-foreign/) | active | lab-tool | Fremd: Spotify Web API + PKCE Remote · **0.7.1** |
| [`open-bike-computer-2026-foreign`](open-bike-computer-2026-foreign/) | active | lab-tool | Fremd: Open Bike Computer Ride BLE Display · **0.7.1** |
| [`esp-ble-finder-2026-foreign`](esp-ble-finder-2026-foreign/) | active | lab-tool | Fremd: BLE RSSI Proximity Hunt · **0.7.1** |
| [`esp32-i2s-ble-2026-foreign`](esp32-i2s-ble-2026-foreign/) | active | lab-tool | Fremd: I2S-Mic → Custom BLE PCM Notify · **0.7.1** |
| [`esp32-msc-gadget-refs-2026-foreign`](esp32-msc-gadget-refs-2026-foreign/) | active | lab-tool | Fremd: ESP32 USB-MSC Gadgets + virtual FAT / Perf · **0.6.6** |
| [`tinyusb-msc-busy-retry-2026`](tinyusb-msc-busy-retry-2026/) | closed | lab-tool | TinyUSB MSC `return 0`/BUSY/ASYNC (E7-Basis; Feld S6 validiert) · **0.6.6** + 0.7.0-Retro |
| [`esp-sdr-bridge-2026-foreign`](esp-sdr-bridge-2026-foreign/) | active | lab-tool | Fremd: esp-sdr-bridge IQS→SpyServer/rtl_tcp · **0.6.6** |
| [`bluetooth-stack-2026-foreign`](bluetooth-stack-2026-foreign/) | active | lab-tool | Fremd: bluetooth_stack HCI-Host Kontrast · **0.6.6** |
| [`esp32-heartrate-2026-pilot`](esp32-heartrate-2026-pilot/) | active | firmware | HR Desk-Pilot · **0.6.6** revalidated (from 0.6.0) |
| [`esp32-ergo-2026-pilot`](esp32-ergo-2026-pilot/) | active | firmware | Ergo + Sheet-Wachstum · **0.6.6** revalidated (from 0.6.0) |
| [`esp32-ftmsprobe-2026-pilot`](esp32-ftmsprobe-2026-pilot/) | active | lab-tool | Sonde + Method · **0.6.6** revalidated (from 0.6.0) |
| [`esp32-bt-gateway-2026-planning`](esp32-bt-gateway-2026-planning/) | active | planning | A2DP/AVRCP/PDAP Planung |
| [`esp32-rfmonitor-2026-pilot`](esp32-rfmonitor-2026-pilot/) | closed | firmware | RF-Monitor Desk-Pilot · **0.6.0** → superseded by v2-validation |
| [`esp32-rfmonitor-2026-v2-validation`](esp32-rfmonitor-2026-v2-validation/) | closed | firmware | RF-Monitor 1.5 Observability/Score-v2/Hub-v2 · **0.7.1** → motion-delta |
| [`esp32-rfmonitor-2026-motion-delta`](esp32-rfmonitor-2026-motion-delta/) | active | firmware | RF-Monitor 1.5→1.10.2 Motion/Char/History · **0.7.1** |
| [`esp32-rf-sensing-2026-desk`](esp32-rf-sensing-2026-desk/) | active | planning | RF-Sensing Messvertrag Desk (Phase 0 Reuse/Gap) · **0.7.1** |
| [`esp32-toolnode-2026-pilot`](esp32-toolnode-2026-pilot/) | active | firmware | Modular Node · **0.6.1** Geschwister-RF |
| [`esp32-metermaster-2026-pilot`](esp32-metermaster-2026-pilot/) | active | firmware | OLED + Triple-HTTP · **0.6.1** |
| [`esp32-webradio-2026-pilot`](esp32-webradio-2026-pilot/) | active | firmware | Browser-Radio · **0.6.2** |
| [`esp32-io-control-2026-pilot`](esp32-io-control-2026-pilot/) | active | firmware | Lab-GPIO · **0.6.2** |
| [`esp32-communicator-2026-pilot`](esp32-communicator-2026-pilot/) | active | firmware | ESP-NOW · **0.6.2** |
| [`esp32-network-2026-pilot`](esp32-network-2026-pilot/) | active | firmware | LAN-Scan + TR-064 · **0.6.2** |
| [`esp32-esp-hub-2026-pilot`](esp32-esp-hub-2026-pilot/) | active | firmware | esp-hub-base · **0.6.3** |
| [`esp32-pidrive-2026-pilot`](esp32-pidrive-2026-pilot/) | active | firmware | MSC-Gadget + PUMP · **0.6.3** |
| [`iobroker-esp-hub-2026-pilot`](iobroker-esp-hub-2026-pilot/) | active | adapter | Hub-Adapter · **0.6.3** |
| [`iobroker-metermaster-2026-pilot`](iobroker-metermaster-2026-pilot/) | active | adapter | MeterMaster Adapter · **0.6.3** |
| [`iobroker-kostalpiko-2026-pilot`](iobroker-kostalpiko-2026-pilot/) | active | adapter | Kostal PIKO · **0.6.3** |
| [`iobroker-fritzwireguard-2026-pilot`](iobroker-fritzwireguard-2026-pilot/) | active | adapter | WireGuard + Tunnel · **0.6.3** |
| [`iobroker-freeair100-2026-pilot`](iobroker-freeair100-2026-pilot/) | active | adapter | freeAir Portal · **0.6.3** |
| [`iobroker-kalender-2026-pilot`](iobroker-kalender-2026-pilot/) | active | adapter | Kalender · **0.6.3** |
| [`iobroker-linuxdashboard-2026-pilot`](iobroker-linuxdashboard-2026-pilot/) | active | adapter | Linux Dashboard · **0.6.3** |
| [`iobroker-mbrepository-2026-pilot`](iobroker-mbrepository-2026-pilot/) | active | adapter | MB Repository · **0.6.3** |
| [`metermaster-app-2026-pilot`](metermaster-app-2026-pilot/) | active | ops-field | MeterMaster Android · **0.6.3** |
| [`iobroker-repositories-2026-ops`](iobroker-repositories-2026-ops/) | active | ops-field | Catalog-Fork · **0.6.3** |

Feldmessung AVRCP/A2DP: Desk in [`pidrive-2026-radio-bt`](pidrive-2026-radio-bt/); Gateway-Phase −1 weiter in [`esp32-bt-gateway-2026-planning`](esp32-bt-gateway-2026-planning/).
