# Evidence — hu-probe-bmw-s0s2-field-2026

Feld/Lab 2026-10-15 · **standard_version 0.7.1** · Profile `lab-tool` ·
Rohdaten bleiben in `hu-probe` (Sessions + `docs/feld/`). Hier nur Claims + Links.

**Epistemik:** Device-Stack CBW/CSW/`read`-Events, nicht Wire. Lab ≠ BMW.
PiDrive-Semantik ≠ hu-probe-FACT. Nachgezogene Marker ≠ exakte Operator-Zeit.

## Quellen-Snapshots

| Repository / Artefakt | SHA / Pin | Vertiefter Pfad | Rolle |
|-----------------------|-----------|-----------------|-------|
| https://github.com/MPunktBPunkt/hu-probe | `5dbec434f43757e320f14eacb5198e11d4ed083b` | `docs/feld/2026-10-15-*.md`, `profiles/bmw_nbt_evo.json`, Sessions S0/S2/Lab | Instrument + Feld |
| S0 Kern-Sessions (FW 0.2.17) | Repo @ `5dbec43` | u. a. `sessions/2199_bmw_s0_plug_enum`, `2176_…`, `3085_…` (+ 5 weitere in Auswertung) | BMW S0 Transport |
| S2 Kern-Sessions (FW 0.2.23) | Repo @ `5dbec43` | `2280`, `2276`, `200036`, `200319`, `195417`, `195128`, `195657`, `2210` (`*_bmw_s2_prefetch`) | BMW S2 Transport |
| Lab Offline | Repo @ `5dbec43` | `sessions/20261015-181642_lab_debian_s0_plug_enum` | `ram_offline` E2E |
| technology-audit | Vor-Kampagne + diese | `msc-host-read-semantics-s1s2s3-2026`, Methods | Claim-Trennung |

Primär-Auswertungen (Upstream, reviewed):

- [uebergabe-abend-multi-ki](https://github.com/MPunktBPunkt/hu-probe/blob/5dbec434f43757e320f14eacb5198e11d4ed083b/docs/feld/2026-10-15-uebergabe-abend-multi-ki.md)
- [bmw-s2-0.2.23-auswertung](https://github.com/MPunktBPunkt/hu-probe/blob/5dbec434f43757e320f14eacb5198e11d4ed083b/docs/feld/2026-10-15-bmw-s2-0.2.23-auswertung.md)
- [bmw-s0-0.2.17-auswertung](https://github.com/MPunktBPunkt/hu-probe/blob/5dbec434f43757e320f14eacb5198e11d4ed083b/docs/feld/2026-10-15-bmw-s0-0.2.17-auswertung.md)
- [offline-p0](https://github.com/MPunktBPunkt/hu-probe/blob/5dbec434f43757e320f14eacb5198e11d4ed083b/docs/feld/2026-10-15-offline-p0.md)
- [massnahmen-01d](https://github.com/MPunktBPunkt/hu-probe/blob/5dbec434f43757e320f14eacb5198e11d4ed083b/docs/feld/2026-10-15-massnahmen-01d.md)

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-HUPROBE-2026-10-15-001` | BMW S0 (FW **0.2.17**, 8 brauchbare Sessions): File-Gap-p50 **~3739 µs** (n=724 Gaps, 729 File-Reads); Read-Event-Mode **4096** dominant; `bot_source=tinyusb`; `dropped=0` / `tcp_tx_fail=0`; keine Writes in ausgewerteten CBWs. | `MEASURED` | S0-Auswertung; Sessions z. B. `2199` |
| `EVID-HUPROBE-2026-10-15-002` | S0 SCSI-Mix (Stichprobe): TUR ≫ READ10 ≫ prevent ≫ mode_sense6 ≫ capacity ≫ inquiry; Timeline fragmentiert (WiFi-Gelb) → GATE-01 weiter OPEN; Burst-Fenster belastbar. | `MEASURED` | S0-Auswertung |
| `EVID-HUPROBE-2026-10-15-003` | BMW S2 Live (FW **0.2.23**, 8 Kern-Sessions): File-Gap-p50 **~3783 µs** (n=632 Gaps, 642 File-Reads) ≈ S0 (~1,2 % Diff); dropped=0; bot tinyusb; File-n=4096 dominant (626/642). | `MEASURED` | S2-Auswertung; Übergabe §5 |
| `EVID-HUPROBE-2026-10-15-004` | S2 READ10-`blocks`: häufig **8** (=4096 B) und **240** (=122880 B → typ. 30×4096 `read`-Events); `read`-Events / READ10-CBW ≈ **5,29**. Event-n=4096 = Stack-Chunk und/oder CBW-Größe — nicht blind „HU-Anfrage immer 4 KiB“. | `MEASURED` | Übergabe §6.1 (Rohdaten-Check) |
| `EVID-HUPROBE-2026-10-15-005` | Nach MODE_SENSE6-Pad (**0.2.18**): S2-Stichprobe **ep_stall=0**; **ms6/cap = 2,0** (60/30 in Kern-Sessions) bleibt → Host-Muster, kein Stall-Indiz. | `MEASURED` | S2-Auswertung; Übergabe §6.3 |
| `EVID-HUPROBE-2026-10-15-006` | S0 Offline-P0: **70/84** ep_stall same-`t_us` wie mode_sense6; ms6/cap=2,0 vor Fix → STALL = **Instrument-Artefakt**, nicht HU-Recovery-FACT. | `MEASURED` → Claim „HU-Recovery“ **`REJECTED`** | offline-p0; massnahmen-01d |
| `EVID-HUPROBE-2026-10-15-007` | Lab Offline E2E **PASS**: Session `20261015-181642_lab_debian_s0_plug_enum`, FW 0.2.23, transport **`ram_offline`**, 96 Records, complete, `auto_soft_detach`, dropped=0. BMW Offline (1 Versuch) **FAIL** (keine `ram_offline`-Session); Auto-Abenddaten = **`tcp_live`**. | `MEASURED` | S2-Auswertung § Lab/BMW Offline |
| `EVID-HUPROBE-2026-10-15-008` | gap_p50(n=4096) / FS-Bulk-Erwartung (~3741 µs) ratio ≈ **1,00** (S0 und S2). Gap-p50 bei File als **Messgröße** FACT; als **HU-Scheduler-Pace** nur `INFERRED` bis LBA/CBW-Formal. gap_p50(n=512) ≫ Link (~42 ms) = echte Pause/Host. | `MEASURED` (Messgröße) / `INFERRED` (Scheduler) | Übergabe §6.1 |
| `EVID-HUPROBE-2026-10-15-009` | Burst-Split `gap_us`>500 ms: File-Reads/Burst p50=**39**, Cluster 39×4096=158208 B, Pause p50~10,2 s — Histogramm auch 62–78. **„immer 39“** = `REJECTED` als FACT; Cluster = `INFERRED`. | `INFERRED` / Konstante `REJECTED` | offline-p0 |
| `EVID-HUPROBE-2026-10-15-010` | Prefetch≈15 s / Eager-EOF / Cache-Hit: S2 liefert dichte Operator-Marker (Autoplay/Tip/RST), viele **nachgezogen**; Semantik **ohne** LBA-Formal = weiter `INFERRED` / `needs_field` (Vor-Audit `EVID-MSCRHS-…`). | `INFERRED` | S2-Auswertung; Messplan-Audit |
| `EVID-HUPROBE-2026-10-15-011` | Read-Kind Gap-p50 (S2): file **3783** · fat **1218** · dir **3813** · boot **20863** µs — informativ; Deutung offen. | `MEASURED` (Zahlen) / Deutung `UNKNOWN` | S2-Auswertung |
| `EVID-HUPROBE-2026-10-15-012` | Mount→INQUIRY p50 ~**997 ms** (n=12 chains); Session-TUR-Hz p50 ~**2,06** (nicht idle); QD-max p50=1 (`INFERRED`, Wire UNKNOWN). Profil `enum_s`/`tur_hz` nicht 1:1 ersetzen. | `MEASURED` / QD `INFERRED` | offline-p0 |
| `EVID-HUPROBE-2026-10-19-001` | TUR-Leerlauf **2239 ms** (p10/p50/p90 2238/2239/2239 ms, n=382, 19 BMW-Sessions), phasenstarr über Reads hinweg. „~1 TUR/s" / „0,8–1/s" = **`REJECTED`**. `012` „TUR-Hz ~2,06" = Fenstermittel inkl. Mount-Burst. | `FACT` | hu-probe `docs/feld/2026-10-19-unabhaengige-auswertung.md` §K2 |
| `EVID-HUPROBE-2026-10-19-002` | Mount-Signatur: INQUIRY 1, READ_CAPACITY10 3, MODE_SENSE6 6, PREVENT_ALLOW 7, **32 TUR** (≈15 als Burst in 0,05–0,29 s); 11 READ10 fest `0/8,0/8,24/8,0/8,0/1,1/3,7/2,1/1,2/1,3/5,24/8` (Variante 3/5 → 3/1+4/4 in `195657`, `2363`). | `FACT` | §2 P-MOUNT/P-MREAD |
| `EVID-HUPROBE-2026-10-19-003` | LBA 24/8 doppelt im Mount, liegt in TRACK1 (9–317). Zweck unbekannt. | `MEASURED` / Zweck `UNKNOWN` | §2 P-LBA24 |
| `EVID-HUPROBE-2026-10-19-004` | Resume-Read 0,2–0,3 s nach Mount; zyklischer Next-Track-Read T(n)→T(n+1), T3→T1, ≈ 9–16 s nach Read-Start bzw. 11–18 s vor Ende bei 26,5 s (n≈10). Ob die Regel am Vorlauf vor dem Ende oder an der Verzögerung nach dem Start hängt, ist offen. | `MEASURED` / Regel `INFERRED` | §2 P-RESUME/P-NEXT |
| `EVID-HUPROBE-2026-10-19-005` | Auswahllatenz Marker→READ: manuell 1,7–1,9 s; Autoplay-Sprung ≈ 0,2 s. Marker teils nachgezogen. | `MEASURED` | §2 P-SEL |
| `EVID-HUPROBE-2026-10-19-006` | tail_then_head: T1 als Folgetrack 8/9 Ende zuerst; T2/T3 immer Kopf zuerst. | `MEASURED` / Ursache `UNKNOWN` | §2 P-TAIL |
| `EVID-HUPROBE-2026-10-19-007` | `075344`: Offline-Puffer = BOT-Tags 81–122 (123 Rec); TUR(1)→REQUEST_SENSE→PREVENT(1) = Tags 131–146 live nach `hideMedia()` = **Media-Loss-Grammatik**. „Enum-Grammatik" = **`REJECTED`**. | `FACT` | §K1 |
| `EVID-HUPROBE-2026-10-19-008` | 57,33 s `gap_us` ≠ Enum→Read; der Read lag ≈ 15,7 s nach dem Arm. M3 „Prefetch geschwächt" → **`HYPOTHESIS`** (Cache-Hit bei identischen Tracks gleich plausibel). | `REJECTED` / `HYPOTHESIS` | §K3/K4 |
| `EVID-HUPROBE-2026-10-19-009` | B21 = Klassifikator-Artefakt (Hardcode-Bänder ≠ Demo-FAT); B7-Ursache = `ProbeClock::publishUs()`-Klemmung im Replay. Fix FW 0.2.31. | `FACT` (Instrument) | §K5/K6 |
| `EVID-HUPROBE-2026-10-19-010` | T2-Atom offline `(318,240)+(558,69)`, 158208 B, Session `20261019-075344` (FW-Label 0.2.30, sha `5a33518`, B20). | `FACT` | `docs/feld/2026-10-19-bmw-s2-t2-offline.md` |
| `EVID-HUPROBE-2026-10-15-013` | Upstream `profiles/bmw_nbt_evo.json` war zum Audit-Pin `5dbec43` noch **PiDrive-`class: FACT`** (eager/prefetch/cache/gap_ms…); **P1c damals offen**. **Nachzug 2026-10-17:** schema 3 mit `origin: hu_probe_field` für Transport (Gap µs, Event-n, CBW 8/240, writes, ms6/cap, bot_source); Semantik abgestuft; A7-Sequenz aus PiDrive MessCapture als `pidrive_field`. | `FACT` (Stand 15.10.) → **P1c closed 17.10.** | Profil @ `5dbec43` (offen); Upstream-Patch 2026-10-17; checklist `docs/feld/2026-10-15-p1c-checklist.md` |

## Claim-Diff vs. Vor-Audit / Profil

| Claim | Vorher (hu-probe Desk / Profil) | Neu (diese Kampagne) |
|-------|----------------------------------|----------------------|
| Gap-p50 ~4 ms | Profil `gap_ms_p50_*` PiDrive; `needs_field` | S0 ~3739 µs / S2 ~3783 µs **MEASURED** als Messgröße; Scheduler INFERENCE |
| read_size 4096 | Profil FACT pidrive | Event-Mode bestätigt; CBW `blocks` oft 8 **und** 240 — Profil nicht blind „HU-Pace“ |
| ms6/cap / Stalls | Stalls als mögl. HU-Recovery | Stalls Instrument (`REJECTED` HU); Ratio 2,0 = HU `MEASURED` |
| Burst-39 | teils als FACT diskutiert | Konstante `REJECTED`; Cluster INFERENCE |
| Prefetch ~15 s | Profil FACT pidrive / hypothesis | weiter INFERENCE (`010`) |
| Offline-Capture | geplant | Lab PASS / BMW FAIL (`007`) |
| Profil P1c | offen (`013`) | **done 2026-10-17** Upstream schema 3 |

## Profil-P1c — ausgeführt 2026-10-17 (Upstream)

Gesicherte hu-probe-Feldwerte mit `origin: hu_probe_field`, `fw` Pins (plus PiDrive A7 als `pidrive_field`):

| Key | Wert | class / Hinweis |
|-----|------|-----------------|
| `gap_us_p50_file_s0` / `_s2` | ~3739 / ~3783 | FACT Messgröße; Caveat: nicht Scheduler |
| `read_event_n_mode` | 4096 | FACT Event-Ebene |
| `read10_blocks_mode_common` / `read10_max_blocks` | [8, 240] / 240 | FACT CBW; getrennt von Event-n |
| `writes_expected` | false | FACT (gesehen) |
| `bot_source` | tinyusb | FACT Instrument |
| `mode_sense6_per_capacity` | 2.0 | FACT HU-Muster |
| `eager_eof` / `prefetch_lead_s` / `cache_hit_*` | INFERENCE / HYPOTHESIS | **nicht** hochgestuft |
| `full_file_512kib_block_seq` | [240,240,32,240,240,32] | FACT `pidrive_field` (MessCapture A7) |
| `burst_file_reads_always_39` | — | **REJECTED** (im Profil `rejected`) |

Epistemik: PiDrive klar von `hu_probe_field` getrennt.

## Offene Claims (ohne neue ID)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Prefetch-Lead formal (LBA + Marker) | `UNKNOWN` / `needs_field` | GATE-01 mit FW 0.2.31 `capture_t_us`; Regel via `SEQ-DUR` |
| Prefetch geschwächt / read-all (M3) | `HYPOTHESIS` | `SEQ-CACHE` mit unterschiedlichem Inhalt pro Track |
| Eager-EOF S1 ≥4 MiB | `UNKNOWN` | P3 |
| Cache-Hit S3 | `UNKNOWN` | P2 Rest |
| BMW Offline-Ursache | `UNKNOWN` | P0c |
| WiFi-Death Root-Cause | `UNKNOWN` | Coex parallel |
| Wire / QD hard | `UNKNOWN` | |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-15 | Desk Messplan `msc-host-read-semantics-s1s2s3-2026` (keine NBT-Zahlen) |
| 2026-10-15 | S0 Feld 0.2.17 + Offline-P0 + MODE_SENSE6 Fix 0.2.18 |
| 2026-10-15 | Lab ram_offline 0.2.23 PASS; BMW Offline FAIL; S2 Live Transport |
| 2026-10-15 | Übergabe Multi-KI + Rohdaten-Check @ `5dbec43` |
| 2026-10-15 | Diese Kampagne: Evidence + Applications in technology-audit |
| 2026-10-17 | Upstream P1c: `bmw_nbt_evo.json` schema 3; `013` geschlossen; PiDrive A7/CBW-max eingezogen |
| 2026-10-19 | T2 offline (`075344`); unabhängige Auswertung aller BMW-Sessions: `EVID-HUPROBE-2026-10-19-001…010` (TUR 2,239 s, Mount-Signatur, Media-Loss-Grammatik, M3 → HYPOTHESIS, B7/B21 Ursachen) |
