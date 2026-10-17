# Evidence — pidrive-2026-storm-capture-tooling

Desk 2026-10-18 · **standard_version 0.7.1** · Profile `lab-tool` · keine Builds,
keine USB-Hardware, kein NBT-Capture.

## Quellen-Snapshots

| Repository | SHA | Fokus-Pfad | Lizenz (GitHub/Datei) |
|------------|-----|------------|------------------------|
| https://github.com/MPunktBPunkt/pidrive | `2f58066d374860f7e5a5fbe17a713d3aeae58364` | `docs/betrieb/artifacts-2026-10-17-feld/MASSNAHMEN-NACH-LIVELOCK-AUDIT-2026-10-17.md`, `tools/mess_hu_capture.py`, `tools/mess_band_report.py` | (Projekt) |
| https://github.com/MPunktBPunkt/esp32.pidrive | `4340866325d9dce9aedab365dd3fe3afe05553d3` | `src/msc/MessCapture.{h,cpp}`, `UsbMscGadget.{h,cpp}`, `MscGeometry.h` | (Projekt) |
| https://github.com/SecurityRonin/fat-forensic | `a2ea7b0defe9e0430aa33770bef498e7c9b3a8f1` | `core/src/{lib,fs,boot,fat}.rs`, `forensic/src/lib.rs`, README | Apache-2.0 |
| https://github.com/forensicanalysis/fslib | `8b57b816f61e154765260cb246328da4c5091742` | `fat16/`, README | MIT · **archived** |
| https://github.com/msuhanov/dfir_ntfs | `ec3ae0884048ade106c91a68dab7c9fb3af393bf` | `fat_parser`, `dfir_ntfs/addons/FAT.py` | GPL-3.0 |
| https://github.com/sdgathman/lbatofile | `4ad5c9fddd360ac3f9d91816ba266e774392a630` | `lbatofile.py` | GPL-2.0 |
| https://github.com/cea-sec/usbsas | `77079c28b903aa2eaa6e89d96a2ce08239ce7a9c` | `usbsas-scsi/`, `usbsas-fsrw/`, README | GPL-3.0 |
| https://github.com/yeet-src/usbsnoop | `30f9fad04871252934ca0edd74b0089cb96688da` | `main.js` `decodeScsi`, README | `UNKNOWN` (GitHub `null`) |
| https://github.com/pixfid/luft | `ff000d2c359ace75b9f5b34d4193b67064cbd83d` | README (`events --mass-storage`) | MIT |
| https://github.com/Viaszx/BMW_HU_Info | `c140b1d62ca59e0043a8c620eb390c96e6272c76` | nur `README.md` | `null` |
| https://github.com/hathach/tinyusb | `98741b55959564746998d0453c32d87064629d7c` | `examples/device/cdc_msc`, `msc_dual_lun` | MIT |

usbsnoop-Pin identisch mit
[`usb-bot-observation-2026-instrument-sources`](../usb-bot-observation-2026-instrument-sources/)
(`30f9fad`). TinyUSB HEAD neu; MSC-Hook-Claims der Vor-Kampagne bleiben gültig
(Schema unverändert geprüft über Beispielpfade, keine Hook-Neuaufnahme).

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-STORMTOOL-2026-10-18-001` | `MessCapture` rekonstruiert READ10-Grenzen aus TinyUSB-Chunk-Callbacks (`noteRead10Chunk`/`noteRead10Complete`); `MessCmd` trägt `lba`, `bytes`, `chunks`, `busyN`, `op`, Timestamps (`t0Us`/`t1Us`/`gapUs`), Ring bis 512 (`PIDRIVE_MESS`). | `FACT` | `MessCapture.h` @ `4340866` |
| `EVID-STORMTOOL-2026-10-18-002` | Linker-Wrap `__wrap_tud_msc_read10_cb` instrumentiert den realen Callback und ruft `noteRead10Chunk` auf — Device-seitiges LBA-Journal ohne CBW-Struct-Fork. | `FACT` | `MessCapture.cpp` Wrap @ `4340866` |
| `EVID-STORMTOOL-2026-10-18-003` | `pidrive` Tool `mess_hu_capture.py` arm/dump/q10 steuert Soft-USB + Mess-Dump (HTTP Lab-API); dokumentiert Feld-CBW-Blöcke 8/240. | `FACT` | `tools/mess_hu_capture.py` @ `2f58066` |
| `EVID-STORMTOOL-2026-10-18-004` | `UsbMscGadget` zählt getrennt `bytesBoot`/`bytesFat`/`bytesDir`/`bytesMeta`/`bytesFile`, `prefetchHits`, `playGuessCount`; Slot-Stats `fromHead`/`midFile`; Events `play.guess` / `msc.prefetch`. | `FACT` | `UsbMscGadget.cpp` Accounting + `toJson` @ `4340866` |
| `EVID-STORMTOOL-2026-10-18-005` | Maßnahmen M30–M32 fordern eine Session mit UART + Storm-Capture + Status-Achsen + LBA/Read-Klasse + Guess-Korrelation; Q/S nie über `reads/rej` allein. | `FACT` (Upstream-Doku) | `MASSNAHMEN-NACH-LIVELOCK-AUDIT-2026-10-17.md` @ `2f58066` |
| `EVID-STORMTOOL-2026-10-18-006` | `mess_band_report.py` mappt READ10-`lba` auf Bands (`boot_fat`, `root_dir`, `DIR_*`, `file_fav0/1/2`, …) für **L3 Favoriten**-Geometrie — Post-Capture LBA→Read-Klasse ohne Fremd-Parser. | `FACT` | `tools/mess_band_report.py` @ `2f58066` |
| `EVID-STORMTOOL-2026-10-18-007` | `fat-forensic`/`fat-core`: Auto-Detect FAT12/16/32/exFAT; `Geometry` mit `cluster_offset`; `follow_chain`; `FatFs::runs(id) → Vec<(offset,len)>`; Auditor für Boot/FAT-Mirror/Deleted — **kein** öffentliches `lba_to_path`. | `FACT` | README, `boot.rs`, `fat.rs`, `fs.rs` `runs` @ `a2ea7b0` |
| `EVID-STORMTOOL-2026-10-18-008` | Reverse LBA→Datei mit `fat-forensic` wäre **eigenes** Indexieren über Directory-Walk + `runs()` / `cluster_offset` (Byte-Offset÷512 → LBA) — INFERENCE für Pipeline-Design, nicht Upstream-API. | `INFERENCE` | abgeleitet aus `007` |
| `EVID-STORMTOOL-2026-10-18-009` | `UsbMscGadget`/`MscGeometry` pinnt Virtual-FAT-Layout (Legacy/L0/L0-16M/L3); `fileForLba`, `metaTag` (BOOT/FAT/DIR), `lbaToCluster` — Runtime-Klasse ohne externes Image. | `FACT` | `MscGeometry.h`, `UsbMscGadget.h/.cpp` @ `4340866` |
| `EVID-STORMTOOL-2026-10-18-010` | `lbatofile.py` registriert `EXTLayout` und nutzt `debugfs icheck/ncheck` — **kein** FAT/VFAT-Layout. Für PiDrive-Virtual-FAT ungeeignet. | `FACT` | `lbatofile.py` `EXTLayout` / `icheck` @ `4ad5c9f` |
| `EVID-STORMTOOL-2026-10-18-011` | usbsnoop dekodiert BOT CBW `READ(10) lba=… blocks=…` und CSW; eBPF an `usb_submit_urb`/`usb_hcd_giveback_urb`; Lizenz am Pin weiter `UNKNOWN`. Geeignet als **Lab-Host**-Gegenprobe, nicht als NBT-Feldspur. | `FACT` | `main.js` `decodeScsi`; GitHub license null; Reuse Vor-Kampagne |
| `EVID-STORMTOOL-2026-10-18-012` | `usbsas`: Userspace SCSI/BOT (`usbsas-scsi` CBW/CSW, `read_10`) + FAT-FS (`usbsas-fsrw`) zum sicheren Lesen untrusted MSC — Host-Sheepdip/Forensik, **kein** Device-Gadget-Storm-Journal. | `FACT` | README, `cdb.rs`, `bot.rs` @ `77079c2` |
| `EVID-STORMTOOL-2026-10-18-013` | `luft`: USB-Event-Log mit Filter `--mass-storage` — Connect/Whitelist, **kein** SCSI/LBA-Decode. | `FACT` | README @ `ff000d2` |
| `EVID-STORMTOOL-2026-10-18-014` | `BMW_HU_Info` Tree enthält nur `README.md` (NBTEVO/MGU Claims ohne Code). | `FACT` | Tree @ `c140b1d`; Reuse `bmw-nbt-media-index` |
| `EVID-STORMTOOL-2026-10-18-015` | Kein geprüftes Repo implementiert Q-vs-S-Stuck-Klassifikator oder Prefetch-Livelock-Detektor auf den PiDrive-Statusachsen. | `FACT` (Negativbefund Desk) | Corpus-Scan dieser Kampagne |
| `EVID-STORMTOOL-2026-10-18-016` | `fslib` archived; `fat16` mit Cluster→Byte-Offset (`getOffset`), kein generisches LBA→Pfad; nur FAT16 im Bundle. | `FACT` | GitHub `archived`; `fat16.go` @ `8b57b81` |
| `EVID-STORMTOOL-2026-10-18-017` | `dfir_ntfs` liefert `fat_parser` + `addons/FAT.py` / exFAT für Offline-Volumes (Timestamps/Struktur). | `FACT` | `fat_parser`, Tree @ `ec3ae08` |
| `EVID-STORMTOOL-2026-10-18-018` | TinyUSB bleibt MSC-Device-Grundlage (`cdc_msc`, `msc_dual_lun` Beispiele am Pin). | `FACT` | Tree examples @ `98741b5` |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „lbatofile löst M32 für Virtual-FAT“ | `REJECTED` | nur EXT (`010`) |
| „fat-forensic = fertiges Storm-LBA→UID“ | `REJECTED` | kein Reverse-API (`007`); Index Eigenarbeit (`008`) |
| „usbsnoop-Capture = NBT Storm“ | `REJECTED` | Linux-Host-eBPF; NBT `UNKNOWN` (`011`) |
| „luft deckt Mass-Storage-Reads ab“ | `REJECTED` | nur Events (`013`) |
| „BMW_HU_Info ist Capture-Implementierung“ | `REJECTED` | README-only (`014`) |
| „Fremdrepo liefert Q/S-Klassifikator“ | `REJECTED` | `015` |
| „Meta-Rescan verursacht Storm“ aus Tool-Dasein | `REJECTED` | Abend-Audit: Meta session-konstant; Tools beweisen das nicht neu |

## Pipeline-Skizze (Desk-Hypothese, kein Lab-FACT)

```text
Feld P0 (M30)
  UART ──┐
  MessCapture.arm → OTG → Storm-Fenster → dump cmds[]  ──┐
  Status-Poll (pref/midFile/bytes*/guess) + Event-Log ──┼─► Artefakt-Bundle
                                                         │
Post (M32)                                               ▼
  mess_band_report(mess.json)  → Band-Histogramm / Timeline
  optional: Guess-Timestamps × Band vor Guess
  optional P2: fat-forensic audit auf exportiertem Image (Struktur)

Lab parallel (nicht Fahrzeug)
  usbsnoop / Wireshark-USB am Kontrollhost ↔ Device-MessCapture Tag/LBA
```

## Engineering Review Checks aus Evidence

| Evidence-ID | Review Check |
|-------------|--------------|
| `001`–`003` | Capture aktiv + Drops; Dump nach Storm vor Ring-Overwrite |
| `004`–`005` | Q/S-Label aus pref/midFile/bytesFile/Ohr, nie nur reads/rej |
| `006`/`009` | Geometrie-Profil (L3 vs Legacy) im Artefakt vermerken |
| `010` | lbatofile nicht in Runbooks |
| `011` | usbsnoop LICENSE-Hinweis; nur Lab |
| `007`–`008` | fat-forensic optional; Reverse-Index nicht als „Upstream-Feature“ verkaufen |

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| Storm-Episode: dominante Bands = File-Body (nicht Meta) | `UNKNOWN` | Feld M30 Dump + `006` |
| Read-Klasse unmittelbar vor Storm-Guess | `UNKNOWN` | M32 Korrelation |
| Runtime-`class` in MessCmd vs post-hoc Report | `UNKNOWN` | FW-/Tool-Entscheidung |
| usbsnoop↔MessCapture LBA-Match Lab | `UNKNOWN` | Lab (Vor-Kampagne Kill präreg.) |

## Wissens-Chronik

| Zeitpunkt | Label |
|-----------|-------|
| Vor diesem Desk | Livelock-Abend: Meta konstant, Storm=File-Body-Hypothese, Capture fehlt |
| Während Desk | Eigener Stack deckt M30/M32-Bausteine; lbatofile/luft/BMW_HU_Info fallout |
| Nach Desk | Feld-Session bleibt P0; Fremd-FAT nur optional Post |

## Querverweise

- [`pidrive-2026-10-17-prefetch-livelock`](../pidrive-2026-10-17-prefetch-livelock/) — Muster Q/S; Exit #9 Capture
- [`usb-bot-observation-2026-instrument-sources`](../usb-bot-observation-2026-instrument-sources/) — usbsnoop/TinyUSB Hooks
- [`bmw-nbt-media-index-2026-foreign`](../bmw-nbt-media-index-2026-foreign/) — BMW_HU_Info README-only
