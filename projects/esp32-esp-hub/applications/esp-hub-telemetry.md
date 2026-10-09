# Project Application: esp-hub-telemetry in esp32-esp-hub

```yaml
project_id: esp32-esp-hub
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-esp-hub-2026-pilot/
maturity:
  technology: R4
  implementation: R3
  field_evidence: R2
  reusability: W4
```

## Rolle im Projekt

Referenz-Client: Heartbeat-Felder inkl. chipModel/freeSketch/ios; Response interval/otaUrl. **Arduino/C++** — Contract identisch zur Adapter-Spec.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Heartbeat-Feldtabelle | `EVID-HUB-2026-10-09-070` | `FACT` |
| Kein fwType-Pflicht in Basis | `EVID-HUB-2026-10-09-071` | `FACT` |
