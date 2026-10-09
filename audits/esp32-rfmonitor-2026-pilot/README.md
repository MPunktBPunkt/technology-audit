# Audit Campaign: esp32-rfmonitor-2026-pilot

```yaml
id: esp32-rfmonitor-2026-pilot
project_id: esp32-rfmonitor
started: 2026-10-09
ended: null
status: active
profile: firmware
standard_version: "0.6.0"
standard_gaps: ["0.6.1 Geschwister-Reuse / G9–G11 / Arduino-Layout — Kampagne vor Regelstand"]
reviewed_commit: 95314cd
```

## Ziel

Desk-Audit von `esp32.rfmonitor` unter **Audit-Standard 0.6.0** — Test von `standard_version` + Reuse/Profile. Neues Sheet `rf-environment-monitor`; Hub/Web wachsen.

## Scope

Siehe [SCOPE](../../projects/esp32-rfmonitor/SCOPE.md).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | YAML `standard_version: "0.6.0"` + profile | erfüllt |
| 2 | Reuse-Match Inventar | erfüllt |
| 3 | Sheet `rf-environment-monitor` + Apps Hub/Web | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 5 | Feldkalibrierung RF-Score an ≥1 Standort | offen |

## Bezug

[INVENTORY](../../projects/esp32-rfmonitor/INVENTORY.md) · [evidence](evidence.md) · Standard: [`STANDARD-CHANGELOG`](../../docs/STANDARD-CHANGELOG.md) · [`VERSION`](../../VERSION)

## Offene Punkte

- Exit 5 Feldserie
- Optional: Method Note für RF-Score-Kalibrierung
