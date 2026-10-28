# Audit Campaign: esp32-esp-hub-2026-pilot

```yaml
id: esp32-esp-hub-2026-pilot
project_id: esp32-esp-hub
started: 2026-10-09
ended: 2026-10-28
status: closed
profile: firmware
standard_version: "0.6.3"
standard_gaps: ["0.7.x Decision/Review-Kreislauf — Kampagne vor Regelstand; Revalidation unter 0.7.1"]
reviewed_commit: a03400a
superseded_by: esp32-esp-hub-2026-1.10-validation
reuse_outcomes:
  reused:
    - esp-hub-telemetry
    - esp-embedded-web-sse
  new:
    - esp-hub-base-template
  not_helped: []
  process: "Desk-Pilot 1.7.0 unter 0.6.3; Nachzug AppCore/M0–M11/gzip/Derived A/B → 1.10-validation 0.7.1."
```

## Ziel

Desk-Audit von `ESP32.esp-hub` unter **0.6.3**.

## Scope

Siehe [SCOPE](../../projects/esp32-esp-hub/SCOPE.md) (Stand Nachzug: 1.10.5; dieser Pilot pinte **1.7.0** @ `a03400a`).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.3 + profile | erfüllt |
| 2 | Template-Sheet + Hub/Web wachsen | erfüllt |
| 3 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 4 | Ableiten-Checkliste in Bootstrap | teilweise → Sheet in [1.10-validation](../esp32-esp-hub-2026-1.10-validation/); Bootstrap-Prompt FOLLOW-ON |

## Bezug

[INVENTORY](../../projects/esp32-esp-hub/INVENTORY.md) · [evidence](evidence.md) · Nachfolger: [`esp32-esp-hub-2026-1.10-validation`](../esp32-esp-hub-2026-1.10-validation/) · [`PROJECT-START`](../../docs/PROJECT-START.md) · [`VERSION`](../../VERSION)

## Lessons

- Neues Sheet `esp-hub-base-template` als Ableiten-Muster; Hub/Web als Contract-/UI-Sheets wachsen lassen.
- Pilot @ 1.7.0 / Monolith-Pfad reichte nicht für AppCore-Standard — Nachzug in [`1.10-validation`](../esp32-esp-hub-2026-1.10-validation/).
- Bootstrap-Prompt-Checkliste blieb bewusst offen (FOLLOW-ON).
