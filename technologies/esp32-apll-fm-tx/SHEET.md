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
**Chip-Scope:** **Classic ESP32** (D0WD / WROOM / WROVER) mit **APLL** für die belegten FM-Upstreams. **ESP32-S2** hat laut IDF ebenfalls APLL (`SOC_CLK_APLL_SUPPORTED`) — aber **kein** belegter UKW-FM-Upstream in dieser KB (Gate). **ESP32-S3/C3/C5/…:** kein APLL im IDF-clk_tree → **nicht** im Scope; S3-Falsifikation siehe Fallstricke.

## Kurzfassung

Muster: UKW-FM-Träger aus der **Audio-PLL (APLL)** des klassischen ESP32, ausgegeben als **I2S-MCLK** über **CLK_OUT** auf einen GPIO; Modulation durch **Echtzeit-Updates** der APLL-Fractional-Register (`sdm0`/`sdm1`/`sdm2`, `o_div`) im Takt der Audio-Sample-Rate. Rechteckträger → **Harmonische**. Analog im Prinzip zu `rpi-gpio-fm-tx` (Clock/PLL statt GPIO-Bitbang), aber **anderer Chip-Contract**.

## Abgrenzung

- **Ist:** Classic-ESP32 APLL → I2S MCLK/CLK_OUT → GPIO als lab-only UKW-FM-Quellenpfad; Teiler-/Frac-FM.
- **Ist nicht:** ESP32-S3-FM über APLL (kein APLL — Gate/`esp32-polar-phy-tx` ist anderer Contract); S2-UKW ohne Gate; Raspberry-Pi BCM-GPCLK (`rpi-gpio-fm-tx`); RDS allein (`fm-rds`); externe FM-Chips (z. B. QN8027); AM-DAC-Pfad (bitluni); legale Sendestation.

## Signalpfad-Kette

| Stufe | Claim | Status | Evidence |
|-------|-------|--------|----------|
| XTAL (typ. 40 MHz) | Referenz für APLL | `FACT` | TRM / Upstream-Calc |
| APLL VCO 350–500 MHz | Lock-Fenster; `o_div`/`sdm*` | `FACT` | beide Upstreams + README |
| APLL → I2S MCLK ~87–125 MHz | Träger im UKW-nahen Bereich | `FACT` | Code + Docs (classic ESP32) |
| CLK_OUT1 ← I2S0 MCLK | Pin-Mux Routing | `FACT` | `fm_route_to_pin` |
| Physical GPIO | GPIO0 oder GPIO16 (projektabhängig) | `FACT` | Apps |
| Measured RF / Harmonics | Pegel, Spurious | `UNKNOWN` | kein Lab in dieser KB |
| ESP32-S3 gleicher Pfad | APLL-Äquivalent | `REJECTED` (APLL absent) | IDF S3 clk_tree / soc_caps; FM-Upstreams `#error` |
| ESP32-S2 APLL→CLK_OUT CW | APLL vorhanden | `FACT` (gist) | cibomahto; UKW-FM auf S2 = `UNKNOWN` |

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
| „ESP32 kann FM“ gilt für alle ESP32-Serien | `REJECTED` | Classic-FM-Upstreams: nur `CONFIG_IDF_TARGET_ESP32`; S3 ohne APLL |
| Alexxdal `#error`-Text „S2 hat kein APLL“ | `REJECTED` (überzogen) | IDF: S2 **hat** APLL; belegt CW-Pfad (cibomahto). UKW-FM auf S2 trotzdem Gate |
| ESP32-S3 erbt APLL-FM automatisch | `REJECTED` | IDF S3: keine `SOC_MOD_CLK_APLL`; Forum+soc_caps |
| LEDC als drop-in 32 MHz/UKW-Clock auf S3 | `INFERRED` | esp32.com: fractional LEDC → Jitter; nicht als FM-SoT |
| I2S teilt APLL-Ausgang oft ÷2 | `FACT` | cibomahto: Ziel×2 programmieren |
| Naive APLL-Search = genaue Audio-/Trägerfreq | `INFERRED` | IDF#2634 Historie; UKW-Frac weiter lab-`UNKNOWN` |
| Antenne am GPIO = harmlos | `REJECTED` | oft illegal; geschirmte Direktverbindung zum Messgerät |
| Spektrum ist „sauberes FM“ | `REJECTED` | Rechteck → ungerade Harmonische |
| Clock-Tree-Ausgang ist der einzige UKW-Kandidat auf S3 | `HYPOTHESIS` | zu absolut vor E-0; polar-PHY ist **anderes Band/Contract** |
| GPIO0 immer ideal | `REJECTED` | Strapping/Boot; Alternativen (z. B. GPIO16); benpeoples CW@GPIO0 |
| RDS = Text an den Sender | `REJECTED` | siehe `fm-rds`; PixelRadio = QN8027+RDS, nicht APLL |
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
- Espressif ESP32 TRM / IDF APLL & I2S (classic); IDF S3 clk_tree (kein APLL)
- [cibomahto APLL/CLK_OUT gist](https://gist.github.com/cibomahto/d427add5031fc1eb5bbb80274688bca0) (S2) · [benpeoples 38.4 MHz GPIO0](https://gist.github.com/benpeoples/8fde115cda0f7c8c334cc373d4234462)
- [cnlohr/esp32-apll-test](https://github.com/cnlohr/esp32-apll-test) · [esp-idf#2634](https://github.com/espressif/esp-idf/issues/2634)
- [esp32.com 32 MHz clock on S3](https://esp32.com/viewtopic.php?t=27214) — Forum/`INFERENCE` zu LEDC
- Kontrast: [`esp32-polar-phy-tx`](../esp32-polar-phy-tx/SHEET.md) · PixelRadio (QN8027) · bitluni AM-DAC

## Offene Fragen

- Welche max. Clock-Out-Frequenz erreicht ein **ESP32-S3**-Pad messbar? (E-0/E-1; LCD-PCLK-Kandidat aus Forum)
- Harmonic-Pegel / benötigte Filterdämpfung im Lab?
- Glitches beim SDM-Umschalten unter Last (WiFi gleichzeitig)?
- S2 APLL-FM (nicht nur CW) messbar?
