# Project Application: bmw-rhmi in bimmergestalt-idrive-refs

```yaml
project_id: bimmergestalt-idrive-refs
tech_slug: bmw-rhmi
status: active
sheet: ../../../technologies/bmw-rhmi/SHEET.md
audit: ../../../audits/bimmergestalt-idrive-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

Pins: IDriveConnectKit RHMI-*, AAIdrive carapp/*, HassGestalt, IDriveExperiments/richtext.

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| XML loadFromXML → models/actions/events/states | `EVID-BG-2026-10-28-013` | `FACT` |
| Lifecycle create→setResource→initialize→handlers | `EVID-BG-2026-10-28-013` | `FACT` |
| hmi.type/version steuern Layout (ID4/5/6) | `EVID-BG-2026-10-28-014` | `FACT` |
| AV av_create + av_requestConnection Entertainment | `EVID-BG-2026-10-28-015` | `FACT` |
| richtext List-Model Experiment | `EVID-BG-2026-10-28-017` | `FACT` (Code); HU-Verhalten `UNKNOWN` |
