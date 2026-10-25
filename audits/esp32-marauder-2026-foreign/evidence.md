# Evidence — esp32-marauder-2026-foreign

Desk 2026-10-25 · **standard_version 0.7.1** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/justcallmekoko/ESP32Marauder | `9386f3c0348c171eb58ef2e1ce1f0c2f555ba30c` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-MARAUDER-2026-10-25-001` | README: „suite of WiFi/Bluetooth offensive and defensive tools for the ESP32“; Topics inkl. deauthentication, wardriving, dualband, esp32-c5 | `FACT` | README, GitHub topics |
| `EVID-MARAUDER-2026-10-25-002` | `WiFiScan`: Promiscuous enable; Sniff-Callbacks; Mode `WIFI_SCAN_PACKET_RATE`; CLI sniff*/packetcount | `FACT` | WiFiScan.h/cpp, CommandLine.h |
| `EVID-MARAUDER-2026-10-25-003` | `Buffer`: bufA/bufB, `portMUX`, `pcapOpen`/`append(wifi_promiscuous_pkt_t)`; `PcapHeader`; `BUF_SIZE`/`SNAP_LEN` je PSRAM-Profil | `FACT` | Buffer.*, PcapHeader.*, configs.h |
| `EVID-MARAUDER-2026-10-25-004` | `DUAL_BAND_CHANNELS 51` + dual_band_channel_index; C5 Board-Targets; Desk-Scan ohne `xTaskCreatePinnedToCore` | `FACT` | configs.h, WiFiScan.cpp; code search |
| `EVID-MARAUDER-2026-10-25-005` | Produkt enthält Attack-Mode-Enums/CLI (`WIFI_ATTACK_*`, `attack`/`deauth`/`beacon`) — **Existenz**, keine Verfahrensdoku in KB | `FACT` | WiFiScan.h, CommandLine.h |
| `EVID-MARAUDER-2026-10-25-006` | `HAS_BT` → NimBLE; BLE sniff/scan CLI (`sniffbt`, …) | `FACT` | WiFiScan.h, CommandLine.h, configs |
| `EVID-MARAUDER-2026-10-25-007` | `MARAUDER_VERSION` `v1.19.2`; viele Board-Targets (Mini/V6–V8/CYD/Flipper/C5/…) | `FACT` | configs.h |
| `EVID-MARAUDER-2026-10-25-008` | Filter-Konstante MGMT\|DATA in WiFiScan.h | `FACT` | WiFiScan.h |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-25 | Desk-Bootstrap Capture/PCAP; Offensive TX existence-only |
