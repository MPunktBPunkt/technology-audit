# Project Scope: esp32sdr (Fremd)

```yaml
project_id: esp32sdr
title: ESP32SDR — S3 Burst RX + Wi-Fi Tone Keying TX (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "dbff7bb"
repos:
  - https://github.com/lozaning/ESP32SDR
status: active
```

## Zweck

S3 Full-Duplex-Lab (zwei Boards): Undoc burst I/Q RX plus **arbeitender** TX über Wi-Fi-Tone-Keying — und explizite Falsifikation Raw-I/Q-DAC-TX auf S3.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| lozaning/ESP32SDR | Firmware RX+TX + GUI | ja (Desk) |
| ESPARGOS/esp-sdr | Burst-RX Provenance | angrenzend |
| Antennen-Feld-TX | — | **nein** |
| Eigene Remessung BER | — | FOLLOW-ON |

## Nicht-Ziele

- Raw-I/Q-TX als produktiven Contract behaupten
- Tone-TX mit polar-PHY oder APLL vermengen
- Author 0 % BER als KB-`MEASURED`

## Prioritäten

1. RX → `esp32-undoc-iq-rx`  
2. Neues Sheet `esp32-wifi-tone-tx`  
3. Raw-I/Q DAC = `REJECTED` auf S3 dokumentieren  
4. Kontrast zu `esp32-polar-phy-tx`
