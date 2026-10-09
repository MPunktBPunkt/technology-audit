# Technology Sheet: RTL-SDR

```yaml
slug: rtl-sdr
title: RTL-SDR (RTL2832U Host Stack)
primary: A
tags: [sdr, usb-host]
type: technology
status: active
seen_in: [pidrive]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/pidrive-2026-radio-bt
```

## Kurzfassung

Günstiger USB-SDR (typisch **RTL2832U + R820T/R820T2**): ein Stick, viele Nutzerprozesse (`rtl_fm`, `rtl_sdr`, `welle-cli`). Erfolg hängt von **Exklusivität**, DVB-Kernel-Modulen, PPM/Gain und USB-Recovery ab — nicht nur von der Demod-App.

## Abgrenzung

- **Ist:** Host-seitige Stick-Verwaltung und Sample-Quelle.
- **Ist nicht:** DAB-/FM-/PMR-Semantik selbst; FFT-Algorithmus (→ `sdr-spectrum-fft`).

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Mehrere Apps öffnen den Stick parallel | `REJECTED` | Kernel/USB claim — flock/Owner nötig |
| DVB-Module dürfen geladen bleiben | `REJECTED` | oft Blacklist `dvb_usb_rtl28xxu` etc. |
| usbreset allein reicht immer | `REJECTED` | `authorized=0` → sysfs re-enable |
| Ein Gain-Wert passt FM/Airband/DAB | `REJECTED` | getrennte Defaults/Übersteuerung |
| PPM ist optional bei schmalen Kanälen | `HYPOTHESIS` | bei PMR/Airband oft spürbar |

### Projektstart-Checkliste

- [ ] Erkennung passiv (kein Open) vs. aktiver Test
- [ ] Lock-Owner-Modell (fm/dab/scanner/spectrum)
- [ ] DVB-Blacklist + USB-Reset-Pfad
- [ ] PPM-Kalibrierung / Gain-Profile pro Mode
- [ ] Application + `seen_in`

## Referenzen

- osmocom rtl-sdr · PiDrive `modules/radio/rtlsdr.py`
