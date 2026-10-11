# Project Inventory: ESP FM Transmit (Fremd)

```yaml
project_id: esp-fm-tx
updated: 2026-10-11
reviewed_commit: "ESP32FMRadio@f62c72b esp32_fm_radio@870dc33"
profile: lab-tool
pilot_order: [esp32-apll-fm-tx]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| APLL + I2S MCLK + CLK_OUT FM (classic ESP32) | `esp32-apll-fm-tx` | **neu** (nicht `rpi-gpio-fm-tx` aufblasen) |
| polar_mod / Multi-Mode um denselben RF-Pfad | `esp32-apll-fm-tx` | gleicher Slug; Tiefe in Application |
| Compile-Guard ohne APLL (S2/S3/C3) | `esp32-apll-fm-tx` | Fallstrick A + Gate |
| Pi BCM-GPCLK FM | `rpi-gpio-fm-tx` | **Abgrenzung** |
| RDS-Protokoll | `fm-rds` | Abgrenzung (hier nicht implementiert) |
| ESP32-S3 Clock-Out UKW | — | FOLLOW-ON / `hw-path-gate` — kein Sheet |
| APLL calc / I2S÷2 / GPIO0 CW (Gists, cnlohr, IDF#2634) | `esp32-apll-fm-tx` | **Evidence** Fallstricke (2026-10-11 Nachzug) |
| S3 kein APLL + LEDC-Jitter (Forum) | `esp32-apll-fm-tx` | Falsifikation APLL; LEDC=`INFERENCE` |
| PixelRadio QN8027+RDS | `fm-rds` | Kontrast (externer Chip) — kein Bootstrap |
| bitluni AM+DAC | — | Kontrast Baseband — kein Sheet |
| S3 polar PHY TX / Undoc I/Q | `esp32-polar-phy-tx` / `esp32-undoc-iq-rx` | **Abgrenzung** (eigene Projekte) |

Kampagne: [`esp-fm-tx-2026-foreign`](../../audits/esp-fm-tx-2026-foreign/).  
Kontrast Pi-TX: [`pi-fm-tx`](../pi-fm-tx/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp32-apll-fm-tx` | ESP32 APLL/MCLK FM TX | D | `radio-tx`, `lab-only`, `esp-idf` | applied | partial | [SHEET](../../technologies/esp32-apll-fm-tx/SHEET.md) | [app](applications/esp32-apll-fm-tx.md) |
| `rpi-gpio-fm-tx` | RPi GPIO/Clock FM TX | D | `radio-tx` | documented | none | [SHEET](../../technologies/rpi-gpio-fm-tx/SHEET.md) | — (Kontrast) |
| `fm-rds` | FM-RDS | C | `radio-tx` | documented | none | [SHEET](../../technologies/fm-rds/SHEET.md) | — |
| `esp-idf-apll` | APLL Register/API | D | `esp-idf` | observed | none | — | — |
| `esp-embedded-web-sse` | SoftAP WebUI (Alexxdal) | D | `esp-idf` | observed | none | — | — |

## Nach Kategorie

### D — Embedded

`esp32-apll-fm-tx` (+ observed APLL/WebUI)

### C — Protokolle

`fm-rds` (nur Abgrenzung)

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| ESP32-S3 Clock-Out @ UKW | kein APLL; ungemessen | E-0/E-1 (`hw-path-gate`) |
| Harmonic-/Filter-Messung | kein Lab | optional Method + Lab |
| WiFi+TX gleichzeitig (Alexxdal SoftAP) | Desk nur Code | Lab-Jitter |

## Signale ohne Eintrag

- dg6rs/polar (SSB/CW-Quelle für polar_mod) — Upstream-Credit, nicht separat inventarisiert
- Hackaday-Writeup zu ESP32FMRadio — Desk-Nebenquelle
