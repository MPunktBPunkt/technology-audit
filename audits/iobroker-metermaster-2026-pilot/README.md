# Audit Campaign: iobroker-metermaster-2026-pilot

```yaml
id: iobroker-metermaster-2026-pilot
project_id: iobroker-metermaster
started: 2026-10-09
ended: null
status: active
profile: adapter
standard_version: "0.6.3"
reviewed_commit: be89348
```

## Ziel

Desk-Audit von `ioBroker.metermaster` unter **0.6.3** — Produkt-Adapter :8089, Abgrenzung Hub/Simple-API, Link zur ESP-Firmware.

## Scope

Siehe [SCOPE](../../projects/iobroker-metermaster/SCOPE.md).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.3 + profile adapter | erfüllt |
| 2 | Sheet Adapter ≠ Hub-Contract | erfüllt |
| 3 | Querverweis `esp32-metermaster` | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (lokal) |

## Bezug

[INVENTORY](../../projects/iobroker-metermaster/INVENTORY.md) · [evidence](evidence.md) · [`VERSION`](../../VERSION)
