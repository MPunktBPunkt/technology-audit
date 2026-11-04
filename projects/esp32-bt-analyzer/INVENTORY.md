# Project Inventory: esp32.bt-analyzer

```yaml
project_id: esp32-bt-analyzer
updated: 2026-11-04
reviewed_commit: 7c20367
fw_pin: "0.2.7"
profile: lab-tool
pilot_order: [esp-hub-telemetry, esp32-s3-silicon, esp32-s3-usb-wifi-coex, esp-usb-host]
```

Ursprungsrepo: [esp32.bt-analyzer](https://github.com/MPunktBPunkt/esp32.bt-analyzer).  
Methods: [bt-passive-host-sniff](../../methods/bt-passive-host-sniff.md) (HCI semantics).  
Lab: `.88` Central · `.89` Peripheral peer · `.87` Classic+BLE.

**Match (Signal → Slug):**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Hub register / OTA | `esp-hub-telemetry` | Application |
| YD-ESP32-S3 N8R2 / PSRAM | `esp32-s3-silicon` | Application |
| WiFi + BT coexistence | `esp32-s3-usb-wifi-coex` | BT13 stress MEASURED |
| On-chip VHCI HCI | Method `bt-passive-host-sniff` | Anker |
| USB OTG + dongle | `esp-usb-host` | legacy optional |
| Classic on-chip S3 | `bluetooth-a2dp` | **REJECTED** |
| RF Air | — | **BT15 deferred** |

## Übersicht

| Slug / Artifact | Status | Coverage |
|-----------------|--------|----------|
| On-chip VHCI BT1–BT3 | MEASURED | lab 0.2.6+ |
| BTAC / JSONL / PCAPNG BT4/7/8 | MEASURED | `tools/lab_run_gates.py` |
| BLE peer + connect BT9/11 | MEASURED | F_ONCHIP |
| Classic discoverable BT10 | MEASURED (HCI path) | `.87` |
| PSRAM ring / lossless BT5/6 | MEASURED | S3 512 slots |
| `esp-usb-host` dongle path | deferred/legacy | A_OBSERVE |

## Coverage-Lücken

| Bereich | Status | Nächster Schritt |
|---------|--------|------------------|
| External audit sign-off | partial | BT14 reviewer |
| Classic×Classic peer | limited (one Classic board) | second ESP32 or phone |
| RF/Air | out of scope | BT15 separate |
