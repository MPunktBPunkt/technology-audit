# Audit Campaign: tinyusb-msc-busy-retry-2026

```yaml
id: tinyusb-msc-busy-retry-2026
project_id: esp32-pidrive
started: 2026-10-12
ended: 2026-10-12
status: closed
profile: lab-tool
standard_version: "0.6.6"
reuse_outcomes:
  reused: [usb-msc, esp32-msc-gadget-refs, msc-lba-timing-instrument]
  new: [msc-busy-retry-semantics]
  not_helped: []
  process: "Desk TinyUSB MSC return-0 / BUSY / ASYNC semantics for E7; no NBT host FACTS"
```

## Ziel

Exakte Semantik von `tud_msc_read10_cb` / Arduino `onRead` bei **return 0** / `TUD_MSC_RET_BUSY`, Partial-Read, ERROR und ASYNC — inklusive Retry-Mechanismus, `tud_task`-Blockade (Issue #2035) und Arduino-ESP32-/TinyUSB-0.15-Port — als technische Basis für E7 (Busy-Retry / Stall-FW).

## Scope

- **Im Scope:** TinyUSB Device MSC Upstream (`msc_device.h`/`.c`), Issue #2035, PR #2967 (ASYNC), Arduino-ESP32 `USBMSC`→Callback-Mapping, gebündelter TinyUSB 0.15 auf ESP32-S3, `CFG_TUD_MSC_EP_BUFSIZE`, PiDrive `onReadLiveStall` nur als **B**-Vertragsnotiz.
- **Nicht im Scope:** BMW NBT Host-Timeouts als FACT; allgemeines USB-MSC-/Virtual-FAT-Audit; neues Gadget-Repo; Autocommit „E7 PASS“.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | `standard_version` 0.6.6 | erfüllt |
| 2 | Kernfragen A1–A8 aus Upstream belegt oder `UNKNOWN` | erfüllt |
| 3 | Kernfragen B9–B11 Arduino/PiDrive belegt | erfüllt |
| 4 | Sheet `usb-msc` A-Delta Busy/Async (kein NBT-C) | erfüllt |
| 5 | Method `msc-busy-retry-semantics` | erfüllt |
| 6 | Evidence-Register mit IDs | erfüllt |
| 7 | Follow-on Audit-2 / NBT nur skizziert | erfüllt |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Busy-/Retry-Semantik (neu) | [`methods/msc-busy-retry-semantics.md`](../../methods/msc-busy-retry-semantics.md) |
| LBA-/Timing-Instrument (Follow-on Lab) | [`methods/msc-lba-timing-instrument.md`](../../methods/msc-lba-timing-instrument.md) |

## Bezug Inventar / Sheets

- Sheet: [`technologies/usb-msc/SHEET.md`](../../technologies/usb-msc/SHEET.md)
- Application B: [`projects/esp32-pidrive/applications/usb-msc.md`](../../projects/esp32-pidrive/applications/usb-msc.md)
- Gadget-Refs (Reuse, nicht wiederholt): [`esp32-msc-gadget-refs-2026-foreign`](../esp32-msc-gadget-refs-2026-foreign/)
- Host-C bleibt: [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/) · [`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md)

## Ergebnisse

- [evidence.md](evidence.md) — Evidence-IDs `EVID-TINYUSB-MSC-2026-10-12-*`
- Sheet-Wachstum: Busy / return-0 / ASYNC / EP_BUFSIZE / Fallstricke
- Method: Busy vs. block vs. ASYNC testen
- Application: PiDrive-Vertrag `return 0` + `vTaskDelay` (B)

## Lessons → Transfer

- **`return 0` = BUSY** ist kanonisch (Header + `proc_read10`): Fake-`dcd_event_xfer_complete`, **derselbe READ10/CBW bleibt offen**, CSW erst nach Daten/ERROR.
- **BUSY ≠ „Main-Loop läuft weiter“** ohne RTOS: Issue #2035 — `tud_task()` spinnt Events; Fix-Pfad Upstream ist **ASYNC** (#2967), nicht „BUSY yieldet von selbst“.
- Arduino-ESP32 (TinyUSB **0.15**, PiDrive-Stack): **kein** `TUD_MSC_RET_ASYNC` / `tud_msc_async_io_done` — nur Busy/Partial/Error; `onRead`-Return **1:1**.
- `CFG_TUD_MSC_BUFSIZE` / EP-Buffer auf Arduino-S3-SDK: **4096** — erklärt beobachtetes 4-KiB-Callback-Raster.
- Device-seitig **kein** BUSY-Timeout in TinyUSB; Abbruch = Host (C / Lab).
- Partial-Read ist spezifiziert; RP2040-Endpoint-Panic bei `bufsize-1` ist Port-spezifisch — ESP32-DWC2-Verhalten dazu `UNKNOWN`.

## Follow-on (nicht vermischen)

1. **Audit-2-Kandidat:** SCSI READ10 Transfergröße × Zeitbudget — Lab mit [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) + Busy-Method; Desk-Literatur allein reicht nicht.
2. **NBT / K3:** Timing-Toleranz bleibt C in [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/) — hier nur Verweis.
3. Optional: ESP-IDF/`esp_tinyusb` Async-Port (Upstream-PR-Linie #2967 / IDF-Folge) vs. Arduino-0.15 vergleichen, falls Stall-FW ASYNC braucht.

## Offene Punkte nach Abschluss

- Host-Abort-Schwelle unter BUSY/Delay-Rastern → Lab + C
- Ob ESP32-S3/DWC2 Partial-Read-Races wie RP2040 hat → `UNKNOWN`
- Ob/wann Arduino-ESP32 TinyUSB mit ASYNC nachzieht → Tracking

## Kernantworten (Kurz)

| # | Frage | Status | Kurz |
|---|-------|--------|------|
| A1 | `return 0` = BUSY? | `FACT` | Ja; Enum `TUD_MSC_RET_BUSY = 0` (Upstream); 0.15-Header: „not ready yet“ |
| A2 | Erneuter Callback gleiche Params? | `FACT` | Ja, nach Fake-Xfer-Complete |
| A3 | READ10/CBW bleibt offen? | `FACT` | Ja, DATA-Stage bis `xferred_len`/`ERROR` |
| A4 | `tud_task` blockiert bei BUSY? | `FACT` | Ja ohne Yield/RTOS (#2035); mit FreeRTOS nur Preemption/Delay im Callback hilft |
| A5 | Block vs. 0 vs. ASYNC | `FACT` | Block hält `tud_task` in Callback; 0 re-queued; ASYNC + `tud_msc_async_io_done` (Upstream ≥ #2967) |
| A6 | Partial return | `FACT` | Rest-Callback; Endpoint-Risiko Port-abhängig (RP2040 belegt) |
| A7 | `CFG_TUD_MSC_EP_BUFSIZE` | `FACT` | Cap pro Callback; Arduino-S3 SDK 4096 |
| A8 | Device-Timeout BUSY? | `FACT` | Keiner im MSC-Driver; Sense/CSW nur bei ERROR |
| B9 | Arduino `onRead` → TinyUSB | `FACT` | 1:1 Return-Wert |
| B10 | ESP-Port weicht ab? | `INFERRED` | 0.15-Pfad = klassisches Busy; kein ASYNC in `libarduino_tinyusb.a` |
| B11 | PiDrive-Vertrag | `FACT` (B) | `onReadLiveStall`: `vTaskDelay` + `return 0`; nie `<0` |
