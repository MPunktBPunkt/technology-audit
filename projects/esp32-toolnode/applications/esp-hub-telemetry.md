# Project Application: esp-hub-telemetry in esp32.toolnode

```yaml
project_id: esp32-toolnode
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-toolnode-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

`HubClient` POST `/api/register`, `fwType: toolnode`, Payload inkl. `enabledModules` und Modul-IO (z. B. `rf_score`).

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `fwType=toolnode` | `EVID-HUB-2026-10-09-010` | `FACT` |
| Register-Payload mit Modulstatus | `EVID-HUB-2026-10-09-011` | `FACT` (ARCHITECTURE) |
