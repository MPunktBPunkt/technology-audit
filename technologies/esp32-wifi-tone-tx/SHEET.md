# Technology Sheet: ESP32-S3 Wi-Fi PHY CW Tone Keying TX

```yaml
slug: esp32-wifi-tone-tx
title: ESP32-S3 Wi-Fi PHY CW Tone Keying TX
primary: D
tags: [radio-tx, lab-only, fragile, esp-idf]
type: implementation
status: active
seen_in: [esp32sdr]
maturity:
  technology: R1
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/esp32sdr-2026-foreign
```

Nur Ebene **A**. Host-GUI, Message-Frames, Board-Serien → Application.  
**Recht:** Aussendung braucht Lizenz / Lab-Last; Sheet = Technik/Risiken, kein Antennenbetrieb.  
**Chip-Scope:** Belegt für **ESP32-S3** (Wi-Fi tone / `esp_phy_wifi_tx_tone` + rftest). Andere SoCs = `UNKNOWN` / Gate.

## Kurzfassung

Arbeitsfähiger Lab-TX auf dem S3, wenn Raw-I/Q-DAC-Replay **nicht** an die Antenne koppelt: der Vendor-**Wi-Fi-Kalibrierträger** wird ein-/ausgetastet bzw. zwischen **5 MHz-Kanalraster**-Frequenzen umgeschaltet. Damit sind **OOK/ASK/2-FSK** (GFSK ohne Formung) möglich — **kein** Phasenpfad (BPSK/QPSK), **kein** polarer Schmalband-SSB-Contract.

## Abgrenzung

- **Ist:** PHY CW tone keying / channel-grid FSK; lab messaging; S3.
- **Ist nicht:** `esp32-polar-phy-tx` (polar freq+gain, 13 cm Modes); `esp32-apll-fm-tx` (Classic UKW Clock-FM); Raw-I/Q DAC replay; undoc I/Q RX allein (`esp32-undoc-iq-rx`).

## Signalpfad-Kette

| Stufe | Claim | Status | Evidence |
|-------|-------|--------|----------|
| `esp_phy_rftest_*` + `esp_phy_wifi_tx_tone` | CW carrier on Wi-Fi channel | `FACT` | Upstream ESP32SDR README/Code |
| Kanalraster 5 MHz | `chan = (freq_mhz-2412)/5+1` | `FACT` | README |
| OOK/ASK via tone on/off | Bit-Keying | `FACT` (Upstream claim) | README + GUI link |
| 2-FSK via two channels | Freq keying | `FACT` (Upstream claim) | README |
| BPSK/QPSK / arbitrary I/Q | Phase / DAC replay | `REJECTED` on S3 | Exhaustive Upstream-Lab |
| Absolute power / legal EIRP | — | `UNKNOWN` | nicht KB-remeasured |

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Host bit/frame orchestrator | Timing oft host-seitig |
| unten | Wi-Fi PHY rftest / tone | Vendor-API, fragil |
| lateral | Undoc RX capture | oft zweites Board |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Tone-TX = polar PHY TX | `REJECTED` | anderer Contract/Band/API |
| DAC-Replay auf S3 strahlt I/Q | `REJECTED` | Upstream: done-bit ohne Antennen-Energie |
| GFSK = echte Gauss-Formung | `REJECTED` | Upstream: gleicher 2-FSK-Pfad |
| Alle ESP32-Serien gleich | `UNKNOWN` / Gate | nur S3 belegt |
| 0 % BER board-to-board = Produktqualität | `INFERRED` | author Lab; eng gekoppelt |

### Projektstart-Checkliste

- [ ] Chip = ESP32-S3? Sonst Gate
- [ ] Tone-keying vs. polar vs. APLL vs. raw-I/Q klar getrennt
- [ ] Recht / Lab-Last; keine Antenne ohne Befugnis
- [ ] Author-BER/SNR als `INFERRED` bis eigene IDs
- [ ] Application + `seen_in`

## Transfer

- Vierte RF-TX-Zelle neben APLL / polar / (rejected) raw-I/Q — wichtig für „was kann S3 senden?“.
- Für Hub-Messaging im 2.4 GHz-Lab denkbar; nicht für UKW oder Phasenmodulation.

## Referenzen

- [lozaning/ESP32SDR](https://github.com/lozaning/ESP32SDR)
- Kontrast: [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr) (RX), `esp32-polar-phy-tx`

## Offene Fragen

- Tone-API Stabilität über IDF/PHY-Rev?
- Übertragbarkeit C5/S31?
