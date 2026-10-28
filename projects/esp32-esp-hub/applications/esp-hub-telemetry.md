# Project Application: esp-hub-telemetry in esp32-esp-hub

```yaml
project_id: esp32-esp-hub
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-esp-hub-2026-1.10-validation/
maturity:
  technology: R4
  implementation: R4
  field_evidence: R3
  reusability: W4
```

## Rolle im Projekt

Referenz-Client `HubClient`: `POST /api/register` schlank (Basis + `freePsram`/`psramSize`); Reply `interval` / `otaUrl` / `name`. Additive `hwSummary`/`module`/`cpu*` in Status und oft Heartbeat — Diag bleibt Base-only.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp-hub-base/src/core/HubClient.cpp` | Register + Reply-Parser |
| `esp-hub-base/src/core/HardwareInfo.*` | Caps / `hwSummary` |
| `esp-hub-base/src/core/CpuLoad.*` | `cpu`/`cpu0`/`cpu1` |
| README Heartbeat-Tabelle | Contract-Doku |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Heartbeat schlank + PSRAM-Felder | `EVID-HUB-2026-10-28-001` | `FACT` |
| Reply interval/otaUrl/name | `EVID-HUB-2026-10-28-002` | `FACT` |
| Additive hwSummary/cpu erlaubt | `EVID-HUB-2026-10-28-003` | `FACT` |
| Kein fwType-Pflicht in Basis | `EVID-HUB-2026-10-09-071` | `FACT` |
