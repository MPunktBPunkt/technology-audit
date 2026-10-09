# Project Application: airband-am in PiDrive

```yaml
project_id: pidrive
tech_slug: airband-am
status: active
sheet: ../../../technologies/airband-am/SHEET.md
audit: ../../../audits/pidrive-2026-radio-bt/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle

AM-Demod über Scanner; Presets `airband_stations.json` (z. B. EDJA); CLI `scanner airband`; WebUI Dauerbeobachtung. Spectrum-Scan 118–137 nur Peak-FFT.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| rtl_fm -M am + Presets | `EVID-AIR-2026-10-09-001` | `FACT` |
| FFT-Scan ≠ AM-Demod | `EVID-AIR-2026-10-09-002` | `FACT` |
