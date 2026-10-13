# Project Application: esp-i2s-audio in esp-usb-audio-example

```yaml
project_id: esp-usb-audio-example
tech_slug: esp-i2s-audio
status: active
sheet: ../../../technologies/esp-i2s-audio/SHEET.md
audit: ../../../audits/esp-usb-audio-example-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

I2S Full-Duplex-Bridge der BOX-Codecs: ES8311 (Speaker out) + ES7210 (Mic in) über I2S STD, getaktet auf USB-Audio-Sample-Rate (48 kHz).

| Repo | Commit | Rolle |
|------|--------|-------|
| [finger563/esp-usb-audio-example](https://github.com/finger563/esp-usb-audio-example) | `662f2c0` | `main/i2s_audio.cpp` + codec components |

## Architektur / Datenfluss

```text
UAC Speakers buffers → I2S TX → ES8311 → Speaker
Mic → ES7210 → I2S RX → UAC Mic buffers
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `main/i2s_audio.cpp` | I2S STD TX/RX, volume/mute |
| `main/box.hpp` / `box_3.hpp` | Pin/Port HAL |
| `components/codec/es8311/` · `es7210/` | Codec Treiber |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| I2S STD + ES8311/ES7210 für BOX | `EVID-USBAUD-EX-2026-10-13-004` | `FACT` |
| Sample-Rate an USB 48 kHz gekoppelt | `EVID-USBAUD-EX-2026-10-13-003` | `FACT` |
| Audio-Qualität gemessen | — | `UNKNOWN` |

## Offene Fragen

- MCLK 256× — Drift vs. USB SOF ohne Feedback-EP Tuning?
