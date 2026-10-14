# Source Snapshots — Next Audits · 2026-10-13

**Standard:** 0.7.1  
**Status:** Arbeitsregister für vier Foreign-Kampagnen. Ein Eintrag ist erst
Evidence, wenn Commit, Lizenz und relevante Codepfade im jeweiligen
`evidence.md` belegt sind.

## Regeln

- README-Claim und Codebeleg getrennt erfassen.
- Branch-HEAD ohne Commit-SHA ist kein stabiler Snapshot.
- Chip-/Board-Scope ist Teil jedes Peripheral-/Clock-Claims.
- Desk-FACT ist kein Lab-/Field-MEASURED.
- Repos mit unklarer Lizenz bleiben Research-Kontrast, nicht
  Implementierungsgrundlage.

## esp-fm-rds-node-2026-foreign

| Repository | Snapshot | Lizenz | Rolle | Reuse-Match |
|------------|----------|--------|-------|-------------|
| `MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER` | `58e16970e3c05cb69d4ae8d51aba6101225f4505` | GPL-3.0 (GitHub) | S3/Classic Stereo-/RDS-MPX | `fm-rds`, `esp-i2s-audio` |
| `MarcFinns/ESP32-S3-STEREO-DSP` | `b9a4a4dd19133f05de890938a7042f423098b158` | `UNKNOWN` (keine erkannte Lizenz) | S3-I2S-Hardwarekontext | `esp-i2s-audio` |
| `thomastech/PixelRadio` | `22a3c3d9be38d090509765cfc1c4d0c015f5ebb0` | GPL-3.0 (GitHub) | ESP32 + QN8027 + RDS/Remote | `fm-rds`, `mqtt-node-telemetry` |
| `russery/fm-streamer` | `cabc20d2600a7c72ae3d6bafb1702176f96de124` | GPL-3.0 (GitHub) | WiFi-MP3 → DAC → Si4713 | `esp-i2s-audio`, `webradio-browser-host` nur Kontrast |
| `ManojBhakarPCM/Arduino-QN8027-with-Full-RDS-support` | `UNAVAILABLE` (GitHub 404 am 2026-10-13) | `UNKNOWN` | QN8027-Control/RDS; nur historischer Verweis | `fm-rds` |
| `adafruit/Adafruit-Si4713-Library` | `fa38460fb0303d7951ff6a20828d707d13225d30` | BSD laut Repository; GitHub `NOASSERTION` | Si4713-Control/RDS | `fm-rds` |
| `RaA-BLNET/Adafruit-Si4713-DynamicRDS` | `638dce6f64ea403462df31a1dc9aae58ffda27b5` | BSD-3-Clause-Text (`license.txt`; GitHub `NOASSERTION`) | Dynamic-RDS-Kontrast | `fm-rds` |
| `dragon-engineer/esp32_fmdevkit` | `f8416d27d4bd5e016d3618a8955cb30e093fbb6d` | GPL-3.0 (`LICENSE`; Rohdatei am Pin geprüft) | integrierte FM/RDS-Hardware | `esp-i2s-audio`, `fm-rds` |
| `emoestudio/ESP32C3_FM_TRANSMITTER` | `89e15ecc685345bd09ffc6144ae0cd63ae41983e` | MIT (GitHub) | C3 + QN8027 Web-Control | `fm-rds`, `esp-embedded-web-sse` |

## esp-network-pcm-clock-2026-foreign

| Repository | Snapshot | Lizenz | Rolle | Reuse-Match |
|------------|----------|--------|-------|-------------|
| `netham45/esp32-rtp` | `04562157e92cb8ee92f2c4623ec860e7e7e9ef78` | `UNKNOWN` (GitHub meldet AGPL-3.0, aber keine Lizenzdatei am Pin) | RTP PCM / adaptive Buffer | `pdap`, `esp-i2s-audio` |
| `shootao/esp_elastic_pcm_buffer` | `93fbda9f2e127f8bbc3f8d00b462f65aaa7788f4` | Espressif Modified MIT / `LicenseRef-Espressif-Modified-MIT` (nur Espressif-Produkte) | Watermark-/Rate-Control | `pdap` |
| `lutyjj/esp32-streamline` | `c607c45b17da2e88f950aa826a5b8d53f5c5059b` | GPL-3.0 (GitHub) | TCP PCM + Bridge/TLS | `pdap` |
| `NaturalDevCR/TCP-Streamer` | `94d5903d37917bb689e23ca6378d0026aef80cfe` | MIT (GitHub) | Host De-Jitter/Drift-Kontrast | `pdap` |
| `badaix/snapcast` | `4fed179e177b251c67326e7b62a25c8d8fb2d1a9` | GPL-3.0 (GitHub) | Zeit-/Multiroom-Kontrast | `pdap` |
| `pschatzmann/arduino-audio-tools` | `0ef1b1547f240aba146b0c100e0da610267aeffc` | GPL-3.0 (GitHub) | ESP-Audiopipeline | `esp-i2s-audio` |

## bmw-nbt-media-index-2026-foreign

| Repository | Snapshot | Lizenz | Rolle | Reuse-Match |
|------------|----------|--------|-------|-------------|
| `Centurix/idrivetools` | `08e0c43c63a64547b018d5c627f59d5453d9505b` | `UNKNOWN` (keine erkannte Lizenz) | iDrive Backup/Metadaten | `bmw-nbt-evo` |
| `sivu22/BMC` | `c22b27edaf4d5aba50fe66f7e005b272b71e5b35` | MIT laut README; GitHub `NOASSERTION` | BRx-Medienkonverter, NBT Evo ID4 | `bmw-nbt-evo` |
| `superabiliter/BMWFirmwareExtractor` | `5cd2895bb92622ded6feb18b79325188e3ac9860` | `UNKNOWN` (keine erkannte Lizenz) | NBT(EVO)/MGU Firmwareextraktion | `bmw-nbt-evo` |
| `Ricardo2192643/BMW-IVI-NBT-ingest-module` | `127fb15c420334dcc6dedf1010b902d8837c9144` | GPL-3.0 (GitHub) | QNX-/Autopsy-Forensik | `bmw-nbt-evo` |
| `Viaszx/BMW_HU_Info` | `c140b1d62ca59e0043a8c620eb390c96e6272c76` | `UNKNOWN` (keine erkannte Lizenz) | HU-Diagnosekontext | `bmw-nbt-evo` |

## usb-bot-observation-2026-foreign

| Repository | Snapshot | Lizenz | Rolle | Reuse-Match |
|------------|----------|--------|-------|-------------|
| `felipebalbi/usb-tools` | `08d4f3bc10bacde31484c945a9679ef38b844a77` | GPL-3.0 (GitHub) | MSC Host-/Blockgrößentest | `usb-msc` |
| `usb-tools/USBProxy-legacy` | `30c4c14150d8c33f9438b32efeb600ed1bcdb441` | GPL-2.0 (GitHub) | transparenter BOT-Filter | `usb-msc` |
| `torvalds/linux` | `2c0f5ca48674a5b5f9fa4a9c3325aa48053af0bc` (Pfad-Snapshot) | `(GPL-2.0-or-later OR BSD-3-Clause)` im SPDX-Header von `f_mass_storage.c` | `f_mass_storage` Referenz | `usb-msc` |
| `espressif/esp-usb` | `f3408e8cfc0ca99bf8686a4acfd9d3de7522df81` (MSC-Pfad) | Apache-2.0 im Upstream; GitHub `NOASSERTION` | ESP Host MSC/BOT | `usb-msc` |
| `hathach/tinyusb` | `3024dd2e31bc7d6dd27b708ad57f880a8d7f85ac` (MSC-Pfad) | MIT (GitHub) | Device-MSC/Callbacksemantik | `usb-msc` |
| `ookaay/PartitionSchemeDetector` | `63c8669dd0e59b91b7852e3111479282ca7b93cd` (Repository jetzt `treblist/...`) | `UNKNOWN` | kleiner libusb-BOT-Kontrast | `usb-msc` |
| `schumilo/vUSBf` | `bc1fb14551bbc97459cc3e2c36e337ad1060b06b` | GPL-2.0 (GitHub) | historisches USB-Replay/Fuzzing | `usb-msc` |

## usb-bot-observation-2026-instrument-sources (Nachtrag 2026-10-14)

| Repository | Snapshot | Lizenz | Rolle | Reuse-Match |
|------------|----------|--------|-------|-------------|
| `hathach/tinyusb` | `4c195b7b94f813a37b77b184bcae7b2b6ef2835e` (MSC-Pfad) | MIT | Device-Hooks CBW/CSW/Control | `usb-msc` |
| `yeet-src/usbsnoop` | `30f9fad04871252934ca0edd74b0089cb96688da` | `UNKNOWN` | Host eBPF SETUP/BOT Decode | `usb-msc` |
| `adafruit/Adafruit_TinyUSB_Arduino` | `1b7317255f7127b816fad7913ffaeb7fd416ace3` | MIT | App-Callbacks vs. Stack | `usb-msc` |
| `tianocore/edk2` | `e4d139f4880625aed2e1e81d800afebc2b2c9630` (nur `UsbMassBot.h`) | BSD-2-Clause-Patent | Struct-Referenz | `usb-msc` |
| `wireshark/wireshark` | `f28ca85a4b40aaa3d9eea4bf2a878ce9b68d4469` (nur `packet-usbms-bot.c`) | GPL-2.0 | Dissector-Schema | `usb-msc` |

## Vorläufige Reuse-Entscheidung

- Kein paralleles NBT-, USB-MSC-, RDS- oder I2S-Sheet nur wegen eines neuen
  Repositories.
- Ein neuer Contract ist nur für **FM-Stereo/RDS-MPX** beziehungsweise einen
  generischen **integrierten FM/RDS-Synthesizer** plausibel; Entscheidung erst
  nach Codeaudit.
- Netzwerk-PCM wird zuerst gegen `pdap` und `pump-control-link` geprüft.
  Jitter-/Clock-Verfahren gehört voraussichtlich in eine Method Note.

## Erfassungsstand

- Alle am 2026-10-13 erreichbaren Kandidaten sind auf immutable SHA gesetzt;
  der ManojBhakar-Link war nicht erreichbar.
- `UNKNOWN`-Lizenzen bleiben Research-Kontrast und sind keine
  Implementierungsgrundlage.
- Pfadspezifische Linux-/ESP-USB-/TinyUSB-Snapshots sind ausdrücklich keine
  Behauptung, dass der gesamte jeweilige Upstream zu diesem SHA vollständig
  auditiert wurde.
- Relevante Codepfade und Claims stehen in den Evidence-Tabellen der vier
  Kampagnen; README-Claims werden dort von Codebelegen getrennt.
