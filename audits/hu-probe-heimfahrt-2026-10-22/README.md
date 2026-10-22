# Audit Campaign: hu-probe-heimfahrt-2026-10-22

```yaml
id: hu-probe-heimfahrt-2026-10-22
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
prior_audit: hu-probe-media-ladder-2026-10-22
related_audits:
  - hu-probe-media-ladder-2026-10-22
  - hu-probe-psram-board-free-2026-10-21
  - hu-probe-bmw-s2-abend-offline-2026-10-18
  - msc-host-read-semantics-s1s2s3-2026
upstream_pin:
  repo: https://github.com/MPunktBPunkt/hu-probe
  commit: "4fdf519"
  gesamtbericht: "28249de"
  gpt_fold: "c413480"
  fw_capture: "0.3.17"
  fw_oneshot: "0.3.19"
reuse_outcomes:
  reused:
    - bmw-nbt-evo
    - usb-msc
    - tur-idle-2238ms-phase-locked
    - bulk-read10-240
    - media-ladder-head-structure-plus-head-contract
    - tripstore-offline-upload-path
  new:
    - remount-not-cold-start
    - remount-395xxx-position-probe
    - three-read-modes-head-eager-neighbor
    - lba-scheduler-interleave-supersedes-global-elevator
    - neighbor-prefetch-near-complete-coverage
    - prefetch-lead-context-dependent-140-240s
    - busy-backpressure-without-reset
    - eager-read-not-play-intent
  not_helped:
    - "Prefetch-Lead ≈8 s als HU-Konstante"
    - "Globaler Elevator immer aufwärts"
    - "Remount = Cold Start / Cache-Flush"
    - "Großer File-Read = Play Intent"
    - "Weitere Media-Ladder-Varianten nur für Prefetch-Zahlen"
  process: "Delta nach Media-Leiter: Heimfahrt Offline Trips #22–#24 (drive_mix); GPT-Konsens + Grok-Übergabe gegen Analyzer-Artefakte geprüft."
  decisions_touched:
    - reject-prefetch-lead-8s-constant
    - supersede-global-elevator-with-lba-scheduler
    - fact-remount-not-cold-start
    - reject-eager-read-as-play-intent
    - elevate-neighbor-prefetch-aggressive
```

## Ziel

Heimfahrt-Messung (`drive_home` / `drive_mix`, Trips `#22`–`#24`) gegen Media-Leiter
abschließen: Remount-Semantik, Read-Modi, Prefetch-Mechanik, Scheduler-Modell und
PiDrive-Konsequenzen schärfen — ohne weitere Ladder-Varianten.

## Scope

- **Im Scope:** Offline-Capture `#22`/`#23`/`#24` (FW 0.3.17, Probe `.89`); Analyzer
  unter `docs/feld/artifacts/20261022-heimfahrt/`; Gesamtbericht + Grok-Übergabe @
  `4fdf519`; Claim-Diff vs. Media-Leiter; PiDrive-Vertragsschärfung.
- **Nicht im Scope:** Audible GATE-01; formale 395xxx-LBA-Semantik; Cache-Key/`seq_ident`
  Feld; Upstream-Profil-Edit; FW-Patches; formal A8/`seq_size`.

```text
kill:
  - Prefetch-Lead = 8 s als Parameter
  - globaler Elevator als alleiniges LBA-Modell
  - Remount = Cold Start / vollständiger Cache-Flush
  - Eager/großer Read = Play Intent
  - „nur noch Media-Ladder sammeln“ als Next
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Trips `#22`–`#24` Integrity PASS + Upload delivered belegt | erfüllt |
| 2 | Remount ≠ Cold Start (395xxx `#22` + Kontext-Resume `#23`) | erfüllt |
| 3 | Drei Read-Modi (Head / Eager Body / Neighbor+Interleave) belegt | erfüllt |
| 4 | Prefetch-Lead kontextabhängig (MIX ~7–8 s vs. ROCK/CLASSIC 140–240 s) | erfüllt |
| 5 | TUR 2,2388 s + 4‑KiB-Takt + 240er Bulk bestätigt | erfüllt |
| 6 | BUSY-Backpressure ohne Reset (`#23`) belegt | erfüllt |
| 7 | Eager-Read ≠ Play Intent als REJECTED-Automatismus | erfüllt |
| 8 | Offene Gates (Audible, Intent, Cache-Key, 395xxx) explizit | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Remount ≠ Cold Start | Gleiche Mount-Signatur / gleicher Startpfad? | `H01`–`H03` | Positions-/Kontext-Resume | `DISCOVERED DURING TEST` |
| Prefetch-Lead ≠ Konstante | Lead immer ~8 s? | `H06` | VARIABLE / kontextabhängig | `DISCOVERED DURING TEST` |
| Globaler Elevator unzureichend | Strikt aufwärts über Dateien? | `H05` | LBA-Scheduler + Interleave | `DISCOVERED DURING TEST` |
| Eager ≠ Play Intent | Coverage≈1 ⇒ hörbar? | `H04`/`H07` | Audible GATE bleibt P0 | `DISCOVERED DURING TEST` |
| PiDrive-Lieferseite reif | Was fehlt noch USB-seitig? | `H08`/`H10` | Next = Audible+Intent, nicht Ladder | `DISCOVERED AFTER TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `H01`/`H02` | `#23`-Remount-Signatur = normale Init — Cold-Start-Reject basiert auf **Verhalten**, nicht immer auf abweichender Probe | `DISCOVERED DURING TEST` |
| `H04` | Coverage-Summe über Episoden kann >1 (Mehrfach-Pass) — Union/Peak prüfen, nicht roh summieren | `DISCOVERED AFTER TEST` |
| `H06` | Analyzer-`lead_before_end_s` ohne Audible — Lead nur Struktur/Proxy | `KNOWN BEFORE TEST` |
| `H05` | R04-Chunk-Liste: Sprünge `7464→1536` o. ä. = Interleave, nicht Rewind-Intent | `DISCOVERED DURING TEST` |
| `H09` | `#22`/`#23` Remount-Zeiten vs. Operator-Stops — 1–2 Stops passen | `KNOWN BEFORE TEST` |

## Kill-Kriterien

**Hypothese:** Heimfahrt liefert Remount-/Scheduler-/Prefetch-Modellkorrektur; USB-Lieferseite bleibt grün; nächster Sprung = Audible+Intent.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Remount immer normale Init + Datei‑1‑Scan | vermieden (`H01`–`H03`) |
| 2 | Lead=8 s als Profil-Konstante bestätigt | vermieden (`H06`) |
| 3 | Eager-Coverage als Play-Intent gewertet | vermieden (`H07`) |
| 4 | Media-Ladder-Varianten als empfohlener Next | vermieden (`H10`) |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| MSC Host-Read-Semantik | [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md) |
| LBA/Timing-Instrument | [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) |

## Bezug Inventar

- Projekt: [`hu-probe`](../../projects/hu-probe/)
- Prior: [`hu-probe-media-ladder-2026-10-22`](../hu-probe-media-ladder-2026-10-22/)
- Upstream: `docs/feld/2026-10-22-gesamtbericht-heimfahrt.md` @ `28249de`,
  Grok-Übergabe @ `4fdf519`, Kurzauswertung, Artefakte `docs/feld/artifacts/20261022-heimfahrt/`

## Ergebnisse

| # | Artefakt | Ort |
|---|----------|-----|
| 1 | Evidence-Register | [`evidence.md`](evidence.md) |
| 2 | Session-Summaries | [`session-summaries.json`](session-summaries.json) |
| 3 | Bericht | [`docs/reports/2026-10-22-hu-probe-heimfahrt.md`](../../docs/reports/2026-10-22-hu-probe-heimfahrt.md) |

## Knowledge Feedback

| Lab/Field | Evidence | Zurück in |
|-----------|----------|-----------|
| Remount ≠ Cold Start; 395xxx; Kontext-Resume | `H01`–`H03` | Application `bmw-nbt-evo` |
| Read-Modi / Neighbor / Interleave / Lead | `H04`–`H06` | Application `bmw-nbt-evo` + FOLLOW-ON |
| TUR/4‑KiB/240/BUSY | `H08`/`H09` | Applications `bmw-nbt-evo` + `usb-msc` |
| Eager ≠ Play Intent; Next = Audible | `H07`/`H10` | FOLLOW-ON + PiDrive Cross-Link |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 Kill-Kriterien | PASS |
| C13 Knowledge Feedback | PASS → Apps/FOLLOW-ON; Profil-Edit absichtlich nicht |

## Lessons → Transfer

- **Remount:** HU nimmt positions-/zustandsabhängigen Kontext wieder auf — kein Medium-von-vorne.
- **Prefetch:** mehrere Mechanismen (Head, Eager Body, Neighbor, Partial Refill); Lead situationsgebunden.
- **Scheduler:** Regionen/Dateien interleaved — lokales `tail_then_head` bleibt erklärbar, globaler Elevator nicht.
- **PiDrive:** Lieferseite (Struktur+Head+240/~1 MiB/s+Multi-Track) beherrschbar; Missing = Audible + Intent + Cache-Key + 395xxx-Semantik.

## Offene Punkte nach Abschluss

- P0: audible-Tap → GATE-01 / Read↔Play-Intent
- P0: Play-Intent-Unterscheidung (Eager ≠ hörbar)
- P1: Cache-Key / Identity (`seq_ident`)
- P1: 395xxx-LBA-Semantik am Remount
- P2: formal A8/`seq_size`; Elevator-Drittstichprobe (lokal) bleibt getrennt
