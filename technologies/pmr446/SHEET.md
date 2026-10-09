# Technology Sheet: PMR446

```yaml
slug: pmr446
title: PMR446 (EU License-Free UHF)
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

**PMR446**: lizenzfreies UHF-Sprachnetz (EU), 16 Kanäle um **446.0–446.2 MHz** (12.5 kHz). Empfang/Monitor oft NFM über SDR; Aktivität kann spektrum-basiert (Kanalenergie/FFT) erkannt werden, bevor `rtl_fm` autotuned.

## Abgrenzung

- **Ist:** Kanalraster + typischer NFM-Hör-/Monitor-Pfad.
- **Ist nicht:** Freenet/LPD433/CB (eigene Raster); Airband-AM; DAB; generisches Spektrum-Tool allein.

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Nur 8 Kanäle sind „das“ PMR446 | `REJECTED` | EU-Erweiterung 16 Kanäle; Altgeräte oft K1–K8 |
| Peek unter Trigger = Activity | `REJECTED` | Hysterese on/off-dB trennen |
| Autotune während Spektrum-Capture unkritisch | `REJECTED` | Stick-Exklusivität / preempt |
| welle-cli spektrum für PMR | `REJECTED` | Frequenz außerhalb DAB-Kanäle |

### Projektstart-Checkliste

- [ ] 16-Kanal-Tabelle + Geräte-Kompatibilität
- [ ] Monitor: trigger_on/off, hold, autotune policy
- [ ] Spektrum-Watch vs. rtl_fm Listen trennen
- [ ] Application + `seen_in`

## Referenzen

- ECC/CEPT PMR446 · PiDrive `SCANNER-PMR.md`, `PMR-MONITOR.md`
