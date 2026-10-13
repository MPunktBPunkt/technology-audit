# Project Scope: esp-usb-audio-example (Fremd)

```yaml
project_id: esp-usb-audio-example
title: ESP USB Audio Example — finger563 (Fremd)
updated: 2026-10-13
profile_hint: lab-tool
reviewed_commit: "662f2c0"
repos:
  - https://github.com/finger563/esp-usb-audio-example
status: active
```

## Zweck

Community-Beispiel: ESP32-S3-BOX/BOX-3 als **USB Audio Headset** (TinyUSB UAC + I2S Codecs) — Kontrast und Bestätigung zum offiziellen `usb_device_uac`.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| Main TinyUSB UAC + I2S | Headset Firmware | ja (Desk) |
| Codecs ES8311/ES7210 | Board-HAL | Application |
| espp Submodule | Dependency | nicht vertieft (leer ohne recursive clone) |
| Host-OS Lab | — | FOLLOW-ON |

## Nicht-Ziele

- Host-UAC (`usb_stream`)
- MSC-Gadget
- BLE/A2DP Claims

## Prioritäten

1. Applications auf `esp-usb-audio-uac` + `esp-i2s-audio`  
2. Chip-Gate S3 (sdkconfig)  
3. Kontrast zu esp-iot-solution Official Component
