# Audit Campaign: prefetch-livelock-public-gap-2026

```yaml
id: prefetch-livelock-public-gap-2026
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
  - pidrive-2026-storm-capture-tooling
  - bmw-nbt-media-index-2026-foreign
  - usb-bot-observation-2026-foreign
  - usb-bot-observation-2026-instrument-sources
  - msc-host-read-semantics-s1s2s3-2026
upstream_pins:
  - url: https://davidpetric.com/2025/06/23/bmw-nbt-evo-id6-system-dump-analysis/
    kind: public-blog
    note: "Desk 2026-10-18; dump-Repo access-restricted"
  - url: https://git.davidpetric.com/thepetric/nbtevo-system-dump
    kind: access-gate
    note: "public listing states dumps request-only / moved"
  - url: https://www.hakstuff.net/blog/dissecting-the-bmw-nbt-hu-evo-infotainment-unit-boot-process
    kind: public-blog
  - url: https://www.hakstuff.net/blog/extracting-qnx-ifs-partitions
    kind: public-blog
  - repo: https://github.com/ttepatti/qnx-boot-script-kaitai-struct
    commit: 30f122cd00e0090abb6890c1238c0d79930d3cbf
  - url: https://i.blackhat.com/USA-19/Thursday/us-19-Cai-0-Days-And-Mitigations-Roadways-To-Exploit-And-Secure-Connected-BMW-Cars-wp.pdf
    kind: public-paper
  - url: https://keenlab.tencent.com/en/whitepapers/Experimental_Security_Assessment_of_BMW_Cars_by_KeenLab.pdf
    kind: public-summary
  - url: https://keenlab.tencent.com/en/2018/05/22/New-CarHacking-Research-by-KeenLab-Experimental-Security-Assessment-of-BMW-Cars/
    kind: public-blog
  - repo: https://github.com/hathach/tinyusb
    commit: 98741b55959564746998d0453c32d87064629d7c
    path: src/class/msc/
  - repo: https://github.com/espressif/esp-usb
    commit: fc9bead300f82484eace377d5dea2f3e11163206
    path: host/class/msc/
  - repo: https://github.com/torvalds/linux
    commit: 58161ead29e50d70a317ea26b472e0c7508e69da
    path: drivers/usb/storage/
reuse_outcomes:
  reused:
    - bmw-nbt-evo
    - usb-msc
    - msc-host-read-semantics
    - msc-trace-correlation
  new: []
  not_helped:
    - "davidpetric/HAKSTUFF Boot-/Dump-Analysen — Architektur/USB-Diagnose-Kontext, kein LBA-/Storm-Muster"
    - "KeenLab/BlackHat BMW — USB als Security-Angriffsfläche (Map-Update/Code-Exec), nicht Media-Prefetch"
    - "Generische MSC-Host-Stacks — normales READ(10), kein NBT Prefetch-Livelock"
    - "Öffentlicher fertiger Q/S-Klassifikator oder Storm-Morphologie-Analyse — nicht gefunden"
  process: "Desk-Gap: drei Ressourcenklassen gegen M30–M32; keine Exploit-Reproduktion; Dump nicht geklont."
  decisions_touched:
    - public-gap-confirms-own-instrumentation-p0
    - boot-dump-blogs-context-only
    - keenlab-security-not-prefetch
    - generic-host-read10-not-nbt-storm
```

## Ziel

Öffentliche Folgequellen (NBT Boot/Dump-Blogs, KeenLab/BlackHat, generische
MSC-Hosts) gegen den Prefetch-Livelock-/Storm-Auftrag prüfen und den
**öffentlichen Gap** festschreiben: kein fertiger Q/S-Klassifikator, keine
NBT-Storm-Morphologie — eigene Instrumentierung bleibt P0.

## Scope

- **Im Scope:** öffentlich erreichbare Blogs/Papers; gepinnte Code-Pfade für
  generisches READ(10); Fitness vs. Quiet/Storm, LBA-Klasse, Guess/Play;
  Epistemik; Security-Grenzen ohne Exploit-Anleitung.
- **Nicht im Scope:** Klonen access-restricted Dumps; Ausführen fremder
  Firmware; Exploit-/Angriffsreproduktion; Fahrzeugzugriff; Sheet-A-Claims
  „NBT liest immer X“; neuer Q/S-Code.

```text
kill:
  - Boot-/Dump-Blog = Storm-LBA-Beweis
  - KeenLab USB-Findings = Media-Prefetch-Modell
  - Generischer MSC-Host = NBT Storm-Verhalten
  - Öffentliches Repo liefert fertigen Q/S-Klassifikator
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1 + Kampagne + Evidence | erfüllt |
| 2 | Drei Ressourcenklassen getrennt bewertet | erfüllt |
| 3 | Expliziter Negativbefund: Prefetch-Livelock öffentlich unerschlossen | erfüllt — `015` |
| 4 | P0 bleibt eigene MessCapture/Status-Pipeline | erfüllt — Decision Trace |
| 5 | Keine Exploit-Schritte / kein Dump-Spiegel | erfüllt |
| 6 | C10–C13 Desk; kein neues Sheet | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Boot/Dump-Quellen nur Architektur-Kontext | Enthalten sie LBA-Traces / Storm-Zähler / Guess-Korrelation? | `001`–`005` | Nein — Kontext ok, Storm `REJECTED` | `DISCOVERED DURING TEST` |
| KeenLab/BH nicht in Prefetch-Pipeline | Fokus Code-Exec / Map-Update / Diagnostic USB? | `006`–`008` | Ja Security-Historie; **kein** Prefetch-Modell | `DISCOVERED DURING TEST` |
| Generische Hosts nur Lab-Kontrast | Modellieren sie aggressives File-Body ohne Play? | `009`–`011` | Nein — normales READ(10) | `DISCOVERED DURING TEST` |
| Kein Parallel-Pfad statt MessCapture | Existiert öffentlicher Q/S- oder Storm-Analyzer? | `015` | Nein — P0 bleibt eigenes Journal | `DISCOVERED DURING TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001`–`005` | Diagnose-USB (`start_usb` / Log-Copy) nicht mit Media-MSC-Storm vermengen | `DISCOVERED DURING TEST` |
| `006`–`008` | Security-Papers nicht als HU-Read-Semantik zitieren; keine Exploit-Übernahme | `KNOWN BEFORE TEST` |
| `009`–`011` | Lab-Host-READ(10) ≠ Feld-NBT Prefetch | `DISCOVERED DURING TEST` |
| `015` + Storm-Tooling | M30 Session-Orchestrierung priorisieren, nicht weitere Fremd-RE | `DISCOVERED DURING TEST` |

## Kill-Kriterien

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Gap-Klassifikation ohne Messlauf. Negativbefunde sind
Scope-/Qualitätsgates, keine präregistrierten HU-Hypothesentests.
```

Feld-Kills bleiben in
[`pidrive-2026-10-17-prefetch-livelock`](../pidrive-2026-10-17-prefetch-livelock/).

## Fitness-Matrix

| Klasse | Quellen | Nutzen | Storm/Q / LBA→Play |
|--------|---------|--------|--------------------|
| NBT Boot / System-Dump-Analysen | davidpetric Blog; HAKSTUFF IFS/Boot; Kaitai-Parser | Boot, Starter, Diagnose-USB, MME-Schema-Kontext | **REJECT** für Muster |
| KeenLab / BlackHat | BH USA 2019 WP; KeenLab Summary 2018 | Architektur, USB als Security-Fläche (historisch, patched) | **REJECT** Prefetch |
| Generische MSC Host/Device | TinyUSB MSC, esp-usb host MSC, Linux `usb-storage` | „Normales“ READ(10)/BOT | **REJECT** NBT-Storm |
| Eigene Pipeline (Reuse) | MessCapture, Status-Poll, `mess_band_report` | einzige realistische Erfassung | **P0** |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| MSC Host-Read-Semantik | [`methods/msc-host-read-semantics.md`](../../methods/msc-host-read-semantics.md) |
| MSC Trace-Korrelation | [`methods/msc-trace-correlation.md`](../../methods/msc-trace-correlation.md) |
| NBT Cache / Play-Intent | [`methods/nbt-cache-eviction-play-intent.md`](../../methods/nbt-cache-eviction-play-intent.md) |

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Desk | `EVID-PREFGAP-2026-10-18-*` | Application `bmw-nbt-evo` (pidrive) + Prefetch-Livelock Querverweis |

Kein Sheet-A-Update (Gap bestätigt fehlende öffentliche Morphologie).

## Lessons → Transfer

- Öffentliche NBT-RE liefert **Boot/Diagnose/Security-Kontext**, nicht Quiet/Storm.
- USB in KeenLab ≠ Media-Prefetch-USB.
- Generisches READ(10) bleibt Lab-Kontrast (Reuse usb-bot-observation).
- **Fazit:** Prefetch-Livelock öffentlich praktisch unerschlossen → MessCapture +
  LBA-Journal + Status-Poll in `esp32.pidrive`/`pidrive` bleiben der Weg.

## Offene Punkte

- Feld M30 (UART + Storm-Capture) unverändert P0.
- Dump-Zugriff nur bei eigener rechtmäßiger Beschaffung / Freigabe — kein KB-Spiegel.

Evidence: [`evidence.md`](evidence.md).
