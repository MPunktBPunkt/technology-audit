# Evidence — hu-probe-heimfahrt-2026-10-22

Delta-Audit hu-probe · Heimfahrt Offline · Remount / Scheduler / Prefetch · FW 0.3.17  
Pin: `hu-probe@4fdf519` (Grok-Übergabe); Gesamtbericht @ `28249de`; GPT-Fold @ `c413480`; Capture FW **0.3.17** (Probe `.89`); one-shot Auto-Aus ab **0.3.19**.

## Quellen

| Quelle | Pin / Datum | Rolle |
|--------|-------------|-------|
| https://github.com/MPunktBPunkt/hu-probe | `4fdf519` | Grok-Übergabe + Link aus Gesamtbericht |
| `docs/feld/2026-10-22-gesamtbericht-heimfahrt.md` | `28249de` / `c413480` | Operator + GPT-Konsens |
| `docs/feld/2026-10-22-uebergabe-heimfahrt-grok.md` | `4fdf519` | Übergabe-Claims |
| `docs/feld/2026-10-22-heimfahrt-auswertung.md` | archived | Kurzauswertung |
| `docs/feld/artifacts/20261022-heimfahrt/*/analysis.json` | archived | Analyzer MEASURED |
| `docs/feld/artifacts/20261022-heimfahrt/*/session.json` | archived | Capture Meta / Integrity |
| Prior Audit | [`hu-probe-media-ladder-2026-10-22`](../hu-probe-media-ladder-2026-10-22/) | Head/Tail/Bulk/Elevator-STRONG |

## Evidence-Register

| ID | Claim | Klasse | Quelle |
|----|-------|--------|--------|
| `EVID-HUPROBE-2026-10-22H-001` | Drei Heimfahrt-Trips Offline: `#22` `12777_bmw_drive_home` (`power_loss`, 50 187 Events, 2 Remounts), `#23` `20261022-171751_bmw_drive_home` (`max_duration`, 24 456 Events, 2 Remounts), `#24` `20261022-173030_bmw_drive_home` (`power_loss`, kurz, 1 Mount). Jeweils `transport=ram_offline`, FW **0.3.17**, `integrity_pass=true`, `upload_status=delivered`, `msc_sample_overflow=0`, Medium/`scenario=drive_home` auf `drive_mix`. | `MEASURED` | session.json ×3; Gesamtbericht §1 |
| `EVID-HUPROBE-2026-10-22H-002` | `#22` Remount @ **595,709 s**: Mount-Signatur `0/1,0/1,0/8,395136/8,395248/8,8/8,395256/1…395260/1` — **abweichend** von normaler Init (`0/8,0/8,96/40,…,131072/8` @ 0,24 s). Positionsbezogene Probe; Semantik der 395xxx-LBAs **UNKNOWN**. | `FACT` (Signatur-Diff) / `UNKNOWN` (395xxx-Zweck) | analysis mount_signatures; Gesamtbericht §2 |
| `EVID-HUPROBE-2026-10-22H-003` | Remount ≠ Cold Start (**STRONG**): (a) `#22` zweite Signatur ≠ Init + Fortsetzung MIX/M01 statt Medium-von-vorne; (b) `#23` Remount @ **448,475 s** hat **normale** Init-Signatur, Verhalten aber `R04 → R01 → R02 → CLASSIC/C0x` (Kontext nahe letztem Bereich). Cold-Start-Reject basiert auf Verhalten, nicht immer auf abweichender Probe. | `FACT` / STRONG INFERENCE | mount_signatures; episodes/prefetch `#23`; Gesamtbericht §2–3 |
| `EVID-HUPROBE-2026-10-22H-004` | Drei Read-Modi: **A Head/Selection** `0/240 + 240/240 + 480/32` (u. a. R01/C0x); **B Eager Body** Coverage ≈0,93–0,99 auf R01/R02/C01–C04 in `#23` (Episode-`coverage`); **C Neighbor/Partial + Interleave** (R04 Regionen verzahnt; CHARTS H0x Browse in `#22`). | `FACT` / `MEASURED` | episodes.chunks/coverage `#23`; analysis.md; Gesamtbericht §5 |
| `EVID-HUPROBE-2026-10-22H-005` | LBA-Scheduler mit Interleave (**STRONG**): R04-Episode `#23` t≈2,58 s Chunks springen u. a. `…1504/32 → 7464/128… → 1536/240…` (kein strikter Aufwärts-Elevator über die Datei). Erklärt lokales `tail_then_head` (Media-Leiter) ohne globales Elevator-Modell. Media-Leiter Elevator-STRONG an `cache_place` bleibt lokal gültig; **globaler Elevator SUPERSEDED**. | `MEASURED` / STRONG INFERENCE | episodes ROCK/R04.MP3; Grok §2; GPT §9 |
| `EVID-HUPROBE-2026-10-22H-006` | Prefetch-Lead **kontextabhängig**: `#22` MIX M01→M02 / M02→M03 `lead_before_end_s` **7,725 / 7,157 s**; `#23` ROCK/CLASSIC Prefetch-Leads **140,5–237,1 s** (n=8, alle ≥140 s). „8 s Prefetch“ als HU-Konstante **REJECTED** (Media-Leiter VARIABLE bestätigt/verschärft). | `FACT` / `REJECTED` (Konstante) | prefetch[]; Gesamtbericht §5 |
| `EVID-HUPROBE-2026-10-22H-007` | Eager-/Nachbar-Read ≠ Play Intent: `#23` C01→C02→C03→C04 mit Start→Start ~3,6–5,1 s und Atom-Ende→nächster Read teils **~4 ms** (`0,004035` / `0,004068` s); Coverage nahe 1 ohne Audible-Anker. Automatismus „großer Read = jetzt spielen“ **REJECTED**. | `MEASURED` / `REJECTED` (Intent-Automatismus) | analysis.md Atom-Übergänge; coverage; GATE-01 offen |
| `EVID-HUPROBE-2026-10-22H-008` | Timing-Stabilität Heimfahrt: TUR idle Median **2,2388 s** (alle drei Sessions); `tur_phase.period_ms` ≈ **2238,8–2238,9**; 4‑KiB-Chunk-Takt `#23` p50 **3,896 ms** (n=10 256); Bulk READ10 **240** dominant; Durchsatz ~1 MiB/s (CBW-Fenster). Bestätigt Media-Leiter Live-FACTS im Offline-Pfad. | `FACT` | tur / tur_phase / chunk_pacing |
| `EVID-HUPROBE-2026-10-22H-009` | BUSY als kontrollierter Backpressure: `#23` `read_stalls.held` @ t=453,365 s, `ROCK/R04.MP3`, **16 Blöcke**, `hold_s=1,623`, `outcome=abandoned`, `reset_or_remount=false`, danach normale TUR/READ10-Fortsetzung. | `FACT` | analysis read_stalls; Gesamtbericht §6 |
| `EVID-HUPROBE-2026-10-22H-010` | Instrument: Offline Heimfahrt → Stored-Replay → Collector für `#22`–`#24` `delivered` + Integrity PASS (PSRAM/TripStore-Pfad nach 0.3.17). FW **0.3.19** one-shot: Heimnetz+Collector+leeres Journal → `autoCapture=false`. Lab-Replay B50 bleibt getrennt FAIL (prior). | `MEASURED` | session capture; Gesamtbericht §7–8; prior `…-22-009`/`011` |
| `EVID-HUPROBE-2026-10-22H-011` | PiDrive-Konsequenz (nach Heimfahrt): USB-Lieferseite (Struktur+Head+Size/Extents, 240er/~1 MiB/s, Multi-Track/Neighbor, BUSY-Pacing) weitgehend verstanden. Offen vor robustem Live: **P0 Audible GATE**, **P0 Play-Intent**, **P1 Cache-Key**, **P1 395xxx/Remount-State**. Weitere Media-Ladder-Varianten nur für Prefetch-Zahlen = **nicht** Next. | `INFERRED` (Vertrag) / Prozess | Grok §4–7; GPT §9–10; Evidence `H01`–`H09` |

## Claim-Diff vs. Prior (Media-Leiter 22.10.)

| Claim | Vorher (Leiter) | Jetzt (Heimfahrt) |
|-------|-----------------|-------------------|
| Prefetch-Lead ~8 s | VARIABLE (ohne Audible) | **Kontextabhängig FACT**; MIX ~7 s vs. 140–240 s; Konstante **REJECTED** |
| Elevator | STRONG lokal (`cache_place` tail_then_head) | Lokal unverändert erklärbar; **globaler Elevator SUPERSEDED** durch LBA-Scheduler/Interleave |
| Remount / Cache | Identity/Remount OPEN; free: Resume beobachtet | **Remount ≠ Cold Start STRONG**; 395xxx-Probe `#22`; Kontext-Resume `#23` |
| Große Reads | Bulk/Prefetch Phasen | Eager Body ~90–99 % + Neighbor; **≠ Play Intent** |
| TUR 2238,78 ms | Live + Offline free | Heimfahrt Offline **2,2388 s** ×3 bestätigt |
| Trip Offline Upload | `#17`/`#18` PASS | `#22`–`#24` drive_home PASS (lange Fahrten) |
| „Nur Struktur“ | REJECTED; Struktur+Head | unverändert; plus Eager/Neighbor beherrschbar |

## Offene Claims

- audible-Marker → GATE-01 / Read↔hörbarer Track
- Play-Intent-Mapping (wann Decode vs. nur Cache)
- 395xxx-LBA-Semantik am Remount
- Cache-Key / Identity (`seq_ident` / `ident_b`)
- formal A8/`seq_size` (getrennt)
- Elevator-Drittstichprobe lokal (zwei ungelesene Spans) — Modellkorrektur ersetzt das nicht
