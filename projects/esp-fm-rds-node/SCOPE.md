# Project Scope: ESP FM/RDS Node (Fremdrepos)

```yaml
project_id: esp-fm-rds-node
title: ESP FM/RDS Node (Fremdrepos)
updated: 2026-10-13
profile_hint: lab-tool
reviewed_commit: "PiratESP32@58e16970e3c05cb69d4ae8d51aba6101225f4505 ESP32-S3-STEREO-DSP@b9a4a4dd19133f05de890938a7042f423098b158 PixelRadio@22a3c3d9be38d090509765cfc1c4d0c015f5ebb0 fm-streamer@cabc20d2600a7c72ae3d6bafb1702176f96de124 Adafruit-Si4713@fa38460fb0303d7951ff6a20828d707d13225d30 DynamicRDS@638dce6f64ea403462df31a1dc9aae58ffda27b5 esp32_fmdevkit@f8416d27d4bd5e016d3618a8955cb30e093fbb6d ESP32C3_FM_TRANSMITTER@89e15ecc685345bd09ffc6144ae0cd63ae41983e"
reviewed_commit_note: Acht erreichbare Upstreams auf immutable SHA; ManojBhakar-URL 404/stale
repos:
  - https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER
  - https://github.com/MarcFinns/ESP32-S3-STEREO-DSP
  - https://github.com/thomastech/PixelRadio
  - https://github.com/russery/fm-streamer
  - https://github.com/adafruit/Adafruit-Si4713-Library
  - https://github.com/RaA-BLNET/Adafruit-Si4713-DynamicRDS
  - https://github.com/dragon-engineer/esp32_fmdevkit
  - https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER
status: active
```

## Zweck

Desk-only klären, welche Teile eines ESP-FM/RDS-Nodes bereits durch vorhandene
KB-Contracts abgedeckt sind und wo Chip-, Audio- und RF-Grenzen liegen.
Insbesondere wird **S3 → I2S-MPX → externer FM-Modulator** von Classic-ESP32-
und C3-Steuerpfaden mit QN8027/Si4713 getrennt.

## Systeme und Grenzen

| System | Chip-/Board-Scope | Rolle | Im Scope? |
|--------|-------------------|-------|-----------|
| PiratESP32 | ESP32-S3 und Classic ESP32 im Code | Stereo-/RDS-MPX als I2S-DAC-Signal | ja, Desk |
| ESP32-S3-STEREO-DSP | ESP32-S3 N16R8 | PCM1808 RX, 4×-Upsampling, PCM5102A TX | ja, Desk |
| PixelRadio | Classic ESP32 / Wemos D1 Mini32 | QN8027, Analogaudio, RDS, Web/MQTT/HTTP/Serial | ja, Desk |
| fm-streamer | ESP32/ESP8266 | README: I2S-DAC → Analog → Si4713; gepinnter Code: Si47xx-Digitalinput | ja, Desk; reale Hardwaretopologie `UNKNOWN` |
| Adafruit-Si4713-Library | Arduino-MCU nicht auf ESP-Variante festgelegt | Si4713-I2C, Tune/Power/RDS | ja, Desk-Referenz |
| DynamicRDS | Arduino + Si4713 | dynamisches PS/RT über Serial | ja, Desk-Kontrast |
| esp32_fmdevkit | Classic ESP32 | A2DP → I2S-DAC + QN8027/RDS | ja, Desk |
| ESP32C3_FM_TRANSMITTER | ESP32-C3 | QN8027-I2C, Analogaudio, OLED/Web/Serial | ja, Desk |
| ManojBhakarPCM Upstream | URL 404/stale | QN8027-Library-Ursprung | unavailable; nur vendorte Kopien als Sekundärbeleg |
| Antennen-/Feldsendung | alle | regulatorisches und RF-Verhalten | **nein** |
| Labmessung | alle | MPX-/RF-/RDS-Validierung | **nicht durchgeführt** |

## Nicht-Ziele

- keine Anleitung zu unlizenzierter Aussendung und kein Antennenbetrieb
- keine erfundenen Pegel-, Spektrum-, Stereo-, RDS- oder Reichweitenmessungen
- keine Gleichsetzung von ESP32 Classic, ESP32-S3 und ESP32-C3
- kein Transfer von Classic-APLL/MCLK-FM auf S3 oder C3
- keine Aussage, dass ein I2S-MPX-DAC direkt RF moduliert
- keine Änderungen an Shared Indexes, Technology Sheets, Methods oder
  `next-audits`

## Quellen für das Audit

Alle Links sind auf den geprüften Commit fixiert.

| Quelle | Immutable URL | Bemerkung |
|--------|---------------|-----------|
| PiratESP32 | [58e16970](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/tree/58e16970e3c05cb69d4ae8d51aba6101225f4505) | GPL-3.0-Datei; README nennt zusätzlich „educational/non-commercial“ — Lizenzklarheit offen |
| ESP32-S3-STEREO-DSP | [b9a4a4dd](https://github.com/MarcFinns/ESP32-S3-STEREO-DSP/tree/b9a4a4dd19133f05de890938a7042f423098b158) | keine Lizenzdatei im Snapshot gefunden |
| PixelRadio | [22a3c3d9](https://github.com/thomastech/PixelRadio/tree/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0) | GPL-3.0; QN8027 + RDS/Remote |
| fm-streamer | [cabc20d2](https://github.com/russery/fm-streamer/tree/cabc20d2600a7c72ae3d6bafb1702176f96de124) | GPL-3.0; Si4713/Si47xx |
| Adafruit Si4713 | [fa38460f](https://github.com/adafruit/Adafruit-Si4713-Library/tree/fa38460fb0303d7951ff6a20828d707d13225d30) | BSD-3-Clause |
| DynamicRDS | [638dce6f](https://github.com/RaA-BLNET/Adafruit-Si4713-DynamicRDS/tree/638dce6f64ea403462df31a1dc9aae58ffda27b5) | BSD-Text im Snapshot; Fork-/Änderungslizenz nicht weiter verifiziert |
| esp32_fmdevkit | [f8416d27](https://github.com/dragon-engineer/esp32_fmdevkit/tree/f8416d27d4bd5e016d3618a8955cb30e093fbb6d) | GPL-3.0 |
| ESP32-C3 QN8027 | [89e15ecc](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/tree/89e15ecc685345bd09ffc6144ae0cd63ae41983e) | MIT |
| ManojBhakarPCM | [stale URL](https://github.com/ManojBhakarPCM/Arduino-QN8027-with-Full-RDS-support) | 404/unavailable am Auditzeitpunkt |
| Lab / Feld | — | `UNKNOWN`; keine Messartefakte erzeugt |

## Prioritäten für die Analyse

1. A/B/C-Trennung und Reuse von `fm-rds` sowie `esp-i2s-audio`
2. Chip-Scope nach G17: Classic ESP32 ≠ ESP32-S3 ≠ ESP32-C3
3. MPX-Basisband strikt vom RF-Modulator trennen
4. QN8027 und Si4713 als unterschiedliche externe Senderfamilien benennen
5. Desk-/Lab-Gates und Kill-Kriterien vor jeder späteren Messung präregistrieren

## Offene Scope-Fragen

- Ob der PiratESP32-DAC-MPX-Ausgang einen ausgewählten externen Modulator
  normgerecht treibt: `UNKNOWN`.
- Ob QN8027 und Si4713 einen gemeinsamen neuen KB-Contract rechtfertigen:
  `HYPOTHESIS`; erst Interface-/Parametervergleich und Lab-Gate.
- Lab- und Field-Eignung aller Pfade: `UNKNOWN`.
