# Technology Sheet: ESP32 Undocumented I/Q RX Dump

```yaml
slug: esp32-undoc-iq-rx
title: ESP32 Undocumented I/Q RX Dump
primary: A
tags: [radio-rx, sdr, lab-only, fragile, esp-idf]
type: implementation
status: active
seen_in: [espargos-espsdr, c5vrx, esp32-sdr-trx]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/espargos-espsdr-2026-foreign
```

Nur Ebene **A**. Board-Ports, Host-Bridges und Demod-Apps → Application.  
**Recht / Vendor:** undokumentierter PHY-Debug-Pfad — kein öffentlicher Contract; kann in IDF/ROM-Revisionen brechen. Lab-/Amateur-Kontext, kein Produkt-SoT.

## Kurzfassung

Mehrere unabhängige Projekte nutzen einen **undokumentierten Sample-Dump** der Wi‑Fi-/Modem-PHY auf ESP32-Familie-Chips: rohe **I/Q-Basisbandproben** (typisch gepackt, oft 10‑bit) statt nur Paket-MAC. Capture-Raten, Duty-Cycle und Transport (UART/USB/Ethernet/FPGA) sind **stark chipabhängig**. Das Sheet ist die **Chip-Capability-Matrix** und Abgrenzung — keine Anleitung zum Missbrauch.

## Abgrenzung

- **Ist:** Undokumentierter RX-I/Q-/Modem-Diagnose-Pfad; chipweise Raten/Modi; Host-Bridges (rtl_tcp, Soapy, WebSDR) als laterale Muster.
- **Ist nicht:** Classic APLL/MCLK UKW-FM (`esp32-apll-fm-tx`); polar PHY-TX (`esp32-polar-phy-tx`); RTL-SDR USB-Dongle (`rtl-sdr`); dokumentierte Espressif-SDR-API; legale Breitband-Abhörstation.

## Chip-Capability-Matrix (Desk, Upstream-dokumentiert)

Epistemic: Zellen sind **FACT als Upstream-Doku/Code** — nicht als eigene Lab-Messung dieser KB. Absolute Sensitivität/ENOB = `UNKNOWN`.

| Chip | Dump / Capture (Upstream) | Continuous / Spezial | Band-Hinweis | Status |
|------|---------------------------|----------------------|--------------|--------|
| Classic ESP32 | Burst/FFT (ESPARGOS) | — | ~2.2–2.7 GHz typ. | `FACT` (esp-sdr) |
| S2 | Burst + USB-OTG | — | wie Familie | `FACT` |
| S3 | Burst; narrowband CIC/FIR→USB; FPGA@80 Msps | IQS 15.625–250 kSa/s (esp-sdr); 80 Msps+FPGA (h0m3us3r) | 2.4 GHz-nah | `FACT` |
| S31 | Burst; stream firmware | bis ~20 MSa/s USB / ~40 MSa/s Eth (experimentell) | wie Familie | `FACT` (doku); Qualität `UNKNOWN` |
| C3 / C6 / C61 / H2 / C2 | Burst/FFT | — | chipabhängig | `FACT` (Tabelle) |
| C5 | Burst; **5 GHz**-Band | Continuous MODEM_DIAG→Demod (C5VRX) | 4.8–6.0 GHz (esp-sdr); 5.8 GHz FPV (C5VRX) | `FACT` |
| P4 | kein integriertes Radio | — | — | `FACT` (unsupported) |
| H21 / H4 | WIP | — | — | `UNKNOWN` / preview |

## Signalpfad-Kette (generisch)

| Stufe | Claim | Status |
|-------|-------|--------|
| Undokumentierter PHY dump / MODEM_DIAG | I/Q oder Diagnose-Samples | `FACT` (mehrere Upstreams) |
| On-chip Decimation / FFT / BitScrambler | chip-/projektabhängig | `FACT` pro Application |
| Transport (UART / USB / Eth / GPIO→FPGA) | Bandbreite begrenzt Duty-Cycle | `FACT` |
| Host SDR (rtl_tcp / Soapy / custom) | Backend-Portabilität (G7) | `FACT` als Muster |
| Absolute RF-Performance | Sensitivität, Spurs, DC-Peak | `UNKNOWN` ohne eigene Messung |

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Spektrum / Demod / Video / rtl_tcp-Client | Application |
| unten | Undokumentierte PHY-Register / libphy | bricht ohne Warnung möglich |
| lateral | Chip-Matrix, IDF-Target, Kristall | G17: nie still übertragen |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| „ESP32 kann SDR“ gilt für alle Targets gleich | `REJECTED` | Matrix: Raten/Continuous/Bands differieren |
| S3-80 Msps ohne FPGA = Universal-Node | `REJECTED` / Gate | High-rate-Pfad braucht externes Transport (FPGA/USB3) oder Decimation |
| C5/S31 = gleiche Caps wie S3 | `UNKNOWN` bis Gate | eigene Zeile; nicht aus S3 ableiten |
| Undokumentiert = stabiler Vendor-Contract | `REJECTED` | Debug-Pfad |
| TX öffentlich in ESPARGOS-Firmware | `REJECTED` (Stand Desk) | Site: TX möglich, Code withheld |
| Tutorial/AI-Code ersetzt Messung | `REJECTED` | Author-reported ≠ KB-`MEASURED` |

### Projektstart-Checkliste

- [ ] Ziel-Chip in Matrix benannt (G17)?
- [ ] Burst vs. continuous vs. FPGA-Pfad klar?
- [ ] Host-Backend (rtl_tcp/Soapy/custom) gewählt — Portabilität notiert?
- [ ] Kein Merge mit `esp32-apll-fm-tx` / polar-TX?
- [ ] Application + `seen_in`; Claims ohne Lab = max. `INFERRED`/`FACT`-Upstream

## Transfer

- Primärquelle für **Chip-Matrix** und G7 (Host-Backend-Wechsel bei gleichem Dump-Contract).
- Kontrast zu polar-TX: RX-Dump ≠ Träger-Steuerung.
- Universal-RF-Node: S3-narrowband (esp32-sdr-trx) und esp-sdr-IQS sind Kandidaten — High-rate-S3 braucht FPGA oder Decimation.

## Referenzen

- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr) · [espargos.net/espsdr](https://espargos.net/espsdr)
- [ESPARGOS/SoapyESPSDR](https://github.com/ESPARGOS/SoapyESPSDR)
- [h0m3us3r/eSpDR](https://github.com/h0m3us3r/eSpDR) · [jochenhammes/esp32-sdr-trx](https://github.com/jochenhammes/esp32-sdr-trx)
- [Twotoz/C5VRX](https://github.com/Twotoz/C5VRX)

## Offene Fragen

- Welche Dump-Register bleiben über IDF-Versionen stabil?
- S31 DC-Peak / Signalqualität nach Upstream-Hinweis?
- Phase-Kohärenz Multi-Chip (ESPARGOS-Array) für Hub-Szenarien?
