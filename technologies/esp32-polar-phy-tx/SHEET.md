# Technology Sheet: ESP32-S3 Polar PHY Test-Tone TX

```yaml
slug: esp32-polar-phy-tx
title: ESP32-S3 Polar PHY Test-Tone TX
primary: D
tags: [radio-tx, sdr, lab-only, fragile, esp-idf]
type: implementation
status: active
seen_in: [esp32-sdr-trx]
maturity:
  technology: R1
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/esp32-sdr-trx-2026-foreign
```

Nur Ebene **A**. Host-CLI, Thermal-Modelle, Board-Serien → Application.  
**Recht:** Aussendung im Amateurfunkband braucht Lizenz; unlizenzierter Antennenbetrieb ist illegal. Sheet = Technik/Risiken, kein Sendebetrieb.  
**Chip-Scope:** Belegt für **ESP32-S3** in den Upstream-Repos. Andere SoCs = `UNKNOWN` / Gate (G17/G19).

## Kurzfassung

Statt APLL→GPIO-Clock oder Sample-I/Q-TX steuert die Firmware den **undokumentierten PHY-Testträger** in **Frequenz und Amplitude** (polare Modulation). Damit sind schmalbandige **FM / SSB / RTTY** im 13‑cm-Bereich auf einem S3 ohne FPGA möglich. Das ist ein **anderer Contract** als Classic `esp32-apll-fm-tx` und als Raw-I/Q-Playback.

## Abgrenzung

- **Ist:** S3 PHY test-tone polar steer (freq + gain); narrowband Modes; lab/Amateur-Experiment.
- **Ist nicht:** Classic APLL/MCLK UKW (`esp32-apll-fm-tx`); undokumentierter I/Q-RX-Dump allein (`esp32-undoc-iq-rx`); Raw-I/Q SRAM-TX @80 Msps (Research-Zweig, nicht Release-Pfad); externe FM-Chips (QN8027); legale Broadcast-Station.

## Signalpfad-Kette

| Stufe | Claim | Status | Evidence |
|-------|-------|--------|----------|
| Undokumentierter PHY test tone | Trägerquelle ohne Sample-Buffer | `FACT` | Upstream Firmware/Docs |
| Freq-Steuerung (PLL/SDM low-byte / offset records) | Schmalband-FM/SSB/RTTY | `FACT` | `transmit.h` Protocol |
| Amplitude / gain codes | Polar (mag) | `FACT` | Protocol gain field |
| Host record stream @ 8–40 kHz | Live-Modulation | `FACT` | Protocol + host tools |
| Thermal drift @ 2.3 GHz | kHz-Drift ohne Korrektur | `INFERRED` | Author-reported Lab; nicht KB-remeasured |
| Absolute Power / Spurs / Harmonics | Pegel, Nebenaussendungen | `UNKNOWN` | Author: uncalibrated |
| Gleicher Pfad auf C5/S31/Classic | Transfer | `UNKNOWN` | Gate |

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Audio/Text → Mode-Encoder (FM/SSB/RTTY) | Host |
| unten | Undokumentierte PHY + libphy | Vendor-Risiko |
| lateral | Temp-Sensor → Drift-Modell | board-spezifisch |
| lateral | RX-Dump / rtl_tcp | oft gleiches Board, anderer Contract |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Polar-TX = APLL-FM auf anderem Chip | `REJECTED` | anderer Peripheral-Contract, anderes Band |
| S3 Universal-RF-Node „fertig“ | `HYPOTHESIS` | RX+TX experimentell; Power/Spurs offen |
| Author-Hz/dB = KB-`MEASURED` | `REJECTED` | Claude-assistiert + 1–2 Boards → revalidieren |
| Raw I/Q TX ist Release-Pfad | `REJECTED` | `research/iq-tx`; polar ist Release-TX |
| Thermal-Modell board-übertragbar | `REJECTED` | Upstream: Modell pro Board |
| Ohne Lizenz Antenne ok | `REJECTED` | Legal |

### Projektstart-Checkliste

- [ ] Chip = ESP32-S3? Sonst Gate
- [ ] Polar vs. Raw-I/Q vs. APLL klar getrennt
- [ ] Recht: Lizenz / Lab-Last, keine Antenne ohne Befugnis
- [ ] Author-Messwerte als `INFERRED` bis eigene Lab-IDs
- [ ] Application + `seen_in`

## Transfer

- Starke Kontrastzelle zu `esp32-apll-fm-tx` (Classic UKW Clock-FM vs. S3 13 cm polar PHY).
- Für Hub-/Universal-Node: S3 kann RX-Dump **und** polar-TX tragen — aber getrennte Contracts, getrennte Evidence.
- Methoden: `hw-path-gate` für jeden neuen SoC; keine Matrix-Zelle aus Marketing.

## Referenzen

- [jochenhammes/esp32-sdr-trx](https://github.com/jochenhammes/esp32-sdr-trx) (`NOTICE`: from h0m3us3r/eSpDR `f279bf8`)
- [h0m3us3r/eSpDR](https://github.com/h0m3us3r/eSpDR) (RX-Ursprung; TX-Research Issues)
- Kontrast: [`esp32-apll-fm-tx`](../esp32-apll-fm-tx/SHEET.md), [`esp32-undoc-iq-rx`](../esp32-undoc-iq-rx/SHEET.md)

## Offene Fragen

- Reproduktion polar-TX auf zweitem Lab-Board (fremde Messung)?
- Spurious / ACLR / Harmonics messbar?
- Übertragbarkeit C5 5 GHz-PHY (vermutlich nein ohne Gate)?
