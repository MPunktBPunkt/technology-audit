# Evidence — esp32-bt-analyzer-host-profiles-2026-desk

Desk 2026-11-04 · **standard_version 0.7.1** · Campaign pins in README YAML.

Epistemics: Desk `FACT` = documented upstream behavior / license text. No Lab `MEASURED` in this campaign.

## BTstack

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTHPF-2026-11-04-001` | Architecture = cooperating state machines; single-threaded run loop; non-blocking; optional statically bounded memory; app Communication Logic as FSM + packet handlers | `FACT` | [Architecture manual](https://bluekitchen-gmbh.com/btstack/architecture/) |
| `EVID-BTHPF-2026-11-04-002` | Public LICENSE clause 4: redistribution/use/modification solely for personal benefit, not commercial / monetary gain; commercial licensing via BlueKitchen | `FACT` | [`LICENSE`](https://github.com/bluekitchen/btstack/blob/master/LICENSE) |
| `EVID-BTHPF-2026-11-04-003` | HOGP Host demo FSM scan→connect→pair→`hids_host_connect`; Report Map in caller buffer; Boot/Report protocol; `GATTSERVICE_SUBEVENT_HID_REPORT`; reconnect timers | `FACT` | [`example/hog_host_demo.c`](https://github.com/bluekitchen/btstack/blob/master/example/hog_host_demo.c) |
| `EVID-BTHPF-2026-11-04-004` | Classic HID Host API: `hid_host_init(storage)`, `hid_host_connect(addr, protocol_mode, &cid)`; descriptor available / capacity exceeded statuses | `FACT` | [`src/classic/hid_host.h`](https://github.com/bluekitchen/btstack/blob/master/src/classic/hid_host.h) |
| `EVID-BTHPF-2026-11-04-005` | Documented GATT Service Clients include HOGP Host; Classic profiles include A2DP/AVRCP/HFP/HID; ESP32 FreeRTOS port listed | `FACT` | [GitHub README / Profiles manual](https://bluekitchen-gmbh.com/btstack/profiles/) |

## ESP-IDF

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTHPF-2026-11-04-010` | Bluedroid GATTC: connect → MTU → `DIS_SRVC_CMPL` → `search_service` → char discovery → notify register; search may source remote or NVS cache | `FACT` | [`gattc_demo.c`](https://github.com/espressif/esp-idf/blob/master/examples/bluetooth/bluedroid/ble/gatt_client/main/gattc_demo.c) · [GATT Client API](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gattc.html) |
| `EVID-BTHPF-2026-11-04-011` | NimBLE `blecent`: peer_disc services→chars→descriptors→complete; optional encryption before GATT ops; EATT gating documented | `FACT` | [`examples/bluetooth/nimble/blecent`](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/nimble/blecent) README + main |
| `EVID-BTHPF-2026-11-04-012` | A2DP Sink example: SBC decode + I2S; at most one A2DP connection; can coexist with HFP/SPP but not A2DP Source simultaneously | `FACT` | [`classic_bt/a2dp_sink`](https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt/a2dp_sink) README |
| `EVID-BTHPF-2026-11-04-013` | Classic-only examples call `esp_bt_controller_mem_release(ESP_BT_MODE_BLE)` | `FACT` | Prior `EVID-BTCL-2026-10-28-003`/`030` + a2dp_source main |
| `EVID-BTHPF-2026-11-04-014` | Host/Controller VHCI scenarios documented; Bluedroid tasks BTC/BTU/HCI | `FACT` | [BT architecture overview](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/bt-architecture/overview.html) |

## Zephyr

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTHPF-2026-11-04-020` | LE Host layers: HCI driver → GAP roles (Kconfig) → L2CAP/GATT/SM; callbacks must stay short / defer work; ATT timeout initiates disconnect | `FACT` | [LE Host docs](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/bluetooth-le-host.html) |
| `EVID-BTHPF-2026-11-04-021` | HOGP Host RFC proposes 18-state discovery FSM, `bt_hogp_host_connect()`, BAS/DIS, Input Report auto-subscribe (tracking / phased — not assumed merged SoT) | `FACT` | [Issue #108582](https://github.com/zephyrproject-rtos/zephyr/issues/108582) |
| `EVID-BTHPF-2026-11-04-022` | Existing HOG samples are primarily HID **service/device** attribute layouts (Report Map, CCC, Control Point) | `FACT` | Zephyr `samples/bluetooth` HOG/HID history |

## FTMS specialized

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTHPF-2026-11-04-030` | pyftms: Apache-2.0 async FTMS client; machine-specific realtime models + Control Point models; Bleak transport | `FACT` | [dudanov/python-pyftms](https://github.com/dudanov/python-pyftms) · [PyPI](https://pypi.org/project/pyftms/) |
| `EVID-BTHPF-2026-11-04-031` | FTMS.NET: GPL-3.0; transport-agnostic connection interface; does not gate writes on Feature flags (manufacturer flags unreliable) | `FACT` | [nilsauf/FTMS.NET](https://github.com/nilsauf/FTMS.NET) README · NuGet 0.7.0 |
| `EVID-BTHPF-2026-11-04-032` | KB sheet already: CP Success ≠ Wirkung; Indicate-vs-Notify hypothesis; Feature bits ≠ IBD fields | `FACT` | [`technologies/bluetooth-ftms/SHEET.md`](../../technologies/bluetooth-ftms/SHEET.md) |

## TI HOGP / BlueZ / bluetooth_stack

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTHPF-2026-11-04-040` | TI HOGP example implements HOGP **Device** (keyboard/mouse/consumer), not Host | `FACT` | [TexasInstruments/HOGP-BLE-HID-EXAMPLE](https://github.com/TexasInstruments/HOGP-BLE-HID-EXAMPLE) · [SWRA715](https://www.ti.com/lit/pdf/swra715) |
| `EVID-BTHPF-2026-11-04-041` | Prior Classic-gaps: BTstack has Classic HID Host; IDF mouse example is Device-only / BR/EDR-only defaults | `FACT` | `EVID-BTCL-2026-10-28-032`/`050` |
| `EVID-BTHPF-2026-11-04-042` | bluetooth_stack: educational dual-mode HCI-up stack; ESP32 listed; prior audit warns chip matrix ≠ full host on ESP | `FACT` | Prior [`bluetooth-stack-2026-foreign`](../bluetooth-stack-2026-foreign/) · upstream README |

## Analyzer project anchors

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTHPF-2026-11-04-050` | Project SCOPE: Analyzer ≠ Universal Host; full A2DP/HFP / HID keystroke path deferred; F_ONCHIP VHCI primary; Classic on S3 REJECTED | `FACT` | [`projects/esp32-bt-analyzer/SCOPE.md`](../../projects/esp32-bt-analyzer/SCOPE.md) |
| `EVID-BTHPF-2026-11-04-051` | FW pin documented 0.3.0 in SCOPE; inventory still notes thin ATT L2 ≠ Air FACT | `FACT` | SCOPE `fw_pin: "0.3.0"` · INVENTORY |

## Offene Claims (FOLLOW-ON Lab)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Flavor-on vs Flavor-off PSRAM loss delta | `UNKNOWN` | S1 Lab |
| NimBLE GATTC beside VHCI tap without host double-consume | `HYPOTHESIS` | Needs architecture spike |
| HOGP Report Map sizes on real keyboards vs buffer budget | `UNKNOWN` | S3 |
| A2DP Sink + HCI dump concurrent on `.87` | `UNKNOWN` | S6 or REJECTED |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-28 | Classic-gaps + GATT-bridge desks |
| 2026-11-04 | Host-Profiles desk → Flavor adoption order |
