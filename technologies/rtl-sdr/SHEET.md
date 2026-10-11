# Technology Sheet: RTL-SDR

```yaml
slug: rtl-sdr
title: RTL-SDR (RTL2832U Host Stack)
primary: A
tags: [sdr, usb-host]
type: technology
status: active
seen_in: [pidrive, welle-io]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/pidrive-2026-radio-bt
```

## Kurzfassung

Günstiger USB-SDR (typisch **RTL2832U + R820T/R820T2**): ein Stick, viele Nutzerprozesse (`rtl_fm`, `rtl_sdr`, `welle-cli`). Erfolg hängt von **Exklusivität**, DVB-Kernel-Modulen, PPM/Gain und USB-Recovery ab — nicht nur von der Demod-App. Apps können Gain als **dB**, als **Index** in die librtlsdr-Tabelle oder als Software-AGC über Indizes modellieren — nicht vermischen.

**Chip-/Tuner-Scope:** belegte Familie in dieser KB = **RTL2832U + R820T/R820T2** (welle/PiDrive). Andere Tuner/SDR (Airspy, …) nicht still übernehmen — Bandbreite/API prüfen.

## Abgrenzung

- **Ist:** Host-seitige Stick-Verwaltung und Sample-Quelle (lokal oder rtl_tcp).
- **Ist nicht:** DAB-/FM-/PMR-Semantik selbst; FFT-Algorithmus (→ `sdr-spectrum-fft`); Pi-GPIO-**Sendung** (→ `rpi-gpio-fm-tx`); beliebiger SDR ohne denselben Stick-Contract.

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Mehrere Apps öffnen den Stick parallel | `REJECTED` | Kernel/USB claim — flock/Owner nötig |
| DVB-Module dürfen geladen bleiben | `REJECTED` | oft Blacklist `dvb_usb_rtl28xxu` etc. |
| usbreset allein reicht immer | `REJECTED` | `authorized=0` → sysfs re-enable |
| Ein Gain-Wert passt FM/Airband/DAB | `REJECTED` | getrennte Defaults/Übersteuerung |
| PPM ist optional bei schmalen Kanälen | `HYPOTHESIS` | bei PMR/Airband oft spürbar |
| „Gain 40“ ist überall 40 dB | `REJECTED` | welle.io: Index in `rtlsdr_get_tuner_gains`; Anzeige dB = Tabelle/10 |
| Hardware-AGC der Stick-API reicht für DAB-welle | `REJECTED` | welle setzt manual mode und regelt in Software |
| Jeder USB-SDR erbt denselben Lock/Gain-Contract | `REJECTED` (als FACT) | Tuner-/API-Scope; DAB-Bandbreite prüfen |

### Projektstart-Checkliste

- [ ] Tuner-Familie / Stick-Contract benennen (RTL2832U+R820T vs. andere)
- [ ] Erkennung passiv (kein Open) vs. aktiver Test
- [ ] Lock-Owner-Modell (fm/dab/scanner/spectrum)
- [ ] DVB-Blacklist + USB-Reset-Pfad
- [ ] PPM-Kalibrierung / Gain-Profile pro Mode (Index vs dB klären)
- [ ] rtl_tcp vs. lokales USB bewusst wählen
- [ ] Application + `seen_in`

## Referenzen

- osmocom rtl-sdr · PiDrive `modules/radio/rtlsdr.py` · welle.io `src/input/rtl_sdr.cpp`
- Kampagnen: `pidrive-2026-radio-bt`, `welle-io-2026-foreign`
