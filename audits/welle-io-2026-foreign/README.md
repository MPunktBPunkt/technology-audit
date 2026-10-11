# Audit Campaign: welle-io-2026-foreign

```yaml
id: welle-io-2026-foreign
project_id: welle-io
started: 2026-10-11
ended: null
status: active
profile: lab-tool
standard_version: "0.6.5"
reviewed_commit: "512558d"
reuse_outcomes:
  reused: [dab-plus, rtl-sdr]
  new: []
  not_helped: []
```

## Ziel

Fremd-Upstream [AlbrechtL/welle.io](https://github.com/AlbrechtL/welle.io) in die KB: bestehende Empfangs-Sheets validieren/wachsen lassen (Gain-Index, Kanalmodell, Web-Spektrum-Grenze), Applications für den Quellcode, Kontrast zu PiDrive-Ops und zu Allzweck-FFT / GPIO-TX.

## Scope

[SCOPE](../../projects/welle-io/SCOPE.md) — Desk only; **kein** Feldempfang.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | `standard_version` 0.6.5 + Profil `lab-tool` | erfüllt |
| 2 | Reuse: kein neues DAB-/RTL-Sheet; RX≠TX; Spectrum≠Allzweck-FFT | erfüllt |
| 3 | Sheets `dab-plus`, `rtl-sdr` gewachsen + Apps | erfüllt |
| 4 | Evidence auf Commit `512558d` | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 6 | Feldempfang gemessen | offen (bewusst) |

## Bezug

[INVENTORY](../../projects/welle-io/INVENTORY.md) · [evidence](evidence.md) · Ops [`pidrive-2026-radio-bt`](../pidrive-2026-radio-bt/) · TX-Kontrast [`pi-fm-tx-2026-foreign`](../pi-fm-tx-2026-foreign/)

## Lessons → Transfer

- Gain ist Upstream-seitig **Index** in die librtlsdr-Gain-Tabelle; AGC = Software-Schritte — bestätigt PiDrive-Fallstrick.
- `/spectrum` FFT über `dabparams.T_u` des aktuellen Kanals — kein Ersatz für `sdr-spectrum-fft`.
