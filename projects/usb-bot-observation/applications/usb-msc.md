# Project Application: USB-MSC in USB BOT Observation

```yaml
project_id: usb-bot-observation
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/usb-control-stall-recovery-2026/
maturity:
  technology: R4
  implementation: R1
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt

Der bestehende `usb-msc`-Vertrag ist Raster für Fremdquellen. Das Projekt
implementiert kein Gadget und keinen Sniffer; es ordnet, welche Schicht welche
BOT-Grenze beobachten kann, und (seit 2026-10-14) **wo** ein Device-Logger
eingehängt werden muss — inkl. Control-/Enum-Epochs.

Audits:

- Pfadvergleich: [`usb-bot-observation-2026-foreign`](../../../audits/usb-bot-observation-2026-foreign/)
- Instrumentierung: [`usb-bot-observation-2026-instrument-sources`](../../../audits/usb-bot-observation-2026-instrument-sources/)
- Control/Stall/Enum: [`usb-control-stall-recovery-2026`](../../../audits/usb-control-stall-recovery-2026/)

## A/B/C-Trennung

| Ebene | Aussage in diesem Projekt |
|-------|---------------------------|
| **A — allgemein** | BOT = CBW → optional Data → CSW; CDB im CBW. Structs/Hooks im Sheet. |
| **B — Projekt** | Fremdquellen als Device-/Inline-/Host-Pfade; Hook-Karte und Schema-Abgleich in Evidence. |
| **C — konkreter Host** | NBT: CDBs, Sense, Reset, Transfergrenzen, Timing `UNKNOWN`. |

## Architektur / Beobachtungspfade

```text
                 Device-Logger  ← usbd SET_ADDRESS/CONFIG + mscd_xfer_cb / send_csw / Control
NBT Host ─ USB ─ MSC Device/TinyUSB (+ esp_tinyusb Mount/Umount)
    │            enum epochs + bot_cbw + chunks + bot_csw + stall/reset
    │
    ├─ Inline-Proxy / Bus-Capture ─ vollständige Busfolge, aber Eingriff
    │
    └─ kontrollierter Host/Gadget-Kontrast
       esp-usb/libusb/usb-tools ↔ TinyUSB/Linux f_mass_storage
       + usbsnoop (eBPF SETUP/BOT Decode) als Lab-Validate
       (Labmodell; kein NBT-Beweis)
```

### Device-seitige Instrumentierung

TinyUSB hält CBW, CDB, Gesamt-Datenlänge, übertragenen Stand und CSW intern.
Nach gültigem CBW (`MSC_STAGE_CMD`, nach `memcpy`) sind Tag, Lun, `total_bytes`,
`cmd_len` und `command[]` verfügbar — das ist der Ort für `bot_cbw`. CSW wird
in `send_csw` mit `data_residue = total_bytes - xferred_len` gebaut — Ort für
`bot_csw`. Control: BOT Reset (`0xFF`), Get Max LUN (`0xFE`), Clear-Halt und
`MSC_STAGE_NEED_RESET` sind Epoch-Grenzen.

**Enum / Stack-Control** (`usbd.c`, Follow-on 2026-10-14): `SET_ADDRESS` setzt nur
die Adresse; Klassen-EPs öffnen erst bei `SET_CONFIGURATION n` → `tud_mount_cb`.
cfg 0 → `tud_umount_cb`. Endpoint CLEAR_FEATURE Halt clear/stallt im Stack und
leitet an die Klasse weiter. Bei `MSC_STAGE_NEED_RESET` **heilt Clear-Halt nicht** —
weiter stall bis BOT Reset (`EVID-USBCTRL-2026-10-14-004`).

**ESP-Port** (`esp_tinyusb`): Mount/Umount koppeln MSC-Storage-Ownership und
`TINYUSB_EVENT_ATTACHED`/`DETACHED` (`EVID-USBCTRL-…-006`).

**Replug ohne VBUS-Sense** (EspUsbDevice Docs): Unplug oft ohne umount; State
auch bei Mount clearen (`EVID-USBCTRL-…-007`/`008`).

Ein Read-Callback sieht nur `(lba, offset, bufsize)`: mehrere Chunks können zu
**einem** READ(10) gehören. Adafruit `Adafruit_USBD_MSC` mappt App-Callbacks auf
`tud_msc_read10_cb` und verwirft `offset` — **kein** Ersatz für Stack-Hooks
(`EVID-USBBOT-INST-2026-10-14-010`).

### Inline-Proxy

USBProxy-legacy erkennt 31-Byte-CBW und 13-Byte-CSW und dekodiert READ(10) /
WRITE(10). Der Filter ist heuristisch; Upstream-README: Alpha / potenziell
nicht kompilierbar. Transparenz am NBT: `UNKNOWN`.

### Kontrollierter Host/Gadget-Kontrast

`esp-usb` und PartitionSchemeDetector erzeugen CBW→Data→CSW; Linux
`f_mass_storage` und TinyUSB liefern Device-Referenzen. **usbsnoop** dekodiert
am Linux-Host Control-SETUP (inkl. `SET_ADDRESS` / `SET_CONFIGURATION`) und
BOT CBW/CSW inkl. READ(10)-LBA/Blocks — geeignet als Lab-Gegenprobe zum
Device-Logger. Lizenz am Pin `UNKNOWN` → Research-Kontrast, keine Code-Übernahme
ohne Klärung (`EVID-USBBOT-INST-2026-10-14-007`).

### Schema-Referenzen

edk2 `UsbMassBot.h` und Wireshark `packet-usbms-bot.c` bestätigen dieselben
Signaturen, Tag/Residue/Status-Felder und CDB-Einbettung — Abgleich für
Logger-Feldnamen, kein neues Sheet.

## Relevante Pfade

| Repo @ Snapshot | Pfad | Beobachtbare Grenze |
|-----------------|------|----------------------|
| `felipebalbi/usb-tools@08d4f3b` | `src/msc.c`, `src/msc.sh` | Block-I/O oberhalb BOT |
| `USBProxy-legacy@30c4c14` | `PacketFilter_MassStorage.cpp` | CBW, READ/WRITE-Daten, CSW |
| `linux@2c0f5ca` | `f_mass_storage.c` | CBW-Validierung, CDB, Sense, CSW/Reset |
| `esp-usb@f3408e8` | `msc_scsi_bot.c` | Host-CBW, Datenphase, CSW, Sense/Recovery |
| `tinyusb@4c195b7` (Vor `3024dd2`) | `msc.h`, `msc_device.c`, **`usbd.c`** | Structs, Stages, BOT-Hooks, Enum/STALL |
| `esp-usb@c40b86d` (Device; Host war `f3408e8`) | `device/esp_tinyusb/` | Mount/Umount, Descriptors, S2/S3/P4 |
| `EspUsbDevice@c10a44e` | `docs/usb-device-*.md` | Enum-Stufen, kein VBUS, Replug |
| `PartitionSchemeDetector@63c8669` | `app.cpp` | libusb CBW/Data/CSW-/Reset |
| `vUSBf@bc1fb14` | Replay-/Fuzzing | VM-Sequenzen, nicht Live-Capture |
| `usbsnoop@30f9fad` | `main.js`, `usbsnoop.bpf.c` | Host SETUP + BOT Decode |
| `Adafruit_TinyUSB_Arduino@1b73172` | `Adafruit_USBD_MSC.cpp`, MSC-Beispiele | App-Callbacks ohne CBW |
| `edk2@e4d139f` | `UsbMassBot.h` | CBW/CSW-Struct-Referenz |
| `wireshark@f28ca85` | `packet-usbms-bot.c` | Dissector-Feldnamen |

## Beobachtungsmodell und Parameter

| Feld | Warum separat loggen? | Desk-Status |
|------|------------------------|-------------|
| CBW-Tag | korreliert Command und CSW | `FACT` |
| CDB-Bytes + CDB-Länge | Opcode, LBA, Transferblöcke | `FACT` |
| CBW DataTransferLength | Host-Erwartung in Bytes | `FACT` |
| Callback `bufsize` / Chunk | Stack-/Endpoint-Teilung | `FACT`; **nicht** CDB-Länge |
| Datenrichtung und kumulierte Bytes | Datenphase / Partial Transfer | `FACT` |
| CSW-Tag, Residue, Status | Abschluss oder Phase Error | `FACT` |
| Sense Key / ASC / ASCQ | Fehler nach fehlgeschlagenem Command | `FACT` in Referenzen |
| Reset-Epoch / Clear-Halt | Recovery-Grenze | `FACT` in Referenzen |
| SET_ADDRESS / SET_CONFIGURATION | Enum-Epoch; Mount erst bei cfg n | `FACT` (`EVID-USBCTRL-…-001`) |
| NEED_RESET vs. Clear-Halt | Clear heilt NEED_RESET **nicht** | `FACT` (`EVID-USBCTRL-…-004`) |
| Mount ohne VBUS-Sense | Replug oft ohne umount | `FACT` Doku (`EVID-USBCTRL-…-007`/`008`) |
| Control SETUP (Host-Lab) | Enumeration / Class-Reset | `FACT` in usbsnoop Decode |
| USB↔WiFi unter Last | PHY/PLL / Last-Korrelation | `HYPOTHESIS` (`EVID-USBCTRL-…-009`); Sonde `UNKNOWN` |
| monotone Zeitstempel | Latenzanalyse | erforderlich; NBT `UNKNOWN` |
| Drop-/Overflow-Zähler | Capture-Vollständigkeit | erforderlich; nicht implementiert |

## Ebene C — NBT Host-/Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Konkrete NBT-READ(10)-CDB-Länge | `EVID-USBBOT-2026-10-13-013` | `UNKNOWN` |
| NBT Sense-/Reset-Sequenz | `EVID-USBBOT-2026-10-13-013` | `UNKNOWN` |
| NBT Command-/Inaktivitäts-Timing | `EVID-USBBOT-2026-10-13-013` | `UNKNOWN` |
| Ein Proxy-/Loggerpfad ist am NBT transparent | `EVID-USBBOT-2026-10-13-012` | `UNKNOWN` |
| Device↔Host Tag-Match (Lab) | — | `UNKNOWN` (nächster Lab) |

## Grenzen transparenten Captures

- **Semantisch:** Block-I/O oder Read-Callbacks verlieren CBW-/CSW-Grenzen.
- **Vollständigkeit:** Ringoverflow, fehlende Zeitstempel oder verlorene
  Reset-/Control-Transfers machen eine Folge nicht beweiskräftig.
- **Kausalität:** REQUEST SENSE muss zum vorangehenden fehlgeschlagenen Command
  korreliert werden.
- **Intervention:** Inline-Hardware, Logging und Firmware können Latenz,
  Enumeration und Recovery verändern. Ohne Baseline ist „transparent“ kein
  `FACT`.
- **Übertragbarkeit:** PC-, ESP- und VM-Sequenzen sind Kontraste, keine
  NBT-Feldbelege.
- **Lizenz:** usbsnoop ohne erkannte LICENSE → keine ungeprüfte Übernahme.

## Beobachtungen

Keine Lab- oder Feldbeobachtungen. Evidence-IDs sind Desk-Code-/Dokumentationsbefunde
(`EVID-USBBOT-2026-10-13-*`, `EVID-USBBOT-INST-2026-10-14-*`,
`EVID-USBCTRL-2026-10-14-*`).

## Offene Fragen

- Kann ein Device-Ring CBW/CDB/CSW plus Control-Reset ohne Timingstörung halten?
- Tag-Match Device-Logger ↔ usbsnoop am Kontrollhost?
- Wie wird die Beobachterwirkung vor einem NBT-Lauf quantifiziert?
- Stirbt WiFi der Sonde unter USB-Last (Lab), und welcher Chip-/PHY-Pfad?

## Verwandte Applications / Methods

- Sheet: [`usb-msc`](../../../technologies/usb-msc/SHEET.md)
- Device-Referenzen:
  [`esp32-msc-gadget-refs`](../../esp32-msc-gadget-refs/applications/usb-msc.md)
- Busy-Vertrag:
  [`tinyusb-msc-busy-retry-2026`](../../../audits/tinyusb-msc-busy-retry-2026/)
- Methods:
  [`usb-bot-command-observation`](../../../methods/usb-bot-command-observation.md) ·
  [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md) ·
  [`msc-trace-correlation`](../../../methods/msc-trace-correlation.md)
