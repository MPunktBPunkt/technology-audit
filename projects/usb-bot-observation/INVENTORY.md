# Project Inventory: USB BOT Observation

```yaml
project_id: usb-bot-observation
updated: 2026-10-13
reviewed_snapshots: 7
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

- **Device-seitig:** TinyUSB-/Gadget-Telemetrie
- **Inline:** USBProxy-/Hardware-Proxy
- **Kontrollierter Host/Gadget-Kontrast:** Host-Generator plus
  Referenz-Gadget

Keiner dieser Pfade hat in dieser Kampagne NBT-Daten erzeugt.

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| NBT-CBW/CDB/CSW | kein Fahrzeug-Capture | nur nach separatem Go und präregistrierten Gates |
| READ(10)-Commandgrenze | Callback-Chunks sind keine CDB-Grenzen | CBW-CDB und CSW-Tag gemeinsam loggen |
| Sense-Folge | keine NBT-Fehlersession | REQUEST SENSE kausal zum fehlgeschlagenen CSW korrelieren |
| BOT Reset | Desk kennt Referenzpfade, nicht NBT-Verhalten | Reset-Epoch und Endpoint-Recovery instrumentieren |
| Timing / Transparenz | Beobachterwirkung nicht gemessen | Baseline gegen Instrumentierungsvariante |

## Signale ohne Eintrag

- USBProxy-legacy ist ein riskanter Altbestand, kein eigener Technologie-Slug.
- vUSBf ist Replay-/Fuzzing-Kontrast, kein transparenter Fahrzeug-Capture.
- PartitionSchemeDetector bleibt ein kleiner BOT-Codekontrast; die Weiterleitung
  `ookaay` → `treblist` erzeugt keinen zweiten Projekteinstieg.
