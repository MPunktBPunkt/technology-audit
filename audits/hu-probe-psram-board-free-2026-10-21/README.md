# Audit Campaign: hu-probe-psram-board-free-2026-10-21

```yaml
id: hu-probe-psram-board-free-2026-10-21
project_id: hu-probe
started: 2026-10-21
ended: 2026-10-21
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: bmw-nbt-evo
related_tech:
  - esp32-s3-silicon
  - esp32-s3-usb-wifi-coex
  - usb-msc
prior_audit: hu-probe-bmw-s2-abend-offline-2026-10-18
related_audits:
  - hu-probe-bmw-s2-abend-offline-2026-10-18
  - hu-probe-bmw-s0s2-field-2026
  - esp32-s3-usb-wifi-coexistence-2026
  - msc-host-read-semantics-s1s2s3-2026
upstream_pin:
  repo: https://github.com/MPunktBPunkt/hu-probe
  commit: f985459
  fw: "0.3.1"
  field_core_fw: "0.2.40"
reuse_outcomes:
  reused:
    - bmw-nbt-evo
    - usb-msc
    - esp32-s3-usb-wifi-coex
    - esp32-s3-silicon
    - msc-host-read-semantics
    - track-load-cbw-240-plus-69
  new:
    - psram-n8r2-1mib-offline-capture
    - free-offline-grammar-demo-v1
    - tur-idle-2239ms-phase-locked
    - tail-then-head-elevator-inference
    - remount-resume-not-playlist-restart
  not_helped:
    - "PSRAM als Coex-Heilung (Lab: Heap besser, RF-Tod bleibt)"
    - "R21 ~15s Prefetch auf 158 KiB demo_v1"
    - "HARDWARE.md §2.3 als aktuelle PSRAM-SoT (veraltet)"
  process: "Delta seit Abend-18.10.: Board-Doc + PSRAM-Build + free Offline 0.2.40 + Profil-Expand gegen Sessions/Analyzer; Größenleiter präregistriert offen."
  decisions_touched:
    - enable-psram-qio-qspi-n8r2
    - reject-prefetch-15s-demo-v1
    - supersede-next-track-9-18s-as-resume
    - reject-tail-then-head-reentry
    - reject-remount-playlist-t1
```

## Ziel

Delta-Audit nach neuen Messdaten, erweitertem `bmw_nbt_evo`-Profil, **PSRAM-Aktivierung**
und Board-HW-Dokumentation: was ist jetzt FACT, was bleibt OPEN, was ist Doc-Drift.

## Scope

- **Im Scope:** YD-ESP32-S3 Board/PSRAM/Flash-Build; Offline-Puffer 1 MiB; free Offline
  BMW 0.2.40 (3× PASS); Profil-Erwartungen/Rejects; Lab-Coex vs. PSRAM; Verweis 0.3.x Drive-Mode.
- **Nicht im Scope:** Größenleiter-Auswertung abschließen; FW-Patches; Prefetch-Beweis bei großen Dateien;
  Drive-Home TripStore-Census; Upstream-Doc-Edit in hu-probe.

```text
kill:
  - PSRAM heilt USB↔WiFi-Coex
  - Prefetch-Lead 15 s als FACT auf demo_v1
  - next_track 9–18 s als Prefetch-FACT
  - remount = Playlist-Restart bei T1
  - tail_then_head = Re-Entry-Zustand (ohne Elevator-Test)
  - HARDWARE §2.3 „PSRAM aus“ als aktuelle Build-Wahrheit
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | PSRAM-Build + Feld-`capacity_bytes=1MiB` belegt | erfüllt |
| 2 | Board-Identifikation + Doc-Drift §2.3 dokumentiert | erfüllt |
| 3 | free Offline 3× PASS Grammatik (Atom/TUR/Idle/Reject Prefetch) | erfüllt |
| 4 | Profil-Delta (FACTS/Rejects) gegen Evidence gemappt | erfüllt |
| 5 | Coex: PSRAM ≠ Heilung (Lab) | erfüllt |
| 6 | Offene Gates (Größenleiter, Elevator-Test, Drive-Home) explizit | erfüllt |
| 7 | Report + Session-Summaries im Audit | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| PSRAM für Capture/Bus nutzen (N8R2 qio_qspi) | Ist Modul R2 + Build aktiv? | `001`–`003` | 1 MiB Offline; Ring in PSRAM | `KNOWN BEFORE TEST` (Lab 0.2.35+) / Feld `DISCOVERED DURING TEST` |
| Prefetch-15s auf demo_v1 verwerfen | File-Reads im Idle? | `008` | GATE-01 schrumpft auf audible-Rest | `DISCOVERED DURING TEST` |
| next_track 9–18s = Resume | Mid-Track nach Mount? | `013` | Profil SUPERSEDED | `DISCOVERED AFTER TEST` (§7) |
| Re-Entry-Morphologie verwerfen | Alle tth = T3→T1? | `012` | Elevator-INFERENCE; Test präreg. | `DISCOVERED AFTER TEST` |
| Größenleiter nicht als FACT schließen | H-A/B/C gemessen? | `017` | OPEN trotz Feldplan | `KNOWN BEFORE TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001`/`005` | HARDWARE/Build-Flags gegen `capacity_bytes` und `ESP.getPsramSize` prüfen | `DISCOVERED DURING TEST` |
| `002` | Offline-Aussagen nur mit `capacity_bytes` + overflow + integrity | `KNOWN BEFORE TEST` |
| `008`/`009` | Zeitachse = `capture_t_us`; Medien-Dauer ≠ HU-Timer | `DISCOVERED DURING TEST` |
| `012` | Order-Label vor Morphologie-Zustand; Elevator nur nach Rückwärtssprung-Test | `DISCOVERED AFTER TEST` |
| `015` | Heap/PSRAM-Verbesserung ≠ Coex-PASS | `KNOWN BEFORE TEST` |
| `018` | drive_home ohne Footer nicht als PASS zählen | `DISCOVERED DURING TEST` |

## Kill-Kriterien

**Hypothese:** PSRAM + free Offline liefern belastbare Instrument-/Host-Grammatik auf demo_v1; große-Datei-Prefetch bleibt getrennt.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | PSRAM als Coex-Root-Cause-Fix behauptet | vermieden (`015`) |
| 2 | Prefetch-15s als demo_v1-FACT | vermieden (`008`) |
| 3 | Größenleiter-Ergebnis ohne präreg. H-A/B/C nachgezogen | vermieden (`017` OPEN) |
| 4 | drive_home unvollständig als Offline-PASS | vermieden (`018`) |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| MSC Host-Read-Semantik | [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md) |
| LBA/Timing-Instrument | [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) |

## Bezug Inventar

- Projekt: [`hu-probe`](../../projects/hu-probe/)
- Prior: [`hu-probe-bmw-s2-abend-offline-2026-10-18`](../hu-probe-bmw-s2-abend-offline-2026-10-18/)
- Upstream-Feld: `docs/feld/2026-10-20-bmw-free-offline-0.2.40.md`, Multi-Review, `profiles/bmw_nbt_evo.json`
- Rohdaten: lokal `sessions/20261020-*_bmw_free` (gitignored); Summaries hier

## Ergebnisse

| # | Artefakt | Ort |
|---|----------|-----|
| 1 | Evidence-Register | [`evidence.md`](evidence.md) |
| 2 | Session-/PSRAM-Meta | [`session-summaries.json`](session-summaries.json) |
| 3 | Bericht | [`docs/reports/2026-10-21-hu-probe-psram-board-free.md`](../../docs/reports/2026-10-21-hu-probe-psram-board-free.md) |

## Knowledge Feedback

| Lab/Field | Evidence | Zurück in |
|-----------|----------|-----------|
| PSRAM 1 MiB Capture + N8R2 Build | `001`–`003` | Application `usb-msc` / `esp32-s3-silicon`; FOLLOW-ON |
| free Offline Grammar + Rejects | `006`–`014` | Application `bmw-nbt-evo`; Profil schon upstream |
| Coex ≠ PSRAM | `015` | Application `esp32-s3-usb-wifi-coex` |
| Doc-Drift HARDWARE §2.3 | `005` | FOLLOW-ON Upstream-Fix |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 Kill-Kriterien | PASS |
| C13 Knowledge Feedback | PASS → Apps/FOLLOW-ON; Upstream-HARDWARE-Edit absichtlich nicht |

## Lessons → Transfer

- **Instrument:** PSRAM macht Offline-Fenster groß genug für volle free-Ketten ohne Overflow — Coex bleibt separat.
- **Host demo_v1:** Trackwechsel = volles Atom; Idle = nur TUR ~2,239 s; kein File-Prefetch.
- **Order:** `tail_then_head` an T3→T1 gebunden; Elevator testen, nicht Re-Entry annehmen.
- **Docs:** Build-/Session-Meta schlagen narrative HARDWARE-Abschnitte.

## Offene Punkte nach Abschluss

- P0: Größenleiter `seq_size` / H-A vs H-B vs H-C auswerten
- P0: Rückwärtssprung-Test (Elevator-Vorhersage)
- P1: Replug `ident_b` Cache-Key; audible-Marker
- P1: Upstream `HARDWARE-YD-ESP32-S3.md` §2.3 aktualisieren
- P2: Drive-Home 0.3.x Integrity-Census
