# Technology Sheet: PUMP Control Link

```yaml
slug: pump-control-link
title: PUMP Control Link
primary: C
tags: [uart, streaming, usb-device]
type: protocol
status: active
seen_in: [esp32-pidrive]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/esp32-pidrive-2026-pilot
```

Nur Ebene **A**. PiDrive-/ESP-Pfade → Application [`pump-control-link`](../../projects/esp32-pidrive/applications/pump-control-link.md).

## Kurzfassung

**PUMP** ist ein schlanker Control-/Media-Link zwischen einem „Gehirn“-Host (Menü, Encode) und einem USB-Medien-Gadget: **Line-JSON** für Session/Menü/Play plus optionale **Binärframes** für Audio/Metadaten. Transport ist austauschbar (UART/CDC oder TCP) bei gleichem Framing.

## Abgrenzung

- **Ist:** Framing, Ops (`hello`/`menu_set`/`play_uid`/`audio_*`), Soft-Paging-Idee (wenige sichtbare Slots).
- **Ist nicht:** USB-MSC/FAT selbst (→ `usb-msc`); Hub-Register (→ `esp-hub-telemetry`); Host-Prefetch der Headunit (→ Host-Sheet); Infotainment-Quellenwahl auf dem Pi.
- **Grenzt an:** PDAP (andere Media/Control-Semantik über WiFi); generisches MQTT/SSE.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Host → Gadget | Line-JSON | u. a. `hello`, `menu_set`, `audio_start`/`stop`, `ping` |
| Gadget → Host | Line-JSON Events | u. a. `play_uid`, Diag, gebatchte Read-Timelines |
| optional | Binary nach Magic | Audio- und sticky-ID3/Cover-Frames |
| lateral | MSC-Gadget | Slots/Menünamen; Play-Guess triggert Control-Events |

## Typische Fallstricke (A)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Control-Link = MSC-Stream | `REJECTED` | MSC liefert Blöcke; Audio kommt aus Overlay/Puffer nach Control-Pfad |
| Ein Transport (nur UART) ist Teil der Spec | `REJECTED` | Framing transportneutral halten |
| Unbegrenzte Menütiefe muss 1:1 auf Stick-Slots | `REJECTED` | Soft-Paging / Seiten am Bridge-Ende ist üblich |
| play_uid bei Down-Link darf verworfen werden | `HYPOTHESIS` | Replay nach Re-Hello oft nötig |
| Binary und JSON dürfen sich im Stream mischen ohne State-Machine | `REJECTED` | Byte-Framer nötig |

## Transfer

Überall, wo ein Host-Menü ein USB-Stick-Gadget steuert und optional Live-Bytes nachschiebt (Auto-Infotainment, Lab-Medienquellen). Host-spezifische Decode-Quirks nicht hierher.

### Projektstart-Checkliste

- [ ] Transport(e) und Baud/Port dokumentieren — Framing gleich halten
- [ ] Ops-Tabelle (`hello`/`menu_set`/`play_uid`/…) in Application
- [ ] Soft-Paging vs. physische Slot-Anzahl klären
- [ ] Binary-Kinds und Max-Größen (Cover/ID3) begrenzen
- [ ] Application + `seen_in`

## Referenzen

- Firmware/Doku: [`esp32.pidrive` PUMP.md](https://github.com/MPunktBPunkt/esp32.pidrive/blob/main/docs/planung/PUMP.md)
- Bridge: `tools/pump_bridge.py` im selben Repo

## Offene Fragen (A)

- Wie weit sich PUMP von produkt-spezifischen UIDs (`pump:page_*`) lösen lässt.
- Ob ein zweites Sheet für „virtuelles Soft-Paging“ nötig wird (eher Application).
