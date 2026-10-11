# Evidence — esp-fm-tx-2026-foreign

Desk 2026-10-11 · **standard_version 0.6.6** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/Alexxdal/ESP32FMRadio | `f62c72b` |
| https://github.com/hiperiondev/esp32_fm_radio | `870dc33` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-ESPAPLL-2026-10-11-001` | Nur Classic ESP32: `#error` ohne APLL (S2/S3/C3) | `FACT` | `ESP32FMRadio/main/fm_tx.c` L40–43; `esp32_fm_radio/.../esp32_tx.c` L56–58 |
| `EVID-ESPAPLL-2026-10-11-002` | APLL enable + coeff (`rtc_clk_apll_*`) und Live-Update `clk_ll_apll_set_config` | `FACT` | beide `fm_*` / `esp32_tx.c` |
| `EVID-ESPAPLL-2026-10-11-003` | I2S mit APLL als Clock; Alexxdal `use_apll`+`fixed_mclk=100e6`; hiperion `I2S_CLK_SRC_APLL` | `FACT` | `fm_i2s_init` beider Repos |
| `EVID-ESPAPLL-2026-10-11-004` | CLK_OUT1 ← I2S0 MCLK (`PIN_CTRL` / `PIN_FUNC_SELECT`); GPIO16 (Alexxdal) bzw. GPIO0 (hiperion) | `FACT` | `fm_route_to_pin` |
| `EVID-ESPAPLL-2026-10-11-005` | `esp_timer` @ 8 kHz skaliert Audio → Frac-Deviation (FM) | `FACT` | `fm_timer_cb` / `fm_start_audio` |
| `EVID-ESPAPLL-2026-10-11-006` | hiperiondev basiert auf Alexxdal + dg6rs/polar | `FACT` | `esp32_tx.c` Header-Credits; README |
| `EVID-ESPAPLL-2026-10-11-007` | Docs: Rechteck-Harmonische, kurze Antenne, Legal/low-power Warnung | `FACT` | beide READMEs |
| `EVID-ESPAPLL-2026-10-11-008` | VCO-Fenster 350–500 MHz / o_div-Suche in Calc | `FACT` | `fm_calc_apll` beider Repos |
| `EVID-ESPAPLL-2026-10-11-009` | hiperion: Carrier-Range-Check bis 125 MHz; Default 108 MHz | `FACT` | `fm_apll_init` + `main.c` |
| `EVID-ESPAPLL-2026-10-11-010` | Alexxdal PlatformIO `board = esp32dev` (classic) | `FACT` | `platformio.ini` |
| `EVID-MATCH-2026-10-11-001` | Vor Audit kein ESP-APLL-FM-Sheet; Pi-TX ≠ ESP-TX | `FACT` | technologies Index vor Import |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Harmonic-Pegel gemessen | `UNKNOWN` | kein Lab |
| ESP32-S3 Clock-Out ≥90 MHz auf Pad | `UNKNOWN` | Gate E-0/E-1 |
| SoftAP+TX Jitter (Alexxdal) | `UNKNOWN` | Code vorhanden, ungemessen |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-11 | KB-Cross-Check (Prompt gegen Audit) → Prozess 0.6.6 |
| 2026-10-11 | Desk-Audit zwei Upstreams; Sheet `esp32-apll-fm-tx` |
