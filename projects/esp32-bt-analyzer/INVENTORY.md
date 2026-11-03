# Project Inventory: esp32.bt-analyzer

```yaml
project_id: esp32-bt-analyzer
updated: 2026-11-03
reviewed_commit: pending
profile: lab-tool
pilot_order: [esp-usb-host, esp-hub-telemetry, esp32-s3-silicon, esp32-s3-usb-wifi-coex]
```

Bootstrap-Stub vor erstem Lab-Lauf. Ursprungsrepo: [esp32.bt-analyzer](https://github.com/MPunktBPunkt/esp32.bt-analyzer).  
Methods: [bt-usb-hci-observe-baseline](../../methods/bt-usb-hci-observe-baseline.md), [bt-passive-host-sniff](../../methods/bt-passive-host-sniff.md).  
Capture-Kontext: [bt-sniffing-capture-refs](../bt-sniffing-capture-refs/).  
Instrument lab: `.88` OBSERVE_A · `.89` B/C · `.87` REF_ENDPOINT (classic, no OTG).

**Match (Signal → Slug):**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| USB OTG Host enum BT-Dongle | `esp-usb-host` | wachsen (Lab) |
| Hub register / OTA | `esp-hub-telemetry` | Application light |
| YD-ESP32-S3 N8R2 / OTG PHY | `esp32-s3-silicon` | Application light |
| HCI over WiFi TCP | `esp32-s3-usb-wifi-coex` | später BT4/BT13 |
| HCI snoop Semantik | Method `bt-passive-host-sniff` | Anker (kein Sheet) |
| Classic on-chip S3 | `bluetooth-a2dp` | **REJECTED** — nur referenzieren |
| Endpoint JSONL | `bt-endpoint-event-stream` | Contrast only |

## Übersicht

| Slug | Status | Coverage | Application |
|------|--------|----------|-------------|
| `esp-usb-host` | planned | none | [app](applications/esp-usb-host.md) |
| `esp-hub-telemetry` | planned | none | [app](applications/esp-hub-telemetry.md) |
| `esp32-s3-silicon` | planned | none | — |
| `esp32-s3-usb-wifi-coex` | planned | none | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| USB-HCI Capture auf S3 | kein KB FACT | BT1–BT3 Lab → EVID |
| BTAC / PCAPNG | Design only | BT4/BT8 |
| Classic vs BLE Dongle | Hardware pending | BT9/BT10 |
