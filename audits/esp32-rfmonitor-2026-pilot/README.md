# Audit Campaign: esp32-rfmonitor-2026-pilot

```yaml
id: esp32-rfmonitor-2026-pilot
project_id: esp32-rfmonitor
started: 2026-10-09
ended: 2026-10-25
status: closed
profile: firmware
standard_version: "0.6.0"
standard_gaps: ["0.6.1 Geschwister-Reuse / G9–G11 / Arduino-Layout — Kampagne vor Regelstand"]
reviewed_commit: 95314cd
superseded_by: esp32-rfmonitor-2026-v2-validation
reuse_outcomes:
  reused:
    - esp-hub-telemetry
    - esp-embedded-web-sse
  new:
    - rf-environment-monitor
  not_helped: []
  process: "Desk-Pilot 1.1.0 unter 0.6.0; Nachzug Observability/Score-v2/Lab → v2-validation 0.7.1."
```

## Ziel

Desk-Audit von `esp32.rfmonitor` unter **Audit-Standard 0.6.0** — Test von `standard_version` + Reuse/Profile. Neues Sheet `rf-environment-monitor`; Hub/Web wachsen.

## Scope

Siehe [SCOPE](../../projects/esp32-rfmonitor/SCOPE.md) (Stand 1.1.0 @ `95314cd`).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | YAML `standard_version: "0.6.0"` + profile | erfüllt |
| 2 | Reuse-Match Inventar | erfüllt |
| 3 | Sheet `rf-environment-monitor` + Apps Hub/Web | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 5 | Feldkalibrierung RF-Score an ≥1 Standort | teilweise → Lab-Baseline in [v2-validation](../esp32-rfmonitor-2026-v2-validation/); zweiter Standort offen |

## Bezug

[INVENTORY](../../projects/esp32-rfmonitor/INVENTORY.md) · [evidence](evidence.md) · Nachfolger: [`esp32-rfmonitor-2026-v2-validation`](../esp32-rfmonitor-2026-v2-validation/) · Standard: [`STANDARD-CHANGELOG`](../../docs/STANDARD-CHANGELOG.md)

## Lessons

- Neues Pattern-Sheet `rf-environment-monitor` unter 0.6.0 tragfähig; Hub/Web Reuse ohne Fork.
- Desk @ 1.1.0 reicht nicht für Observation/Score-v2 — Upstream-Update braucht eigene Kampagne (→ v2-validation).
- Exit #5 „Kalibrierung“ war zu grob: Lab-Baseline schließt Desk→Lab, nicht Standort-Transfer.

## Offene Punkte

- Übernommen von v2-validation: Exit #5 Rest (Standort 2), Hub-Adapter Contract v2
