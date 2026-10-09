# Technology Sheet: Airband AM (VHF)

```yaml
slug: airband-am
title: VHF Airband AM Reception
primary: A
tags: [sdr, radio]
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

## Kurzfassung

Flugfunk-**Airband** (ca. **118–137 MHz**, AM): Empfang typisch `rtl_fm -M am` mit schmaler Bandbreite und Sprach-Filter; Presets (ATIS/Tower/…) lokal. FFT-Peak-Scan im Band ≠ AM-Demod/Zero-Span.

## Abgrenzung

- **Ist:** VHF-AM Hör-/Scan-Pfad + Preset-Modell.
- **Ist nicht:** PMR446-NFM; UKW-WBFM; legale Hinweise ersetzen keine lokale Vorschrift.

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| spectrum scan 118–137 = Airband hören | `REJECTED` | Peak-FFT ≠ AM-Demod |
| Airband-Gain = FM-Gain | `REJECTED` | oft deutlich höher / anderes Overload |
| Eine globale Stationstabelle reicht überall | `REJECTED` | Flugplatz-Presets lokal pflegen |

### Projektstart-Checkliste

- [ ] AM-Parameter (SR, squelch, HP/LP)
- [ ] Preset-Datei vs. Freitext-Freq
- [ ] Monitor/Dauerbeobachtung vs. manueller Tune
- [ ] Application + `seen_in`

## Referenzen

- ICAO VHF COM band overview · PiDrive `airband_stations.json`, `scanner.py`
