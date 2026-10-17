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
| Prefetch-Lead formal (LBA + Marker) | `UNKNOWN` / `needs_field` | P0b |
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
