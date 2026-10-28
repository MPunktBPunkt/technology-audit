# Project Scope: bt-classic-profile-refs (Fremd)

```yaml
project_id: bt-classic-profile-refs
title: Bluetooth Classic Profile Gaps — HFP / SPP / HID / Dual-Mode (Fremd)
updated: 2026-10-28
profile_hint: lab-tool
reviewed_commit: "a2dpSinkHfpClient@df6c5f4 EspBle@ef09bed esp32-hsp-hf@a7c9529 esp32-bthidbridge@5d3a563 BTClassicSPP@0186d36 esp-idf@4d80c1b btstack@0f4dd2a"
repos:
  - https://github.com/walinsky/a2dpSinkHfpClient
  - https://github.com/tanakamasayuki/EspBle
  - https://github.com/atomic14/esp32-hsp-hf
  - https://github.com/anarsoul/esp32-bthidbridge
  - https://github.com/gmag11/BTClassicSPP
  - https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/bluedroid/classic_bt
  - https://github.com/bluekitchen/btstack
status: active
```

## Zweck

Desk-Extraktion der **Classic-Lücken** neben A2DP/AVRCP: HFP (Call + SCO), SPP (RFCOMM), HID (Device/Host) + HOGP-Kontrast, Dual-Mode/BTDM-Coexistence, optional Cross-Transport HID-Bridge. **Nicht** „noch mehr A2DP“.

## Systeme und Grenzen

| Quelle | Rolle | Im Scope? |
|--------|-------|-----------|
| a2dpSinkHfpClient | A2DP Sink + HFP HF + I2S-Mux + PBAC | ja (HFP-Fokus) |
| EspBle | Classic HFP/SPP/HID/A2DP + HCI-Broker Dual-Host | ja (ESP32-only) |
| esp32-hsp-hf | BTstack HFP HF + SCO (Name irreführend ≠ HSP) | ja |
| esp32-bthidbridge | BLE HOGP Host → Classic HID Device Bridge | ja |
| BTClassicSPP | Minimal SPP Server/Client | ja |
| esp-idf classic_bt | Offizielle HFP/SPP/HID/A2DP-Beispiele | ja |
| btstack src/classic | Alternative Host-Sicht HFP/HSP/SPP/HID | ja (Protokoll) |
| pschatzmann ESP32-A2DP | Kontrast (kein HFP) | Querverweis only |
| esp32-bt-gateway / pidrive | Reuse-Ziel | Querverweis |

## Nicht-Ziele

- Neues A2DP-/AVRCP-Sheet-Wachstum außer Cross-Refs
- Classic-Lab gegen BMW HU in dieser Kampagne
- Generisches „classic-relay“ ohne Profil
- Attack/Impersonation

## Prioritäten

1. Sheets `bluetooth-hfp`, `bluetooth-spp`, `bluetooth-hid`, `bt-dual-mode-coex`, `hid-cross-transport-bridge`  
2. Beobachtetes HFP in a2dpsinkhfpclient/espble → dokumentiert  
3. Reuse → bt-gateway / pidrive / Bridge-Projekte  
