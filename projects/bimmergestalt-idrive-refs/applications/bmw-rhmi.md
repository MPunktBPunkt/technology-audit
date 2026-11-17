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

Pins: IDriveConnectKit RHMI-* (`95492b0`), AAIdrive carapp/* (`3e93419`),
IDriveConnectAddons screen_mirror (`270032d`), BMWConnectedAnalysis (`9e96ac6`),
HassGestalt, IDriveExperiments/richtext.

Follow-on Audit: [`bimmergestalt-rhmi-checkresource-2026-11-17`](../../../audits/bimmergestalt-rhmi-checkresource-2026-11-17/).

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| XML loadFromXML → models/actions/events/states | `EVID-BG-2026-10-28-013` | `FACT` |
| Lifecycle create→setResource→initialize→handlers | `EVID-BG-2026-10-28-013` | `FACT` |
| `checkResource(true)` skips `setResource`; MD5 cache vs SHA-256 whitelist | `EVID-BG-RHMI-2026-11-17-001` (`RHMIUtils` + `authentication.md`) | `FACT` (Desk) |
| App Resource-Matrix Music/Notification/Sneaky/ScreenMirror | `EVID-BG-RHMI-2026-11-17-002` | `FACT` (Desk Code) |
| ScreenMirror JPEG → RaImageModel / IMAGEDATA setData | `EVID-BG-RHMI-2026-11-17-003` | `FACT` (Desk Code) |
| ServiceException(213) on ImageID←0 (2019 mock) | `EVID-BG-RHMI-2026-11-17-004` | `FACT` (Desk Mock) |
| hmi.type/version steuern Layout (ID4/5/6) | `EVID-BG-2026-10-28-014` | `FACT` |
| AV av_create + av_requestConnection Entertainment | `EVID-BG-2026-10-28-015` | `FACT` |
| richtext List-Model Experiment | `EVID-BG-2026-10-28-017` | `FACT` (Code); HU-Verhalten `UNKNOWN` |
