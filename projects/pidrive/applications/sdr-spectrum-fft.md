# Project Application: sdr-spectrum-fft in PiDrive

```yaml
project_id: pidrive
tech_slug: sdr-spectrum-fft
status: active
sheet: ../../../technologies/sdr-spectrum-fft/SHEET.md
audit: ../../../audits/pidrive-2026-radio-bt/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle

`spectrum.py`: IQ/`rtl_sdr`, FFT, Peaks, channelized watch für PMR; CLI `pidrivectl spectrum scan|peek|last`. Presets FM/Airband/PMR/DAB-Anker/GSM in WebUI — Analyse, kein Demod.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| capture_spectrum + peaks API | `EVID-FFT-2026-10-09-001` | `FACT` |
| welle-/spectrum ≠ Allzweck | `EVID-FFT-2026-10-09-002` | `FACT` |
