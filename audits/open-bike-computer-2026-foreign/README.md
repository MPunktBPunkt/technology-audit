# Audit Campaign: open-bike-computer-2026-foreign

```yaml
id: open-bike-computer-2026-foreign
project_id: open-bike-computer
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "cd7ad00bb6c4f9566195cd44ab4d6a675518b94d"
reuse_outcomes:
  reused: [bluetooth-ftms, ble-hrm-gatt]
  new: [ride-ble-display]
  not_helped: []
  process: "Desk custom Ride/Nav BLE display + ownership; contrast FTMS/HRM/proximity"
```

## Ziel

open-bike-computer als Fremd-Upstream für **Custom Ride BLE Display** (Nav/Workout/Ownership) — getrennt von Standard-FTMS/HRM und von RSSI-Proximity-Hunt.

## Scope

[SCOPE](../../projects/open-bike-computer/SCOPE.md) — Desk; kein iOS-Feldtest.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + Commit | erfüllt |
| 2 | Sheet `ride-ble-display` + App; Kontrast FTMS/HRM | erfüllt |
| 3 | Adv v2 + Auth + framed fallback Evidence | erfüllt |
| 4 | C10–C12 | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 6 | Ride Lab | offen |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neues Sheet vs FTMS? | Custom oder Standard? | `…-001` | Neu Ride Display | KNOWN BEFORE |
| Auth vor Nav? | Ownership? | `…-001` | Ja — Session zuerst | KNOWN BEFORE |
| GATT-Cache? | Fallback? | `…-002` | Framed MAPR/… | DISCOVERED |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-001` | Unauthenticated Nav-Writes = REJECTED |
| `…-002` | GATT-Cache ohne Fallback = Gate |
| `…-001` | Ride-Display ≠ FTMS/HRM |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Nur Standard-FTMS ohne Custom Display-Pfad | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk; Ride Lab UNKNOWN ≠ STOP.
```

## Bezug

[INVENTORY](../../projects/open-bike-computer/INVENTORY.md) · [evidence](evidence.md)
