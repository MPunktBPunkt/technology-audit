# Evidence — prefetch-livelock-public-gap-2026

Desk 2026-10-18 · **standard_version 0.7.1** · Profile `lab-tool`.
Keine Builds, kein Fahrzeug, **kein Dump-Klon**, **keine Exploit-Reproduktion**.

## Quellen-Snapshots

| Quelle | Pin / Datum | Rolle | Hinweis |
|--------|-------------|-------|---------|
| davidpetric Blog „Inside BMW’s NBT EVO ID6…“ | URL; Desk 2026-10-18 (Inhalt zuvor gelesen; Origin zeitweise HTTP 520) | Boot/Init/USB-Diagnose/MME-Kontext | öffentlich |
| `git.davidpetric.com/…/nbtevo-system-dump` | Access-Gate-Seite 2026-10-18 | Dump **request-only / moved** | kein Klon |
| HAKSTUFF „Dissecting the BMW NBT EVO HU Boot Process“ | URL; Desk 2026-10-18 | QNX IFS / Boot-Script / starter | öffentlich |
| HAKSTUFF „Extracting QNX IFS Partitions“ | URL; Desk 2026-10-18 | IFS-Dump-Kontext | öffentlich |
| `ttepatti/qnx-boot-script-kaitai-struct` | `30f122cd00e0090abb6890c1238c0d79930d3cbf` | Boot-Script-Parser | GitHub |
| BlackHat USA 2019 WP (Cai et al.) | `i.blackhat.com/...Cars-wp.pdf` | Security-Assessment NBT/TCB | öffentlich; **nur Abstract/Scope** |
| KeenLab Summary Report 2018 | keenlab.tencent.com whitepaper PDF | Summary Security-Assessment | öffentlich; **nur Scope** |
| KeenLab Blog 2018-05-22 | keenlab.tencent.com/en/2018/05/22/… | Ankündigung/Scope | öffentlich |
| `hathach/tinyusb` | `98741b55…` `src/class/msc/` | MSC Device/Host READ10 | MIT |
| `espressif/esp-usb` | `fc9bead3…` `host/class/msc/` | MSC Host `read_sector`/READ10 | (Upstream) |
| `torvalds/linux` | `58161ead…` `drivers/usb/storage/` | Kernel USB mass-storage Host | GPL-2.0 |

Verwandte KB: [`bmw-nbt-media-index-2026-foreign`](../bmw-nbt-media-index-2026-foreign/) (Offline-Medien/Forensik) ·
[`usb-bot-observation-2026-foreign`](../usb-bot-observation-2026-foreign/) (BOT/READ10-Pfade).

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-PREFGAP-2026-10-18-001` | davidpetric-Analyse beschreibt NBT EVO ID6 (FW 18-03) Boot/Init: u. a. `sysinit`, `start_net.sh`, `start_usb.sh`, `copy_corefiles2usb.sh`; USB-Einschub für **Log-/Crash-Export** (`/dev/sda1` mount, Copy von Log-/Core-Pfaden) — Diagnose-/Debug-USB, nicht als Media-Prefetch-Trace. | `FACT` (Blog) | davidpetric Blog §2.2 / §3.3 |
| `EVID-PREFGAP-2026-10-18-002` | Derselbe Blog nennt MME-Kontext (`usbdev_sync`, SQLite-Schemata für Media-Index/Playback-Metadaten) als **Offline-Dump-/Schema-Beschreibung** — keine LBA-/Storm-Zeitreihe, keine Quiet/Storm-Klassifikation. | `FACT` (Blog) | Blog §5.2 |
| `EVID-PREFGAP-2026-10-18-003` | Öffentliche Dump-Repo-Seite stellt System-Dumps als **access-restricted / request-only** dar (Missbrauch durch Scraper/AI-Agents genannt). Desk dieser Kampagne klont keinen Dump. | `FACT` | Gitea Access-Gate 2026-10-18 |
| `EVID-PREFGAP-2026-10-18-004` | HAKSTUFF Boot-Teil-1: QNX 6.5 IFS, `.script`-Startup (u. a. `sysinit`, `starter`), Fokus Boot/Process-Launch — **kein** SCSI-READ(10)-Storm-/Prefetch-Modell. | `FACT` (Blog) | hakstuff.net Boot-Process |
| `EVID-PREFGAP-2026-10-18-005` | `qnx-boot-script-kaitai-struct` @ Pin ist ein Format-Parser für QNX-Boot-Scripts — Werkzeug für Boot-RE, nicht HU-Media-Capture. | `FACT` | Repo @ `30f122c` |
| `EVID-PREFGAP-2026-10-18-006` | KeenLab/BlackHat-Material (2018 Summary, BH USA 2019 WP) behandelt NBT/TCB **Security-Assessment**: USB u. a. als externe Angriffsfläche neben Ethernet/OBD/Cellular; Schwerpunkt Code-Execution / Systemkompromittierung / Map-Update-Pfad — **nicht** Media-Prefetch- oder Play-Intent-Morphologie. | `FACT` (Scope/Abstract) | BH WP Abstract; KeenLab Blog/Summary Scope |
| `EVID-PREFGAP-2026-10-18-007` | Papers erwähnen Navigation-Map-Update über USB als untersuchten Update-Pfad (Security). Das ist ein **anderer USB-Use-Case** als laufendes MSC Media-Streaming/Prefetch. | `FACT` (Themenzuordnung) | BH WP Abschnitte zu Navigation Update (Titel/Scope only) |
| `EVID-PREFGAP-2026-10-18-008` | Diese Kampagne übernimmt **keine** Exploit-Schritte, Payloads oder PoCs aus den Security-Papers; Countermeasures laut Autoren historisch ausgerollt (Disclosure-Kontext). | `FACT` (Kampagnengrenze) | Scope + Abstract Mitigation-Hinweis |
| `EVID-PREFGAP-2026-10-18-009` | TinyUSB MSC (Device/Host) am Pin implementiert BOT + SCSI READ(10)-Parameter (LBA/Blocks) — **generischer** Stack, kein NBT-Timing. | `FACT` | TinyUSB `src/class/msc/` @ `98741b5`; Reuse usb-bot |
| `EVID-PREFGAP-2026-10-18-010` | esp-usb MSC Host bietet Sector-Read über READ(10) — Lab-Host-Kontrast, nicht Feld-NBT. | `FACT` | `host/class/msc/` @ `fc9bead` |
| `EVID-PREFGAP-2026-10-18-011` | Linux `drivers/usb/storage/` ist der übliche Kernel-MSC-Host-Pfad — „normales“ Host-Verhalten, kein Prefetch-Livelock-Modell. | `FACT` | linux @ `58161ead` path pin |
| `EVID-PREFGAP-2026-10-18-012` | In den geprüften öffentlichen Boot-/Dump-/Security-/Generic-Host-Quellen findet sich **kein** Quiet-vs-Storm-Klassifikator, kein Prefetch-Livelock-Detektor und keine korrelierte LBA↔Guess-Analyse für NBT Media. | `FACT` (Negativbefund Desk) | Corpus dieser Kampagne |
| `EVID-PREFGAP-2026-10-18-013` | Vor-Kampagnen [`bmw-nbt-media-index`](../bmw-nbt-media-index-2026-foreign/) und [`storm-capture-tooling`](../pidrive-2026-storm-capture-tooling/) decken Offline-Medien bzw. Capture-Bausteine ab — bestätigen ebenfalls fehlende Live-Storm-Public-Analyse. | `FACT` (Reuse) | Vor-Evidence `011` / Stormtool `015` |
| `EVID-PREFGAP-2026-10-18-014` | Eigene Instrumentierung (MessCapture LBA-Journal, Status-Poll `prefetchHits`/`midFile`/`bytesFile`, Guess-Events, `mess_band_report`) bleibt der in der KB belegte Weg zur Storm-Morphologie. | `INFERENCE` (Pipeline) | Prefetch-Livelock + Storm-Tooling Audits |
| `EVID-PREFGAP-2026-10-18-015` | **Urteil:** Prefetch-Livelock (aggressives File-Body-Lesen ohne zuverlässigen Play-Intent) ist in den geprüften öffentlichen Quellen **praktisch unerschlossen**; Fremdmaterial liefert höchstens Bausteine/Kontext. | `FACT` (Gap-Urteil Desk) | `001`–`014` |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „`start_usb.sh` erklärt Storm midFile“ | `REJECTED` | Diagnose-Export (`001`), kein Body-Prefetch-Trace |
| „MME SQLite-Schema = Live-Storm-Beweis“ | `REJECTED` | Offline-Schema (`002`); Reuse Media-Index |
| „KeenLab USB = NBT Prefetch-Modell“ | `REJECTED` | Security/Map-Update-Scope (`006`–`007`) |
| „Paper-Details nachbauen“ | `REJECTED` | Scope; keine Exploit-Hilfe (`008`) |
| „TinyUSB/esp-usb Host = NBT Storm“ | `REJECTED` | generisch (`009`–`011`) |
| „Öffentliches Fertig-Tool für Q/S“ | `REJECTED` | Negativbefund (`012`, `015`) |

## Security- / Ethics-Gates

- Keine Zugriffsanleitungen, keine Exploit-Rezepte, keine Dump-Spiegelung.
- Access-restricted Dumps nur mit Eigentümerfreigabe / eigener rechtmäßiger
  Erhebung — nicht über diese KB.
- Security-Papers nur für **Themenabgrenzung** (was sie *nicht* für Prefetch
  liefern); Mitigations historisch Upstream/OEM.

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| Storm-Episode LBA-Band-Dominanz | `UNKNOWN` | Feld M30 |
| Interne HU-Logs während Storm | `UNKNOWN` | nur mit Autorisierung; nicht aus Public Gap ableitbar |

## Wissens-Chronik

| Zeitpunkt | Label |
|-----------|-------|
| Vor | Storm-Muster Feld-Desk; Tooling-Fitness P0 eigen |
| Während | Public Boot/Security/Generic klassifiziert; Gap bestätigt |
| Nach | Kein Sheet-A; Fokus bleibt Capture-Session |
