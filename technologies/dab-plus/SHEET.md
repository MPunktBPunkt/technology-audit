# Technology Sheet: DAB+

```yaml
slug: dab-plus
title: DAB+ Digital Audio Broadcasting
primary: A
tags: [sdr, streaming]
type: protocol
status: active
seen_in: [pidrive, welle-io]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/pidrive-2026-radio-bt
```

Nur Ebene **A**. Konkrete Pfade (`welle-cli`, Gain-Index-UI, Audio-Route) → Applications (`pidrive`, `welle-io`).

## Kurzfassung

**DAB/DAB+** (Band III, optional L-Band): Ensemble mit Services; Empfang typisch über SDR (Referenz-Stack: **welle.io** / `welle-cli` + RTL-SDR o. Ä.). Audio nach Demod/Decode (AAC/MP2); Metadaten u. a. DLS. Spektrum-/Mux-Diagnose im Webmodus ist **DAB-kanalgebunden** — kein Allzweck-Analysator.

## Abgrenzung

- **Ist:** Digitaler Rundfunk-Empfang + Ensemble/Service-Modell.
- **Ist nicht:** UKW-FM; PMR/Airband; generisches FFT-Spektrum über beliebige MHz (→ `sdr-spectrum-fft`); Stick-Locking (→ `rtl-sdr`); Pi-GPIO-FM-TX (→ `rpi-gpio-fm-tx`); ESP-APLL-FM-TX (→ `esp32-apll-fm-tx`). **RX ≠ TX.**

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | IQ/Samples (RTL-SDR, rtl_tcp, RAW, …) | Gain oft **Index**, nicht dB |
| oben | PCM / HTTP-Stream / ALSA | Decoder-Pfad |
| lateral | mux.json /spectrum im Webmodus | nur DAB-Kanäle / aktuelle Tunung |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Gain-Parameter = dB wie bei rtl_fm | `REJECTED` | welle/R820T: Index in Tuner-Gain-Tabelle (`setGain(index)`) |
| welle `/spectrum` ersetzt UKW/PMR-FFT | `REJECTED` | FFT über OFDM-`T_u` des laufenden Kanals |
| DAB-Audio folgt automatisch der BT/PipeWire-Politik | `HYPOTHESIS` | oft eigener ALSA-/HTTP-Pfad — Route explizit prüfen |
| Scan und Play teilen Stick konfliktfrei ohne Lock | `REJECTED` | exklusiver SDR-Zugriff nötig |
| Beliebiger SDR ohne Bandbreite/Tunability | `REJECTED` | DAB braucht ~2.048 MS/s und Band-III/L-Frequenzen (z. B. Airspy HF+ explizit ungeeignet) |
| CLI `-g -1` und manueller Index sind austauschbar ohne Semantik | `REJECTED` | `-1` = Software-AGC; sonst fester Tabellenindex |
| Empfangs-Sheet deckt Software-FM-TX ab | `REJECTED` | getrennte TX-Slugs; siehe `pi-fm-tx` / `esp-fm-tx` |

### Projektstart-Checkliste

- [ ] Toolkette (`welle-cli`) + Stick-Blacklist DVB
- [ ] Gain-Semantik (Index vs dB; Auto = Software-AGC) dokumentieren
- [ ] Audio-Route vs. andere Quellen (BT/Klinke/HTTP)
- [ ] DLS/Meta-Pfad getrennt von AVRCP/MPRIS klären
- [ ] Spektrum: DAB-Web vs. Allzweck-FFT trennen
- [ ] Application + `seen_in`

## Referenzen

- ETSI DAB/DAB+ · [welle.io](https://github.com/AlbrechtL/welle.io) · PiDrive `docs/referenz/WELLE-CLI.md`
- Kampagnen: `pidrive-2026-radio-bt`, `welle-io-2026-foreign`
