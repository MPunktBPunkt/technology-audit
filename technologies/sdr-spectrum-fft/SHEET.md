# Technology Sheet: SDR Spectrum FFT

```yaml
slug: sdr-spectrum-fft
title: SDR Spectrum / FFT Analysis
primary: H
tags: [sdr, lab-only]
type: pattern
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

Muster: IQ von RTL-SDR → **FFT** → dB-Kurve / Peaks / kanalisierte Energie über Zeit. Dient Peak-Scan (UKW, Airband-Range, …) und Aktivitäts-Trigger (z. B. PMR). Getrennt von Demod-Pipelines und von DAB-`welle`‑Spektrum (kanalgebunden).

## Abgrenzung

- **Ist:** Mess-/Analyse-Pfad (Snapshot, Sweep, channelized watch).
- **Ist nicht:** Audio-Demod; DAB-OFDM-Interna allein; RF-Environment-WLAN-Scan (→ `rf-environment-monitor`).

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Ein Spektrum-Endpunkt für alle Bänder | `REJECTED` | Tool/API an Band/Zweck binden |
| JSON/`<pre>` reicht als UI | `HYPOTHESIS` | Kurve braucht Render-Pfad |
| FFT parallel zu Demod auf einem Stick | `REJECTED` | Lock/preempt nötig |
| Averaging optional ohne DC/Offset-Bewusstsein | `HYPOTHESIS` | Peek-Fenster DC-sicher halten |

### Projektstart-Checkliste

- [ ] Capture-API (center, rate, bins, peaks)
- [ ] Rate-Limit / Pi-Ressourcen
- [ ] Integration Scanner-Trigger
- [ ] UI: Kurve vs. nur JSON
- [ ] Application + `seen_in`

## Referenzen

- PiDrive `spectrum.py`, `SPECTRUM-CLI.md`
