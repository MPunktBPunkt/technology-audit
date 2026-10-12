# Project Scope: esp32-msc-gadget-refs (Fremd)

```yaml
project_id: esp32-msc-gadget-refs
title: ESP32 USB-MSC Gadget References — Callback / Virtual FAT / Perf (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "aoscarius@67ffb6b atomic14@5e7c5a7 idf@86f72d0 arduino-esp32@0862e23 adafruit@1b73172 EspTinyUSB@f4d6315 esp32-usb-v2@4b4232c"
repos:
  - https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/device/tusb_msc
  - https://github.com/aoscarius/esp32usbmsc
  - https://github.com/atomic14/esp32-sdcard-msc
  - https://github.com/espressif/arduino-esp32
  - https://github.com/adafruit/Adafruit_TinyUSB_Arduino
  - https://github.com/chegewara/EspTinyUSB
  - https://github.com/chegewara/esp32-usb-v2
status: active
```

## Zweck

Tiefe Referenz-Aufnahme für PiDrive-Nische: **Read-Callback = on-the-fly LBA-Content**, virtuelles FAT12/16, USB-Full-Speed-Throughput-Grenzen, alternative TinyUSB-Stacks — klar getrennt von BMW-Host-C.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| IDF `tusb_msc` | Official SPI-Flash/SD LUN baseline | ja |
| aoscarius/esp32usbmsc | Virtual FAT12/16 in PSRAM + onRead/onWrite | ja (Kernvorlage) |
| atomic14/esp32-sdcard-msc | Measured USBMSC↔SD throughput | ja (Perf) |
| Arduino-ESP32 `USBMSC` | Callback-API | ja |
| Adafruit TinyUSB MSC examples | msc_read_cb / ramdisk / external flash | ja |
| EspTinyUSB / esp32-usb-v2 | Alternative MSC stacks + ramdisk | ja |
| BMW NBT Evo Feld | — | **nein** (→ `bmw-nbt-evo` / pidrive) |
| Fertiges Live-MP3-HU-Produkt | öffentlich nicht gefunden | **observed gap** |

## Nicht-Ziele

- Host-Timing-Claims als MSC-Spec
- atomic14-Zahlen als on-the-fly-CPU-Budget ohne Remessung
- C3 als OTG-MSC ohne Gate

## Prioritäten

1. Sheets `usb-msc` + neu `virtual-fat` wachsen  
2. Method `msc-lba-timing-instrument` (+ `msc-trace-correlation`)  
3. Perf-Baseline USB FS ≈ 0.5–1 MB/s Read (author MEASURED → INFERRED für KB)  
4. Transfer-Hinweise nach `esp32-pidrive` / `pidrive`
