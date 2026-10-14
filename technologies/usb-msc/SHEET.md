# Technology Sheet: USB Mass Storage Class

```yaml
slug: usb-msc
title: USB Mass Storage Class
primary: C
tags: [usb-device, automotive, streaming]
type: protocol
status: active
seen_in: [pidrive, esp32-pidrive, esp32-msc-gadget-refs, usb-bot-observation]
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
**Wachstum 2026-10-14 (BOT-Hooks/Schema):** CBW/CSW-Felder, TinyUSB Hook-Punkte, Control/STALL/Reset-Epoch, Host-eBPF-Decode — Desk [`usb-bot-observation-2026-instrument-sources`](../../audits/usb-bot-observation-2026-instrument-sources/).  
**Wachstum 2026-10-14 (Control/Enum):** `usbd.c` SET_ADDRESS/SET_CONFIGURATION → mount/umount; CLEAR_HALT vs. NEED_RESET; esp_tinyusb Port-Kopplung; kein-VBUS-Replug — Desk [`usb-control-stall-recovery-2026`](../../audits/usb-control-stall-recovery-2026/).

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

### BOT-Structs und Device-Hooks (A)

CBW (31 B) und CSW (13 B) sind die Commandgrenzen — nicht der Read-Callback.

| Struct | Kernfelder | Signatur (LE) |
|--------|------------|---------------|
| CBW | `tag`, `total_bytes`, `dir`, `lun`, `cmd_len`, `command[16]` | `0x43425355` (`USBC`) |
| CSW | `tag`, `data_residue`, `status` (0 pass / 1 fail / 2 phase error) | `0x53425355` (`USBS`) |

TinyUSB-Device (Instrumentierung, nicht App-API):

| Hook | Wann | Typisches Event |
|------|------|-----------------|
| `usbd.c` `SET_ADDRESS` | Adressphase | `usb_set_address` (noch **nicht** mounted) |
| `usbd.c` `SET_CONFIGURATION` | cfg 0 → `tud_umount_cb`; cfg n → `process_set_config` + `tud_mount_cb` | `usb_set_config` / mount / umount |
| `usbd.c` CLEAR/SET_FEATURE `EDPT_HALT` | Endpoint Stall / Clear-Halt | `ep_stall` / `ep_clear_halt` |
| `mscd_xfer_cb` / `MSC_STAGE_CMD` nach gültigem CBW | neuer Command | `bot_cbw` |
| `send_csw` | Statusphase; Residue = `total_bytes - xferred_len` | `bot_csw` |
| `mscd_control_xfer_cb` | BOT Reset `0xFF`, Get Max LUN `0xFE`, Clear-Halt | Epoch / Control |
| `MSC_STAGE_NEED_RESET` | ungültiger CBW → Stall beider Bulk-EPs; Clear-Halt **heilt nicht** | Recovery-Epoch |
| `tud_msc_set_sense` | Sense Key / ASC / ASCQ | Fehlerkontext |

ESP-Port (`esp_tinyusb`): `tud_mount_cb` / `tud_umount_cb` koppeln MSC-Storage-Ownership (`mount_to_usb` / `mount_to_app`) und `TINYUSB_EVENT_ATTACHED` / `DETACHED`. Descriptor-Callbacks liegen in `descriptors_control.c`.

Enum-Praxis (ohne VBUS-Sense, typisch ESP-Boards): Unplug feuert oft **kein** umount; Replug geht in Re-Enumeration — State auch bei Mount (`SET_CONFIGURATION n`) clearen.

App-Layer-Callbacks (`tud_msc_read10_cb` / Adafruit `onRead`) sehen **keine** CBW-Felder; Chunk-`bufsize` ≠ CDB-Transferlänge. Schema-Abgleich: edk2 `UsbMassBot.h`, Wireshark `packet-usbms-bot.c` — gleicher Contract, kein paralleles Sheet.

Host-Lab-Validate (Linux): eBPF-Sniffer können SETUP (Enumeration) und BOT CBW/CSW dekodieren; das ersetzt keinen Hardware-Analyzer und keinen Zielhost-Lauf.

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
| App-`onRead` = vollständiges CBW-Event | `REJECTED` | CBW nur im Class Driver (`EVID-USBBOT-INST-2026-10-14-002`/`010`) |
| CBW 31 B / CSW 13 B mit USBC/USBS | `FACT` | TinyUSB `msc.h`; edk2/Wireshark Abgleich |
| Ungültiger CBW → Stall + Reset-Recovery | `FACT` | TinyUSB `MSC_STAGE_NEED_RESET`; BOT Spec §6.6.1 |
| Clear-Halt beendet NEED_RESET | `REJECTED` | TinyUSB stallt weiter bis BOT Reset (`EVID-USBCTRL-2026-10-14-004`) |
| SET_ADDRESS = Klassen-EPs aktiv / mounted | `REJECTED` | Mount erst bei SET_CONFIGURATION n (`EVID-USBCTRL-…-001`) |
| Unplug feuert immer `tud_umount_cb` auf ESP | `REJECTED` | ohne VBUS-Sense oft nein (`EVID-USBCTRL-…-007`/`008`) |
| USB↔WiFi-Issue = Root-Cause jeder Sonde | `REJECTED` | nur Chip-/Modus-`HYPOTHESIS` (`EVID-USBCTRL-…-009`) |
| Host-eBPF-Decode = physische Paketebene | `REJECTED` | URB-/Class-Ebene; DATA0/1 out-of-scope |

## Transfer

Wiederverwendbar für MCU-als-Stick, Diagnose-Gadgets, virtuelle Medien. **Host-Timing nie hier.**  
Perf-Baseline und Callback-Hooks: Desk [`esp32-msc-gadget-refs-2026-foreign`](../../audits/esp32-msc-gadget-refs-2026-foreign/).  
Busy/Async-Vertrag: [`tinyusb-msc-busy-retry-2026`](../../audits/tinyusb-msc-busy-retry-2026/).  
BOT-Hooks/Schema: [`usb-bot-observation-2026-instrument-sources`](../../audits/usb-bot-observation-2026-instrument-sources/).  
Control/Enum/STALL: [`usb-control-stall-recovery-2026`](../../audits/usb-control-stall-recovery-2026/).  
Instrumentierung: [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) · [`msc-busy-retry-semantics`](../../methods/msc-busy-retry-semantics.md) · [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md).

### Projektstart-Checkliste

- [ ] BOT+SCSI vs. `virtual-fat` klar trennen
- [ ] Read-Callback Signatur + Multi-Sektor `bufsize` / `EP_BUFSIZE` geplant
- [ ] Busy-Strategie gewählt: Block vs. `return 0` vs. ASYNC (Port-Check!)
- [ ] Falls Command-Observation: Logger an CBW/CSW-Hooks, nicht nur an `onRead`
- [ ] Enum-Epochs: SET_ADDRESS ≠ Mount; SET_CONFIGURATION 0/n; ohne VBUS Mount-Clear
- [ ] NEED_RESET vs. Clear-Halt vs. BOT Reset getrennt
- [ ] Host-Prefetch/Timing → Host-Sheet / Application C
- [ ] Throughput vs. Latenz getrennt messen
- [ ] Application + `seen_in`

## Referenzen

- USB MSC BOT; SCSI SBC READ(10)
- TinyUSB `src/class/msc/msc.h` / `msc_device.h` / `.c`; Issue [#2035](https://github.com/hathach/tinyusb/issues/2035); PR [#2967](https://github.com/hathach/tinyusb/pull/2967)
- Espressif `tusb_msc`; Arduino `USBMSC.h`; Adafruit TinyUSB MSC; aoscarius/esp32usbmsc; atomic14/esp32-sdcard-msc
- Schema-Kontrast: edk2 `UsbMassBot.h`; Wireshark `packet-usbms-bot.c`
- PiDrive: [`esp32.pidrive`](https://github.com/MPunktBPunkt/esp32.pidrive)

## Offene Fragen (A)

- UASP vs. BOT für Zielhosts?
- Max Callback-/BUSY-Latenz vor typischem Host-Abort → Lab/C ([`msc-busy-retry-semantics`](../../methods/msc-busy-retry-semantics.md)); NBT Busy-Pacing belegt nur als **C** (`EVID-BMWHU-2026-10-12-*`); Host-ms nie als A-FACT
- ESP32-S3/DWC2: Partial-Read Endpoint-Verhalten vs. RP2040?

## Lessons

- Sheet bleibt ohne HU-Timing.
- Callback-Zelle + USB-FS-Budget sind die transferierbaren A-Erweiterungen aus dem Gadget-Referenz-Audit.
- Busy/return-0 ist etabliert, aber **kein** kooperatives Yield ohne RTOS/ASYNC — Stall-FW muss den Port-Vertrag kennen.
- Echte `bot_cbw`/`bot_csw`-Events gehören in den Class Driver; App-Callbacks und Host-eBPF sind Ergänzung bzw. Lab-Validate, kein Ersatz füreinander.
- Enumeration-/Stall-Epochs sitzen in `usbd.c` + MSC-Control; Clear-Halt ≠ NEED_RESET-Heilung; ohne VBUS-Sense ist der Mount-Hook die zuverlässige Replug-Grenze.
