# Audit Campaign: tinysstv-2026-foreign

```yaml
id: tinysstv-2026-foreign
project_id: tinysstv
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "b9977a62d45dbd459d6bbec6e971383e721ddcf4"
reuse_outcomes:
  reused: [esp32-apll-fm-tx, rpi-gpio-fm-tx]
  new: [sstv-martin-m1]
  not_helped: []
  process: "Desk Martin M1 AF SSTV; contrast APLL RF FM; no unlicensed TX guidance"
```

## Ziel

TinySSTV als Fremd-Upstream für **Martin-M1-SSTV-AF-Synthese** (DDS/PDM) — klar getrennt von APLL-UKW-FM.

## Scope

[SCOPE](../../projects/tinysstv/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + Commit | erfüllt |
| 2 | Sheet + App; Kontrast APLL/Pi-FM | erfüllt |
| 3 | PDM/LPF + PTT-Gap Evidence | erfüllt |
| 4 | C10–C12 | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 6 | Eigenes Lab | offen |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neues Sheet vs APLL-FM? | AF oder RF? | `…-002` | Neu `sstv-martin-m1` | KNOWN BEFORE |
| PTT dokumentieren? | Implemented? | `…-003` | Gap only | DISCOVERED |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-002` | Nie PDM-GPIO ohne LPF an Radio |
| `…-001` | Upstream Off-Air ≠ eigene Lab-FACT |
| `…-003` | PTT nicht als fertig behaupten |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Nur JPEG-Host ohne Tone-Pfad | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk; eigenes Demod UNKNOWN ≠ STOP.
```

## Bezug

[INVENTORY](../../projects/tinysstv/INVENTORY.md) · [evidence](evidence.md)
