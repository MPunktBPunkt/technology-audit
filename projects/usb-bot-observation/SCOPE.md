# Project Scope: USB BOT Observation (Fremd)

```yaml
project_id: usb-bot-observation
title: USB BOT Observation — CBW/CDB/Data/CSW (Fremd)
updated: 2026-10-14
profile_hint: lab-tool
status: active
repos:
  - https://github.com/felipebalbi/usb-tools
  - https://github.com/usb-tools/USBProxy-legacy
  - https://github.com/torvalds/linux
  - https://github.com/espressif/esp-usb
  - https://github.com/hathach/tinyusb
  - https://github.com/treblist/PartitionSchemeDetector
  - https://github.com/schumilo/vUSBf
  - https://github.com/yeet-src/usbsnoop
  - https://github.com/adafruit/Adafruit_TinyUSB_Arduino
  - https://github.com/tianocore/edk2
  - https://github.com/wireshark/wireshark
```

## Zweck

Desk-Audit vorhandener Host-, Device-, Proxy- und Replay-Pfade für die Frage,
welcher Beobachtungspunkt BOT-Commandgrenzen zuverlässig sichtbar machen kann.
Folge-Kampagne 2026-10-14 vertieft **Instrumentierungshooks** (TinyUSB) und
**Host-Lab-Decode** (usbsnoop). Der bestehende Slug
[`usb-msc`](../../technologies/usb-msc/SHEET.md) wird wiederverwendet; es
entsteht kein paralleles BOT-/SCSI-Sheet.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| BOT-Transport | CBW → optionale Datenphase → CSW | ja, Desk |
| SCSI READ(10), REQUEST SENSE, START STOP | relevante CDB-Semantik | ja, soweit im Quellcode sichtbar |
| Device-Instrumentierung | TinyUSB / Linux `f_mass_storage` | ja, Referenz |
| Host-Kontrast | `usb-tools`, `esp-usb`, PartitionSchemeDetector | ja, Referenz |
| Inline-Proxy | USBProxy-legacy | ja, Eignung und Grenzen |
| Host-eBPF-Sniffer | usbsnoop (Lab-Validate) | ja, Desk; Lizenz `UNKNOWN` |
| Arduino-/ESP32-Wrapper | Adafruit TinyUSB MSC | ja, Callback- vs. Stack-Sicht |
| BOT-Struct-Referenz | edk2 `UsbMassBot.h`, Wireshark BOT-Dissector | ja, Schema-Abgleich |
| VM-Replay/Fuzzing | vUSBf | ja, Kontrast |
| BMW NBT / Fahrzeug | konkreter Host | **nein** — keine Capture-Daten |
| Timing-/Transparenzmessung | Einfluss des Beobachters | **nein** — `UNKNOWN` |
| Physische Paketebene | DATA0/1, ACK/NAK | **nein** — Hardware-Sniffer out-of-scope |

## Nicht-Ziele

- kein Lab-, Hardware-, USB-Analyzer- oder Fahrzeuglauf
- keine Aussage über reale NBT-CDBs, READ(10)-Transferlängen, Sense-Sequenzen,
  BOT-Resets oder Zeitgrenzen
- keine Gleichsetzung von TinyUSB-Callback-Chunks mit einer CDB-Grenze
- keine Produktivfreigabe von USBProxy-legacy, vUSBf oder unlizenzierter
  usbsnoop-Übernahme
- kein paralleles Technology Sheet (`usb-bot-protocol` / `tinyusb-msc-device`)

## Quellen für das Audit

| Quelle | Snapshot / relevanter Pfad | Scope-Hinweis |
|--------|-----------------------------|---------------|
| [`felipebalbi/usb-tools`](https://github.com/felipebalbi/usb-tools/tree/08d4f3bc10bacde31484c945a9679ef38b844a77) | `08d4f3bc10bacde31484c945a9679ef38b844a77`; `src/msc.c`, `src/msc.sh` | gesamter kleiner Upstream, MSC-Pfade vertieft |
| [`usb-tools/USBProxy-legacy`](https://github.com/usb-tools/USBProxy-legacy/tree/30c4c14150d8c33f9438b32efeb600ed1bcdb441) | `30c4c14150d8c33f9438b32efeb600ed1bcdb441`; `PacketFilter_MassStorage.cpp`, README | Proxy-/Filterpfad |
| [`torvalds/linux`](https://github.com/torvalds/linux/blob/2c0f5ca48674a5b5f9fa4a9c3325aa48053af0bc/drivers/usb/gadget/function/f_mass_storage.c) | `2c0f5ca48674a5b5f9fa4a9c3325aa48053af0bc`; nur `drivers/usb/gadget/function/f_mass_storage.c` | **pfadspezifisch**, kein Linux-Gesamtaudit |
| [`espressif/esp-usb`](https://github.com/espressif/esp-usb/tree/f3408e8cfc0ca99bf8686a4acfd9d3de7522df81/host/class/msc/usb_host_msc) | `f3408e8cfc0ca99bf8686a4acfd9d3de7522df81`; nur `host/class/msc/usb_host_msc/` | **pfadspezifisch**, Host-Kontrast |
| [`hathach/tinyusb`](https://github.com/hathach/tinyusb/tree/3024dd2e31bc7d6dd27b708ad57f880a8d7f85ac/src/class/msc) | `3024dd2e31bc7d6dd27b708ad57f880a8d7f85ac` (Vor); Instrumentierung `4c195b7b94f813a37b77b184bcae7b2b6ef2835e`; nur `src/class/msc/` | **MSC-pfadspezifisch**, Device-Kontrast |
| [`treblist/PartitionSchemeDetector`](https://github.com/treblist/PartitionSchemeDetector/tree/63c8669dd0e59b91b7852e3111479282ca7b93cd) | `63c8669dd0e59b91b7852e3111479282ca7b93cd`; `app.cpp`, README | von `ookaay/...` weitergeleitet |
| [`schumilo/vUSBf`](https://github.com/schumilo/vUSBf/tree/bc1fb14551bbc97459cc3e2c36e337ad1060b06b) | `bc1fb14551bbc97459cc3e2c36e337ad1060b06b`; README, Replay-/Fuzzing-Gerüst | historischer Kontrast |
| [`yeet-src/usbsnoop`](https://github.com/yeet-src/usbsnoop/tree/30f9fad04871252934ca0edd74b0089cb96688da) | `30f9fad04871252934ca0edd74b0089cb96688da` | Host-eBPF Lab-Validate; Lizenz `UNKNOWN` |
| [`adafruit/Adafruit_TinyUSB_Arduino`](https://github.com/adafruit/Adafruit_TinyUSB_Arduino/tree/1b7317255f7127b816fad7913ffaeb7fd416ace3) | `1b7317255f7127b816fad7913ffaeb7fd416ace3`; MSC-Wrapper + `examples/MassStorage/` | App- vs. Stack-Sicht |
| [`tianocore/edk2`](https://github.com/tianocore/edk2/blob/e4d139f4880625aed2e1e81d800afebc2b2c9630/MdeModulePkg/Bus/Usb/UsbMassStorageDxe/UsbMassBot.h) | `e4d139f4880625aed2e1e81d800afebc2b2c9630`; nur `UsbMassBot.h` | **pfadspezifisch**, Struct-Referenz |
| [`wireshark/wireshark`](https://github.com/wireshark/wireshark/blob/f28ca85a4b40aaa3d9eea4bf2a878ce9b68d4469/epan/dissectors/packet-usbms-bot.c) | `f28ca85a4b40aaa3d9eea4bf2a878ce9b68d4469`; nur `packet-usbms-bot.c` | **pfadspezifisch**, Decode-Referenz |

## Prioritäten für die Analyse

1. CBW/CDB/Data/CSW-Grenzen und Tag-/Residue-Korrelation
2. READ(10)-CDB-Länge vs. Datenlänge vs. Callback-Chunk
3. Sense- und BOT-Reset-/Recovery-Pfade
4. Device-, Inline- und Host/Gadget-Beobachtung sowie Grenzen
   „transparenten“ Captures
5. Instrumentierungshooks (TinyUSB) + Host-eBPF-Validate (usbsnoop)
6. NBT-bezogene Claims ausdrücklich `UNKNOWN` halten

## Offene Scope-Fragen

- Welcher physische Beobachtungspunkt ist am NBT elektrisch und zeitlich
  ausreichend transparent?
- Reicht Device-Telemetrie für die konkrete Entscheidung, oder ist ein
  unabhängiger Bus-Capture nötig?
