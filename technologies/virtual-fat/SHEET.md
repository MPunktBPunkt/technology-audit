# Technology Sheet: Virtual FAT Disk (Synthetic Geometry)

```yaml
slug: virtual-fat
title: Virtual FAT Disk (Synthetic Geometry)
primary: E
tags: [usb-device, filesystem, lab-only, fragile]
type: implementation
status: active
seen_in: [esp32-msc-gadget-refs, pidrive, esp32-pidrive]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/esp32-msc-gadget-refs-2026-foreign
```

Nur Ebene **A**. Host-Prefetch/BMW → `bmw-nbt-evo` / Application C. MSC-Transport → `usb-msc`.

## Kurzfassung

Synthetisches **FAT12/FAT16**-Volume als Byte-/Sektor-Image (RAM, PSRAM oder on-the-fly), das einem USB-MSC-Host als Stick erscheint. Volume Label, BPB, FAT-Tabellen und Directory-Einträge sind Firmware-konstruiert; Dateiinhalte können aus einem Puffer kommen oder im **Read-Callback** pro LBA erzeugt werden.

## Abgrenzung

- **Ist:** FAT-Geometrie + synthetische Directory/File-Layout-Regeln für Gadgets.
- **Ist nicht:** USB-MSC/BOT/SCSI (`usb-msc`); echte SD/Flash-Dateisysteme als Persistenz; MP3-Decode; HU-Caching.
- **Grenzt an:** on-the-fly Body (Live-Stream in File-LBAs) = Application-Strategie auf gleichem Contract.

## Signalpfad-Kette

| Stufe | Claim | Status |
|-------|-------|--------|
| Sektorgröße typ. 512 B | Industry default für USB-Sticks | `FACT` |
| FAT12 wenn Cluster &lt; 4085; sonst FAT16 | Upstream FAT decision rule | `FACT` (aoscarius FAT-FAQ / Spec-Praxis) |
| Volume Label im Bootsektor / Root | Hosts cachen oft darüber | `FACT` als Mechanismus; HU-Wirkung = C |
| Root-Einträge / Cluster-Größe begrenzen Dateizahl | Layout-Wahl | `FACT` |
| On-the-fly File-Body ohne Full-Image | möglich über MSC Read-Callback | `FACT` (API); Stabilität = Host-C |

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Dateinamen, Slot-Map, Media-UIDs | Application |
| unten | LBA-Raum → MSC Read/Write Callbacks | `usb-msc` |
| lateral | Serial/VID/PID/Inquiry strings | Host-Cache-Trigger |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Virtuelles FAT = echtes Flash-Image nötig | `REJECTED` | Callback kann Sektoren live liefern |
| FAT32 immer „besser“ für Gadgets | `HYPOTHESIS` | Automotive-Hosts oft FAT32-freundlich — aber PiDrive Lab nutzt FAT12/16 bewusst; Gate pro Host |
| Volume Label ändern ist kosmetisch | `REJECTED` (für viele Hosts) | Re-Index/Cache oft an Label+Serial gekoppelt (**C** messen) |
| Unbegrenzte Dateizahl im Root | `REJECTED` | Root-Entries / Cluster-Limits |
| C3 „native USB MSC“ wie S2/S3 | `UNKNOWN` / Gate | OTG-Device-Caps chipweise prüfen |
| Full-PSRAM-Disk skaliert auf große MP3-Libs | `REJECTED` | 1 MiB-Demo ≠ Multi-MiB Live-Body; on-the-fly nötig |

### Projektstart-Checkliste

- [ ] FAT12 vs FAT16 vs FAT32 für Zielhost gewählt (Evidence)
- [ ] Sektor 512 B? Multi-Sektor-Bursts im Callback bedienen
- [ ] Volume Label + USB Serial bewusst versionieren (Cache)
- [ ] Full-Image vs. on-the-fly Body getrennt planen
- [ ] Application + `seen_in`; Host-Timing nicht hier

## Transfer

Primärvorlage für PiDrive-Slots und jedes „Fake-Stick“-Gadget. Referenz: aoscarius `onRead(lba,offset,buf,size)` + FAT.begin; Adafruit/EspTinyUSB RAM-Disk-Callbacks.

## Referenzen

- [aoscarius/esp32usbmsc](https://github.com/aoscarius/esp32usbmsc) (+ `FAT-FAQ.md`)
- Arduino-ESP32 `USBMSC.h` Callback-API
- Microsoft/Spec FAT docs; USB MSC BOT

## Offene Fragen

- Welche FAT32-Minimalgeometrie NBT Evo akzeptiert vs. Lab FAT16?
- Root-Entry vs. langer Dateiname — Index-Limits der HU?
