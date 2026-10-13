# Evidence — esp-fm-rds-node-2026-foreign

Desk 2026-10-13 · **standard_version 0.7.1** · Profile `lab-tool` · keine
Messung. `FACT` bezeichnet hier Code-/Dokumentbefunde am fixierten Snapshot,
nicht Lab- oder Field-Erfolg.

## Immutable Source Snapshots

| Repository | Commit |
|------------|--------|
| [MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/tree/58e16970e3c05cb69d4ae8d51aba6101225f4505) | `58e16970e3c05cb69d4ae8d51aba6101225f4505` |
| [MarcFinns/ESP32-S3-STEREO-DSP](https://github.com/MarcFinns/ESP32-S3-STEREO-DSP/tree/b9a4a4dd19133f05de890938a7042f423098b158) | `b9a4a4dd19133f05de890938a7042f423098b158` |
| [thomastech/PixelRadio](https://github.com/thomastech/PixelRadio/tree/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0) | `22a3c3d9be38d090509765cfc1c4d0c015f5ebb0` |
| [russery/fm-streamer](https://github.com/russery/fm-streamer/tree/cabc20d2600a7c72ae3d6bafb1702176f96de124) | `cabc20d2600a7c72ae3d6bafb1702176f96de124` |
| [adafruit/Adafruit-Si4713-Library](https://github.com/adafruit/Adafruit-Si4713-Library/tree/fa38460fb0303d7951ff6a20828d707d13225d30) | `fa38460fb0303d7951ff6a20828d707d13225d30` |
| [RaA-BLNET/Adafruit-Si4713-DynamicRDS](https://github.com/RaA-BLNET/Adafruit-Si4713-DynamicRDS/tree/638dce6f64ea403462df31a1dc9aae58ffda27b5) | `638dce6f64ea403462df31a1dc9aae58ffda27b5` |
| [dragon-engineer/esp32_fmdevkit](https://github.com/dragon-engineer/esp32_fmdevkit/tree/f8416d27d4bd5e016d3618a8955cb30e093fbb6d) | `f8416d27d4bd5e016d3618a8955cb30e093fbb6d` |
| [emoestudio/ESP32C3_FM_TRANSMITTER](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/tree/89e15ecc685345bd09ffc6144ae0cd63ae41983e) | `89e15ecc685345bd09ffc6144ae0cd63ae41983e` |
| [ManojBhakarPCM/Arduino-QN8027-with-Full-RDS-support](https://github.com/ManojBhakarPCM/Arduino-QN8027-with-Full-RDS-support) | **unavailable — 404/stale; kein Snapshot behauptet** |

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle | Review / Gate |
|----|--------------|--------|--------|---------------|
| `EVID-FMRDS-2026-10-13-001` | PiratESP32 initialisiert getrennte I2S-RX-/TX-Pfade für ADC und DAC; der Ausgang ist Audio/MPX, nicht RF | `FACT` | [ESP32I2SDriver.cpp](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/ESP32I2SDriver.cpp), [main sketch](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/PiratESP32-FM-RDS-STEREO-ENCODER.ino) | ERC: Pfad bei DAC/MPX enden lassen |
| `EVID-FMRDS-2026-10-13-002` | PiratESP32 DSP: Preemphasis, 19-kHz-Notch, 4×-Upsampling, L+R/L-R, 19/38/57-kHz-Mix | `FACT` | [DSP_pipeline.cpp](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/DSP_pipeline.cpp), [MPXMixer.cpp](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/MPXMixer.cpp) | G-MPX-0/1 |
| `EVID-FMRDS-2026-10-13-003` | PiratESP32 implementiert RDS 0A/2A, PI/PTY/PS/RT, CRC/Bitstream und 57-kHz-BPSK | `FACT` | [RDSAssembler.cpp](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/RDSAssembler.cpp), [RDSSynth.cpp](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/RDSSynth.cpp) | Reuse `fm-rds`; G-MPX-2 |
| `EVID-FMRDS-2026-10-13-004` | PiratESP32 trennt Pinblöcke für Classic ESP32 und ESP32-S3; Snapshot-Default 44,1→176,4 kHz, 4× | `FACT` | [Config.h](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/Config.h) | ERC G17: Varianten nie zusammenziehen |
| `EVID-FMRDS-2026-10-13-005` | PiratESP32 enthält GPL-3.0-Lizenzdatei; README nennt zusätzlich educational/non-commercial | `FACT` | [LICENSE](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/LICENSE), [README](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/README.md) | G-LIC-1; kein Code-Reuse vor Klärung |
| `EVID-FMRDS-2026-10-13-006` | S3-DSP-Board dokumentiert ESP32-S3 N16R8, PCM1808, PCM5102A und getrennte I2S-Pins mit gemeinsamem MCLK | `FACT` | [README](https://github.com/MarcFinns/ESP32-S3-STEREO-DSP/blob/b9a4a4dd19133f05de890938a7042f423098b158/README.md) | Reuse `esp-i2s-audio`; G17 S3 |
| `EVID-FMRDS-2026-10-13-007` | S3-Testsketch konfiguriert 48-kHz-RX, 192-kHz-TX, 4× Hermite-Interpolation und gemeinsamen 24,576-MHz-MCLK; keine Lizenzdatei im Tree | `FACT` | [Testsketch](https://github.com/MarcFinns/ESP32-S3-STEREO-DSP/blob/b9a4a4dd19133f05de890938a7042f423098b158/test%20sketch/AUDIO_DSP_TEST_48_192_PASSTHROUGH.ino), [Tree](https://github.com/MarcFinns/ESP32-S3-STEREO-DSP/tree/b9a4a4dd19133f05de890938a7042f423098b158) | G-I2S-1 und G-LIC-1 |
| `EVID-FMRDS-2026-10-13-008` | PixelRadio ist Classic-ESP32-Steuerung für externen QN8027; QN8027-Präsenz und Register werden über I2C geprüft | `FACT` | [radio.cpp](https://github.com/thomastech/PixelRadio/blob/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0/src/radio.cpp), [platformio.ini](https://github.com/thomastech/PixelRadio/blob/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0/platformio.ini) | ERC: Classic + externer Chip |
| `EVID-FMRDS-2026-10-13-009` | PixelRadio sendet PI/PTY, Program Service und RadioText über QN8027 | `FACT` | [rds.cpp](https://github.com/thomastech/PixelRadio/blob/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0/src/rds.cpp), [QN8027Radio.cpp](https://github.com/thomastech/PixelRadio/blob/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0/src/QN8027Radio.cpp) | Reuse `fm-rds`; G-IC-1 |
| `EVID-FMRDS-2026-10-13-010` | PixelRadio konfiguriert QN8027-Frequenz, Deviation, Pilot, Preemphasis, Analog-/Digitalgain, Stereo und RF-Power | `FACT` | [radio.cpp](https://github.com/thomastech/PixelRadio/blob/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0/src/radio.cpp) | QN8027 nicht mit Si4713 gleichsetzen |
| `EVID-FMRDS-2026-10-13-011` | PixelRadio nimmt RDS aus Serial, MQTT oder HTTP an und priorisiert Controller im Code | `FACT` | [rds.cpp](https://github.com/thomastech/PixelRadio/blob/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0/src/rds.cpp), [mqtt.cpp](https://github.com/thomastech/PixelRadio/blob/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0/src/mqtt.cpp) | Ebene B, kein allgemeiner RDS-Claim |
| `EVID-FMRDS-2026-10-13-012` | fm-streamer decodiert HTTP-MP3 und führt Samples an einen I2S-Output | `FACT` | [internet_stream.cpp](https://github.com/russery/fm-streamer/blob/cabc20d2600a7c72ae3d6bafb1702176f96de124/fm-streamer/internet_stream.cpp) | Reuse `esp-i2s-audio` |
| `EVID-FMRDS-2026-10-13-013` | fm-streamer beschreibt im README den Pfad ESP32-I2S → UDA1334-DAC → Analog → Si4713; Si4713-Steuerung über I2C | `FACT` | [README](https://github.com/russery/fm-streamer/blob/cabc20d2600a7c72ae3d6bafb1702176f96de124/README.md) | Dokumentationspfad, nicht mit aktivem Codepfad gleichsetzen |
| `EVID-FMRDS-2026-10-13-014` | Der gepinnte fm-streamer-Code startet den Si47xx-Digitalinput und setzt ihn auf 44,1 kHz; die tatsächlich eingesetzte Hardwaretopologie ist nicht belegt | `FACT` | [fm_radio.cpp](https://github.com/russery/fm-streamer/blob/cabc20d2600a7c72ae3d6bafb1702176f96de124/fm-streamer/fm_radio.cpp), [si47xx.cpp](https://github.com/russery/fm-streamer/blob/cabc20d2600a7c72ae3d6bafb1702176f96de124/fm-streamer/si47xx.cpp) | README-/Code-Differenz vor Hardwaretransfer klären |
| `EVID-FMRDS-2026-10-13-015` | fm-streamer-Si47xx-Treiber implementiert Tune/Power, Analog-/Digitalaudio und PS/RT-RDS-Properties/Buffer | `FACT` | [si47xx.cpp](https://github.com/russery/fm-streamer/blob/cabc20d2600a7c72ae3d6bafb1702176f96de124/fm-streamer/si47xx.cpp) | G-IC-1; Si4713-Familie |
| `EVID-FMRDS-2026-10-13-016` | Adafruit-Si4713 ist BSD-I2C-Treiber mit Reset, Part-ID, Tune, Power und Status/Noise-Messkommandos | `FACT` | [Adafruit_Si4713.cpp](https://github.com/adafruit/Adafruit-Si4713-Library/blob/fa38460fb0303d7951ff6a20828d707d13225d30/Adafruit_Si4713.cpp), [license.txt](https://github.com/adafruit/Adafruit-Si4713-Library/blob/fa38460fb0303d7951ff6a20828d707d13225d30/license.txt) | Referenz für Si4713; kein Messresultat |
| `EVID-FMRDS-2026-10-13-017` | Adafruit-Si4713 setzt RDS-Properties und schreibt PS-/RadioText-Slots über Chipkommandos | `FACT` | [Adafruit_Si4713.cpp](https://github.com/adafruit/Adafruit-Si4713-Library/blob/fa38460fb0303d7951ff6a20828d707d13225d30/Adafruit_Si4713.cpp) | Reuse `fm-rds`; G-IC-1 |
| `EVID-FMRDS-2026-10-13-018` | DynamicRDS ergänzt serial-gesteuerte PS-/RT-Updates, 64-Zeichen-RT und gepagete PS-Puffer | `FACT` | [adaradio.ino](https://github.com/RaA-BLNET/Adafruit-Si4713-DynamicRDS/blob/638dce6f64ea403462df31a1dc9aae58ffda27b5/examples/adaradio/adaradio.ino), [README](https://github.com/RaA-BLNET/Adafruit-Si4713-DynamicRDS/blob/638dce6f64ea403462df31a1dc9aae58ffda27b5/README.md) | Dynamic-RDS-Testvektor |
| `EVID-FMRDS-2026-10-13-019` | esp32_fmdevkit ist Classic ESP32 mit I2S-DAC, QN8027, OLED und RF-SMA; Snapshotlizenz GPL-3.0 | `FACT` | [README](https://github.com/dragon-engineer/esp32_fmdevkit/blob/f8416d27d4bd5e016d3618a8955cb30e093fbb6d/README.md), [LICENSE](https://github.com/dragon-engineer/esp32_fmdevkit/blob/f8416d27d4bd5e016d3618a8955cb30e093fbb6d/LICENSE) | G17 Classic |
| `EVID-FMRDS-2026-10-13-020` | fmdevkit führt A2DP-Audio über Classic-I2S-TX/DAC zum QN8027 und erzeugt MCLK per LEDC/PWM | `FACT` | [FMDevKit_BluetoothAudio.ino](https://github.com/dragon-engineer/esp32_fmdevkit/blob/f8416d27d4bd5e016d3618a8955cb30e093fbb6d/example_firmware/FMDevKit_BluetoothAudio/FMDevKit_BluetoothAudio.ino) | Review: PWM-MCLK-Risiko bleibt Ebene B |
| `EVID-FMRDS-2026-10-13-021` | fmdevkit enthält einen Pfad, der A2DP-Metadaten in einen gepageten QN8027-RDS-Puffer übernimmt; `RDS_ENABLED` ist im Beispiel standardmäßig aus | `FACT` | [FMDevKit_BluetoothAudio.ino](https://github.com/dragon-engineer/esp32_fmdevkit/blob/f8416d27d4bd5e016d3618a8955cb30e093fbb6d/example_firmware/FMDevKit_BluetoothAudio/FMDevKit_BluetoothAudio.ino), `symbols.h` | Reuse `fm-rds` nur als Codepfad, kein Laufzeit-PASS |
| `EVID-FMRDS-2026-10-13-022` | ManojBhakarPCM-URL war 404/stale; PixelRadio und C3 enthalten vendorte QN8027-Codekopien, die nur über deren Host-SHAs belastbar sind | `FACT` | [unavailable URL](https://github.com/ManojBhakarPCM/Arduino-QN8027-with-Full-RDS-support), [PixelRadio vendored tree](https://github.com/thomastech/PixelRadio/tree/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0/lib/Arduino-QN8027-with-Full-RDS-support), [C3 vendored source](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/blob/89e15ecc685345bd09ffc6144ae0cd63ae41983e/lib/QN8027/QN8027Radio.cpp) | Kanonischen Upstream nicht als verfügbar ausgeben |
| `EVID-FMRDS-2026-10-13-023` | C3-Projekt ist auf `esp32-c3-devkitm-1` fixiert; QN8027/OLED hängen an GPIO8/9-I2C, Audio kommt extern analog | `FACT` | [platformio.ini](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/blob/89e15ecc685345bd09ffc6144ae0cd63ae41983e/platformio.ini), [README_EN.md](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/blob/89e15ecc685345bd09ffc6144ae0cd63ae41983e/README_EN.md) | G17 C3; kein I2S/APLL-Transfer |
| `EVID-FMRDS-2026-10-13-024` | C3-Code steuert QN8027-Frequenz/Power/Deviation/Mono/Preemphasis und aktualisiert PS/RT zyklisch | `FACT` | [src/main.cpp](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/blob/89e15ecc685345bd09ffc6144ae0cd63ae41983e/src/main.cpp) | Reuse `fm-rds`; QN8027 |
| `EVID-FMRDS-2026-10-13-025` | C3-Code bietet STA→AP-Fallback, HTTP-JSON-Settings, Serial-Steuerung und NVS; Snapshotlizenz MIT | `FACT` | [src/main.cpp](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/blob/89e15ecc685345bd09ffc6144ae0cd63ae41983e/src/main.cpp), [LICENSE](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/blob/89e15ecc685345bd09ffc6144ae0cd63ae41983e/LICENSE) | Ebene B; kein neuer FM-Contract |
| `EVID-FMRDS-2026-10-13-026` | S3 RX→DSP→TX ist im präregistrierten Dauerfenster glitch-/underrun-frei | `UNKNOWN` | kein Labartefakt | G-I2S-1 |
| `EVID-FMRDS-2026-10-13-027` | S3-DAC-MPX ist elektrisch/spektral mit einem ausgewählten externen FM-Modulator kompatibel | `UNKNOWN` | kein Modulator gewählt; kein Labartefakt | G-MPX-0/1/2; K1–K3 |
| `EVID-FMRDS-2026-10-13-028` | QN8027-Pfade liefern im geschirmten Aufbau reproduzierbares Stereo/RDS/PS/RT | `UNKNOWN` | kein Labartefakt | G-IC-2 |
| `EVID-FMRDS-2026-10-13-029` | Si4713-Pfade liefern im geschirmten Aufbau reproduzierbares Audio/RDS ohne Clipping/Noise-Befund | `UNKNOWN` | kein Labartefakt | G-IC-2 |
| `EVID-FMRDS-2026-10-13-030` | Field-/Antennenbetrieb ist technisch validiert und rechtlich freigegeben | `UNKNOWN` | Desk-only; kein Field-Artefakt | G-LEGAL-1; K6/K7 |

## Offene Claims

Alle offenen technischen Ergebnisclaims besitzen oben eine ID:

- I2S-Dauerverhalten: `EVID-FMRDS-2026-10-13-026`
- S3-MPX → externer Modulator: `EVID-FMRDS-2026-10-13-027`
- QN8027-Lab: `EVID-FMRDS-2026-10-13-028`
- Si4713-Lab: `EVID-FMRDS-2026-10-13-029`
- Field/Recht: `EVID-FMRDS-2026-10-13-030`

README-Angaben zu Reichweite, Ausgangsleistung, „broadcast quality“,
CPU-Auslastung oder „tested/works great“ wurden nicht als Kampagnenmessung
übernommen.

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | Acht vorgegebene SHAs lokal ausgecheckt und Codepfade desk-geprüft |
| 2026-10-13 | ManojBhakarPCM als 404/stale erfasst; vendorte Linien getrennt |
| 2026-10-13 | Reuse `fm-rds` und `esp-i2s-audio`; keine neuen Sheets |
| 2026-10-13 | G17-Matrix, C10–C13 und Kill-/Lab-Gates präregistriert |
