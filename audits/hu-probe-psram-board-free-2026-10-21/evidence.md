# Evidence — hu-probe-psram-board-free-2026-10-21

Delta-Audit hu-probe · Board/PSRAM · free Offline · Profil · FW 0.3.x  
standard **0.7.1** · Profile `lab-tool`  
Pin: `hu-probe@f985459` (FW **0.3.1** PlatformIO; Kernfeld **0.2.40** free Offline).

**Epistemik:** Device-Stack CBW/`bot_data` + Session-Meta, nicht Wire. Prefetch bei großen Dateien weiter UNKNOWN.

## Quellen-Snapshots

| Artefakt | Pin / Ort | Rolle |
|----------|-----------|-------|
| https://github.com/MPunktBPunkt/hu-probe | `f985459` | FW 0.3.1 + Docs + Profil |
| `firmware/platformio.ini` | @ `f985459` | `BOARD_HAS_PSRAM`, `qio_qspi`, 8 MB Flash |
| `docs/HARDWARE-YD-ESP32-S3.md` | 2026-10-19 | Board-Foto/Pinout; §2.3 PSRAM-Text **veraltet** |
| `docs/feld/2026-10-19-lab-wifi-otg-coex-freeze.md` | Lab `.88` N8R2 | PSRAM ab 0.2.35; Coex-Tod bleibt |
| `docs/feld/2026-10-20-bmw-free-offline-0.2.40.md` | Feld + §7 Nachrechnung | free Grammar / Profil-Quelle |
| `docs/feld/2026-10-21-feldplan-groessenleiter.md` | Präregistriert | Größenleiter H-A/B/C |
| `profiles/bmw_nbt_evo.json` | schema 3, stark erweitert | hu-parameter |
| `derived/free_20261020_compare.*` | lokal | Analyzer-Vergleich |
| Sessions free Offline | `20261020-075{616,935}_bmw_free`, `080508` | Roh + `derived/analysis.json` |
| Prior Audit | [`hu-probe-bmw-s2-abend-offline-2026-10-18`](../hu-probe-bmw-s2-abend-offline-2026-10-18/) | CBW-Atom 240+69 |

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-HUPROBE-2026-10-21-001` | Build aktiviert PSRAM: `board_build.arduino.memory_type = qio_qspi`, `-DBOARD_HAS_PSRAM`, Flash 8 MB, Partition `partitions_huprobe_8mb.csv`. Zielmodul **N8R2** (Kommentar + Lab-Doku). | `MEASURED` (Build) | `platformio.ini`; Lab-Feldbericht |
| `EVID-HUPROBE-2026-10-21-002` | Offline-Capture-Puffer im Feld/Lab ab **0.2.37+**: `capture.capacity_bytes = 1048576` (1 MiB). Vorher typ. 24–64 KiB (0.2.30). Overflow=0 bei free Offline BMW. | `MEASURED` | Session-Census; Summaries |
| `EVID-HUPROBE-2026-10-21-003` | PSRAM-Nutzung im Code: EventBus-Slots `callocPreferPsram` (`ring_in_psram`); OfflineCapture `kTryPsram` 1 MiB→64 KiB; JSONL-Payloads weiter interner Heap. | `MEASURED` (Code) | `EventBus.cpp`, `OfflineCapture.cpp`, Lab-Doku §4 |
| `EVID-HUPROBE-2026-10-21-004` | Board: VCC-GND **YD-ESP32-S3 2022-V1.4**, WROOM-1, Dual-USB-C (USB=OTG / COM=CH343P), RGB GPIO48, BOOT GPIO0. Feld: HU kann Sonde allein speisen (Betreiber). | `MEASURED` / Betreiber | `HARDWARE-YD-ESP32-S3.md` |
| `EVID-HUPROBE-2026-10-21-005` | `docs/HARDWARE-YD-ESP32-S3.md` §2.3 behauptet noch „PSRAM ist nicht aktiviert“ — **Dokument veraltet** gegenüber Build+Sessions. | `MEASURED` (Doc-Drift) | Diff Doc vs. `001`/`002` |
| `EVID-HUPROBE-2026-10-21-006` | Drei BMW Offline Integrity-PASS Experiment `free` FW **0.2.40**: `075616`, `075935`, `080508`. `transport=ram_offline`, `end_reason=auto_media_hide`, Upload `delivered`, `capacity_bytes=1MiB`. | `MEASURED` | Sessions + Feldbericht |
| `EVID-HUPROBE-2026-10-21-007` | Track-Atom bestätigt: 14/14 volle **240+69** (=158208 B); Timing ~149 ms Atom; Continuation-Gap ~4,0–4,1 ms ≠ Head→Tail-CBW-Lücke (~118 ms Start→Start). | `MEASURED` | Feld §2A; analysis.json |
| `EVID-HUPROBE-2026-10-21-008` | Idle zwischen Atomen: **0 File-READ10**; nur TUR, Periode **2238–2239 ms** (p10=p50=p90 auf free). Prefetch-Lead ~15 s für **demo_v1 158 KiB** = **REJECTED**. | `MEASURED` / `REJECTED` | Feld §2C; Profil `rejected.prefetch_lead_15s_demo_v1` |
| `EVID-HUPROBE-2026-10-21-009` | Track-Wechsel-Intervall ≈ **26,473 s** = Medien-Trackdauer demo_v1 (1013 Frames @48 kbit), **kein** generischer NBT-Timer. | `MEASURED` | Feld §2B; Profil `demo_v1_track_change_interval_s` |
| `EVID-HUPROBE-2026-10-21-010` | Plug→erster Audio-Read: **~1,51 s** ab `set_address` (n=2); Kette Config~23 ms → MaxLUN ~997 ms → mount_done ~408–429 ms → first_read 70–86 ms. | `MEASURED` | `075935`, `080508` plug_timeline |
| `EVID-HUPROBE-2026-10-21-011` | Media-Loss nach Hide: Detekt-Latenz 0,39–2,18 s; Burst ~11 TUR + 12 REQUEST_SENSE + 1 PREVENT; Dauer ~180–220 ms; erster Fail-TUR auf Idle-Grid. | `MEASURED` | media_loss in analysis; Profil |
| `EVID-HUPROBE-2026-10-21-012` | `tail_then_head`: 5/5 bekannte Fälle = **T3→T1** (LBA-Rücksprung). Re-Entry-Grammatik **REJECTED**; Elevator/Nearest-LBA = **INFERENCE** (Rückwärtssprung-Test präregistriert). | `MEASURED` / `INFERRED` / `REJECTED` | Feld §7; Profil |
| `EVID-HUPROBE-2026-10-21-013` | Remount/Replug: Resume an Aussteckstelle (Operator n=1 `080508`); „Playlist startet immer bei T1“ **REJECTED**. S2 „next_track 9–18 s“ = Restzeit nach Mid-Track-Resume, nicht Prefetch (**SUPERSEDED**/**REJECTED**). | `MEASURED` / `REJECTED` | Feld §7; Profil |
| `EVID-HUPROBE-2026-10-21-014` | `parse_errors=47` in alten Sessions = Collector-Globalzähler (B44), nicht Capture-Fehler. Fix: Zähler pro Session. | `MEASURED` (Ursache) | Feld §7.1 B44 |
| `EVID-HUPROBE-2026-10-21-015` | Lab Coex 0.2.37–0.2.39: Recovery-Fixes **PASS**; PSRAM verbessert Heap, **heilt USB↔WiFi-Tod nicht**. | `MEASURED` (Lab) | Lab-Coex-Bericht |
| `EVID-HUPROBE-2026-10-21-016` | Profil `bmw_nbt_evo.json` enthält die free-/TUR-/Atom-/Media-Loss-FACTS und Rejects (schema 3). | `MEASURED` (Artefakt) | `profiles/bmw_nbt_evo.json` |
| `EVID-HUPROBE-2026-10-21-017` | Größenleiter / Fenster-Modell A8 (`240,240,32` / ~16,4 s @128 kbit): **präregistriert**, Feldauswertung dieser Kampagne **nicht** abgeschlossen. | `HYPOTHESIS` / OPEN | Feldplan 2026-10-21 |
| `EVID-HUPROBE-2026-10-21-018` | FW **0.3.0/0.3.1**: Drive-Mode / TripStore / 8 MB-Partitionen vorhanden; viele `bmw_drive_home`-Sessions ohne Footer/`integrity_pass` → kein Offline-PASS-Census. | `OBSERVED` | Sessions 20./21.10.; Code DriveMode |

## Claim-Diff vs. Prior (Abend 18.10. / S0S2)

| Claim | Vorher | Jetzt |
|-------|--------|-------|
| Track-Atom 240+69 | FACT Abend | **bestätigt** free 14/14 + Timing |
| Prefetch ~15 s | INFERENCE/PiDrive | **REJECTED** für demo_v1; große Dateien OPEN |
| Hold = Reverse-Order | FACT Order | **geschärft**: Elevator-INFERENCE; Re-Entry REJECTED |
| Offline-Puffer 32 KiB | Feld-Engpass | **1 MiB** mit PSRAM |
| PSRAM | ungenutzt / offen | **aktiviert** N8R2 qio_qspi |
| next_track 9–18 s | MEASURED S2 | **SUPERSEDED** (Resume-Artefakt) |
| Auto Offline BMW | FAIL vs Lab | **PASS** free 0.2.40 (3×) |

## Offene Claims

- Prefetch / Fenster-Refill bei ≥1 MiB (Größenleiter H-A/B/C)
- Elevator-Vorhersage Rückwärtssprung ohne Wrap (D180→D026)
- Cache-Key (Serial/Label/Volume) bei Replug `ident_b`
- `audible_change`-Marker → GATE-01 Restlatenz
- Drive-Home Integrity-/TripStore-Auswertung unter 0.3.x
- HARDWARE-Doc §2.3 nachziehen (Upstream)
