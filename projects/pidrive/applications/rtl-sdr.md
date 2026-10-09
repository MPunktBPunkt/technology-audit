# Project Application: rtl-sdr in PiDrive

```yaml
project_id: pidrive
tech_slug: rtl-sdr
status: active
sheet: ../../../technologies/rtl-sdr/SHEET.md
audit: ../../../audits/pidrive-2026-radio-bt/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle

Zentrale Stick-Verwaltung: flock-Lock, DVB-Check, USB-Reset (sysfs `0bda`), Diagnose `/tmp/pidrive_rtlsdr.json`. Owner: fm / dab / scanner / spectrum.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Exklusives Lock + Owner | `EVID-RTL-2026-10-09-001` | `FACT` |
| USB-Reset über sysfs authorized | `EVID-RTL-2026-10-09-002` | `FACT` |
