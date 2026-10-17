# Audit Campaign: pidrive-2026-storm-capture-tooling

```yaml
id: pidrive-2026-storm-capture-tooling
project_id: pidrive
started: 2026-10-18
ended: 2026-10-18
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: bmw-nbt-evo
prior_audit: pidrive-2026-10-17-prefetch-livelock
related_audits:
  - pidrive-2026-10-17-prefetch-livelock
  - pidrive-2026-bmw-hu
  - usb-bot-observation-2026-instrument-sources
  - bmw-nbt-media-index-2026-foreign
  - msc-host-read-semantics-s1s2s3-2026
upstream_pins:
  - repo: https://github.com/MPunktBPunkt/pidrive
    commit: 2f58066d374860f7e5a5fbe17a713d3aeae58364
  - repo: https://github.com/MPunktBPunkt/esp32.pidrive
    commit: 4340866325d9dce9aedab365dd3fe3afe05553d3
  - repo: https://github.com/SecurityRonin/fat-forensic
    commit: a2ea7b0defe9e0430aa33770bef498e7c9b3a8f1
  - repo: https://github.com/forensicanalysis/fslib
    commit: 8b57b816f61e154765260cb246328da4c5091742
  - repo: https://github.com/msuhanov/dfir_ntfs
    commit: ec3ae0884048ade106c91a68dab7c9fb3af393bf
  - repo: https://github.com/sdgathman/lbatofile
    commit: 4ad5c9fddd360ac3f9d91816ba266e774392a630
  - repo: https://github.com/cea-sec/usbsas
    commit: 77079c28b903aa2eaa6e89d96a2ce08239ce7a9c
  - repo: https://github.com/yeet-src/usbsnoop
    commit: 30f9fad04871252934ca0edd74b0089cb96688da
  - repo: https://github.com/pixfid/luft
    commit: ff000d2c359ace75b9f5b34d4193b67064cbd83d
  - repo: https://github.com/Viaszx/BMW_HU_Info
    commit: c140b1d62ca59e0043a8c620eb390c96e6272c76
  - repo: https://github.com/hathach/tinyusb
    commit: 98741b55959564746998d0453c32d87064629d7c
reuse_outcomes:
  reused:
    - bmw-nbt-evo
    - usb-msc
    - virtual-fat
    - msc-trace-correlation
    - msc-host-read-semantics
  new: []
  not_helped:
    - "sdgathman/lbatofile — nur EXT via debugfs; kein FAT → kein LBA→Datei für Virtual-FAT"
    - "pixfid/luft — nur USB-Connect-Events, kein SCSI/LBA"
    - "Viaszx/BMW_HU_Info — README-only; kein prüfbarer Capture-Code (Reuse Vor-Kampagne)"
    - "forensicanalysis/fslib — archived; nur FAT16; kein LBA→Pfad-Reverse"
    - "Q/S-Klassifikator / Prefetch-Livelock-Detektor — in keinem Fremdrepo vorhanden"
  process: "Desk-Fitness für M30–M32 Pipeline; Pins immutable; kein Build/Lab/Fahrzeug."
  decisions_touched:
    - m30-primary-instrument-own-stack
    - m32-lba-class-via-geometry-not-lbatofile
    - fat-forensic-postcapture-optional
    - usbsnoop-lab-only-license-unknown
```

## Ziel

Geplante Repositories auf **Tauglichkeit für die P0-Pipeline M30–M32** prüfen
(Storm/Q-Capture, LBA/Read-Klasse, File-Body, FAT-Struktur) — was **primär**,
was **post-capture optional**, was **nicht hilft**. Kein Q/S-Klassifikator und
kein Prefetch-Livelock-Detektor in Fremdquellen erwarten (M31 bleibt Eigenbau).

Upstream-Anker Maßnahmen:
[`MASSNAHMEN-NACH-LIVELOCK-AUDIT-2026-10-17.md`](https://github.com/MPunktBPunkt/pidrive/blob/2f58066d374860f7e5a5fbe17a713d3aeae58364/docs/betrieb/artifacts-2026-10-17-feld/MASSNAHMEN-NACH-LIVELOCK-AUDIT-2026-10-17.md)
(`pidrive@2f58066`).

## Scope

- **Im Scope:** Desk-Code/README an gepinnten SHAs; Fitness-Matrix M30/M31/M32;
  Reuse bestehender Instrument-/BMW-Audits; Epistemik FACT/INFERENCE/UNKNOWN.
- **Nicht im Scope:** Firmware-Änderung, Lab-/Feldlauf, Code-Übernahme in Produkt,
  Sheet-A-Claims zu NBT-Verhalten, paralleles neues Technology Sheet,
  Integration-Skelett als lauffähiger Code.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1 + Kampagne + Evidence-Register | erfüllt |
| 2 | Alle 11 Quellen auf immutable SHA | erfüllt |
| 3 | Fitness-Matrix M30/M31/M32 pro Repo | erfüllt |
| 4 | Primärpfad: eigener Stack (`esp32.pidrive` MessCapture + Status + `mess_band_report`) | erfüllt — `001`–`006` |
| 5 | `lbatofile` als FAT-LBA→Datei **REJECTED** | erfüllt — `010` |
| 6 | `fat-forensic` als optionale Post-Capture-Strukturhilfe (nicht Runtime) | erfüllt — `007`–`008` |
| 7 | usbsnoop: Lab-Host-Validate; Lizenz `UNKNOWN`; ≠ NBT-Capture | erfüllt — Reuse + `011` |
| 8 | Gap M31 (Q/S) / fertiger Livelock-Detektor dokumentiert | erfüllt — `015` |
| 9 | C10–C13; kein neues Sheet | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| M30-Instrumentierung primär im eigenen Stack | Hat `esp32.pidrive` bereits LBA-Journal + Meta/File-Zähler + Guess-Events? | `001`–`005` | Ja — P0 = Session mit UART+MessCapture+Status-Poll, nicht neues Fremd-FW | `DISCOVERED DURING TEST` |
| M32 LBA→Read-Klasse ohne `lbatofile` | Mappt `lbatofile` FAT? Existiert Geometrie-Band-Tool? | `006`, `010` | `mess_band_report` + FW-`fileForLba`/`metaTag`; `lbatofile` verwerfen | `DISCOVERED DURING TEST` |
| `fat-forensic` nur Post-Capture | Liefert Reverse-LBA→Pfad out-of-box? | `007`–`008` | Optional: Image-Audit + `runs()`→eigenes Reverse-Index; nicht Storm-Runtime | `DISCOVERED DURING TEST` |
| usbsnoop nicht als Fahrzeug-Capture | Host-eBPF am NBT? Lizenz? | `011`, Vor-`EVID-USBBOT-INST-…-005/007` | Lab-PC Validate; Produktkopie STOP | `KNOWN BEFORE TEST` / Confirm |
| Kein neues Sheet / kein Fremd-Q/S | Existiert fertiger Klassifikator? | `015` | M31 Eigenbau auf Status-Achsen | `DISCOVERED DURING TEST` |

## Engineering Review Checks

Ziel: nächste P0-Session / ggf. kleines FW-/Tool-Wachstum (**C11**).

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001`–`003` | Storm-Window: MessCapture **arm** vor OTG; Ring-Drops (`dropCount`) mitschreiben | `DISCOVERED DURING TEST` |
| `004`–`005` | Status-Poll: `prefetchHits`, `fav*.midFile`, `bytesFile/Meta`, `playGuessCount` + Event-Zeit | `DISCOVERED DURING TEST` |
| `006` | Post: `mess_band_report` auf Dump; Geometrie-Pin (L3 vs Legacy) dokumentieren | `DISCOVERED DURING TEST` |
| `010` | Kein Pipeline-Schritt „lbatofile auf Virtual-FAT“ | `DISCOVERED DURING TEST` |
| `007`–`008` | Fremd-FAT-Parser: nur gegen exportiertes Image; Lizenz Apache-2.0 ok für Lab-Tool | `DISCOVERED DURING TEST` |
| `011` | usbsnoop nur Lab-Host; LICENSE-Gate | `KNOWN BEFORE TEST` |
| `015` | Q/S-Trigger nie nur `readCount`/`playRejectCount` | Reuse Livelock-Abend |

## Kill-Kriterien

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Fitness-Klassifikation ohne Messlauf. Ausschluss von Repos
(Lizenz, kein FAT, README-only) sind Quality-/Scope-Gates, keine
präregistrierten Hypothesentests für HU-Verhalten.
```

Für die **nächste Feld-Session (M30)** gelten die Kill-Kriterien aus
[`pidrive-2026-10-17-prefetch-livelock`](../pidrive-2026-10-17-prefetch-livelock/)
weiter (H1 File-Body vs Meta-Rescan; H2 167/136 ≠ Stuck).

## Fitness-Matrix (Kurz)

| Repo | M30 Capture | M31 Q/S | M32 LBA→Klasse | Urteil |
|------|-------------|---------|----------------|--------|
| `pidrive` | Tools/Doku/Maßnahmen | Achsen spezifiziert | `mess_band_report` | **P0 Pflicht** |
| `esp32.pidrive` | MessCapture + Status + Events | Zähler vorhanden; Klassifikator fehlt | `fileForLba`/`metaTag`/midFile | **P0 Pflicht** |
| `fat-forensic` | nein | nein | Chain/`runs()` → eigenes Reverse | **P2 optional Post** |
| `fslib` | nein | nein | FAT16 lesen, archived | **P3 Kontrast** |
| `dfir_ntfs` | nein | nein | FAT-Parser offline | **P3 optional** |
| `lbatofile` | nein | nein | **kein FAT** | **REJECT** |
| `usbsas` | Host-Sheepdip | nein | SCSI/FAT Userspace-Ref | **P2 Schema-Ref** |
| `usbsnoop` | Lab-Host BOT/LBA | nein | LBA in CBW-Decode | **P1 Lab-Validate** |
| `luft` | Connect-Events | nein | nein | **REJECT M30–32** |
| `BMW_HU_Info` | nein | nein | nein | **REJECT (README)** |
| `tinyusb` | MSC-Callback-Basis | nein | nein | **Reuse Stack** |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| MSC Trace-Korrelation | [`methods/msc-trace-correlation.md`](../../methods/msc-trace-correlation.md) |
| MSC Host-Read-Semantik | [`methods/msc-host-read-semantics.md`](../../methods/msc-host-read-semantics.md) |
| NBT Cache / Play-Intent | [`methods/nbt-cache-eviction-play-intent.md`](../../methods/nbt-cache-eviction-play-intent.md) |

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Desk only | `EVID-STORMTOOL-2026-10-18-*` | diese Kampagne + Querverweis Prefetch-Livelock Exit #9 |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact. Kein Sheet-A-Update.

## Praktische Empfehlung (P0) — bestätigt

1. **Storm-Capture** → `esp32.pidrive` MessCapture + Status/Events (+ UART Gate) in **einer** Session (M30).
2. **LBA→Klasse** → eigenes `mess_band_report` / FW-Geometrie; **nicht** `lbatofile`.
3. **Live-Host-Sicht (Lab)** → usbsnoop oder Wireshark-USB; usbsas nur Schema/sicheres Lesen.
4. **Post-Image-Audit (optional)** → `fat-forensic` (Meta-Konstanz / Chain), nicht Runtime.
5. **M31** → Eigenbau Q/S auf `prefetchHits` / `midFile` / `bytesFile` / Ohr.

## Lessons → Transfer

- Der Engpass ist **Session-Orchestrierung + Klassifikator**, nicht fehlende Fremd-FAT-Bibliotheken.
- Fremd-„LBA→Datei“-Tools sind oft **Linux-EXT-Admin**-Tools — Virtual-FAT braucht Geometrie-Pin.
- usbsnoop bleibt Research/Lab (Lizenz `UNKNOWN`); Device-seitiges Journal ist die Feldspur.

## Offene Punkte nach Abschluss

- Feld: eine Storm-Episode mit MessCapture-Dump + UART + Guess-Marker (M30).
- Tool/FW: optional Read-Klasse **in** MessCmd-Events (heute post-hoc Band-Report).
- M31 Detektor-Skizze (Status-Poll) — Follow-on, nicht Teil dieses Desk-Laufs.

Evidence: [`evidence.md`](evidence.md).
