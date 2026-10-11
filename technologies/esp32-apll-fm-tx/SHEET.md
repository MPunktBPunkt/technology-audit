# Technology Sheet: ESP32 APLL / MCLK FM Transmit

```yaml
slug: esp32-apll-fm-tx
title: ESP32 APLL / MCLK FM Transmit
primary: D
tags: [radio-tx, lab-only, fragile, esp-idf]
type: implementation
status: active
seen_in: [esp-fm-tx]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/esp-fm-tx-2026-foreign
```

Nur Ebene **A**. Repo-Pfade und WebUI → Application.  
**Recht:** unlizenzierter Sendebetrieb mit Antenne ist in den meisten Ländern illegal — Sheet beschreibt Technik/Risiken, keinen Sendebetrieb.  
**Chip-Scope:** **Classic ESP32** (D0WD / WROOM / WROVER) mit **APLL**. ESP32-S2/S3/C3: **nicht** im Scope dieses Sheets (kein APLL-Äquivalent in den belegten Upstream-Projekten).

## Kurzfassung

Muster: UKW-FM-Träger aus der **Audio-PLL (APLL)** des klassischen ESP32, ausgegeben als **I2S-MCLK** über **CLK_OUT** auf einen GPIO; Modulation durch **Echtzeit-Updates** der APLL-Fractional-Register (`sdm0`/`sdm1`/`sdm2`, `o_div`) im Takt der Audio-Sample-Rate. Rechteckträger → **Harmonische**. Analog im Prinzip zu `rpi-gpio-fm-tx` (Clock/PLL statt GPIO-Bitbang), aber **anderer Chip-Contract**.

## Abgrenzung

- **Ist:** Classic-ESP32 APLL → I2S MCLK/CLK_OUT → GPIO als lab-only UKW-FM-Quellenpfad; Teiler-/Frac-FM.
- **Ist nicht:** ESP32-S3/S2/C3-FM (kein belegter APLL-Pfad — Gate nötig); Raspberry-Pi BCM-GPCLK (`rpi-gpio-fm-tx`); RDS-Protokoll allein (`fm-rds`); externe FM-Modulator-Chips; legale Sendestation.

## Signalpfad-Kette

| Stufe | Claim | Status | Evidence |
|-------|-------|--------|----------|
| XTAL (typ. 40 MHz) | Referenz für APLL | `FACT` | TRM / Upstream-Calc |
| APLL VCO 350–500 MHz | Lock-Fenster; `o_div`/`sdm*` | `FACT` | beide Upstreams + README |
| APLL → I2S MCLK ~87–125 MHz | Träger im UKW-nahen Bereich | `FACT` | Code + Docs (classic ESP32) |
| CLK_OUT1 ← I2S0 MCLK | Pin-Mux Routing | `FACT` | `fm_route_to_pin` |
| Physical GPIO | GPIO0 oder GPIO16 (projektabhängig) | `FACT` | Apps |
| Measured RF / Harmonics | Pegel, Spurious | `UNKNOWN` | kein Lab in dieser KB |
| ESP32-S3 gleicher Pfad | APLL-Äquivalent | `UNKNOWN` | Upstream `#error` ohne APLL |

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | PCM (oft 8 kHz, 8-bit mono embedded) | Sample-Takt = Modulations-ISR |
| unten | GPIO + APLL/MCLK Rechteck | Root/Firmware; Strapping-Pin-Risiko (GPIO0) |
| lateral | `esp_timer` / ISR | Frac-Nudges; IRAM_ATTR üblich |
| lateral | optional polar_mod (Filter/AGC/Modes) | Implementierungsvariante, gleicher RF-Contract |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| „ESP32 kann FM“ gilt für alle ESP32-Serien | `REJECTED` | Upstream: S2/S3/C3 ohne APLL → Compile-`#error` |
| ESP32-S3 erbt APLL-FM automatisch | `UNKNOWN` / Gate | eigenes E-0/E-1; kein Sheet-Ausweiten vor Evidence |
| Antenne am GPIO = harmlos | `REJECTED` | oft illegal; geschirmte Direktverbindung zum Messgerät |
| Spektrum ist „sauberes FM“ | `REJECTED` | Rechteck → ungerade Harmonische |
| Clock-Tree-Ausgang ist der einzige UKW-Kandidat auf S3 | `HYPOTHESIS` | zu absolut vor E-0; RMT/LEDC unter UKW plausibel ausgeschlossen (`INFERRED`) |
| GPIO0 immer ideal | `REJECTED` | Strapping/Boot; Alternativen (z. B. GPIO16) existieren |
| RDS = Text an den Sender | `REJECTED` | siehe `fm-rds` |
| Pi-DMA-Exit-Risiko existiert identisch am ESP | `UNKNOWN` | als Prüfpunkt übernehmen, nicht als Behauptung |

### Projektstart-Checkliste

- [ ] Chip = Classic ESP32 mit APLL? Sonst Stop / Gate
- [ ] Recht: kein Antennen-TX; Lab mit Dämpfung
- [ ] Pin: Strapping vs. alternativer CLK_OUT-Pin
- [ ] Hub ±75 kHz / Sample-Rate vs. Frac-Auflösung
- [ ] Harmonische / Filterbedarf einkalkulieren
- [ ] S3 oder Netzwerk-Knoten? → FOLLOW-ON + `hw-path-gate`, nicht dieses Sheet verbiegen
- [ ] Application + `seen_in`

## Transfer

- Kontrast zu `rpi-gpio-fm-tx`: gleiches *Muster* (PLL/Clock-FM), anderer Peripheral-Contract.
- Für Hub-Architekturen: ESP eher als **deterministischer Clock-/Modulations-Endpunkt** denkbar — aber nur nach Gate auf dem Zielchip.
- Kein Produkt-Infotainment-Sendepfad.

## Referenzen

- [Alexxdal/ESP32FMRadio](https://github.com/Alexxdal/ESP32FMRadio) · [hiperiondev/esp32_fm_radio](https://github.com/hiperiondev/esp32_fm_radio)
- Espressif ESP32 TRM / IDF APLL & I2S (classic)
- Hackaday.io Projekt 203719 (ESP32 FM transmitter using GPIO) — Desk-Hinweis

## Offene Fragen

- Welche max. Clock-Out-Frequenz erreicht ein **ESP32-S3**-Pad messbar? (E-0/E-1)
- Harmonic-Pegel / benötigte Filterdämpfung im Lab?
- Glitches beim SDM-Umschalten unter Last (WiFi gleichzeitig)?
