# hu-probe — PSRAM / Board / free Offline — 2026-10-21

**Delta-Audit seit Abend-Offline 2026-10-18**

| Feld | Wert |
|------|------|
| Repo | `MPunktBPunkt/hu-probe` @ **`f985459`** |
| FW Pin | **0.3.1** (PlatformIO); Kernfeld **0.2.40** free Offline |
| Audit | [`audits/hu-probe-psram-board-free-2026-10-21/`](../../audits/hu-probe-psram-board-free-2026-10-21/) |
| Profil | `profiles/bmw_nbt_evo.json` (schema 3, stark erweitert) |
| Board | YD-ESP32-S3 **N8R2** · 8 MiB Flash · 2 MiB Quad-PSRAM |

---

## 1. Kurzfazit

Drei Dinge sind seit dem letzten Audit belastbar neu:

1. **PSRAM ist an** (`qio_qspi` + `BOARD_HAS_PSRAM`) — Offline-Capture im Feld **1 MiB** statt ~32 KiB.  
2. **Board ist kartiert** (YD 2022-V1.4, Dual-USB-C, Pinout, Versorgungsregeln) — aber HARDWARE.md §2.3 ist **noch auf „PSRAM aus“** stecken geblieben.  
3. **free Offline 0.2.40** liefert die Host-Grammatik auf `demo_v1`: volles **240+69**-Atom am Trackwechsel, Idle nur TUR **~2239 ms**, **kein** File-Prefetch; Prefetch-~15 s und „next_track 9–18 s“ sind für dieses Medium beerdigt bzw. als Resume umgedeutet.

Größenleiter / große-Datei-Fenster und Drive-Home 0.3.x bleiben **OPEN**.

---

## 2. Board & PSRAM

### 2.1 Hardware (FACT / Betreiber)

| Merkmal | Wert |
|---------|------|
| Board | VCC-GND Studio YD-ESP32-S3, Silkscreen 2022-V1.4 |
| Modul-Ziel | **N8R2** (8 MiB Quad-Flash + 2 MiB Quad-PSRAM) |
| Ports | **USB** = nativer OTG (HU); **COM** = CH343P UART |
| LED / BOOT | RGB GPIO48; BOOT GPIO0 = Marker/Stop |
| Feldversorgung | HU allein kann speisen; Standard: COM am Netzteil |

Brückenregel: **USB-OTG offen lassen** (sonst VBUS-Kurz zwischen Netzteil und HU).

### 2.2 Build (FACT)

```text
board_build.arduino.memory_type = qio_qspi
-DBOARD_HAS_PSRAM
board_upload.flash_size = 8MB
board_build.partitions = partitions_huprobe_8mb.csv
```

Nutzung: EventBus-Slots in PSRAM; Offline-Puffer-Stufen bis **1 MiB** in PSRAM; String-Payloads weiter DRAM.

### 2.3 Feld-Messgröße (FACT)

| Ära | `capture.capacity_bytes` |
|-----|--------------------------|
| ≤ 0.2.30 | 24–64 KiB (Feld oft 32 KiB) |
| ≥ 0.2.37 | **1048576** (1 MiB) |

Beispiel free Offline: `075616`/`075935`/`080508` — overflow=0, integrity PASS.

### 2.4 Doc-Drift

`docs/HARDWARE-YD-ESP32-S3.md` §2.3 sagt noch „PSRAM ist nicht aktiviert“. Das widerspricht Build und Sessions → Upstream-Fix (FOLLOW-ON), nicht in diesem Audit-Repo.

### 2.5 Coex

Lab 0.2.35–0.2.39: PSRAM verbessert Heap (`ring_in_psram=1`); **USB↔WiFi-Tod bleibt**. Offline-Pfad bleibt die Messstrategie unter Host-Last.

---

## 3. free Offline Grammatik (`demo_v1`, FW 0.2.40)

### 3.1 Sessions (FACT)

| Session | Setup | Records | Atome / Order |
|---------|-------|--------:|---------------|
| `075616` | schon gesteckt | 69 | 2× head_first (T2→T3) |
| `075935` | Plug nach Start | 207 | 3× head_first (T1→T2→T3) |
| `080508` | Replug mitte T3 | 231 | head / **tail_then_head** / head |

Alle: `ram_offline`, `auto_media_hide`, Upload `delivered`, 1 MiB Capture.

### 3.2 Kanonische Muster

| ID | Muster | Klasse |
|----|--------|--------|
| M1 | Trackwechsel → volles Atom **240+69** = 158208 B (~149 ms) | FACT |
| M2 | Idle: nur TUR **2238–2239 ms**, 0 File-Reads | FACT |
| M3 | Δ `next_track` ≈ **26,473 s** = Trackdauer Medium | FACT (mediengebunden) |
| M4 | Plug→first audio read ≈ **1,51 s** ab set_address | FACT (n=2) |
| M5 | Prefetch-Lead 15 s auf 158 KiB | **REJECTED** |
| M6 | `tail_then_head` = T3→T1 Nearest-LBA (Elevator) | INFERENCE; Re-Entry **REJECTED** |
| M7 | Remount = Resume, nicht Playlist-Restart T1 | FACT (n=1) + REJECT Playlist-Claim |
| M8 | S2 „9–18 s next_track“ | **SUPERSEDED** (Resume-Restzeit) |

CBW-Atom vom Abend-18.10. bleibt die Basis; free schärft **Timing + Idle + Rejects**.

---

## 4. hu-parameter (`bmw_nbt_evo.json`)

Profil enthält u. a. als `hu_probe_field`:

- `tur_idle_period_ms` / `tur_period_ms_precise`
- `demo_v1_track_atom_bytes`, `demo_v1_atom_timing_ms`, `demo_v1_idle_file_reads`
- `plug_to_first_audio_read_s`, `media_loss_*`, `atom_end_to_next_read_s`
- `prefetch_lead_demo_v1_s = 0`
- Rejects: Prefetch-15s, Head-only, Re-Entry, Playlist-T1, next_track-9–18s
- Offen: `read_window_blocks` HYPOTHESIS (A8 / Größenleiter)

---

## 5. Ampel

| Bereich | Status |
|---------|--------|
| Instrument PSRAM / 1 MiB Offline | **grün** |
| Board-Identifikation | **grün** (Doc §2.3 nachziehen) |
| Host-Grammatik demo_v1 / free | **grün** |
| Prefetch große Dateien / Fenster A8 | **gelb** (präregistriert, unausgewertet) |
| Elevator-Test Rückwärtssprung | **gelb** |
| Drive-Home 0.3.x Integrity | **gelb/rot** (Sessions oft ohne Footer) |
| USB↔WiFi Coex Root-Cause | **unverändert offen** (Offline-Workaround) |

---

## 6. Auftrag Next

1. **P0** Größenleiter `seq_size` auswerten → H-A / H-B / H-C abhaken (Feldplan 21.10.).  
2. **P0** Rückwärtssprung D180→D026 (noch ungelesen) → Elevator ja/nein.  
3. **P1** HARDWARE.md §2.3 + Modul-eFuse-Ist (`hw.module`) im Upstream.  
4. **P1** audible-Marker; Replug `ident_b`.  
5. **P2** Drive-Home/TripStore unter 0.3.1 sauber closen (Footer/integrity).

---

## 7. Verweise

- Audit: [`audits/hu-probe-psram-board-free-2026-10-21/`](../../audits/hu-probe-psram-board-free-2026-10-21/)
- Prior: [`2026-10-18-hu-probe-bmw-s2-abend-offline`](2026-10-18-hu-probe-bmw-s2-abend-offline.md)
- Upstream-Feld: `docs/feld/2026-10-20-bmw-free-offline-0.2.40.md`, `docs/HARDWARE-YD-ESP32-S3.md`, `docs/feld/2026-10-21-feldplan-groessenleiter.md`
