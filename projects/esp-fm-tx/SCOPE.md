# Project Scope: ESP FM Transmit (Fremdrepos)

```yaml
project_id: esp-fm-tx
title: ESP FM / APLL Clock Transmit (Fremd)
updated: 2026-10-11
profile_hint: lab-tool
reviewed_commit: "ESP32FMRadio@f62c72b esp32_fm_radio@870dc33"
reviewed_commit_note: Zwei Upstream-Repos; Desk-Audit ohne Feldaussendung
repos:
  - https://github.com/Alexxdal/ESP32FMRadio
  - https://github.com/hiperiondev/esp32_fm_radio
status: active
```

## Zweck

KB-Vertiefung: Classic-ESP32 **APLL/MCLK-FM** als eigenständige Tech neben Pi-GPIO-FM. Transfer-Fallen (S3 ohne APLL) und Lab-Gates festhalten — **kein** Sendebetrieb.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| Alexxdal/ESP32FMRadio | APLL+I2S-MCLK FM + WebUI | ja (Desk) |
| hiperiondev/esp32_fm_radio | gleiche Basis + polar_mod / Modes | ja (Desk) |
| ESP32-S3 FM-Pfad | Hypothese / Gate | angrenzend (FOLLOW-ON, kein Sheet) |
| Pi GPIO FM | Kontrast | angrenzend (`pi-fm-tx`) |
| Antennen-Feld-TX | — | **nein** |

## Nicht-Ziele

- Anleitung zu unlizenzierter Aussendung
- Vollständige FM-TX-Firmware für Hub vor E-0/E-1
- Behauptung „S3 kann UKW-FM“ ohne Messung

## Prioritäten

1. Sheet `esp32-apll-fm-tx` mit Chip-Scope Classic only  
2. Evidence auf zwei Upstreams (unabhängige Bestätigung)  
3. Abgrenzung zu `rpi-gpio-fm-tx` und S3-Gate  
4. Prozess-Rückfluss (0.6.6 Transfer-Gates)
