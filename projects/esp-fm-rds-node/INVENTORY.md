# Project Inventory: ESP FM/RDS Node

```yaml
project_id: esp-fm-rds-node
updated: 2026-10-13
reviewed_commit: "PiratESP32@58e16970e3c05cb69d4ae8d51aba6101225f4505 ESP32-S3-STEREO-DSP@b9a4a4dd19133f05de890938a7042f423098b158 PixelRadio@22a3c3d9be38d090509765cfc1c4d0c015f5ebb0 fm-streamer@cabc20d2600a7c72ae3d6bafb1702176f96de124 Adafruit-Si4713@fa38460fb0303d7951ff6a20828d707d13225d30 DynamicRDS@638dce6f64ea403462df31a1dc9aae58ffda27b5 esp32_fmdevkit@f8416d27d4bd5e016d3618a8955cb30e093fbb6d ESP32C3_FM_TRANSMITTER@89e15ecc685345bd09ffc6144ae0cd63ae41983e"
profile: lab-tool
pilot_order: [fm-rds, esp-i2s-audio]
```

## Reuse / Match

| Signal | Ziel-Sheet | Entscheidung |
|--------|-------------|--------------|
| RDS PI/PTY/PS/RT, Gruppen-/Buffersteuerung | [`fm-rds`](../../technologies/fm-rds/SHEET.md) | **Reuse** über [Application](applications/fm-rds.md) |
| ESP I2S RX/TX, MCLK, DAC-/ADC-Pfade | [`esp-i2s-audio`](../../technologies/esp-i2s-audio/SHEET.md) | **Reuse** über [Application](applications/esp-i2s-audio.md) |
| S3 Software-Stereo/RDS-MPX am I2S-DAC | `fm-stereo-rds-mpx` (Kandidat) | **kein neuer Contract jetzt**: Implementation belegt, Modulator-/Lab-Transfer offen |
| QN8027/Si4713 integrierte FM/RDS-Sender | `fm-rds-synthesizer-ic` (Kandidat) | **kein Merge/Sheet jetzt**: zwei Chipfamilien, abweichende Audio-/RDS-Interfaces |
| PixelRadio MQTT-Steuerung | [`mqtt-node-telemetry`](../../technologies/mqtt-node-telemetry/SHEET.md) | Kontrast; kein Application-Scope dieser Kampagne |
| C3/PixelRadio Websteuerung | [`esp-embedded-web-sse`](../../technologies/esp-embedded-web-sse/SHEET.md) | Kontrast; kein FM/RDS-Kerncontract |
| Classic APLL/MCLK RF | [`esp32-apll-fm-tx`](../../technologies/esp32-apll-fm-tx/SHEET.md) | **nicht wiederverwenden**: hier externer Modulator/IC |

## Übersicht

| Ziel-Sheet / Kandidat | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|-----------------------|------|---------|------|--------|----------|-------|-------------|
| `fm-rds` | FM Radio Data System | C | `radio-tx`, `metadata` | applied | partial | [SHEET](../../technologies/fm-rds/SHEET.md) | [app](applications/fm-rds.md) |
| `esp-i2s-audio` | ESP I2S Audio | D | `esp32`, `audio` | applied | partial | [SHEET](../../technologies/esp-i2s-audio/SHEET.md) | [app](applications/esp-i2s-audio.md) |
| `fm-stereo-rds-mpx` | Software FM Stereo/RDS MPX | B | `dsp`, `radio-tx`, `baseband` | observed | partial | — | — |
| `fm-rds-synthesizer-ic` | Integrierter FM/RDS-Synthesizer | D | `qn8027`, `si4713`, `i2c` | observed | partial | — | — |
| `mqtt-node-telemetry` | MQTT Node Telemetry | C | `mqtt`, `control` | documented | none | [SHEET](../../technologies/mqtt-node-telemetry/SHEET.md) | — |
| `esp-embedded-web-sse` | ESP Embedded Web UI | G | `http`, `control` | documented | none | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | — |
| `esp32-apll-fm-tx` | Classic ESP32 APLL/MCLK FM | D | `radio-tx`, `clock` | documented | none | [SHEET](../../technologies/esp32-apll-fm-tx/SHEET.md) | — |

Legende Status: `candidate` · `observed` · `documented` · `applied` · `transferred`  
Legende Coverage: `none` · `partial` · `full`

## Nach Kategorie

### B — Audio

- `fm-stereo-rds-mpx`: PiratESP32 erzeugt 19-kHz-Pilot, 38-kHz-Stereo-
  Differenzsignal und 57-kHz-RDS in einem DAC-MPX-Stream. Das ist Desk-
  `observed`, aber ohne externen RF-Modulator kein vollständiger Sender.

### C — Protokolle

- `fm-rds`: wiederverwendet; Software-Assembler sowie QN8027-/Si4713-
  RDS-Kommandopfad sind Implementierungsvarianten desselben RDS-Themas.
- `mqtt-node-telemetry`: PixelRadio-Kontrast, nicht als FM/RDS-Kern inventarisiert.

### D — Embedded

- `esp-i2s-audio`: wiederverwendet für S3/Classic-I2S-Audio.
- `fm-rds-synthesizer-ic`: QN8027 und Si4713 sind externe RF-/Stereo-/RDS-
  Bausteine. Ein gemeinsamer Contract ist plausibel, aber wegen abweichender
  Digitalaudio- und RDS-APIs noch nicht gerechtfertigt.
- `esp32-apll-fm-tx`: reine Abgrenzung; Classic-APLL-RF ist nicht der hier
  gewählte S3-MPX-Pfad.

### G — Steuerung / UI

- `esp-embedded-web-sse`: nur angrenzender Web-Control-Kontrast.

## Chip-/Pfadmatrix (G17)

| Variante | Belegter Desk-Pfad | Nicht belegt |
|----------|--------------------|--------------|
| ESP32-S3 | PCM1808/I2S RX → DSP/MPX → PCM5102A/I2S TX | direkter FM-RF-Ausgang; QN8027-/Si4713-Kompatibilität ohne Integration |
| Classic ESP32 | I2S-Audio zu DAC; QN8027/Si4713-Steuerung; A2DP im fmdevkit | Übertragbarkeit des PiratESP32-S3-Timings; C3-GPIOs |
| ESP32-C3 | I2C-Steuerung QN8027, Web/OLED/NVS; externer Analogaudioeingang | Classic-APLL-FM; S3-I2S-MPX; integrierter Audio-Decode-Pfad |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| S3-MPX → externer Modulator | kein Modulator gewählt, kein Lab | G-MPX-1/G-MPX-2 in [FOLLOW-ON](FOLLOW-ON-IDEAS.md) |
| MPX-Spektrum, Pilot, Stereo, RDS | keine Messartefakte | geschirmtes Lab erst nach Präregistrierung |
| QN8027 vs. Si4713 Contract | API-/Audioeingänge unterscheiden sich | Desk-Matrix G-IC-1 |
| RF-Leistung, Harmonische, Reichweite | Desk-only; README-Angaben sind keine Messung dieser Kampagne | `UNKNOWN`; nur geschirmtes Lab |
| Lizenz PiratESP32 | GPL-Datei vs. README-Zusatz | Lizenzklärung vor Code-Reuse |
| ESP32-S3-STEREO-DSP Lizenz | keine Lizenzdatei gefunden | Upstream-Klärung vor Code-Reuse |
| ManojBhakarPCM | kanonische URL 404/stale | unavailable belassen; vendorte Kopien nicht als lebenden Upstream ausgeben |

## Signale ohne neuen Eintrag

- PixelRadio HTTP/MQTT/Serial-Priorisierung und C3-Web-UI sind projektspezifische
  Steuerung, kein neuer FM/RDS-Contract.
- OLED, TFT, NVS, SPIFFS und Buttons sind Nebenfunktionen.
- README-Performance-, Reichweiten- und „works great“-Aussagen werden nicht als
  `MEASURED` übernommen.
