# Project Application: USB-MSC in USB BOT Observation

```yaml
project_id: usb-bot-observation
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/usb-bot-observation-2026-foreign/
maturity:
  technology: R4
  implementation: R1
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt

Der bestehende `usb-msc`-Vertrag wird als Raster für sieben Fremdquellen
verwendet. Das Projekt implementiert kein Gadget und keinen Sniffer; es ordnet,
welche Schicht welche BOT-Grenze beobachten kann.

## A/B/C-Trennung

| Ebene | Aussage in diesem Projekt |
|-------|---------------------------|
| **A — allgemein** | BOT besteht aus CBW, optionaler Datenphase und CSW; die CDB sitzt im CBW. Allgemeines Wissen bleibt im bestehenden Sheet. |
| **B — Projekt** | Die Fremdquellen werden als Device-, Inline- und Host-Kontrastpfade verglichen; Claims stehen im Kampagnen-Evidence-Register. |
| **C — konkreter Host** | Reales NBT-Verhalten ist nicht beobachtet: CDBs, Sense, Reset, Transfergrenzen und Timing sind `UNKNOWN`. |

## Architektur / Beobachtungspfade

```text
                 Device-Logger
NBT Host ─ USB ─ MSC Device/TinyUSB
    │            CBW/CDB + Callback + CSW/Reset
    │
    ├─ Inline-Proxy / Bus-Capture ─ vollständige Busfolge, aber Eingriff
    │
    └─ kontrollierter Host/Gadget-Kontrast
       esp-usb/libusb/usb-tools ↔ TinyUSB/Linux f_mass_storage
       (Labmodell; kein NBT-Beweis)
```

### Device-seitige Instrumentierung

TinyUSB hält CBW, CDB, Gesamt-Datenlänge, übertragenen Stand und CSW-Zustand
intern getrennt. Das ist der direkteste Desk-Kandidat für korrelierte
Commandgrenzen. Ein Read-Callback sieht jedoch nur `(lba, offset, bufsize)`:
mehrere Callback-/Endpoint-Chunks können zu **einem** READ(10) gehören.

### Inline-Proxy

USBProxy-legacy erkennt 31-Byte-CBW und 13-Byte-CSW und dekodiert READ(10) /
WRITE(10). Der Filter ist aber heuristisch und das Upstream-README bezeichnet
den Stand als Alpha bzw. potenziell nicht kompilierbar. Elektrische und
zeitliche Transparenz am NBT ist daher `UNKNOWN`.

### Kontrollierter Host/Gadget-Kontrast

`esp-usb` und PartitionSchemeDetector erzeugen explizite CBW→Data→CSW-Folgen;
Linux `f_mass_storage` und TinyUSB liefern Device-Referenzen. Der Pfad ist gut
für Parser-/Logger-Tests, kann aber keine NBT-Sequenz vorwegnehmen.

## Relevante Pfade

| Repo @ Snapshot | Pfad | Beobachtbare Grenze |
|-----------------|------|----------------------|
| `felipebalbi/usb-tools@08d4f3b` | `src/msc.c`, `src/msc.sh` | Block-I/O-Größen/Throughput oberhalb BOT |
| `USBProxy-legacy@30c4c14` | `src/Plugins/Filters/PacketFilter_MassStorage.cpp` | CBW, READ/WRITE-Daten, CSW |
| `linux@2c0f5ca` | `drivers/usb/gadget/function/f_mass_storage.c` | CBW-Validierung, CDB, Sense, CSW/Reset |
| `esp-usb@f3408e8` | `host/class/msc/usb_host_msc/src/msc_scsi_bot.c` | Host-CBW, Datenphase, CSW, Sense/Recovery |
| `tinyusb@3024dd2` | `src/class/msc/msc_device.c`, `.h` | Device-Stages, READ10-Callback, CSW, BOT Reset |
| `PartitionSchemeDetector@63c8669` | `app.cpp` | kleiner libusb CBW/Data/CSW-/Reset-Kontrast |
| `vUSBf@bc1fb14` | Replay-/Fuzzing-Gerüst | reproduzierbare VM-Sequenzen, nicht Live-Capture |

## Beobachtungsmodell und Parameter

| Feld | Warum separat loggen? | Desk-Status |
|------|------------------------|-------------|
| CBW-Tag | korreliert Command und CSW | `FACT` |
| CDB-Bytes + CDB-Länge | Opcode, LBA, Transferblöcke | `FACT` |
| CBW DataTransferLength | Host-Erwartung in Bytes | `FACT` |
| Callback `bufsize` / Chunk | Stack-/Endpoint-Teilung | `FACT`; **nicht** CDB-Länge |
| Datenrichtung und kumulierte Bytes | Datenphase / Partial Transfer | `FACT` |
| CSW-Tag, Residue, Status | Abschluss oder Phase Error | `FACT` |
| Sense Key / ASC / ASCQ | Fehlerbedeutung nach fehlgeschlagenem Command | `FACT` in Referenzen |
| Reset-Epoch / Clear-Halt | Recovery-Grenze | `FACT` in Referenzen |
| monotone Zeitstempel | Latenzanalyse | erforderlich; NBT-Werte `UNKNOWN` |
| Drop-/Overflow-Zähler | Capture-Vollständigkeit | erforderlich; nicht implementiert |

## Ebene C — NBT Host-/Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Konkrete NBT-READ(10)-CDB-Länge | `EVID-USBBOT-2026-10-13-013` | `UNKNOWN` |
| NBT Sense-/Reset-Sequenz | `EVID-USBBOT-2026-10-13-013` | `UNKNOWN` |
| NBT Command-/Inaktivitäts-Timing | `EVID-USBBOT-2026-10-13-013` | `UNKNOWN` |
| Ein Proxy-/Loggerpfad ist am NBT transparent | `EVID-USBBOT-2026-10-13-012` | `UNKNOWN` |

## Grenzen transparenten Captures

- **Semantisch:** Block-I/O oder Read-Callbacks verlieren CBW-/CSW-Grenzen.
- **Vollständigkeit:** Ringoverflow, fehlende Zeitstempel oder verlorene
  Reset-/Control-Transfers machen eine Folge nicht beweiskräftig.
- **Kausalität:** REQUEST SENSE muss zum vorangehenden fehlgeschlagenen Command
  korreliert werden; eine isolierte Sense-Zeile reicht nicht.
- **Intervention:** Inline-Hardware, Logging und Firmware können Latenz,
  Enumeration und Recovery verändern. Ohne Baseline ist „transparent“ kein
  `FACT`.
- **Übertragbarkeit:** PC-, ESP- und VM-Sequenzen sind Kontraste, keine
  NBT-Feldbelege.

## Beobachtungen

Keine Lab- oder Feldbeobachtungen. Alle Evidence-IDs dieser Kampagne sind
Desk-Code-/Dokumentationsbefunde.

## Offene Fragen

- Kann ein Device-Ring CBW/CDB/CSW plus Control-Reset ohne Timingstörung halten?
- Welche Daten müssen auf dem Bus, nicht nur im Class Driver, beobachtet werden?
- Wie wird die Beobachterwirkung vor einem NBT-Lauf quantifiziert?

## Verwandte Applications / Methods

- Sheet: [`usb-msc`](../../../technologies/usb-msc/SHEET.md)
- Bestehende Device-Referenzen:
  [`esp32-msc-gadget-refs`](../../esp32-msc-gadget-refs/applications/usb-msc.md)
- Busy-Vertrag:
  [`tinyusb-msc-busy-retry-2026`](../../../audits/tinyusb-msc-busy-retry-2026/)
- Verwendete Methods:
  [`usb-bot-command-observation`](../../../methods/usb-bot-command-observation.md) ·
  [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md) ·
  [`msc-trace-correlation`](../../../methods/msc-trace-correlation.md)
