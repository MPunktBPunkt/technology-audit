# Project Application: esp-i2s-audio in esp32-i2s-ble

```yaml
project_id: esp32-i2s-ble
tech_slug: esp-i2s-audio
status: active
sheet: ../../../technologies/esp-i2s-audio/SHEET.md
audit: ../../../audits/esp32-i2s-ble-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

I2S **RX**-Pfad: SPH0645LM4H MEMS Mic am Adafruit ESP32-S3 Feather; SEL→3V3 = RIGHT channel; 32-bit Samples → int16 Scale.

| Repo | Commit | Rolle |
|------|--------|-------|
| [iancarscadden/esp32-i2s-BLE](https://github.com/iancarscadden/esp32-i2s-BLE) | `4d053c4` | Capture Task |

## Architektur / Datenfluss

```text
SPH0645 DOUT
  → I2S STD RX (16 kHz, 32-bit containers, mono RIGHT)
  → shift/clamp → int16
  → optional downsample → BLE Ring
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/main.cpp` | Pins D5/D6/D9, I2S STD init, convert |
| `README.md` | Wiring + SEL-Hinweis |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Pins LRCLK=5 BCLK=6 DIN=9; SEL high = RIGHT | `EVID-I2SBLE-2026-10-13-004` | `FACT` |
| IDF 5.x I2S STD; 8 DMA desc × 512 samples | `EVID-I2SBLE-2026-10-13-005` | `FACT` |
| Audioqualität / Static Lab | — | `UNKNOWN` |

## Offene Fragen

- Shift-by-14 Skalierung — Mic-spezifisch oder übertragbar?
