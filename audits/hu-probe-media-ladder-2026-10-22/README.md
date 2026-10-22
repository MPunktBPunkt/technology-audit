# Audit Campaign: hu-probe-media-ladder-2026-10-22

```yaml
id: hu-probe-media-ladder-2026-10-22
project_id: hu-probe
started: 2026-10-22
ended: 2026-10-22
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: bmw-nbt-evo
related_tech:
  - usb-msc
  - esp32-s3-silicon
  - esp32-s3-usb-wifi-coex
prior_audit: hu-probe-psram-board-free-2026-10-21
related_audits:
  - hu-probe-psram-board-free-2026-10-21
  - hu-probe-bmw-s2-abend-offline-2026-10-18
  - hu-probe-bmw-s0s2-field-2026
  - msc-host-read-semantics-s1s2s3-2026
upstream_pin:
  repo: https://github.com/MPunktBPunkt/hu-probe
  commit: "8234982"
  field_core: "e1da0c6"
  fw: "0.3.17"
reuse_outcomes:
  reused:
    - bmw-nbt-evo
    - usb-msc
    - tur-idle-2239ms-phase-locked
    - tail-then-head-elevator-inference
    - psram-n8r2-1mib-offline-capture
  new:
    - media-scan-head-32-plus-128
    - tail-prefetch-track-rhythm-id3-cover
    - bulk-read10-240-bitrate-mix
    - pidrive-structure-plus-head-contract
    - trip-replay-0.3.17-heap-pass
  not_helped:
    - "Nur Ordnerstruktur, kein Dateiinhalt"
    - "Prefetch-Lead ≈8 s als Konstante"
    - "26,5 s = generischer HU-Timer"
    - "Fenster A8 (240,240,32 @16,4 s) als geschlossen"
    - "Lab ram_offline Replay (B50) als PASS"
  process: "Delta nach PSRAM/free: Media-Leiter tcp_live 0.3.17 + Multi-KI/Wire-Gesamtbericht; Instrument TripStore-Replay 0.3.9–0.3.17."
  decisions_touched:
    - reject-scan-structure-only
    - fact-head-scan-160-blocks
    - elevate-elevator-to-strong
    - pidrive-head-required-rest-dynamic
    - supersede-large-prefetch-unknown-with-phase-model
```

## Ziel

Nach dem großen hu-probe-Update (PSRAM, Offline/Trip-Replay, SynthFat-Leiter)
HU-Facts aus den Messdaten ziehen: Scan-/Play-Phasen, Head-Geometrie, Tail-Prefetch,
TUR, Elevator, und den PiDrive-Vertrag schärfen.

## Scope

- **Im Scope:** BMW Media-Leiter 2026-10-22 (`tcp_live`, FW 0.3.17); Wire-/Analyzer-FACTs;
  Reject „nur Struktur“; PiDrive Struktur+Head; Trip-Replay-Instrument 0.3.17 PASS;
  Abgleich prior free/demo_v1.
- **Nicht im Scope:** Formales Schließen H-A/B/C auf `seq_size`; audible-Tap GATE-01;
  Cache-Key `ident_b`; Upstream-Profil-Edit; FW-Patches; HARDWARE.md-Edit.

```text
kill:
  - „HU liest nur Ordnerstruktur“
  - Prefetch-Lead 8 s als universelle Konstante
  - 26,5 s Intervall = HU-Timer (statt Trackdauer)
  - tail_then_head = Re-Entry-Zustand
  - beliebige Audio-Payload hinter gemeldeter Größe/FAT ohne konsistenten Head
  - Lab-Replay B50 als Offline-PASS zählen
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 5× BMW Live Integrity PASS + Referenzsession `id3_cover` belegt | erfüllt |
| 2 | Head-Scan 32+128 (=160 Blöcke ≈80 KiB) FACT | erfüllt |
| 3 | Tail-Prefetch-Struktur (160 @ file_off 160, Track-Rhythmus) FACT | erfüllt |
| 4 | TUR idle 2238,78 ms bestätigt (Live) | erfüllt |
| 5 | Elevator STRONG an `cache_place`; „nur Struktur“ REJECTED | erfüllt |
| 6 | PiDrive-Vertrag Struktur+Head vs. dynamischer Rest dokumentiert | erfüllt |
| 7 | Instrument: Trip-Replay 0.3.17 + Lab B50 getrennt | erfüllt |
| 8 | Offene Gates (audible, B47, Identity, seq_size A8) explizit | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Scan ≠ nur Directory | Liest HU Dateiköpfe? | `001`–`003` | Head 160 Pflicht | `DISCOVERED DURING TEST` |
| Prefetch groß ≠ UNKNOWN-blanket | Gibt es File-Reads vor Trackwechsel? | `004`–`005` | Phasenmodell; Lead VARIABLE | `DISCOVERED DURING TEST` |
| Elevator STRONG | Startet Rücksprung am Tail? | `007` | Re-Entry bleibt REJECTED | `DISCOVERED DURING TEST` |
| PiDrive: Head stabil, Rest dynamisch | Was muss virtuell stimmen? | `010` | ~80 KiB+ID3/FAT Pflicht | `DISCOVERED AFTER TEST` |
| Trip-Replay Instrument PASS | Heap/Leak unter Upload? | `011` | Offline→Transfer nutzbar | `KNOWN BEFORE TEST` / Feld `DISCOVERED` |
| A8 Fenster nicht schließen | `seq_size` 16,4 s-Refill? | `013` | OPEN / Leiter ersetzt nicht Formal | `KNOWN BEFORE TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `002`/`003` | Episode-`chunks` [[0,32],[32,128]] vs. aggregierte 160 | `DISCOVERED DURING TEST` |
| `004` | Absolute t-Werte: Analyzer vs. Gesamtbericht-Origin (~1,55 s Offset) — Struktur/Δt zählen | `DISCOVERED AFTER TEST` |
| `005`/`012` | Analyzer-Prefetch-Stats können Scan mischen (B47) — Lead nicht als Konstante | `DISCOVERED AFTER TEST` |
| `006` | TUR nur Idle-Fenster; Live bestätigt free-Offline | `KNOWN BEFORE TEST` |
| `008` | Browse 8.3 ≠ Player-ID3-Quelle | `DISCOVERED DURING TEST` |
| `009`/`011` | Lab Replay FAIL ≠ BMW Live PASS; Trip uploaded getrennt | `DISCOVERED DURING TEST` |

## Kill-Kriterien

**Hypothese:** Media-Leiter liefert belastbare Scan/Play-Grammatik und PiDrive-Schichtenvertrag; formal A8/`seq_size` bleibt getrennt.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | „Nur Ordnerstruktur“ als FACT | vermieden (`010` REJECT) |
| 2 | Lead=8 s als Profil-Konstante | vermieden (`005` VARIABLE) |
| 3 | A8 geschlossen ohne `seq_size` | vermieden (`013` OPEN) |
| 4 | B50 Lab FAIL als Offline-PASS | vermieden (`009`) |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| MSC Host-Read-Semantik | [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md) |
| LBA/Timing-Instrument | [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) |

## Bezug Inventar

- Projekt: [`hu-probe`](../../projects/hu-probe/)
- Prior: [`hu-probe-psram-board-free-2026-10-21`](../hu-probe-psram-board-free-2026-10-21/)
- Upstream: `docs/feld/2026-10-22-bmw-media-ladder-live.md`,
  `docs/feld/2026-10-22-gesamtbericht-media-ladder-pruefung.md` @ `8234982`,
  `docs/feld/2026-10-21-trip-upload-hang-phasegate.md`
- Rohdaten: `sessions/20261022-*_bmw_free`, Artefakte unter `docs/feld/artifacts/20261022-bmw-media-ladder/`

## Ergebnisse

| # | Artefakt | Ort |
|---|----------|-----|
| 1 | Evidence-Register | [`evidence.md`](evidence.md) |
| 2 | Session-Summaries | [`session-summaries.json`](session-summaries.json) |
| 3 | Bericht | [`docs/reports/2026-10-22-hu-probe-media-ladder.md`](../../docs/reports/2026-10-22-hu-probe-media-ladder.md) |

## Knowledge Feedback

| Lab/Field | Evidence | Zurück in |
|-----------|----------|-----------|
| Head 32+128 / Tail-Prefetch / Bulk 240 / TUR Live | `001`–`006` | Application `bmw-nbt-evo`; FOLLOW-ON Profil |
| Elevator STRONG `cache_place` | `007` | Application `bmw-nbt-evo` (INFERENCE→STRONG) |
| PiDrive Struktur+Head | `010` | hu-probe + Cross-Link PiDrive Application |
| Trip-Replay 0.3.17 / Lab B50 | `009`/`011` | Application `usb-msc` |
| Doc-Drift HARDWARE §2.3 | prior `005` | FOLLOW-ON Upstream (unverändert offen) |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 Kill-Kriterien | PASS |
| C13 Knowledge Feedback | PASS → Apps/FOLLOW-ON; Upstream-Profil-Edit absichtlich nicht |

## Lessons → Transfer

- **Scan-Phase:** Directory-Walk + Dateikopf (typisch 32+128) — nicht „nur Menübaum“.
- **Play-Phase:** Prefetch im Track-Rhythmus; kleine Dateien oft schon im Scan voll; große CONT/Bulk 240.
- **Instrument:** PSRAM + TripStore-Replay (Leak-Fix 0.3.17) machen Offline→Upload belastbar; Live-Leiter lief parallel per `tcp_live`.
- **PiDrive:** virtuelles Menü **und** konsistenter ~80 KiB-Head; Rest dynamisch unter Größen-/FAT-Konsistenz.

## Offene Punkte nach Abschluss

- P0: audible-Tap → GATE-01 / Lead mit Anker
- P0: Analyzer B47 (Scan aus Prefetch-Stats)
- P1: Identity/Cache-Key Remount; Head-vs-Rest A→B→A
- P1: Lab-Replay B50 (`.88` vs `.89`)
- P2: formal `seq_size` A8; Elevator-Drittstichprobe; `drive_mix` CBW-Vollnachzug
- P2: HARDWARE.md §2.3; `parse_errors=47` Label (B49)
