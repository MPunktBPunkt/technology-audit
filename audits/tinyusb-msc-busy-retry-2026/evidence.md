# Evidence — tinyusb-msc-busy-retry-2026

Desk 2026-10-12 · **standard_version 0.6.6** · Profile `lab-tool`.

| Quelle | Ref |
|--------|-----|
| https://github.com/hathach/tinyusb `msc_device.h` / `msc_device.c` (master) | Upstream Busy/Async |
| https://github.com/hathach/tinyusb/issues/2035 | Slow data source / `tud_task` spin |
| https://github.com/hathach/tinyusb/pull/2967 (merge `0d6cb381`) | `TUD_MSC_RET_ASYNC` + `tud_msc_async_io_done` |
| Arduino-ESP32 package (PlatformIO) tinyusb `39a64334a` · `TUSB_VERSION` **0.15.0** | PiDrive-Stack |
| `cores/esp32/USBMSC.cpp` (framework-arduinoespressif32) | `onRead` → `tud_msc_read10_cb` |
| `sdkconfig` ESP32-S3: `CONFIG_TINYUSB_MSC_BUFSIZE=4096` | EP buffer |
| https://github.com/pekkanikander/pico-tinyusb-msc-panic | Partial-Read / RP2040 panic |
| `esp32.pidrive` `src/msc/UsbMscGadget.cpp` `onReadLiveStall` | B-Vertrag |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-TINYUSB-MSC-2026-10-12-001` | `return 0` / `TUD_MSC_RET_BUSY`: App noch nicht fertig; Callback später mit gleichen Parametern | `FACT` | Upstream `msc_device.h` Enum + Kommentar; 0.15-Header „read == 0 … not ready yet“ |
| `EVID-TINYUSB-MSC-2026-10-12-002` | BUSY → Fake `dcd_event_xfer_complete(..., 0, …)`; kein Fortschritt von `xferred_len`; CBW/DATA-Stage bleibt | `FACT` | `proc_read10_cmd` / `proc_read_io_data` (Upstream + IDF-Beispiel / 0.15-Ära) |
| `EVID-TINYUSB-MSC-2026-10-12-003` | Reines `return 0` ohne Yield: `tud_task()` gibt CPU nicht zurück (Event-Selbst-Queue) | `FACT` | Issue #2035 + Maintainer-Bestätigung |
| `EVID-TINYUSB-MSC-2026-10-12-004` | Upstream-Fix-Pfad für langsame Quelle: `TUD_MSC_RET_ASYNC` + `tud_msc_async_io_done`; in `async_io_done` wird `bytes_io==0` als ERROR behandelt | `FACT` | PR #2967 / aktuelles `msc_device.h`/`.c` |
| `EVID-TINYUSB-MSC-2026-10-12-005` | `0 < ret < bufsize`: Bytes zuerst transferiert, Callback für Rest; `ret < 0`: STALL + CSW failed + Sense | `FACT` | Header-Kommentar + `fail_scsi_op` / ERROR-Zweig |
| `EVID-TINYUSB-MSC-2026-10-12-006` | Kein Device-seitiger Timeout für BUSY-Loops im MSC-Class-Driver | `FACT` | Code-Review: nur Host kann abbrechen/resetten |
| `EVID-TINYUSB-MSC-2026-10-12-007` | Callback-Chunk ≤ `CFG_TUD_MSC_EP_BUFSIZE`; Arduino-ESP32-S3 SDK = **4096** | `FACT` | `tusb_config.h` / `sdkconfig` `CONFIG_TINYUSB_MSC_BUFSIZE` |
| `EVID-TINYUSB-MSC-2026-10-12-008` | Arduino `USBMSC::onRead` Return-Wert 1:1 an `tud_msc_read10_cb`; gebündeltes TinyUSB **0.15** ohne `tud_msc_async_io_done`-Symbol | `FACT` | `USBMSC.cpp`; `nm libarduino_tinyusb.a`; `tusb_option.h` VERSION |
| `EVID-TINYUSB-MSC-2026-10-12-009` | Partial `bufsize-1` kann auf RP2040 Endpoint-Double-Arming/Panic auslösen | `FACT` (Port RP2040) | pico-tinyusb-msc-panic README · TinyUSB #3188 |
| `EVID-TINYUSB-MSC-2026-10-12-010` | PiDrive Stall-Pfad: bei unzureichendem `liveAvail` → `vTaskDelay(retryMs)` + `return 0`; nie `<0` | `FACT` (B) | `UsbMscGadget::onReadLiveStall` |

## Engineering Review Checks (aus Evidence)

| Evidence-ID | Review Check | n/a? |
|-------------|--------------|------|
| `EVID-TINYUSB-MSC-2026-10-12-001`/`002` | Re-Entry: kein Reset nur wegen `offset==0`; Timer nur bei neuem Request; Busy-Pfad zustandsstabil | — |
| `EVID-TINYUSB-MSC-2026-10-12-003` | Hybrid Yield (`vTaskDelay`) vs. reines Busy | — |
| `EVID-TINYUSB-MSC-2026-10-12-004`–`009` | ASYNC/Partial/Port — n/a für aktuellen Arduino-0.15-E7-Pfad außer Partial-Achtung | teilweise n/a |
| `EVID-TINYUSB-MSC-2026-10-12-010` | PiDrive-Vertrag: nie `return <0` im Stall-Pfad | — |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Max BUSY-/Callback-Latenz vor typischem Host-Abort (PC) | `UNKNOWN` | weiter Lab |
| NBT akzeptiert Busy-Pacing / langes Tonfenster | → C | siehe `EVID-BMWHU-2026-10-12-001`–`007` (nicht Desk-FACT hier) |
| ESP32-S3/DWC2: Partial-Read Endpoint-Race analog RP2040? | `UNKNOWN` | nicht belegt |
| Arduino-ESP32 erhält ASYNC-API | `UNKNOWN` | Tracking Upstream/IDF |
| Host sendet parallelen zweiten READ10 während offenem CBW | `UNKNOWN` | BOT typisch sequentiell; Abort/Reset = Host |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-12 | Desk Busy/Async; Sheet + Method; Kampagne closed |
| 2026-10-12 | Feld E7/S6 validiert Hypothese (C in bmw-hu); Retro Review Checks / Decision Trace (0.7.0) |
