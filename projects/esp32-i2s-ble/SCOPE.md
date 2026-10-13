# Project Scope: esp32-i2s-ble (Fremd)

```yaml
project_id: esp32-i2s-ble
title: esp32-i2s-BLE — I2S Mic → BLE PCM (Fremd)
updated: 2026-10-13
profile_hint: lab-tool
reviewed_commit: "4d053c4"
repos:
  - https://github.com/iancarscadden/esp32-i2s-BLE
status: active
```

## Zweck

Arbeitsbeispiel I2S-MEMS-Mic (SPH0645) → Ringbuffer → **Custom GATT PCM Notify** auf ESP32-S3 Feather. Pattern für Speech-Bridges; klar **kein** LE Audio / A2DP.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| PlatformIO Firmware `src/main.cpp` | Capture + BLE | ja (Desk) |
| iPhone Client App | Peer | nicht im Repo (observed) |
| LE Audio / A2DP | — | **nein** (Abgrenzung) |
| Feldmessung Packet-Loss | — | FOLLOW-ON |

## Nicht-Ziele

- Standard-Bluetooth-Audio-Profile erfinden
- README-16 kHz ohne Code-Check als Wire-Rate übernehmen

## Prioritäten

1. Sheet `ble-pcm-notify-stream` + App  
2. App `esp-i2s-audio` (Capture)  
3. Capture vs. Output Sample-Rate dokumentieren
