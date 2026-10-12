# Evidence — esp32-msc-gadget-refs-2026-foreign

Desk 2026-10-12 · **standard_version 0.6.6** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/espressif/esp-idf (tusb_msc) | `86f72d0` |
| https://github.com/aoscarius/esp32usbmsc | `67ffb6b` |
| https://github.com/atomic14/esp32-sdcard-msc | `5e7c5a7` |
| https://github.com/espressif/arduino-esp32 | `0862e23` |
| https://github.com/adafruit/Adafruit_TinyUSB_Arduino | `1b73172` |
| https://github.com/chegewara/EspTinyUSB | `f4d6315` |
| https://github.com/chegewara/esp32-usb-v2 | `4b4232c` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-MSCREF-2026-10-12-001` | onRead/msc_read_cb/tud path exposes LBA hooks | `FACT` | USBMSC.h, Adafruit examples, aoscarius main |
| `EVID-MSCREF-2026-10-12-002` | IDF: app vs USB host exclusive storage mount | `FACT` | tusb_msc README scenarios |
| `EVID-MSCREF-2026-10-12-003` | USBMSC read ~0.5–1.0 MB/s depending on SPI/SDIO/API | `INFERRED` | atomic14 README tables |
| `EVID-MSCREF-2026-10-12-004` | Multi-sector IDF path faster than Arduino single-sector | `INFERRED` | atomic14 |
| `EVID-MSCREF-2026-10-12-005` | Lazy background write: speed up, no error handling | `FACT` | atomic14 README |
| `EVID-VFAT-2026-10-12-001` | FAT12/16 PSRAM disk + onRead memcpy template | `FACT` | esp32usbmsc |
| `EVID-VFAT-2026-10-12-002` | clusters&lt;4085 → FAT12 | `FACT` | FAT-FAQ.md |
| `EVID-VFAT-2026-10-12-003` | Volume label in FAT.begin | `FACT` | main.cpp |
| `EVID-VFAT-2026-10-12-004` | 1 MiB full-image demo limit | `FACT` | DISK_SIZE_BYTES |
| `EVID-MSCREF-2026-10-12-006` | Dual LUN SPI-Flash + SDMMC optional | `FACT` | tusb_msc |
| `EVID-MSCREF-GAP-2026-10-12` | No public live-MP3→automotive-HU MSC repo found | `FACT` (search gap) | Desk research note |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Callback max latency before NBT abort | `UNKNOWN` | Method FOLLOW-ON |
| ESP32-C3 as MSC device like S3 | `UNKNOWN` | Gate |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-12 | Deep foreign desk; virtual-fat + LBA methods |
