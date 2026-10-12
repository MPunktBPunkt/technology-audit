# Method: MSC Busy-Retry / return-0 Semantics

```yaml
slug: msc-busy-retry-semantics
title: MSC Busy-Retry / return-0 Semantics
status: active
tags: [usb-device, tinyusb, lab-only]
```

## Zweck

Unterscheiden und messen, welche der drei Device-Strategien bei langsamer Read-Quelle greift — **blockierender Callback**, **`return 0` / BUSY**, oder **ASYNC** — und was der Host dabei sieht. Grundlage für Stall-/E7-Firmware, ohne Host-Timeouts als Spec zu behaupten.

## Voraussetzungen

- Stack-Kenntnis: TinyUSB Device MSC (`tud_msc_read10_cb`) bzw. Arduino `USBMSC::onRead`
- Wissen, ob der Port **ASYNC** unterstützt (`TUD_MSC_RET_ASYNC` / `tud_msc_async_io_done`) — Arduino-ESP32 TinyUSB 0.15: **nein**
- `CFG_TUD_MSC_EP_BUFSIZE` / `CONFIG_TINYUSB_MSC_BUFSIZE` bekannt (oft 512 oder 4096)
- Lab-Host (PC zuerst); Ziel-HU nur als **C**
- Optional FreeRTOS: andere Tasks beobachtbar (WiFi/Producer)

## Ablauf

1. **Vertrags-Baseline** — dokumentieren: Stack-Version, EP_BUFSIZE, ob ASYNC verfügbar, Callback-Signatur.
2. **Modus A — Block** — im Callback fest `delay(N)` / busy-wait, dann volle `bufsize` liefern. Loggen: `t_enter`, `t_exit`, Host-Fehler.
3. **Modus B — return 0** — wenn Daten fehlen: `return 0` (ohne lange Blockade). Zählen: Retry-Häufigkeit, Zeit bis erste Bytes, ob Main-Loop/`loop()`/`other tasks` noch laufen.
4. **Modus B′ — Hybrid** (Arduino/FreeRTOS üblich) — kurzes `vTaskDelay` *im* Callback, dann `return 0`. Getrennt von reinem Busy und reinem Block dokumentieren.
5. **Modus C — ASYNC** (nur wenn Port ≥ Upstream #2967) — `return TUD_MSC_RET_ASYNC`, IO in Hintergrund-Task, `tud_msc_async_io_done(nbytes)` (nie `0` als „noch busy“ — wird ERROR).
6. **Partial** — bewusst `0 < n < bufsize` (idealerweise Vielfache von 512). Auf ESP32-S3: Disconnect/Stall loggen; RP2040-Panic nicht als ESP-FACT übernehmen.
7. **ERROR** — einmal `return -1` / `TUD_MSC_RET_ERROR`: erwarten STALL + failed CSW (Device-seitig belegt).
8. **Auswertung** — Latenzhistogramm bis Host-Abort; getrennt PC vs. Zielhost (**C**).

## Artefakte

| Artefakt | Inhalt |
|----------|--------|
| `busy-mode-YYYYMMDD.md` | Stack-Version, Modus A/B/B′/C, EP_BUFSIZE |
| `busy-trace-….csv` | t_us, mode, lba, offset, bufsize, ret, retry_n, task_alive |
| Evidence-IDs | `EVID-TINYUSB-MSC-…` / Lab-IDs im Audit |

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Modus klar benannt | A/B/B′/C getrennt | „Busy“ ohne Unterscheidung Block vs. return 0 |
| Stack-Vertrag belegt | Version + ASYNC ja/nein | Annahme „Upstream = Arduino“ |
| Host-Abort nur als C/Lab | Evidence-ID | Abort-ms als Sheet-A-FACT |
| Kein STALL durch `return <0` ungeplant | Retries ≥0 nur bei Absicht | ERROR-Pfad verwechselt mit Busy |

## Fallstricke

- **`return 0` hält denselben READ10 offen** — kein neuer CBW „daneben“; CSW erst nach Daten/ERROR.
- Ohne RTOS kann reines BUSY **`tud_task` festnageln** (TinyUSB #2035) — Producer im Main-Loop stirbt.
- Arduino `USBMSC`: bei `!media_present` liefert Bridge ebenfalls `0` (= Busy-Semantik), nicht ERROR.
- Upstream `tud_msc_async_io_done(0)` → ERROR, nicht Busy.
- Partial-Read ≠ Busy; Endpoint-Races sind Port-abhängig.
- NBT-/HU-Timeouts gehören **nicht** in Technology Sheets.

## Beispiel-Einsätze

| Projekt / Audit | Hinweis |
|-----------------|---------|
| [`tinyusb-msc-busy-retry-2026`](../audits/tinyusb-msc-busy-retry-2026/) | Desk-Semantik A |
| `esp32-pidrive` E7 Stall-FW | Lab: B′ vs. Silence-Fallback |
| PiDrive E7/S6 am BMW NBT (2026-10-12) | Feld: Busy-Pacing ~65 s bis Dateiende; Stall-off ~6 s A/B — `EVID-BMWHU-2026-10-12-001`–`005` |
| [`msc-lba-timing-instrument`](msc-lba-timing-instrument.md) | ergänzt LBA/Burst; diese Method ergänzt Retry-Modi |
