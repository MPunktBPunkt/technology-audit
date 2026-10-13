# Audit Campaign: tinyusb-msc-busy-retry-2026

```yaml
id: tinyusb-msc-busy-retry-2026
project_id: esp32-pidrive
started: 2026-10-12
ended: 2026-10-12
status: closed
profile: lab-tool
standard_version: "0.6.6"
standard_gaps: ["0.7.0 Decision Trace / Review Checks / Kill / Feedback — retro nachgetragen"]
reuse_outcomes:
  reused: [usb-msc, esp32-msc-gadget-refs, msc-lba-timing-instrument]
  new: [msc-busy-retry-semantics]
  not_helped: []
  process: "Desk TinyUSB MSC return-0 / BUSY / ASYNC for E7; Field S6 NBT validated same day (C → pidrive-2026-bmw-hu)"
  decisions_touched: [E7-go, field-go-S6]
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

## Decision Trace (retro 0.7.0)

Desk-Scope dieser Kampagne bleibt ohne NBT-FACTS; Trace dokumentiert, welche Desk-Evidence die späteren Go-Entscheidungen trug.

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz |
|--------------|-----------------|-------------|------------|
| E7 durchführen | Kann TinyUSB BUSY halten (`return 0`)? | `EVID-TINYUSB-MSC-2026-10-12-001` | Ja |
| E7 durchführen | Bleibt READ10/CBW offen? | `EVID-TINYUSB-MSC-2026-10-12-002` | Ja |
| E7 durchführen | Erneuter Callback gleiche Params? | `EVID-TINYUSB-MSC-2026-10-12-001`/`002` | Ja → Review Checks nötig |
| E7 durchführen | Device-Timeout gegen Busy? | `EVID-TINYUSB-MSC-2026-10-12-006` | Nein (Device); Host = UNKNOWN → Lab/Feld |
| Feld-Go S6? | NBT akzeptiert Busy-Pacing? | `EVID-BMWHU-2026-10-12-001` | Ja (Field, nicht dieses Desk-Audit) |
| Feld-Go S6? | Ton über bisheriges Fenster? | `EVID-BMWHU-2026-10-12-002`/`003` | Ja (~65 s vs. ~6 s Stall-off) |

## Engineering Review Checks (retro — Lesson 0.4.47→0.4.48)

Aus Re-Entry-Semantik abgeleitet; hätte den `stallCmdT0_`-Fehler vor dem Lab abfangen können.

| Evidence-ID | Review Check |
|-------------|--------------|
| `EVID-TINYUSB-MSC-2026-10-12-001` | Kein State-Reset ausschließlich wegen `offset == 0` (Re-Entry ≠ neuer Request) |
| `EVID-TINYUSB-MSC-2026-10-12-001`/`002` | Timerstart (`stallCmdT0_` u. Ä.) nur beim Eintritt in einen **neuen** READ10/Request, nicht bei jedem Callback |
| `EVID-TINYUSB-MSC-2026-10-12-001`/`002` | Re-Entry mit identischem `(LBA, offset)` muss idempotent / zustandsstabil sein |
| `EVID-TINYUSB-MSC-2026-10-12-001`/`010` | Busy-Pfad darf Producer-/Live-State nicht unbeabsichtigt zurücksetzen |
| `EVID-TINYUSB-MSC-2026-10-12-003` | Reines `return 0` ohne Yield: `tud_task`-Spin — Hybrid braucht `vTaskDelay` oder gleichwertig |

## Kill-Kriterien (präregistriert für E7/S6 — Referenz)

**Hypothese:** Busy-Pacing ermöglicht dem NBT, ein langes READ10 ohne Abbruch weiterzuführen und über das bisherige ~6‑s-Tonfenster hinaus zu spielen.

| # | Kill / Widerlegt wenn | Status (nach Feld) |
|---|----------------------|-------------------|
| 1 | NBT beendet READ10 trotz korrektem BUSY-Pacing | nicht eingetreten |
| 2 | Kein wiederholter Callback bei BUSY | nicht eingetreten |
| 3 | Host-Timeout vor nutzbarem Tonfenster | nicht eingetreten (bei Stall-Defaults) |
| 4 | Ton trotz kontinuierlicher Reads nicht über bisheriges Fenster | widerlegt durch ~65 s (`EVID-BMWHU-2026-10-12-002`) |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Busy-/Retry-Semantik (neu) | [`methods/msc-busy-retry-semantics.md`](../../methods/msc-busy-retry-semantics.md) |
| Re-Entry State Lifetime (generischer Review Check) | [`methods/callback-reentry-state-lifetime.md`](../../methods/callback-reentry-state-lifetime.md) |
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

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Desk (diese Kampagne) | `EVID-TINYUSB-MSC-2026-10-12-*` | Sheet `usb-msc` · Method · Application B |
| Feld E7/S6 NBT 2026-10-12 | `EVID-BMWHU-2026-10-12-001`–`007` | [`pidrive-2026-bmw-hu/evidence`](../pidrive-2026-bmw-hu/evidence.md) · [`bmw-nbt-evo`](../../projects/pidrive/applications/bmw-nbt-evo.md) · [`esp32-pidrive` usb-msc](../../projects/esp32-pidrive/applications/usb-msc.md) |

## Lessons → Transfer

- **`return 0` = BUSY** ist kanonisch (Header + `proc_read10`): Fake-`dcd_event_xfer_complete`, **derselbe READ10/CBW bleibt offen**, CSW erst nach Daten/ERROR.
- **BUSY ≠ „Main-Loop läuft weiter“** ohne RTOS: Issue #2035 — `tud_task()` spinnt Events; Fix-Pfad Upstream ist **ASYNC** (#2967), nicht „BUSY yieldet von selbst“.
- Arduino-ESP32 (TinyUSB **0.15**, PiDrive-Stack): **kein** `TUD_MSC_RET_ASYNC` / `tud_msc_async_io_done` — nur Busy/Partial/Error; `onRead`-Return **1:1**.
- `CFG_TUD_MSC_BUFSIZE` / EP-Buffer auf Arduino-S3-SDK: **4096** — erklärt beobachtetes 4-KiB-Callback-Raster.
- Device-seitig **kein** BUSY-Timeout in TinyUSB; Abbruch = Host (C / Lab).
- Partial-Read ist spezifiziert; RP2040-Endpoint-Panic bei `bufsize-1` ist Port-spezifisch — ESP32-DWC2-Verhalten dazu `UNKNOWN`.
- **Operationalisierung:** Re-Entry-Evidence war da, fehlte aber als verbindliche Review-Checkliste → Umweg `0.4.47→0.4.48` (`stallCmdT0_`). Ab 0.7.0: Evidence → Engineering Review Checks vor Lab.
- **Feld-Validierung:** Desk hat den Suchraum verkleinert; Beweis blieb bei Lab/Feld (~65 s vs. ~6 s). PSRAM/Ring nicht mehr Default gegen kurzes Tonfenster.

## Follow-on (nicht vermischen)

1. **Audit-2-Kandidat:** SCSI READ10 Transfergröße × Zeitbudget — Lab mit [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) + Busy-Method; Desk-Literatur allein reicht nicht.
2. **NBT C:** Host-Facts leben in [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/) (`EVID-BMWHU-2026-10-12-*`) — hier nur Verweis.
3. Optional: ESP-IDF/`esp_tinyusb` Async-Port (Upstream-PR-Linie #2967 / IDF-Folge) vs. Arduino-0.15 vergleichen, falls Stall-FW ASYNC braucht (nach Feld unwahrscheinlicher Default).

## Offene Punkte nach Abschluss

- Host-Abort-Schwelle jenseits Stall-Defaults → weiter Lab + C
- Ob ESP32-S3/DWC2 Partial-Read-Races wie RP2040 hat → `UNKNOWN`
- Ob/wann Arduino-ESP32 TinyUSB mit ASYNC nachzieht → Tracking
- Upstream-Artefakt-Links für BMWHU-2026-10-12 nachziehen

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
