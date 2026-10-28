# Evidence — bt-classic-gaps-2026-foreign

Desk 2026-10-28 · **standard_version 0.7.1** · Pins siehe Kampagne.

## a2dpSinkHfpClient @ `df6c5f4`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTCL-2026-10-28-001` | HFP HF Client init + call control APIs | `FACT` | [`a2dpSinkHfpHf.c`](https://github.com/walinsky/a2dpSinkHfpClient/blob/df6c5f4/src/a2dpSinkHfpHf.c) `esp_hf_client_*` |
| `EVID-BTCL-2026-10-28-002` | HCI-SCO / external codec path + I2S mux vs A2DP | `FACT` | `bt_app_hf.c` · `bt_i2s.c` · `sdkconfig.defaults` |
| `EVID-BTCL-2026-10-28-003` | Classic-only: `ESP_BT_MODE_CLASSIC_BT` + BLE `mem_release` | `FACT` | `a2dpSinkHfpHf.c` ~129–140 |

## EspBle @ `ef09bed`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTCL-2026-10-28-010` | HFP Client + AG APIs; Classic only `CONFIG_IDF_TARGET_ESP32` | `FACT` | [`EspBleClassicBuild.h`](https://github.com/tanakamasayuki/EspBle/blob/ef09bed/src/EspBleClassicBuild.h) · `EspBleClassic.cpp` hfp accessors |
| `EVID-BTCL-2026-10-28-011` | SPP `esp_spp_start_srv` (SCN dynamisch) | `FACT` | `EspBleClassic.cpp` ~728 |
| `EVID-BTCL-2026-10-28-012` | Classic HID Device+Host module present | `FACT` | `EspBleClassicHid.cpp` |
| `EVID-BTCL-2026-10-28-013` | Dual-Host HCI route NimBLE↔Classic / BTDM | `FACT` | `EspBleHciRouter.*` · Classic init mode |

## esp32-hsp-hf @ `a7c9529`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTCL-2026-10-28-020` | Code = **HFP HF** (`hfp_hf_init`) + SCO handler; CVSD/mSBC ifdef | `FACT` | [`hfp_hf_demo.c`](https://github.com/atomic14/esp32-hsp-hf/blob/a7c9529/main/hfp_hf_demo.c) · `sco_demo_util.c` |

## BTClassicSPP @ `0186d36`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTCL-2026-10-28-040` | SPP Server `SEC_NONE`, SCN 0; second connection rejected | `FACT` | [`BTSPP.cpp`](https://github.com/gmag11/BTClassicSPP/blob/0186d36/BTSPP.cpp) |

## esp-idf classic_bt @ `4d80c1b`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTCL-2026-10-28-030` | `hfp_hf`: `CONFIG_BT_HFP_CLIENT_ENABLE`, BLE off, BR/EDR-only | `FACT` | `examples/.../hfp_hf/sdkconfig.defaults` |
| `EVID-BTCL-2026-10-28-031` | `bt_spp_acceptor`: `CONFIG_BT_SPP_ENABLED`, BR/EDR-only | `FACT` | `.../bt_spp_acceptor/sdkconfig.defaults` |
| `EVID-BTCL-2026-10-28-032` | `bt_hid_mouse_device`: Classic HID Device, BR/EDR-only | `FACT` | `.../bt_hid_mouse_device/sdkconfig.defaults` |
| `EVID-BTCL-2026-10-28-033` | Classic examples default **not** BTDM | `FACT` | gleiche sdkconfig.defaults |

## esp32-bthidbridge @ `5d3a563`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTCL-2026-10-28-060` | BTDM + `HID_BRIDGE_MODE` init | `FACT` | [`sdkconfig.defaults`](https://github.com/anarsoul/esp32-bthidbridge/blob/5d3a563/sdkconfig.defaults) · [`esp_hid_gap.h`](https://github.com/anarsoul/esp32-bthidbridge/blob/5d3a563/main/esp_hid_gap.h) |
| `EVID-BTCL-2026-10-28-061` | BLE `esp_hidh_dev_open` + Classic `esp_hidd_dev_input_set` | `FACT` | [`bridge_main.c`](https://github.com/anarsoul/esp32-bthidbridge/blob/5d3a563/main/bridge_main.c) |
| `EVID-BTCL-2026-10-28-062` | Output/Feature → BLE; forward poll/coex documented in tree | `FACT` | `bridge_main.c` rumble/output paths · README |

## btstack @ `0f4dd2a`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTCL-2026-10-28-050` | Classic modules: `hfp_hf`/`hfp_ag`, `spp_server`, `hid_device`/`hid_host` | `FACT` | `src/classic/*.c` |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Gateway HFP Lab an BMW/Phone | `UNKNOWN` | FOLLOW-ON |
| Classic HID Host Bluedroid produktiv | `UNKNOWN` | kein IDF-Example |
| WiFi+A2DP+HFP+BLE gleichzeitig gemessen | `UNKNOWN` | |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-12 | A2DP-Katalog: HFP nur observed in a2dpsinkhfpclient/espble |
| 2026-10-28 | Classic-Gaps Desk → fünf neue Sheets |
