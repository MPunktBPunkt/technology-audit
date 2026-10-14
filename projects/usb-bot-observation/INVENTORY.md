# Project Inventory: USB BOT Observation

```yaml
project_id: usb-bot-observation
updated: 2026-10-14
reviewed_snapshots: 15
profile: lab-tool
pilot_order: [usb-msc]
```

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `usb-msc` | USB Mass Storage Class / BOT | C | `usb-device`, `lab-only` | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |

Legende Status: `candidate` · `observed` · `documented` · `applied` ·
`transferred`. Coverage bleibt `partial`: Desk-Codevergleich ist kein
NBT-Capture und keine Transparenzmessung.

## Nach Kategorie

### C — Protokolle

`usb-msc` — wiederverwendeter Slug; BOT und SCSI Transparent Command Set
werden hier als Transport-/Command-Signale innerhalb dieser Anwendung
behandelt, nicht als neue Sheets.

### H — Test / Analyse

Beobachtungspfade:

- **Device-seitig:** TinyUSB-/Gadget-Telemetrie (BOT-Hooks + `usbd.c`
  Enum/STALL — Instrumentierungs- und Control-Audits)
- **Inline:** USBProxy-/Device-Proxy
- **Kontrollierter Host/Gadget-Kontrast:** Host-Generator plus
  Referenz-Gadget; Lab-Validate-Kandidat: usbsnoop (Lizenz `UNKNOWN`)

Keiner dieser Pfade hat NBT-Daten erzeugt.

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| NBT-CBW/CDB/CSW | kein Fahrzeug-Capture | nur nach separatem Go und präregistrierten Gates |
| READ(10)-Commandgrenze | Callback-Chunks sind keine CDB-Grenzen | CBW-CDB und CSW-Tag gemeinsam loggen |
| Sense-Folge | keine NBT-Fehlersession | REQUEST SENSE kausal zum fehlgeschlagenen CSW korrelieren |
| BOT Reset / NEED_RESET | Desk: Clear-Halt heilt NEED_RESET nicht; NBT offen | Epochs im Logger trennen; NBT-Capture separat |
| Enum ohne VBUS | Desk: Replug oft ohne umount | Mount-Clear; Lab Replug-Soak |
| Timing / Transparenz / S1–S3 | Beobachterwirkung nicht gemessen | eigene Messung, kein Fremd-Audit |
| WiFi unter USB-Last | Issues = `HYPOTHESIS` | Lab an der Sonde |
| Host Tag-Match | usbsnoop Desk-Decode ohne Lab | kontrollierter Lab nach Lizenzklärung |

## Signale ohne Eintrag

- USBProxy-legacy ist ein riskanter Altbestand, kein eigener Technologie-Slug.
- vUSBf ist Replay-/Fuzzing-Kontrast, kein transparenter Fahrzeug-Capture.
- PartitionSchemeDetector bleibt ein kleiner BOT-Codekontrast; die Weiterleitung
  `ookaay` → `treblist` erzeugt keinen zweiten Projekteinstieg.
- usbsnoop bleibt Research-/Lab-Tool-Kontrast ohne eigenen Slug (Lizenz offen).
- edk2/Wireshark BOT-Dateien sind Schema-Referenzen, keine neuen Sheets.
- EspUsbDevice Docs = Enum-Kontrast; kein zweites Device-Sheet.
- esp-idf/arduino-esp32 USB↔WiFi Issues = Hypothesenregister, kein Fact für die Sonde.
