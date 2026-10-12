# Audit Campaign: bluetooth-stack-2026-foreign

```yaml
id: bluetooth-stack-2026-foreign
project_id: bluetooth-stack
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "6ef9436"
reuse_outcomes:
  reused: [bluetooth-a2dp, avrcp]
  new: []
  not_helped: []
  process: "Desk foreign; contrast HCI-host vs Bluedroid"
```

## Ziel

Leichtgewicht-Host-Stack als Kontrast zu pschatzmann/Bluedroid und Pi BlueZ — Profile-Slugs wachsen um Stack-Neutralität, nicht um Gateway-Empfehlung.

## Scope

[SCOPE](../../projects/bluetooth-stack/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 | erfüllt |
| 2 | Apps A2DP + AVRCP | erfüllt |
| 3 | Sheet-Fallstrick HCI≠Bluedroid | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |

## Lessons → Transfer

- „ESP32“ in einer Chip-Matrix kann **nur Controller** bedeuten.
- Compile-Profile-Flags sind schwache Evidence für Feld-Features.

## Bezug

[INVENTORY](../../projects/bluetooth-stack/INVENTORY.md) · [evidence](evidence.md) · [`esp32-a2dp-2026-foreign`](../esp32-a2dp-2026-foreign/)
