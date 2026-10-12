# Project Application: virtual-fat in esp32-msc-gadget-refs

```yaml
project_id: esp32-msc-gadget-refs
tech_slug: virtual-fat
status: active
sheet: ../../../technologies/virtual-fat/SHEET.md
audit: ../../../audits/esp32-msc-gadget-refs-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

aoscarius liefert die klarste **FAT12/16-in-PSRAM**-Vorlage inkl. Volume Label `ESP32MSC`, 512 B Sektoren, 1 MiB Demo-Disk und `onRead`→`memcpy` aus Image. Adafruit/EspTinyUSB RAM-Disks sind schlankere Callback-Beispiele ohne volle FAT-Library.

## Architektur

```text
FAT.begin(disk, sectors, 512, "LABEL", root_entries)
  → BPB + FAT + Root synthetisch
  → Host enumerates files
  → onRead(lba…) returns directory OR file body sectors
```

Für PiDrive Live-Stream: Directory/FAT aus Geometrie **statisch/prefill**; File-Body-LBAs im Callback aus Stream statt aus `msc_disk[]`.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp32usbmsc/src/FAT12.cpp`, `FAT16.cpp`, `FAT-FAQ.md` | Geometry rules |
| `esp32usbmsc/src/main.cpp` | onRead/onWrite + PSRAM alloc |
| Adafruit `msc_ramdisk*.ino` | Minimal callback disk |
| esp32-usb-v2 `usb_ramdisk.cpp` | Lambda onRead/onWrite |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| FAT12/16 PSRAM virtual disk + onRead template | `EVID-VFAT-2026-10-12-001` | `FACT` |
| Cluster&lt;4085 → FAT12 rule documented | `EVID-VFAT-2026-10-12-002` | `FACT` |
| Volume label set at FAT.begin | `EVID-VFAT-2026-10-12-003` | `FACT` |
| Full 1 MiB image ≠ scalable live library | `EVID-VFAT-2026-10-12-004` | `FACT` (design limit) |
| README C3 native USB MSC | `UNKNOWN` / Gate | chip OTG |

## Abweichungen vs PiDrive

- aoscarius speichert **ganzes** Image in PSRAM; PiDrive braucht Slot-Geometrie + Live-Body.
- Write-Protect-when-plugged Pattern nützlich gegen Host/MCU-Kollision (ähnlich IDF mount exclusivity).
