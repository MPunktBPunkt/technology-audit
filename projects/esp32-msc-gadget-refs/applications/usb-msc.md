# Project Application: usb-msc in esp32-msc-gadget-refs

```yaml
project_id: esp32-msc-gadget-refs
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/esp32-msc-gadget-refs-2026-foreign/
maturity:
  technology: R4
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

Vergleich mehrerer **Device-MSC**-Stacks und Backend-Strategien (Flash/SD/RAM/Callback), mit Fokus auf dem Hook, den PiDrive für Live-Content braucht: **Read-Callback pro LBA**.

## Architektur / Datenfluss

```text
USB Host READ(10)/BOT
  → TinyUSB / USBMSC / EspTinyUSB MSC
  → onRead(lba, offset, buf, bufsize)   [oder tud_msc_read10_cb]
  → SPI-Flash | SD multi-sector | PSRAM image | on-the-fly generator
```

## Relevante Pfade (Upstream)

| Repo @ commit | Pfad | Rolle |
|---------------|------|-------|
| espressif/esp-idf `@86f72d0` | `examples/.../tusb_msc/` | Official LUN SPI-Flash/SD, mount exclusivity |
| aoscarius/esp32usbmsc `@67ffb6b` | `src/main.cpp` `onRead`/`onWrite` | Virtual disk callbacks |
| atomic14/esp32-sdcard-msc `@5e7c5a7` | README perf tables | USBMSC↔SD speeds |
| arduino-esp32 `@0862e23` | `cores/esp32/USBMSC.h` | `msc_read_cb` API |
| Adafruit_TinyUSB `@1b73172` | `examples/MassStorage/msc_*` | `msc_read_cb(lba,buf,bufsize)` |
| EspTinyUSB `@f4d6315` / esp32-usb-v2 `@4b4232c` | `src/device/msc/*`, `usb_ramdisk.cpp` | Alt stack + RAM disk |

## Performance (Desk — author MEASURED → KB `INFERRED`)

| Pfad | Read (MB/s) | Hinweis |
|------|-------------|---------|
| USBMSC + Arduino single-sector SPI | ~0.51 | atomic14 |
| USBMSC + IDF multi-sector SPI | ~0.67 | atomic14 |
| USBMSC + IDF multi-sector SDIO | ~1.00 | atomic14 |
| USB 1.1 FS theoretical payload | ~1.2 | ceiling |
| 320 kbit/s MP3 need | ~0.04 | unkritisch vs. USB FS |

Engpass für Live-Gadgets: **Latenz/Burst**, nicht Average-Throughput.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Callback APIs expose lba+bufsize hooks | `EVID-MSCREF-2026-10-12-001` | `FACT` |
| App vs Host exclusive mount (IDF) | `EVID-MSCREF-2026-10-12-002` | `FACT` |
| USBMSC SD read up to ~1 MB/s FS | `EVID-MSCREF-2026-10-12-003` | `INFERRED` (atomic14 author) |
| Multi-sector beats single-sector API | `EVID-MSCREF-2026-10-12-004` | `INFERRED` |
| Lazy-write trades error handling | `EVID-MSCREF-2026-10-12-005` | `FACT` (README warning) |

## Transfer nach PiDrive

- Instrument `UsbMscGadget` Read-Pfad mit Method `msc-lba-timing-instrument`.
- Multi-Sektor-`bufsize` nicht als 512 annehmen.
- SD-Perf ≠ on-the-fly encode budget.
