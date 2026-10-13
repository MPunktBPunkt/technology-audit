# Project Scope: esp32-audioi2s (Fremd)

```yaml
project_id: esp32-audioi2s
title: ESP32-audioI2S — schreibfaul1 (Fremd)
updated: 2026-10-13
profile_hint: lab-tool
reviewed_commit: "45db753"
repos:
  - https://github.com/schreibfaul1/ESP32-audioI2S
status: active
```

## Zweck

Weit verbreitete Arduino-Library für Decode→I2S-DAC in die KB: Chip-Gates (Multi-Core/PSRAM), Abgrenzung zu Browser-Webradio und zu A2DP-Source-Beispiel.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESP32-audioI2S 4.0.0 | Decode-Player Library | ja (Desk) |
| Examples (SD, TTS, Ethernet, …) | Nutzungsmuster | sampled |
| I2S Bluetooth Transmitter Example | A2DP Source Bridge | angrenzend (Kontrast) |
| Feldmessung DAC/Latenz | — | FOLLOW-ON |

## Nicht-Ziele

- Jeden Codec-Pfad einzeln labormessen
- Browser-Webradio-Claims
- LE Audio

## Prioritäten

1. Sheet `esp-i2s-audio` + Application  
2. Chip-/PSRAM-Fallstricke  
3. Kontrast A2DP / Browser-Host
