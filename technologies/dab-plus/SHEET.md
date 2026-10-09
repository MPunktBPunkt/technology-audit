# Technology Sheet: DAB+

```yaml
slug: dab-plus
title: DAB+ Digital Audio Broadcasting
primary: A
tags: [sdr, streaming]
type: protocol
status: active
seen_in: [pidrive]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/pidrive-2026-radio-bt
```

Nur Ebene **A**. PiDrive-Pfad (`welle-cli`, Gain-Index, Audio-Route) → Application.

## Kurzfassung

**DAB/DAB+** (Band III, optional L-Band): Ensemble mit Services; Empfang typisch über SDR (`welle-cli` + RTL-SDR). Audio nach Demod/Decode (AAC/MP2); Metadaten u. a. DLS. Spektrum-/Mux-Diagnose über Webmodus ist DAB-kanalgebunden — kein Allzweck-Analysator.

## Abgrenzung

- **Ist:** Digitaler Rundfunk-Empfang + Ensemble/Service-Modell.
- **Ist nicht:** UKW-FM; PMR/Airband; generisches FFT-Spektrum über beliebige MHz (→ `sdr-spectrum-fft`); Stick-Locking (→ `rtl-sdr`).

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | IQ/Samples (RTL-SDR, rtl_tcp, RAW) | Gain oft **Index**, nicht dB |
| oben | PCM / HTTP-Stream / ALSA | Decoder-Pfad |
| lateral | mux.json /spectrum im Webmodus | nur DAB-Kanäle |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Gain-Parameter = dB wie bei rtl_fm | `REJECTED` | welle/R820T oft Gain-**Index** |
| welle `/spectrum` ersetzt UKW/PMR-FFT | `REJECTED` | nur Band III/L über Kanalnamen |
| DAB-Audio folgt automatisch der BT/PipeWire-Politik | `HYPOTHESIS` | oft eigener ALSA-Pfad — Route explizit prüfen |
| Scan und Play teilen Stick konfliktfrei ohne Lock | `REJECTED` | exklusiver SDR-Zugriff nötig |

### Projektstart-Checkliste

- [ ] Toolkette (`welle-cli`) + Stick-Blacklist DVB
- [ ] Gain-Semantik (Index vs dB) dokumentieren
- [ ] Audio-Route vs. andere Quellen (BT/Klinke)
- [ ] DLS/Meta-Pfad getrennt von AVRCP/MPRIS klären
- [ ] Application + `seen_in`

## Referenzen

- ETSI DAB/DAB+ · welle.io · PiDrive `docs/referenz/WELLE-CLI.md`
