# Audit Campaign: esp32-metermaster-2026-pilot

```yaml
id: esp32-metermaster-2026-pilot
project_id: esp32-metermaster
started: 2026-10-09
ended: null
status: active
profile: firmware
standard_version: "0.6.1"
reviewed_commit: 60fa14b
```

## Ziel

Desk-Audit von `esp32.MeterMaster` unter **0.6.1** — Dual-/Triple-HTTP (Simple-API / Adapter / Hub), OLED-Sheet, Arduino-Monolith-Layout; kein fälschliches SSE-Sheet.

## Scope

Siehe [SCOPE](../../projects/esp32-metermaster/SCOPE.md).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | YAML `standard_version: "0.6.1"` + profile | erfüllt |
| 2 | Reuse-Match: Hub wachsen; Simple-API + OLED neu | erfüllt |
| 3 | Web-UI ohne SSE → nicht `esp-embedded-web-sse` | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 5 | Feld-Lesbarkeit OLED dokumentiert | offen |

## Bezug

[INVENTORY](../../projects/esp32-metermaster/INVENTORY.md) · [evidence](evidence.md) · [`VERSION`](../../VERSION)

## Offene Punkte

- Exit 4/5
- Adapter-HTTP als generisches Sheet bei zweitem Produkt
