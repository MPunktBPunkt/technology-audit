# Project Application: esp-i2s-audio in esp32-audioi2s

```yaml
project_id: esp32-audioi2s
tech_slug: esp-i2s-audio
status: active
sheet: ../../../technologies/esp-i2s-audio/SHEET.md
audit: ../../../audits/esp32-audioi2s-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Arduino-Library **ESP32-audioI2S** 4.0.0: HTTP/SD/TTS-Quellen → Decoder (wav/mp3/aac/flac/opus/vorbis) → I2S Out zu externem DAC; optional Hook `audio_process_i2s` für BT-Weitergabe.

| Repo | Commit | Rolle |
|------|--------|-------|
| [schreibfaul1/ESP32-audioI2S](https://github.com/schreibfaul1/ESP32-audioI2S) | `45db753` | Library 4.0.0 |

## Architektur / Datenfluss

```text
URL / SD / TTS
  → Audio::loop + Decoder Tasks
  → Volume / EQ / Resampler
  → I2S STD (oft fest 48 kHz Out)
  → DAC (MAX98357A / PCM5102 / …)
     optional → audio_process_i2s → A2DP Source Example
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `library.properties` | version 4.0.0; PSRAM + external DAC |
| `README.md` | Chip-Warnung S3/S31/P4; Classic eingeschränkt; S2/C3 nein |
| `src/Audio.h` / `Audio.cpp` | API `setPinout`, I2S STD configs |
| `examples/I2S Bluetooth Transmitter/` | Bridge zu pschatzmann A2DP Source |

## Konfiguration (Desk)

| Parameter | Wert (Upstream) |
|-----------|-----------------|
| Codecs | wav, mp3, aac, flac, opus, vorbis |
| Sample rates | 16–48 kHz In; Out oft 44.1/48 fest |
| Bits | 8/16/24/32 |
| Volume | 0…21 default scale |
| Chip | multi-core; S2/C3 **nicht** |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| README: nur multi-core (S3/S31/P4); Classic limited; S2/C3 nein | `EVID-AUDIOI2S-2026-10-13-001` | `FACT` |
| I2S Out oft 48 kHz unabhängig von Quelle (BT-Modul-Hinweis) | `EVID-AUDIOI2S-2026-10-13-002` | `FACT` |
| library.properties verlangt PSRAM + external DAC/I2S-BT | `EVID-AUDIOI2S-2026-10-13-003` | `FACT` |
| Eigene DAC-Labmessung | — | `UNKNOWN` |

## Offene Fragen

- Classic-ESP32 „limited“ — welche Codecs praktisch?
- Resampler-Qualität 16→48 vs. native 48?
