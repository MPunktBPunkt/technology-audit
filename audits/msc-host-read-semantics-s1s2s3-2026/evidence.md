# Evidence — msc-host-read-semantics-s1s2s3-2026

Desk 2026-10-15 · **standard_version 0.7.1** · Profile `lab-tool` · keine
Builds, keine USB-Hardware, kein neuer NBT-Messlauf. Zahlen aus PiDrive bleiben
**Herkunfts-Claims**, nicht hu-probe-`FACT`.

## Quellen-Snapshots

| Repository / Artefakt | SHA / Pin | Vertiefter Pfad | Lizenz / Rolle |
|-----------------------|-----------|-----------------|----------------|
| https://github.com/MPunktBPunkt/hu-probe | `463c0f022a9b37d4ee1b37cfe5b6fd49e9a19f99` | `profiles/bmw_nbt_evo.json`, `docs/SZENARIEN.md`, `docs/SCHEMA.md`, `docs/GATES.md`, `docs/KONZEPT.md` | eigenes Instrument |
| https://github.com/MPunktBPunkt/pidrive | `8223719b85fd9a9089fa2ee3971999c254bf2b59` | `tools/profiles/nbt_evo_*.json`, `tools/nbt_hu_sim.py` (G4N), `docs/fahrzeug/HU-Technical-Facts.md` (R15–R21), archivierte ANALYSE/MASSNAHMEN 2026-10-06/07 | Claim-Herkunft |
| https://github.com/MPunktBPunkt/technology-audit | `9b0a28e3f021110d7c5102f086475f5c1aef97c5` (pre-this) | `audits/pidrive-2026-msc`, `pidrive-2026-bmw-hu`, `esp32-msc-gadget-refs-2026-foreign` | Claim-Trennung A/B/C |
| https://github.com/hathach/tinyusb | `ea1d867ced5259d49679f481e5d4e21a36dc11b0` | `examples/device/cdc_msc/src/msc_disk.c`, `src/class/msc/msc_device.h` (`tud_msc_read10_cb`) | MIT |
| https://github.com/espressif/esp-idf | `ab95e70748f2eddac6f87217b0cf62533684a6ba` | `examples/peripherals/usb/device/tusb_msc/` | Apache-2.0 |
| https://github.com/aoscarius/esp32usbmsc | `67ffb6b383af753c205e6dd049ea5c19da5f456e` | `src/main.cpp` (`onRead`, `DISK_SIZE_BYTES`) | siehe Upstream |
| https://github.com/espressif/esp-usb | `c40b86dc3a3e760b3dfdc28ec83010b9799a7e88` | `host/class/msc/usb_host_msc/README.md` | Lab-Host-Kontrast |
| https://github.com/torvalds/linux | `2c0f5ca48674a5b5f9fa4a9c3325aa48053af0bc` (Reuse Vor-Kampagne) | Gadget `f_mass_storage` / Host `usb-storage` (Fußnote) | GPL-2.0-or-later |

Pfadspezifische Pins sind keine Aussage über den gesamten Upstream.

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-MSCRHS-2026-10-15-001` | hu-probe `bmw_nbt_evo.json` markiert `eager_eof`, `prefetch_lead_s_approx=15`, `cache_hit_no_reads_on_replay` als `class: FACT` mit `origin: pidrive_field` und vermerkt epistemisch „FACT from PiDrive field evidence — not HU specification“. Open gates inkl. `HU-A1`/`HU-A2`. | `FACT` (Profiltext) | hu-probe Profil @ `463c0f0` |
| `EVID-MSCRHS-2026-10-15-002` | PiDrive-Modell „File-Cache / Eager-Read“: gewählte Datei wird bus-schnell bis EOF oder Abwahl gelesen; Burst = ungelesener Dateirest (u. a. 524 288 B = Slotgröße). Belege ANALYSE B1–B5; Ampel MSC-AKTUELL. | `MEASURED` (PiDrive-Feld) → für hu-probe **`needs_field`** | ANALYSE 2026-10-06; `EVID-USBMSC-2026-10-04-001` Kontext |
| `EVID-MSCRHS-2026-10-15-003` | Next-Track-Prefetch **R21**: ~15 s vor Wiedergabe-Ende (nicht unmittelbar nach Read-EOF); Status [S] (2 Fälle, 1 Ausreißer ~7 s). Lab-Anker `nbt_hu_sim` G4N `lead_s=15.0`. | `hypothesis` / PiDrive `[S]` → hu-probe **`needs_field`** | `HU-Technical-Facts.md` R21; `nbt_hu_sim.py`; KALIBRIERUNG-LAB |
| `EVID-MSCRHS-2026-10-15-004` | Cache-Hit / Muster B: Datei vor Arm schon komplett gelesen → kein Body-Read, `hostAbs≈0` (PiDrive-Telemetrie). hu-probe erwartet `cache_hit_no_reads_on_replay: true` und Szenario `s3_cache_hit`. | PiDrive `MEASURED` (Session) → hu-probe **`needs_field`** | ANALYSE B3; Stufenplan G2; Profil |
| `EVID-MSCRHS-2026-10-15-005` | 512 KiB-Slot: Bus-Read ≈0,6 s bei ~0,85 MB/s — zu kurz, um Batch-then-Play vs. inkrementellem Decode zu trennen (ANALYSE §4). S1 braucht größere Slots; 512 KiB bleibt Kontrollzelle. Busy-Tonfenster S6 nutzte bewusst 512 KiB (`EVID-BMWHU-2026-10-12-002`) — **anderer** Zweck. | `FACT` (Rechnung+Desk) / Empfehlung | ANALYSE; bmw-hu Evidence |
| `EVID-MSCRHS-2026-10-15-006` | TinyUSB: `tud_msc_read10_cb(lun, lba, offset, buffer, bufsize)`; Example `cdc_msc` mappt `msc_disk[lba]+offset` → memcpy, Capacity `DISK_BLOCK_NUM`×512. | `FACT` | tinyusb @ `ea1d867` |
| `EVID-MSCRHS-2026-10-15-007` | IDF `tusb_msc`: bis 2 LUNs (SPI-Flash / SDMMC), Storage-Exposure vs. App-Mount; kein NBT-Timing. | `FACT` | esp-idf `tusb_msc` @ `ab95e707` |
| `EVID-MSCRHS-2026-10-15-008` | `esp32usbmsc`: FAT12 in RAM/PSRAM, `DISK_SIZE_BYTES=1 MiB`, `onRead(lba,offset,buf,bufsize)` = memcpy aus `msc_disk` — Muster „Host liest feste Blöcke“. | `FACT` | aoscarius @ `67ffb6b`; Reuse `EVID-VFAT-2026-10-12-*` |
| `EVID-MSCRHS-2026-10-15-009` | Linux `usb-storage` / Mass-Storage-Gadget und esp-usb Host-MSC (BOT/SCSI FatFS) beschreiben **Lab-Normalhosts** inkl. VFS/Newlib-File-Cache — **nicht** NBT-Prefetch. | `FACT` (Kontrast) | linux Pin; esp-usb README; Kill-Regel |
| `EVID-MSCRHS-2026-10-15-010` | technology-audit trennt bereits Spec (A) / PiDrive-Impl (B) / HU-C; HU-A1…A11 präregistriert `UNKNOWN`. Open_gate-Logik bleibt verbindlich. | `FACT` | `pidrive-2026-bmw-hu` README |

## PiDrive-Claim → Evidence-Status (für hu-probe S1–S3)

| PiDrive- / Profil-Claim | Herkunft (kurz) | Status für hu-probe S1–S3 |
|-------------------------|-----------------|---------------------------|
| `eager_eof = true` | ANALYSE B1–B4; Profil | **`needs_field`** (S1, größeres Medium) |
| `prefetch_lead_s ≈ 15` | R21 [S]; G4N-Sim-Default | **`hypothesis`** → **`needs_field`** (S2 + Marker) |
| `cache_hit_no_reads_on_replay` | Muster B / G2 | **`needs_field`** (S3) |
| `resume` out-of-order window | R16; Fingerprint-Template; HU-A2 open | **`needs_field`** (nicht S1–S3-Kern; Gate A2) |
| `read_size_bytes_mode = 4096` | Profil / Trace-Hist | **`needs_field`** (Revalidate mit `t_us`) |
| `gap_ms_p50 ≈ 4` | prior ms-quantized | **`needs_field`** (Caveat im Profil) |
| `busy_tone_s ≈ 65` / stall-off ≈ 6 | S6 `EVID-BMWHU-2026-10-12-*` | **out of S1–S3 scope** (S5); nicht hier neu zählen |
| „Burst = Decoder-Puffer“ | frühere Deutung | **`superseded`** (ANALYSE: Burst = Dateirest) |
| „kleiner Ring = Dauerstrom-Grenze“ | vor S6 | **`superseded`** (`EVID-BMWHU-2026-10-12-005`) |
| Linux VFS Read-Ahead = NBT-Prefetch | — | **`superseded`** / Kill (nie FACT) |
| Wire-/Paket-Claims | — | **verboten** (UNKNOWN bleiben) |

## Marker-Protokoll (S2/S3) — Spez-Kern

Operator-/Ohr-Marker in `markers.jsonl` (Schema v2), Pflichtfelder: `t_us` oder Session-relativ + Label.

| Marker-ID | Wann setzen | Pflicht für |
|-----------|-------------|-------------|
| `play_start` | hörbarer/bestätigter Track-Start (oder UI-Play) | S2, S3 |
| `track_next` | Auto-Next oder manuelle Wahl nächster Slot | S2 |
| `audible_change` | Ohr: Inhalt/Sender hörbar gewechselt | S2 |
| `replay` | derselbe Track erneut, **ohne** Replug | S3 |
| `stop` | Stop / Pause / Abwahl | S2, S3 |

Korrelation: Marker-`t_us` gegen READ10-Timeline (`msc-trace-correlation` + Method).

## Auswerte-Regeln (Skript-Spez, keine Zahlen)

Eingabe: `events.jsonl` (read/BOT) + `markers.jsonl` + LBA→Datei-Map.

| Regel | Definition (boolean / Metrik) | Szenario |
|-------|-------------------------------|----------|
| LBA-Monotonie | Innerhalb einer Datei-LBA-Range: steigende LBA (Toleranz: kleine Rücksprünge ≤ dokumentiertem Fenster) | S1, S2 |
| Bytes-bis-EOF | Summe gelieferter Bytes in Datei-Range bis `file_size` oder Abwahl-Marker | S1 |
| Reads-vor-hörbarem-Wechsel | READ10 auf **next**-Slot mit `t_us < audible_change` (und typ. nach `play_start` auf current) | S2 |
| Reads-bei-Replay-ohne-Replug | Nach `replay`: Body-Reads in Datei-Range == 0 (oder unter Schwelle) bei unveränderter Identity | S3 |

Skript-Ausgabe: pro Session `derived/s1s2s3_eval.json` mit Pass/Fail/UNKNOWN je Regel — **ohne** Golden-Zahlen hardcoden.

## Medium-Empfehlung S1

| Slot | Größe | Rolle |
|------|-------|-------|
| Kontroll-Slot | 512 KiB | Vergleich zu PiDrive-L3; Eager-Vollread in &lt;1 s Buszeit |
| Mess-Slot(s) | **≥ 4 MiB**, besser 8 MiB+ (unterscheidbare Audio-/Stille-Marker) | Bytes-bis-EOF und Play-vs-Read zeitlich trennen |
| Prefetch-Nachbar | gleiche Geometrie, anderer Marker-Inhalt | S2 Next-Slot sichtbar |

Virtual-FAT: feste Sample-Dateien (Muster `esp32usbmsc` / bestehende gadget-refs); Identity konstant außer gezielten A2-Läufen.

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „Profil-FACT = hu-probe hat gemessen“ | `REJECTED` | `001` origin pidrive |
| „15 s ist NBT-Spezifikation“ | `REJECTED` | R21 [S]; nicht Spec |
| „Lab-dd Prefetch = NBT“ | `REJECTED` | `009` |
| „S1 mit nur 512 KiB beweist Eager-Semantik vollständig“ | `REJECTED` | `005` |
| Neue NBT-Millisekunden aus diesem Desk | `REJECTED` | Scope |

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| S1 Eager-EOF an hu-probe | `UNKNOWN` | Session `s1_eager_eof` |
| S2 Prefetch-Lead (Zahl) | `UNKNOWN` | Session `s2_prefetch` + Marker |
| S3 Cache-Hit ohne Replug | `UNKNOWN` | Session `s3_cache_hit` |
| GATE-01 Messintegrität | open (Upstream) | hu-probe GATES.md |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-04..12 | PiDrive MSC / BMW-HU Evidence; Busy S6 |
| 2026-10-06..07 | File-Cache-ANALYSE; R21 ~15 s; HU-Sim G4N |
| 2026-10-14 | hu-probe Profil + Szenarien; Coex/BOT-Audits (Instrument) |
| 2026-10-15 | Dieses Desk: Messplan S1–S3, Claim-Status, Method |
