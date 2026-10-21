# Audit Campaign: hu-probe-bmw-s2-abend-offline-2026-10-18

```yaml
id: hu-probe-bmw-s2-abend-offline-2026-10-18
project_id: hu-probe
started: 2026-10-18
ended: 2026-10-18
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: bmw-nbt-evo
prior_audit: hu-probe-bmw-s0s2-field-2026
related_audits:
  - hu-probe-bmw-s0s2-field-2026
  - msc-host-read-semantics-s1s2s3-2026
  - pidrive-2026-10-17-prefetch-livelock
upstream_pin:
  repo: https://github.com/MPunktBPunkt/hu-probe
  commit: 5e60303
  fw: "0.2.30"
  pr: 4
reuse_outcomes:
  reused:
    - bmw-nbt-evo
    - usb-msc
    - msc-host-read-semantics
    - msc-lba-timing-instrument
  new:
    - track-load-cbw-240-plus-69
    - hold-reverse-cbw-order
  not_helped:
    - "39×4KiB als Byte-genaue Burst-Formel (letzter Chunk = 2560 B)"
    - "Burst-Fenster 312 LBA / „3 Meta“ (Zählartefakt; FACT = 309 = 240+69)"
    - "T1b als eigene Start-Karte ~249 (ist Reverse-Order derselben T1-CBW-Paarung)"
  process: "Mistral+GPT Abend-Reviews gegen lokale events.jsonl nachgerechnet; CBW-Ebene vor Event-Chunks."
  decisions_touched:
    - cbw-240-69-track-atom
    - event-39-vs-bytes-158208
    - hold-tail-then-head
    - reject-312-meta-model
```

## Ziel

Abend-Offline BMW S2 (FW **0.2.30**, PR #4) gegen Rohdaten prüfen:
Muster schärfen, Zahlkorrektur (39/309/312), Hold-Morphologie erklären,
Übergabe an die nächste KI mit P0-Experiment.

## Scope

- **Im Scope:** Offline-Sessions `175203`–`212635`; Live-Stichprobe `4028`/`2264`/`8630`/`2995`;
  CBW- vs. `bot_data`-Ebene; Abgleich Mistral/GPT/Feldbericht; Epistemik FACT/INFERENCE;
  Auftrag Next-KI.
- **Nicht im Scope:** FW-Patch B7; Upstream-Profil-Edit; PiDrive-Semantik als hu-probe-FACT;
  Prefetch-Lead-Quantifizierung ohne Marker.

```text
kill:
  - 312-LBA-Burst / „3 Meta“ als FACT ohne CBW-Sum
  - „39×4096 = 159744“ als Byte-FACT
  - T1b als dritte Track-Geometrie neben 9/318/627
  - 212635 als Prefetch-Beweis
  - Offline Gap=0 als HU-Pace
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Rohdaten-Nachrechnung 3× Offline-PASS | erfüllt |
| 2 | CBW-Atom 240+69 pro Track (T1/T2/T3) belegt | erfüllt |
| 3 | Hold = Reverse-Order derselben T1-Paarung | erfüllt |
| 4 | 309/312 und 39×4KiB-Byteformel korrigiert | erfüllt |
| 5 | Next-KI-Bericht mit P0 T2-Hold | erfüllt |
| 6 | Session-Meta maschinenlesbar im Audit | erfüllt (`session-summaries.json`) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Track-Load = 2× READ10 (240+69), nicht 39× READ10(8) | Was steht in `bot_cbw.scsi`? | `001`–`003` | Event-39 = Chunks; CBW-Atom steuert Geometrie | `DISCOVERED DURING TEST` |
| „312 LBA / 3 Meta“ verwerfen | Deckt letzter Chunk 2560 B? | `002`, `004` | Covered = 309 LBA = 158208 B = CBW-Sum | `DISCOVERED DURING TEST` |
| T1-Hold ≠ neue Band-Karte | Ist Order nur reversed? | `005` | T1a/T1b = Order-Label, nicht Start-Geometrie | `DISCOVERED DURING TEST` |
| 212635 bleibt Prefetch-Kandidat, nicht Beweis | Operator Hold-2 vs. Buffer T3? | `006` | P0: direkt T2 starten+halten | `KNOWN BEFORE TEST` (GPT/Mistral) |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001`–`004` | Jede „39er“-Aussage mit CBW-Liste + letztem `actual` prüfen | `DISCOVERED DURING TEST` |
| `005` | Hold-Burst: CBW-Order vor Start-Monotonie werten | `DISCOVERED DURING TEST` |
| `006` | Prefetch nur mit Marker + nicht-kollabierten Timestamps | `KNOWN BEFORE TEST` |

## Kill-Kriterien

**Hypothese:** Offline-Abend liefert belastbare **LBA/CBW-Muster**; Prefetch bleibt getrennt.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | 312-LBA / „3 Meta“ als FACT ohne CBW | vermieden (`004` REJECTED) |
| 2 | 212635 als Prefetch-FACT | vermieden |
| 3 | Offline-Timing als Pace-FACT | vermieden (B7) |
| 4 | Burst-39 als globale HU-Konstante | weiter REJECTED |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| MSC Host-Read-Semantik | [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md) |
| LBA/Timing-Instrument | [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) |

## Bezug Inventar

- Projekt: [`hu-probe`](../../projects/hu-probe/)
- Prior: [`hu-probe-bmw-s0s2-field-2026`](../hu-probe-bmw-s0s2-field-2026/)
- Upstream: PR [#4](https://github.com/MPunktBPunkt/hu-probe/pull/4) @ `5e60303`
- Feld: `docs/feld/2026-10-18-bmw-s2-abend-offline.md`, Multi-KI-Review, Auswertungen
- Rohdaten: lokal `sessions/20261018-*_bmw_s2_prefetch/` (gitignored; Summaries hier)

## Ergebnisse

| # | Artefakt | Ort |
|---|----------|-----|
| 1 | Evidence-Register | [`evidence.md`](evidence.md) |
| 2 | Session-Meta (replizierbar) | [`session-summaries.json`](session-summaries.json) |
| 3 | Bericht / Next-KI | [`docs/reports/2026-10-18-hu-probe-bmw-s2-abend-offline.md`](../../docs/reports/2026-10-18-hu-probe-bmw-s2-abend-offline.md) |

## Knowledge Feedback

| Lab/Field | Evidence | Zurück in |
|-----------|----------|-----------|
| BMW Offline S2 0.2.30 CBW-Atom | `001`–`005` | hu-probe Application `bmw-nbt-evo` / Profil-FOLLOW-ON (`240+69` track load) |
| Hold Reverse-Order | `005` | Operator-Runbook + Profil-Terminologie T1-order |
| Prefetch-Kandidat 212635 | `006` | GATE-01 Messplan (unverändert OPEN) |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 Kill-Kriterien | PASS |
| C13 Knowledge Feedback | PASS → Report + Summaries; Profil-Edit absichtlich nicht |

## Lessons → Transfer

- **Immer CBW vor Chunks:** „39 Reads“ sind `bot_data`-Events; die HU fordert **2× READ10 (240+69)**.
- Letzter Chunk der 69er-CBW ist **2560 B (5 LBA)** — nicht 4096. Deshalb 158208 B / 309 LBA, nicht 159744 / 312.
- Hold-„Nichtmonotonie“ = **Tail-then-Head** derselben Track-Paarung.
- Profil hatte `also_rest_to_eof_e_g_69` schon als Caveat — Abend macht daraus ein **Track-Atom**.

## Offene Punkte nach Abschluss

- P0: Offline T2 direkt starten+halten (Marker)
- P0/P1: B7 `capture_t_us` ≠ Replay
- P1: Medien-Image Dateigrößen (optional; 309 jetzt CBW-seitig geschlossen)
- P2: Hold auf T2/T3 — bleibt Reverse-Order?
- GATE-01 Prefetch-Lead weiter OPEN
