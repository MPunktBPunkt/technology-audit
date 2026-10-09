# Technology Sheet: USB Mass Storage Class

```yaml
slug: usb-msc
title: USB Mass Storage Class
primary: C
tags: [usb-device, automotive, streaming]
type: protocol
status: active
seen_in: [projects/pidrive]
maturity:
  technology: R4
  implementation: R0   # siehe Project Application
  field_evidence: R0   # Host-spezifisch → Application / bmw-nbt-evo
  reusability: W2
pilot: audits/pidrive-2026-msc
```

Ebene **A** (allgemein). PiDrive-Implementierung → [`applications/usb-msc.md`](../../projects/pidrive/applications/usb-msc.md). BMW-Host-Verhalten → [`applications/bmw-nbt-evo.md`](../../projects/pidrive/applications/bmw-nbt-evo.md) + Sheet [`bmw-nbt-evo`](../bmw-nbt-evo/SHEET.md).

## Kurzfassung

USB Mass Storage Class (MSC) lässt ein USB-Device einem Host als blockorientiertes Speichermedium erscheinen. Typischer Transport ist **Bulk-Only Transport (BOT)**; die Kommandosprache ist in der Praxis **SCSI** (inkl. READ(10)/WRITE(10)). Dateisysteme (FAT, …) und LBA-Geometrie sitzen darüber — sie sind nicht „MSC selbst“.

## Abgrenzung

- **Ist:** Geräteklasse + Protokollstapel Device ↔ Host für Block-I/O.
- **Ist nicht:** FAT, MP3, Streaming-Semantik, Headunit-UI, PiDrive-Menülogik.
- **Grenzt an:** SCSI (Kommandos), BOT (USB-Transport), UASP (andere Transportvariante, hier nicht Fokus), Dateisysteme (Ebene darüber).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Host | USB Host Controller + MSC-Treiber | initiiert CBW/CSW, liest/schreibt LBAs |
| Transport | USB Bulk-Only (BOT) | CBW → Daten → CSW |
| Kommandos | SCSI Transparent Subclass | READ/WRITE/INQUIRY/… |
| Darüber | Dateisystem / App | interpretiert Sektorinhalte |
| Darunter | USB Device Controller | Endpoints, DMA, Puffer |

## Typische Fallstricke (A)

| Claim | Status | Hinweis |
|-------|--------|---------|
| MSC „streamt Audio“ | `REJECTED` | MSC liefert nur Blöcke; Streaming ist Application + Dateisystem + Host-Decoder |
| Ein READ-Muster gilt für alle Hosts | `REJECTED` | Host-Caching/Prefetch ist geräteabhängig (**C**, nicht A) |
| BOT + SCSI Transparent ist der übliche Stick-Pfad | `FACT` | Consumer-USB-Sticks |
| LBA-Adressierung ist linear über die exportierte Kapazität | `FACT` | Geometrie ist Geräte-/Firmware-Wahl |

## Transfer

Wiederverwendbar überall, wo ein MCU/SoC einem USB-Host als Stick erscheinen soll (Diagnose-Gadgets, virtuelle Medien, Test-Targets). Host-spezifische Prefetch-/Timing-Profile **nicht** in dieses Sheet ziehen — eigenes Host-Sheet oder Application-C.

Folgeprojekt-Skizze: generisches ESP32-USB-MSC-Gadget / Host-Behavior-Toolkit (ohne BMW-Semantik).

### Projektstart-Checkliste

- [ ] BOT+SCSI vs. Dateisystem/FAT klar trennen (eigene Slugs wenn nötig)
- [ ] Host-Prefetch/Timing **nicht** als MSC-Spec behandeln → Host-Sheet / Application C
- [ ] Lab-/Feld-Evidence-IDs planen bevor Coverage `full`
- [ ] Application + `seen_in` nachziehen

## Referenzen

- USB Mass Storage Class specification (Bulk-Only Transport)
- SCSI Primary Commands / Block Commands (READ(10) etc.)
- PiDrive-Konzept (Architektur, nicht Spec): [`pidrive` KONZEPT-USB-MSC](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/planung/KONZEPT-USB-MSC.md)
- Firmware: [`esp32.pidrive`](https://github.com/MPunktBPunkt/esp32.pidrive)

## Offene Fragen (A)

- Wie weit UASP vs. BOT für Zielhosts relevant ist (für NBT Evo bisher BOT-Pfad).
- Ob ein zweites Sheet `scsi` / `fat` die Block- vs. FS-Themen entlasten soll (ja, sobald Applications sie brauchen).

## Lessons aus dem Pilot

- Sheet bleibt absichtlich schlank: alles HU-Spezifische würde die Wiederverwendbarkeit zerstören.
- Reife **Technology R4** bezieht sich auf Verständnis der Klasse im PiDrive-Kontext, nicht auf eine Zertifizierung.
