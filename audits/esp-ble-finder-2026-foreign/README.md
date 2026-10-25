# Audit Campaign: esp-ble-finder-2026-foreign

```yaml
id: esp-ble-finder-2026-foreign
project_id: esp-ble-finder
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "1a588119bb8d21a5aa939b6e0601585bcf448431"
reuse_outcomes:
  reused: [rf-environment-monitor]
  new: [ble-rssi-proximity]
  not_helped: []
  process: "Desk BLE Adv RSSI proximity hunt; contrast environment monitor / ride display"
```

## Ziel

esp_ble_finder als Fremd-Upstream für **BLE RSSI Proximity Hunt** (findphone-Muster) — Adv-Scan + Bands/Clicker, getrennt von Environment-Score und Ride-GATT.

## Scope

[SCOPE](../../projects/esp-ble-finder/SCOPE.md) — Desk; kein Feld-Hunt; keine Surveillance-Anleitung.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + Commit | erfüllt |
| 2 | Sheet `ble-rssi-proximity` + App; Kontrast RF-Env | erfüllt |
| 3 | Bounds/Bands/Mute/Target Evidence | erfüllt |
| 4 | C10–C12 | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 6 | Lab-Hunt | offen |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neues Sheet vs RF-Env? | Hunt oder Score? | `…-001` | Neu Proximity | KNOWN BEFORE |
| RSSI = Meter? | Bounds? | `…-002` | Heuristik only | KNOWN BEFORE |
| Mute stoppt Scan? | Feedback only? | `…-001` | Nein | DISCOVERED |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-002` | RSSI nicht als Meter-Distanz verkaufen |
| `…-001` | Hunt ≠ Environment-Monitor |
| `…-001` | Mute ≠ Scan-Stop |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Nur Environment-Score ohne Hunt-UX | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk; Lab-Hunt UNKNOWN ≠ STOP.
```

## Bezug

[INVENTORY](../../projects/esp-ble-finder/INVENTORY.md) · [evidence](evidence.md)
