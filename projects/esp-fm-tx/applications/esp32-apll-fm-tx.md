# Project Application: esp32-apll-fm-tx in esp-fm-tx

```yaml
project_id: esp-fm-tx
tech_slug: esp32-apll-fm-tx
status: active
sheet: ../../../technologies/esp32-apll-fm-tx/SHEET.md
audit: ../../../audits/esp-fm-tx-2026-foreign/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R0
  reusability: W2
```

## Rolle

Zwei unabhängige Fremdrepos, **ein** RF-Contract: Classic-ESP32 APLL → I2S MCLK → CLK_OUT → GPIO, FM über Fractional-Updates.

| Repo | Commit | Rolle |
|------|--------|-------|
| [Alexxdal/ESP32FMRadio](https://github.com/Alexxdal/ESP32FMRadio) | `f62c72b` | Referenz: `fm_tx.c`, WebUI/SoftAP, WAV/MP3-Pfad |
| [hiperiondev/esp32_fm_radio](https://github.com/hiperiondev/esp32_fm_radio) | `870dc33` | Ableitung + `polar_mod` (Filter/AGC/FMW…); Credit an Alexxdal |

Beide: `#error` wenn nicht `CONFIG_IDF_TARGET_ESP32` (kein S2/S3/C3).

## Architektur / Datenfluss

```text
PCM (8 kHz) → esp_timer ISR → APLL sdm*/o_div Nudge
                                    ↓
                         APLL → I2S MCLK (~100 MHz)
                                    ↓
                         CLK_OUT1 → GPIO → Rechteck-RF
```

## Relevante Pfade

| Repo / Pfad | Rolle |
|-------------|-------|
| `ESP32FMRadio/main/fm_tx.c` | APLL calc, I2S `use_apll`+`fixed_mclk`, route GPIO16, timer FM |
| `ESP32FMRadio/include/fm_tx.h` | `fm_apll_cfg_t` |
| `ESP32FMRadio/platformio.ini` | `board = esp32dev`, ESP-IDF |
| `ESP32FMRadio/main/main.c` | SoftAP + HTTP WebUI um FM |
| `esp32_fm_radio/components/esp32_tx/esp32_tx.c` | APLL/I2S STD, route GPIO0, `clk_ll_apll_set_config` |
| `esp32_fm_radio/components/esp32_tx/polar_mod.c` | Filter/AGC/Hilbert/CORDIC; `MOD_FMW` ±75 kHz-Skalierung |
| `esp32_fm_radio/main/main.c` | Default Carrier 108 MHz, `MOD_FMW` |

## Konfiguration (Desk)

| Parameter | Alexxdal | hiperiondev |
|-----------|----------|-------------|
| Carrier | 100 MHz (`FM_CARRIER_HZ`) | 108 MHz in `main.c` (API bis ~125 MHz) |
| Deviation | ±75 kHz | ±75 kHz (`MAX_DEV_HZ`) |
| Sample rate | 8 kHz | 8 kHz |
| RF GPIO | **GPIO16** (Code; README historisch GPIO0) | **GPIO0** |
| I2S API | legacy `driver/i2s.h` + `fixed_mclk` | `driver/i2s_std.h` + `I2S_CLK_SRC_APLL` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Compile nur Classic ESP32 (APLL) | `EVID-ESPAPLL-2026-10-11-001` | `FACT` |
| APLL-Koeffizienten + `rtc_clk_apll_*` / `clk_ll_apll_set_config` | `EVID-ESPAPLL-2026-10-11-002` | `FACT` |
| I2S MCLK als Trägerquelle | `EVID-ESPAPLL-2026-10-11-003` | `FACT` |
| CLK_OUT1 ← I2S0 MCLK auf GPIO | `EVID-ESPAPLL-2026-10-11-004` | `FACT` |
| FM via Frac-Update im 8 kHz-Timer | `EVID-ESPAPLL-2026-10-11-005` | `FACT` |
| hiperiondev baut auf Alexxdal (+ polar) | `EVID-ESPAPLL-2026-10-11-006` | `FACT` |
| Rechteck-Harmonische / Legal-Warnung in Docs | `EVID-ESPAPLL-2026-10-11-007` | `FACT` |
| Harmonic-Pegel gemessen | — | `UNKNOWN` |
| ESP32-S3 gleicher Mechanismus | — | `UNKNOWN` |

## Abweichungen vom „Lehrbuch“

- I2S wird nicht für Audio-Payload zum RF genutzt, sondern als **Clock-Engine**.
- Alexxdal-README beschreibt GPIO0; aktueller Code routet **GPIO16**.
- hiperiondev: reichhaltige Baseband-Pipeline (`polar_mod`), RF-Ende bleibt APLL-Nudge.

## Offene Fragen

- S3: E-0/E-1 laut FOLLOW-ON
- SoftAP+TX gleichzeitig: Jitter?
- Ob `fixed_mclk=100e6` in allen IDF-Versionen gleich greift

## Verwandte Applications / Methods

- Kontrast: [`pi-fm-tx` / rpi-gpio-fm-tx](../../pi-fm-tx/applications/rpi-gpio-fm-tx.md)
- Methods: [`hw-path-gate`](../../../methods/hw-path-gate.md), [`kb-cross-check`](../../../methods/kb-cross-check.md)
