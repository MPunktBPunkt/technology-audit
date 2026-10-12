# Technology Sheet: USB Mass Storage Class

```yaml
slug: usb-msc
title: USB Mass Storage Class
primary: C
tags: [usb-device, automotive, streaming]
type: protocol
status: active
seen_in: [pidrive, esp32-pidrive, esp32-msc-gadget-refs]
maturity:
  technology: R4
  implementation: R0   # siehe Project Application
  field_evidence: R0   # Host-spezifisch → Application / bmw-nbt-evo
  reusability: W3
pilot: audits/pidrive-2026-msc
```

Ebene **A** (allgemein). Ops/Feld → [`pidrive/applications/usb-msc.md`](../../projects/pidrive/applications/usb-msc.md). Firmware-Desk → [`esp32-pidrive/applications/usb-msc.md`](../../projects/esp32-pidrive/applications/usb-msc.md). Referenz-Gadgets → [`esp32-msc-gadget-refs`](../../projects/esp32-msc-gadget-refs/). BMW-Host → [`bmw-nbt-evo`](../bmw-nbt-evo/SHEET.md). Virtual FAT → [`virtual-fat`](../virtual-fat/SHEET.md).

**Wachstum 2026-10-12:** Callback-Zelle, USB-FS-Budget, Multi-Sektor-`bufsize`, exclusive-mount — Desk [`esp32-msc-gadget-refs-2026-foreign`](../../audits/esp32-msc-gadget-refs-2026-foreign/).

## Kurzfassung

USB Mass Storage Class (MSC) lässt ein USB-Device einem Host als blockorientiertes Speichermedium erscheinen. Typischer Transport: **Bulk-Only Transport (BOT)**; Kommandos: **SCSI** (READ(10)/WRITE(10)). Auf ESP32-Gadgets liefert der Stack Sektoren über einen **Read-Callback** (`onRead` / `tud_msc_read10_cb` / `msc_read_cb`) — Inhalt kann Flash/SD/RAM **oder on-the-fly** sein.

## Abgrenzung

- **Ist:** Geräteklasse + Protokollstapel Device ↔ Host für Block-I/O — in dieser KB vor allem die **Device/Gadget**-Rolle.
- **Ist nicht:** FAT/MP3/Streaming-Semantik (`virtual-fat` / Application); HU-Prefetch (`bmw-nbt-evo`); ESP als USB-**Host** (`esp-usb-host`).
- **Grenzt an:** SCSI, BOT, UASP (nicht Fokus), Dateisysteme darüber.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Host | USB Host Controller + MSC-Treiber | initiiert CBW/CSW, liest/schreibt LBAs |
| Transport | USB Bulk-Only (BOT) | CBW → Daten → CSW |
| Kommandos | SCSI Transparent Subclass | READ/WRITE/INQUIRY/… |
| Device-API | Read/Write/StartStop Callbacks | TinyUSB / Arduino USBMSC / Adafruit / EspTinyUSB |
| Darüber | Dateisystem / App | interpretiert Sektorinhalte |
| Darunter | USB Device Controller | Full-Speed typisch auf ESP32-S2/S3 |

## Typische Fallstricke (A)

| Claim | Status | Hinweis |
|-------|--------|---------|
| MSC „streamt Audio“ | `REJECTED` | nur Blöcke; Audio = FS + Host-Decoder |
| Ein READ-Muster gilt für alle Hosts | `REJECTED` | Prefetch/Burst = **C** |
| BOT + SCSI Transparent üblich | `FACT` | Consumer-Sticks |
| LBA linear über Kapazität | `FACT` | Geometrie Firmware-Wahl |
| Callback darf beliebig lange blockieren | `REJECTED` | Host-Timeouts; Latenz budgetieren (Method) |
| `bufsize` immer 512 | `REJECTED` | Multi-Sektor-Bursts üblich |
| USB FS Average ≫ 1 MB/s auf ESP MSC | `REJECTED` / Gate | Author-Messungen ~0.5–1 MB/s Read; FS ceiling ~1.2 MB/s |
| 320 kb/s MP3 sprengt USB FS | `REJECTED` | ~40 KB/s ≪ USB; Engpass = Burst/Latenz |
| App und Host gleichzeitig dieselbe Partition | `REJECTED` | IDF: exclusive mount scenarios |
| Single-sector SD API = Multi-sector Perf | `REJECTED` | atomic14: klar langsamer |
| On-the-fly braucht Full-Disk in PSRAM | `REJECTED` | Callback kann Body-LBAs live füllen |

## Transfer

Wiederverwendbar für MCU-als-Stick, Diagnose-Gadgets, virtuelle Medien. **Host-Timing nie hier.**  
Perf-Baseline und Callback-Hooks: Desk [`esp32-msc-gadget-refs-2026-foreign`](../../audits/esp32-msc-gadget-refs-2026-foreign/). Instrumentierung: [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md).

### Projektstart-Checkliste

- [ ] BOT+SCSI vs. `virtual-fat` klar trennen
- [ ] Read-Callback Signatur + Multi-Sektor `bufsize` geplant
- [ ] Host-Prefetch/Timing → Host-Sheet / Application C
- [ ] Throughput vs. Latenz getrennt messen
- [ ] Application + `seen_in`

## Referenzen

- USB MSC BOT; SCSI SBC READ(10)
- Espressif `tusb_msc`; Arduino `USBMSC.h`; Adafruit TinyUSB MSC; aoscarius/esp32usbmsc; atomic14/esp32-sdcard-msc
- PiDrive: [`esp32.pidrive`](https://github.com/MPunktBPunkt/esp32.pidrive)

## Offene Fragen (A)

- UASP vs. BOT für Zielhosts?
- Max Callback-Latenz vor typischem Host-Abort (Method + Lab)?

## Lessons

- Sheet bleibt ohne HU-Timing.
- Callback-Zelle + USB-FS-Budget sind die transferierbaren A-Erweiterungen aus dem Gadget-Referenz-Audit.
