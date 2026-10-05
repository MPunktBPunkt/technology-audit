# Project Inventory: PiDrive

```yaml
project_id: pidrive
updated: 2026-10-05
pilot_order: [usb-msc, bmw-nbt-evo, avrcp]
```

Pilot 1 (`usb-msc`) Schema-Validation **closed** (Feld-AV upstream offen). Pilot 2 (`bmw-nbt-evo`) **active**.

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `dab-plus` | DAB+ | A | `sdr`, `streaming` | observed | none | [SHEET](../../technologies/dab-plus/SHEET.md) | — |
| `rtl-sdr` | RTL-SDR | A | `sdr`, `usb-host` | observed | none | [SHEET](../../technologies/rtl-sdr/SHEET.md) | — |
| `webradio` | Webradio | A | `streaming` | observed | none | [SHEET](../../technologies/webradio/SHEET.md) | — |
| `pipewire` | PipeWire | B | `linux-userspace`, `realtime` | observed | none | [SHEET](../../technologies/pipewire/SHEET.md) | — |
| `usb-msc` | USB Mass Storage Class | C | `usb-device`, `automotive` | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |
| `scsi` | SCSI (über MSC/BOT) | C | `usb-device` | observed | none | [SHEET](../../technologies/scsi/SHEET.md) | — |
| `bluetooth-a2dp` | Bluetooth A2DP | C | `bluetooth-classic`, `streaming` | observed | none | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | — |
| `avrcp` | AVRCP | C | `bluetooth-classic`, `metadata` | observed | none | [SHEET](../../technologies/avrcp/SHEET.md) | — |
| `esp32` | ESP32 | D | `esp-idf` | observed | none | [SHEET](../../technologies/esp32/SHEET.md) | — |
| `fat` | FAT / LBA-Geometrie | E | — | observed | none | [SHEET](../../technologies/fat/SHEET.md) | — |
| `systemd` | systemd | F | `linux-userspace` | observed | none | [SHEET](../../technologies/systemd/SHEET.md) | — |
| `mpris2` | MPRIS2 | G | `metadata`, `linux-userspace` | observed | none | [SHEET](../../technologies/mpris2/SHEET.md) | — |
| `bmw-nbt-evo` | BMW NBT Evo Host-Verhalten | I | `automotive`, `field-verified` | applied | partial | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | [app](applications/bmw-nbt-evo.md) |

## Nach Kategorie

### A — Empfang

`dab-plus`, `rtl-sdr`, `webradio` (+ Kandidaten: FM/Scanner, Airband — bei Bedarf eigene Slugs)

### B — Audio

`pipewire` (+ Kandidaten: ALSA-Routen, EQ)

### C — Protokolle

`usb-msc`, `scsi`, `bluetooth-a2dp`, `avrcp`

### D — Embedded

`esp32` (+ Kandidaten: TinyUSB, Ringbuffer/DMA in MSC-Pfad)

### E — Speicher / Formate

`fat`

### F — Systemintegration

`systemd` (+ Kandidaten: udev, WiFi-Hilfen)

### G — Steuerung / UI

`mpris2` (+ Kandidaten: Trigger-System, WebUI, CLI)

### H — Test / Analyse

noch keine Einträge — Methoden eher unter `methods/` (z. B. MSC-Trace-Korrelation)

### I — Fahrzeug / Geräte

`bmw-nbt-evo`

### J — Architektur

noch keine eigenen Slugs (Producer-Consumer/Bridge bei Applications vertiefen)

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| `usb-msc` | Schema-Pilot done; Feld-AV, scsi/fat-Sheets | Feld-AV `pidrive`; C → `bmw-nbt-evo` |
| `bmw-nbt-evo` | C migriert; Feld-AV/Ohr offen | Evidence + Feld-AV upstream |
| `avrcp` | Pilot 3 | nach BMW-HU |
| DAB+/SDR | stabiler Teilstack, wenig verdichtet | später Sheet `dab-plus` |

## Signale ohne Eintrag

Bei Vertiefung ggf. eigene Slugs:

- Airband / Scanner
- Spotify / raspotify
- Trigger-Dispatcher / Lenkrad-Mapping
- SoftAP / Diagnose-HTTP auf ESP
- Prefill / Body-Seed (MSC-Implementierungsdetail → eher Application als Tech)
