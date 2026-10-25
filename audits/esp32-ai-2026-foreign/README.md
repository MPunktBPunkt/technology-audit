# Audit Campaign: esp32-ai-2026-foreign

```yaml
id: esp32-ai-2026-foreign
project_id: esp32-ai
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "52ebcbbd905270592c1d415efd1128d04d0fa365"
reuse_outcomes:
  reused: [esp32-s3-silicon, ssd1306-oled-ui]
  new: [mcu-ple-inference, mcu-connectome-graph]
  not_helped: []
  process: "Desk foreign: PLE LLM + connectome on S3 N16R8; no weight mirror; Upstream MEASURED cited as Desk FACT"
```

## Ziel

[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) als Fremd-Upstream: Memory-tiered On-Device-LLM (PLE) und Connectome-Graph auf ESP32-S3 in die KB bringen — Reuse wo möglich, neue A-Sheets nur für echte Lücken.

## Scope

[SCOPE](../../projects/esp32-ai/SCOPE.md) — Desk only; keine Board-Remessung; keine Artefakt-Spiegelung.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | `standard_version` 0.7.1 + Profil `lab-tool` + Commit-Pin | erfüllt |
| 2 | Match-Tabelle; Sheets `mcu-ple-inference`, `mcu-connectome-graph` neu; Reuse S3 + OLED | erfüllt |
| 3 | Vier Applications + Evidence-IDs | erfüllt |
| 4 | C10–C12 gesetzt; C13 n/a (Desk) | erfüllt |
| 5 | Keine Weights/Media in KB | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 7 | Eigene Lab-Remessung | offen (bewusst FOLLOW-ON) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neues PLE-Sheet? | Existiert On-Device-LLM-Slug? | Index-Scan | Ja — `mcu-ple-inference` | KNOWN BEFORE TEST |
| Connectome = PLE-Sheet? | Gleicher Contract? | `EVID-ESP32AI-2026-10-25-005` | Nein — eigener Slug | KNOWN BEFORE TEST |
| OLED neues Sheet? | Nur SH1106? | `EVID-ESP32AI-2026-10-25-009` | Reuse `ssd1306-oled-ui` | KNOWN BEFORE TEST |
| S3-Silicon reuse? | N16R8/Tiering = Errata-Sheet? | `EVID-ESP32AI-2026-10-25-008` | Reuse + App (nicht Fork) | KNOWN BEFORE TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-ESP32AI-2026-10-25-002` | „M Parameter“ nicht als Dense-Capability zitieren | KNOWN BEFORE TEST |
| `EVID-ESP32AI-2026-10-25-003` | Flash-Table-Kosten vs Head separat budgetieren | KNOWN BEFORE TEST |
| `EVID-ESP32AI-2026-10-25-012` | Dual-Core Head-Matvec und int8-Staging nicht mit Fly-SIMD vermischen | KNOWN BEFORE TEST |
| `EVID-ESP32AI-2026-10-25-004` | Asym. Vocab: out2in + Boot-Guards vor Deploy | KNOWN BEFORE TEST |
| `EVID-ESP32AI-2026-10-25-006` | Host-Gold/Bundle vor Flash-Write | KNOWN BEFORE TEST |
| `EVID-ESP32AI-2026-10-25-008` | Board = N16R8-Klasse; Classic/no-PSRAM = Gate | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese:** Upstream zeigt belastbares Flash-tiered On-Device-LLM + Connectome-Subgraph auf S3.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Repo enthält nur Cloud-API-Client, keine On-Device-Runtime | nicht eingetreten |
| 2 | Kein Flash-Partition-/mmap-Pfad für Weights/Graph | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Audit ohne eigene Board-Messung. Upstream-tok/s UNKNOWN für uns ≠ automatisches STOP.
```

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| — | (kein Method-Note; Deploy-Gate FOLLOW-ON) |

## Bezug Inventar

[INVENTORY](../../projects/esp32-ai/INVENTORY.md) — Pilot: `mcu-ple-inference`, `mcu-connectome-graph`, `esp32-s3-silicon`, `ssd1306-oled-ui`.

## Knowledge Feedback

Desk only — C13 n/a.

## Lessons → Transfer

- Stored-Parameter-Marketing ≠ Dense-Compute; A-Fallstrick früh setzen.
- PLE und Connectome teilen Flash/PSRAM-Idee, aber nicht denselben Runtime-Contract.
- Host-Verify-before-flash ist wiederkehrendes Edge-ML-Muster (Method-Kandidat).

## Offene Punkte nach Abschluss

- Lab-Remessung Bandwidth/tok/s
- Method Note `host-gold-before-flash` bei zweitem Projekt
