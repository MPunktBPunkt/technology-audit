# Evidence — bluetooth-stack-2026-foreign

Desk 2026-10-12 · **standard_version 0.6.6** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/sj15712795029/bluetooth_stack | `6ef9436` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-BTSTK-A2DP-2026-10-12-001` | A2DP Sink headers + SBC third_party | `FACT` | classical/bt_a2dp_sink.h, sbc/ |
| `EVID-BTSTK-A2DP-2026-10-12-002` | Vendor `H4_NO_FW` = ESP32 support path | `FACT` | bt_vendor_no_fw.*, bt_config comment |
| `EVID-BTSTK-A2DP-2026-10-12-003` | Classical+BLE enable flags | `FACT` | bt_config.h |
| `EVID-BTSTK-AVRCP-2026-10-12-001` | AVRCP Controller header present | `FACT` | bt_avrcp_controller.h |
| `EVID-BTSTK-AVRCP-2026-10-12-002` | linux_bt `PROFILE_AVRCP_ENABLE 0` default | `FACT` | project/linux_bt/bt_config.h |
| `EVID-BTSTK-MATRIX-2026-10-12` | README: ESP32 column under Linux √ | `FACT` | README |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Produktiv einsetzbar vs. Lernstack | `UNKNOWN` | Author-Ziel „kommerziell“ unbelegt |
| ESP32 HCI dual-mode audio quality | `UNKNOWN` | Flag oft aus |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-12 | Desk Kontrast zu esp32-a2dp |
