# Project Application: bmw-etch-rpc in bimmergestalt-idrive-refs

```yaml
project_id: bimmergestalt-idrive-refs
tech_slug: bmw-etch-rpc
status: active
sheet: ../../../technologies/bmw-etch-rpc/SHEET.md
audit: ../../../audits/bimmergestalt-idrive-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

Pins: IDriveConnectKit@`95492b0` (`BMWRemoting.etch`), AAIdrive@`3e93419`,
BMWConnectedAnalysis@`9e96ac6`, Simulator@`6a38086`.

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Service BMWRemoting mit sas/cds/am/rhmi/av/map | `EVID-BG-2026-10-28-009` | `FACT` |
| Auth-Reihenfolge certificate→login | `EVID-BG-2026-10-28-010` | `FACT` |
| ATTACHED Intent host/port/instanceId | `EVID-BG-2026-10-28-011` | `FACT` |
| Etch URI maxPktSize 8388608 | `EVID-BG-2026-10-28-008` | `FACT` |
| Simulator SAS stub Port 4006 | `EVID-BG-2026-10-28-016` | `FACT` |
| Challenge 16 Bytes „observed“ | `EVID-BG-2026-10-28-021` | `INFERENCE` (Doc) |
