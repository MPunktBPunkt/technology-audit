# Evidence — hu-probe-media-ladder-2026-10-22

Delta-Audit hu-probe · Media-Leiter Live · Host-Phasen · PiDrive-Vertrag · FW 0.3.17  
Pin: `hu-probe@8234982` (Gesamtbericht); Feldkern Artefakte @ `e1da0c6`; FW **0.3.17**.

## Quellen

| Quelle | Pin / Datum | Rolle |
|--------|-------------|-------|
| https://github.com/MPunktBPunkt/hu-probe | `8234982` | Gesamtbericht Media-Leiter |
| `docs/feld/2026-10-22-bmw-media-ladder-live.md` | 2026-10-22 | Operator + Session-Census |
| `docs/feld/2026-10-22-gesamtbericht-media-ladder-pruefung.md` | `8234982` | Multi-KI + Wire-Prüfung |
| `docs/feld/artifacts/20261022-bmw-media-ladder/*/analysis.json` | archived | Analyzer MEASURED |
| `docs/feld/artifacts/20261022_bmw_media_ladder_compare.*` | archived | Cross-Session Compare |
| `sessions/20261022-*_bmw_free` | lokal | Roh `events.jsonl` / `session.json` |
| `docs/feld/2026-10-21-trip-upload-hang-phasegate.md` | 0.3.9–0.3.17 | Trip-Replay Instrument |
| Prior Audit | [`hu-probe-psram-board-free-2026-10-21`](../hu-probe-psram-board-free-2026-10-21/) | PSRAM / free Grammar |

## Evidence-Register

| ID | Claim | Klasse | Quelle |
|----|-------|--------|--------|
| `EVID-HUPROBE-2026-10-22-001` | Fünf BMW Live-Sessions Media-Leiter: `transport=tcp_live`, FW **0.3.17**, `integrity_pass=true`, `msc_sample_overflow=0`. Medien: `cache_place`, `dur_mix`, `bitrate_mix`, `id3_cover`, `drive_mix` (+ Warm-up `cache_b`). | `MEASURED` | Session-Census; Feldbericht |
| `EVID-HUPROBE-2026-10-22-002` | Scan-Head-Geometrie: READ10-Episoden mit Chunks **`[0,32] + [32,128]`** = **160 Blöcke ≈ 80 KiB**. Bestätigt an `id3_cover` (`081152`) und `bitrate_mix` Head-Episoden. | `FACT` / `MEASURED` | `analysis.json` episodes.chunks; Gesamtbericht §3.1 |
| `EVID-HUPROBE-2026-10-22-003` | Kleine Dateien können im Scan **nahezu vollständig** gelesen werden (`COVER1` komplette Extent; `B032` Scan-Blöcke ≥ Extent) — nicht nur Metadaten-Kopf. | `MEASURED` | Feld + Wire `id3_cover`/`bitrate_mix` |
| `EVID-HUPROBE-2026-10-22-004` | Tail-Prefetch Autoplay `id3_cover`: nach Scan einzige File-Reads = **160 Blöcke @ `file_off=160`** für COVER2/3/NOCOVER. Analyzer-Episode-Starts **20,966 / 47,545 / 73,967 s**; Gesamtbericht-Wire **22,511 / 49,090 / 75,511 s** (gleicher Δt≈26,5 s, Origin-Offset ~1,55 s). | `FACT` (Struktur) / `MEASURED` | episodes; Gesamtbericht §3.2 |
| `EVID-HUPROBE-2026-10-22-005` | Prefetch-Lead ≈7,5–8 s erscheint in späten `lead_before_end_s` (`id3_cover` 7,78 s; `bitrate_mix` 7,51 s), ist aber **VARIABLE** und ohne `audible_change`-Anker. Frühe Compare-/Prefetch-Zeilen mischen Scan (B47) → Lead≠Konstante. demo_v1 Lead≈0 bleibt FACT (B55). | `MEASURED` / VARIABLE | prefetch[]; Compare; Gesamtbericht |
| `EVID-HUPROBE-2026-10-22-006` | TUR Idle-Periode Live: Analyzer **`period_ms=2238.78`** auf `081152`/`080752`/`080353`/`080544`/`61434`; Wire Idle-Diffs `081152` n=57, p50=2238,786 ms. Bestätigt free-Offline FACT. | `FACT` | tur_phase; Gesamtbericht §3.4 |
| `EVID-HUPROBE-2026-10-22-007` | `cache_place` (`080353`): `tail_then_head` **2/3** — TRACK2/TRACK1 starten bei **`file_blk=240`** (Chunks `[240,70]+[0,240]`); TRACK3 `head_first` `[0,240]+[240,70]`. Elevator/Nearest-LBA **STRONG**; Re-Entry bleibt **REJECTED**. Drittstichprobe offen. | `MEASURED` / STRONG INFERENCE | analysis episodes; Gesamtbericht §3.5 |
| `EVID-HUPROBE-2026-10-22-008` | Browse≠Player-Datenquelle: UI Browse zeigt **8.3**-Namen aus Directory; Player-Titel aus **ID3** im Dateikopf. Directory-Walk + File-Heads bereits im Scan (`drive_mix`). | `FACT` | Feldbericht §5; Operator |
| `EVID-HUPROBE-2026-10-22-009` | Lab `.88` Offline `065150`: `ram_offline`, `offline_records=199`, `upload_status=delivered`, aber `recv_events=56`, `replay_records≈0`, `integrity_pass=false` (B50). ≠ BMW Live-PASS. | `MEASURED` (FAIL) | session.json; Feld §4 |
| `EVID-HUPROBE-2026-10-22-010` | Claim „HU liest nur Ordnerstruktur, nicht den Dateiinhalt“ = **REJECTED**. Tragfähiger PiDrive-Vertrag: **Directory/FAT + Dateikopf (~80 KiB/ID3/MP3) Pflicht**; großer Audio-Rest dynamisch *unter* Größen-/EOF-Konsistenz — nicht beliebige Payload. | `REJECTED` / `INFERRED` (Vertrag) | Gesamtbericht §1; Evidence `002`–`003`/`008` |
| `EVID-HUPROBE-2026-10-22-011` | Instrument TripStore-Replay: FW **0.3.9–0.3.17** (TcpStreamer Single-Owner, Token-Bucket, Progress-Watchdog, **EventBus pop move+clear** Heap-Leak). Feld **0.3.17 PASS**: Trips `#17`/`#18` `uploaded=true`, Heap ~185 KiB stabil. Ermöglicht Offline-Messung → späterer Transfer. | `MEASURED` | trip-upload-hang PhaseGate |
| `EVID-HUPROBE-2026-10-22-012` | Bulk-Play/`bitrate_mix`: READ10-Chunk-Länge **240** dominant (n=24 in Episoden-Chunks); große Tracks CONT vorwärts (kein Rewind an Dateianfang). Throughput-Hinweis ~1 MiB/s im Feldbericht. | `MEASURED` | analysis chunks; Feld |
| `EVID-HUPROBE-2026-10-22-013` | Präregistriertes Fenster-Modell A8 (`240,240,32` / ~16,4 s @128 kbit, H-A/B/C auf `seq_size`): durch diese Leiter **nicht formal geschlossen**. Phasenmodell (Scan-Head → Prefetch/Bulk) ersetzt die UNKNOWN-Blanket-Aussage für große Dateien, schließt A8-Refill-Takt nicht. | `HYPOTHESIS` OPEN | Feldplan 21.10.; Leiter ≠ `seq_size` |
| `EVID-HUPROBE-2026-10-22-014` | `drive_mix`: Head-160 ist **nicht** pauschal die einzige Scan-Tiefe — große Bäume/`R01`/`K01` können früh Tausende `file_blk` ziehen; `J01` Play-/Prefetch-Cluster ~160 s. Policy VARIABLE. | `MEASURED` / VARIABLE | Gesamtbericht §3.6 |
| `EVID-HUPROBE-2026-10-22-015` | `parse_errors=47` weiterhin in Session-Meta (B44/B49 Collector-Zähler) trotz `integrity_pass` Live — kein Capture-Fehler-Indikator. | `OBSERVED` | session capture |
| `EVID-HUPROBE-2026-10-22-016` | Live `tcp_live` unter Host-Last mit Integrity PASS auf 0.3.17 (Leiter) — Coex-Root-Cause unverändert offen; PSRAM≠Heilung bleibt; Live-Pfad für diese Last nutzbar. | `OBSERVED` | Sessions; prior Coex |

## Claim-Diff vs. Prior (PSRAM/free 21.10.)

| Claim | Vorher | Jetzt |
|-------|--------|-------|
| Prefetch große Dateien | UNKNOWN / Größenleiter OPEN | **Phasen-FACTS** (Head/Tail/Bulk); Lead VARIABLE; A8 formal OPEN |
| Head-Scan-Geometrie | nicht isoliert | **32+128 = 160** FACT |
| Elevator | INFERENCE (T3→T1 Wrap) | **STRONG** an `cache_place` (Tail-first bei Rücksprung) |
| „Nur Struktur“ | informell / Cursor-Kurzformel | **REJECTED**; PiDrive Struktur+Head |
| TUR 2238,78 ms | free Offline FACT | **Live bestätigt** |
| Drive-Home / Trip Replay | oft ohne Footer / Hang | **0.3.17 Upload PASS**; Lab Replay B50 FAIL getrennt |
| Offline capacity 1 MiB | FACT PSRAM | unverändert (`065150` capacity=1 MiB) |

## Offene Claims

- audible-Marker → GATE-01 Restlatenz / Lead mit Anker
- Analyzer B47 Scan/Prefetch-Trennung; Compare neu
- Cache-Key / Identity Remount (`ident_b`)
- Formal H-A/B/C auf `seq_size` / A8-Refill
- Elevator-Drittstichprobe (zwei ungelesene Spans)
- Lab Offline Replay B50
- HARDWARE.md §2.3 Doc-Drift (prior)
