# Project Inventory: bt-classic-profile-refs

```yaml
project_id: bt-classic-profile-refs
updated: 2026-10-28
reviewed_commit: "multi-2026-10-28"
profile: lab-tool
pilot_order: [bluetooth-hfp, bluetooth-spp, bluetooth-hid, bt-dual-mode-coex, hid-cross-transport-bridge]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| HFP HF/AG, SCO, CVSD/mSBC, Call-Control | `bluetooth-hfp` | **neu** |
| SPP RFCOMM Server/Client | `bluetooth-spp` | **neu** |
| Classic HID Device/Host + HOGP-Kontrast | `bluetooth-hid` | **neu** |
| BTDM Classic+BLE(+WiFi) Budget/Coex | `bt-dual-mode-coex` | **neu** |
| BLE HOGP → Classic HID Bridge | `hid-cross-transport-bridge` | **neu** |
| A2DP + HFP Audio-Mux | `bluetooth-a2dp` | **wachsen** (Cross-Ref) |
| AVRCP | `avrcp` | reused (Kontrast) |
| BLE UART / Custom GATT Serial | `ble-gatt-transparent-bridge` | Kontrast zu SPP |
| HCI-Host-Stack | `bluetooth-stack` | Kontrast |

Kampagne: [bt-classic-gaps-2026-foreign](../../audits/bt-classic-gaps-2026-foreign/).

## Repo-Kurzinventar

| Quelle @ pin | Profiles / Roles | Dual-Mode | Kern-Mechanismus |
|--------------|------------------|-----------|------------------|
| a2dpSinkHfpClient `df6c5f4` | HFP **HF**, A2DP Sink, AVRCP CT/TG, PBAC | **Classic-only** (BLE mem released) | HCI-SCO + ext codec + I2S Mux A2DP↔HFP |
| EspBle `ef09bed` | HFP HF+AG, SPP multi, HID Dev+Host, A2DP/AVRCP | **BTDM** via HCI-Broker + NimBLE | ESP32-only Dual-Host |
| esp32-hsp-hf `a7c9529` | HFP **HF** (Name≠HSP), SCO CVSD/mSBC | sdkconfig BTDM, App Classic | BTstack VHCI HFP demo |
| esp32-bthidbridge `5d3a563` | BLE HID **Host** + Classic HID **Device** | **BTDM** | Report passthrough + Output/Rumble |
| BTClassicSPP `0186d36` | SPP Server/Client | Arduino-default | Minimal RFCOMM serial, SEC_NONE |
| esp-idf classic_bt `4d80c1b` | HFP HF/AG, SPP, HID Device, A2DP… | Examples meist **BR/EDR-only** | Canonical Bluedroid + PCM/HCI |
| btstack `0f4dd2a` | HFP HF/AG, HSP, SPP, HID Dev/Host | Port BTDM-fähig | Alternative Host-Protokollsicht |

## Übersicht Sheets

| Slug | Primary | Status | Coverage | Sheet | Application |
|------|---------|--------|----------|-------|-------------|
| `bluetooth-hfp` | C | applied | partial | [SHEET](../../technologies/bluetooth-hfp/SHEET.md) | [app](applications/bluetooth-hfp.md) |
| `bluetooth-spp` | C | applied | partial | [SHEET](../../technologies/bluetooth-spp/SHEET.md) | [app](applications/bluetooth-spp.md) |
| `bluetooth-hid` | C | applied | partial | [SHEET](../../technologies/bluetooth-hid/SHEET.md) | [app](applications/bluetooth-hid.md) |
| `bt-dual-mode-coex` | C | applied | partial | [SHEET](../../technologies/bt-dual-mode-coex/SHEET.md) | [app](applications/bt-dual-mode-coex.md) |
| `hid-cross-transport-bridge` | C | applied | partial | [SHEET](../../technologies/hid-cross-transport-bridge/SHEET.md) | [app](applications/hid-cross-transport-bridge.md) |
| `bluetooth-a2dp` | C | documented | partial | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | — |
