# Project Application: esp-i2s-audio in esp-fm-rds-node

```yaml
project_id: esp-fm-rds-node
tech_slug: esp-i2s-audio
status: active
sheet: ../../../technologies/esp-i2s-audio/SHEET.md
audit: ../../../audits/esp-fm-rds-node-2026-foreign/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt

Das vorhandene [`esp-i2s-audio`](../../../technologies/esp-i2s-audio/SHEET.md)-
Sheet deckt die digitalen Audioverbindungen ab. Der Zielpfad ist:

```text
ESP32-S3
  PCM1808 → I2S RX @ 44,1/48 kHz
  → DSP / 4× Upsampling / Stereo-RDS-MPX
  → I2S TX @ 176,4/192 kHz → PCM5102A
  → analoges MPX-Basisband → externer FM-Modulator
```

I2S transportiert hier PCM beziehungsweise MPX zum DAC. Es erzeugt nicht selbst
den FM-RF-Träger.

## Ebene A — wiederverwendeter Contract

- I2S-RX/TX, Master Clock, Slotbreite und DMA bleiben allgemeines
  `esp-i2s-audio`-Wissen.
- Chip-/Peripheral-Claims werden nach G17 auf ESP32-S3, Classic ESP32 oder
  ESP32-C3 begrenzt.
- Diese Kampagne ändert das vorhandene Sheet nicht.

## Ebene B — Projektimplementierungen

### B1: ESP32-S3 Stereo-DSP/MPX

| Repo / Pfad | Rolle | Evidence |
|-------------|-------|----------|
| [PiratESP32 `ESP32I2SDriver.cpp`](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/ESP32I2SDriver.cpp) | getrennte RX-/TX-Channels, ADC/DAC und gemeinsamer MCLK | `EVID-FMRDS-2026-10-13-001` |
| [PiratESP32 `DSP_pipeline.cpp`](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/DSP_pipeline.cpp) | Preemphasis, Notch, 4×-Upsampling und MPX-Ausgabe | `EVID-FMRDS-2026-10-13-002` |
| [PiratESP32 `Config.h`](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/Config.h) | getrennte S3-/Classic-Pinblöcke, Raten und DMA-Längen | `EVID-FMRDS-2026-10-13-004` |
| [S3-DSP Testsketch](https://github.com/MarcFinns/ESP32-S3-STEREO-DSP/blob/b9a4a4dd19133f05de890938a7042f423098b158/test%20sketch/AUDIO_DSP_TEST_48_192_PASSTHROUGH.ino) | S3: PCM1808 RX 48 kHz → 4× → PCM5102A TX 192 kHz | `EVID-FMRDS-2026-10-13-006`–`007` |

S3-Pins im geprüften Pfad: MCLK GPIO8; ADC BCK/LRCK/DIN GPIO4/6/5;
DAC BCK/LRCK/DOUT GPIO9/11/10. Das sind projektspezifische Ebene-B-Werte,
keine universellen S3-Pins.

### B2: Classic ESP32 zu externem Sender-IC

| Repo | Audiofluss | Evidence |
|------|------------|----------|
| [fm-streamer](https://github.com/russery/fm-streamer/tree/cabc20d2600a7c72ae3d6bafb1702176f96de124) | MP3/HTTP → Decoder → I2S; README beschreibt DAC→Analog, gepinnter Code aktiviert Si47xx-Digitalinput | `EVID-FMRDS-2026-10-13-012`–`014` |
| [esp32_fmdevkit](https://github.com/dragon-engineer/esp32_fmdevkit/tree/f8416d27d4bd5e016d3618a8955cb30e093fbb6d) | Bluetooth A2DP → Classic-ESP32 I2S TX → 24-bit-DAC → QN8027-Analoginput | `EVID-FMRDS-2026-10-13-019`–`021` |

Die README-/Code-Differenz bei `fm-streamer` muss vor einem Hardwaretransfer
geklärt werden. Der Digitalinput bei 44,1 kHz wird nicht still auf alle
Si4713-Hardwarevarianten übertragen.

### B3: ESP32-C3

`ESP32C3_FM_TRANSMITTER` belegt im Snapshot **keinen I2S-Audiopfad**. Der C3
steuert QN8027 und erwartet Analogaudio am Sender-IC
(`EVID-FMRDS-2026-10-13-023`). Deshalb ist C3 hier Abgrenzung, nicht
I2S-Reuse-Beleg.

## Konfiguration und Parameter (Desk)

| Pfad | Sample-/Clock-Konfiguration | Status |
|------|-----------------------------|--------|
| S3-DSP Testsketch | RX 48 kHz, TX 192 kHz, 32-bit-Slots, gemeinsamer 24,576-MHz-MCLK | `FACT` (Code) |
| PiratESP32 Snapshot | ADC 44,1 kHz, DAC 176,4 kHz, 4×, 24-bit in 32-bit-Wörtern | `FACT` (Code) |
| fm-streamer | Decoder-Ausgabe über I2S; Rev0 `EnableI2SInput(44100)` | `FACT` (Code) |
| fmdevkit | Classic I2S TX, 16 bit, 44,1-kHz-Default, dynamisch durch A2DP aktualisiert | `FACT` (Code) |
| Störungsfreier Dauerbetrieb | keine Messung | `UNKNOWN` |

## Ebene C — Lab-/Field-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| S3 RX→DSP→TX läuft ohne Underrun/Glitch im präregistrierten Dauerfenster | `EVID-FMRDS-2026-10-13-026` | `UNKNOWN` |
| S3-DAC liefert ein für den ausgewählten FM-Modulator kompatibles MPX-Signal | `EVID-FMRDS-2026-10-13-027` | `UNKNOWN` |
| Classic-fm-streamer-Audio erreicht den Si4713 ohne Clipping/Noise im kontrollierten Lab | `EVID-FMRDS-2026-10-13-029` | `UNKNOWN` |
| Field-Verhalten irgendeines I2S-Pfads | `EVID-FMRDS-2026-10-13-030` | `UNKNOWN` |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| — | Keine Messung durchgeführt; Lab und Field `UNKNOWN` |

## Abweichungen vom „Lehrbuch“

- PiratESP32 verwendet zwei I2S-Controller/Raten und gibt denselben MPX-Kanal
  auf beiden DAC-Kanälen aus.
- Das S3-DSP-Testsketch nennt seine Hermite-Interpolation „polyphase FIR“;
  der Code implementiert kubische Hermite-Interpolation. Die Benennung wird
  nicht als Algorithmus-FACT verallgemeinert.
- fmdevkit erzeugt den benötigten I2S-MCLK per LEDC/PWM und dokumentiert
  Phasenrauschen als Risiko; das ist Classic-spezifische Ebene B.
- C3 hat in diesem Snapshot keinen digitalen Audiopfad zum QN8027.

## Offene Fragen

- Welcher externe Modulator und welche analoge Kopplung passen zum S3-DAC-MPX?
- Sind 176,4 kHz und 192 kHz mit identischem RDS-/Pilotverhalten nutzbar?
- Welche I2S-/DMA-Fehlerkriterien gelten vor einem Lab-Go?
- Ist der Si4713-Digitalinput nur eine Hardware-Rev0-Variante?

## Verwandte Applications / Gates

- [`fm-rds`](fm-rds.md)
- Präregistrierte Gates in [FOLLOW-ON-IDEAS](../FOLLOW-ON-IDEAS.md)
- Frühere Reuse-Beispiele:
  [`esp32-i2s-ble`](../../esp32-i2s-ble/applications/esp-i2s-audio.md) und
  [`esp32-audioi2s`](../../esp32-audioi2s/applications/esp-i2s-audio.md)
