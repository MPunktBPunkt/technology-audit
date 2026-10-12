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
**Wachstum 2026-10-12 (Busy/Async):** TinyUSB `return 0` / `TUD_MSC_RET_BUSY`, Partial/ERROR, ASYNC (#2967), EP_BUFSIZE — Desk [`tinyusb-msc-busy-retry-2026`](../../audits/tinyusb-msc-busy-retry-2026/).

## Kurzfassung

USB Mass Storage Class (MSC) lässt ein USB-Device einem Host als blockorientiertes Speichermedium erscheinen. Typischer Transport: **Bulk-Only Transport (BOT)**; Kommandos: **SCSI** (READ(10)/WRITE(10)). Auf ESP32-Gadgets liefert der Stack Sektoren über einen **Read-Callback** (`onRead` / `tud_msc_read10_cb` / `msc_read_cb`) — Inhalt kann Flash/SD/RAM **oder on-the-fly** sein.

### TinyUSB Read-Callback-Vertrag (A)

| Return | Bedeutung | Stack-Verhalten |
|--------|-----------|-----------------|
| `> 0` (≤ `bufsize`) | Bytes bereit | IN-Transfer; bei `ret < bufsize` weiterer Callback für Rest desselben READ10 |
| `0` / `TUD_MSC_RET_BUSY` | noch nicht fertig | Fake-Xfer-Complete → Callback **mit gleichen Parametern**; **CBW/READ10 bleibt offen**; kein CSW |
| `< 0` / `TUD_MSC_RET_ERROR` | Fehler | Endpoint STALL, CSW failed, Sense gesetzt |
| `TUD_MSC_RET_ASYNC` (−2) | IO asynchron | nur Upstream nach PR #2967; Abschluss via `tud_msc_async_io_done(nbytes)` (`0` dort = ERROR) |

`CFG_TUD_MSC_EP_BUFSIZE` (Alias `CFG_TUD_MSC_BUFSIZE`) begrenzt die pro Callback angeforderte Chunk-Größe; typische SDK-Defaults 512 oder **4096**. Device-MSC hat **keinen** eingebauten Timeout für BUSY-Loops — Abbruch ist Host-Sache (**nicht** hier als ms-FACT).

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
| `return 0` = „fertig, 0 Bytes / neuer Befehl“ | `REJECTED` | = BUSY; gleicher READ10 bleibt offen (`EVID-TINYUSB-MSC-2026-10-12-001/002`) |
| `return 0` gibt `tud_task`/Main-Loop zuverlässig frei | `REJECTED` | Issue #2035: Event-Selbst-Queue; ohne Yield/RTOS Spin (`EVID-…-003`) |
| TinyUSB Device timeoutet BUSY selbst | `REJECTED` | kein Driver-Timeout; Host bricht ab (`EVID-…-006`) |
| Arduino-ESP32 TinyUSB 0.15 = Upstream ASYNC | `REJECTED` | 0.15: Busy/Partial/Error; kein `async_io_done` (`EVID-…-008`) |
| Partial-Read ist spezifiziert | `FACT` | Header: Rest-Callback (`EVID-…-005`) |
| Partial-Read immer endpoint-sicher auf allen Ports | `UNKNOWN` | RP2040: Panic belegt; ESP32-S3/DWC2 offen (`EVID-…-009`) |
| Arduino `onRead` Return mappt 1:1 auf TinyUSB | `FACT` | `USBMSC.cpp` → `tud_msc_read10_cb` (`EVID-…-008`) |

## Transfer

Wiederverwendbar für MCU-als-Stick, Diagnose-Gadgets, virtuelle Medien. **Host-Timing nie hier.**  
Perf-Baseline und Callback-Hooks: Desk [`esp32-msc-gadget-refs-2026-foreign`](../../audits/esp32-msc-gadget-refs-2026-foreign/).  
Busy/Async-Vertrag: [`tinyusb-msc-busy-retry-2026`](../../audits/tinyusb-msc-busy-retry-2026/).  
Instrumentierung: [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) · [`msc-busy-retry-semantics`](../../methods/msc-busy-retry-semantics.md).

### Projektstart-Checkliste

- [ ] BOT+SCSI vs. `virtual-fat` klar trennen
- [ ] Read-Callback Signatur + Multi-Sektor `bufsize` / `EP_BUFSIZE` geplant
- [ ] Busy-Strategie gewählt: Block vs. `return 0` vs. ASYNC (Port-Check!)
- [ ] Host-Prefetch/Timing → Host-Sheet / Application C
- [ ] Throughput vs. Latenz getrennt messen
- [ ] Application + `seen_in`

## Referenzen

- USB MSC BOT; SCSI SBC READ(10)
- TinyUSB `src/class/msc/msc_device.h` / `.c`; Issue [#2035](https://github.com/hathach/tinyusb/issues/2035); PR [#2967](https://github.com/hathach/tinyusb/pull/2967)
- Espressif `tusb_msc`; Arduino `USBMSC.h`; Adafruit TinyUSB MSC; aoscarius/esp32usbmsc; atomic14/esp32-sdcard-msc
- PiDrive: [`esp32.pidrive`](https://github.com/MPunktBPunkt/esp32.pidrive)

## Offene Fragen (A)

- UASP vs. BOT für Zielhosts?
- Max Callback-/BUSY-Latenz vor typischem Host-Abort → Lab ([`msc-busy-retry-semantics`](../../methods/msc-busy-retry-semantics.md)); Host-ms nie als A-FACT
- ESP32-S3/DWC2: Partial-Read Endpoint-Verhalten vs. RP2040?

## Lessons

- Sheet bleibt ohne HU-Timing.
- Callback-Zelle + USB-FS-Budget sind die transferierbaren A-Erweiterungen aus dem Gadget-Referenz-Audit.
- Busy/return-0 ist etabliert, aber **kein** kooperatives Yield ohne RTOS/ASYNC — Stall-FW muss den Port-Vertrag kennen.
