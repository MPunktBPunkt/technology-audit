# Project Inventory: esp32.MeterMaster

```yaml
project_id: esp32-metermaster
updated: 2026-10-09
reviewed_commit: 60fa14b
profile: firmware
pilot_order: [iobroker-simple-api, esp-hub-telemetry, ssd1306-oled-ui]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| `getPlainValue` Port 8087 | `iobroker-simple-api` | **neu** |
| ESP-Hub Heartbeat Port 8093 `fwType` MeterMaster | `esp-hub-telemetry` | wachsen |
| SSD1306 64×48 OLED UI | `ssd1306-oled-ui` | **neu** |
| MeterMaster-Adapter :8089 register/config/cmd | `metermaster-adapter-http` | observed (produktspezifisch) |
| Eingebettete Web-UI (ohne SSE) | `embedded-web-ui` | observed — **nicht** `esp-embedded-web-sse` |
| WiFiManager | `wifi-manager-captive` | observed |
| Arduino `.ino` Monolith | Layout-Hinweis REUSE | — |

Ursprung: [esp32.MeterMaster](https://github.com/MPunktBPunkt/esp32.MeterMaster).  
Kampagne: [esp32-metermaster-2026-pilot](../../audits/esp32-metermaster-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `iobroker-simple-api` | ioBroker Simple-API | F | — | applied | partial | [SHEET](../../technologies/iobroker-simple-api/SHEET.md) | [app](applications/iobroker-simple-api.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `ssd1306-oled-ui` | SSD1306 OLED UI | G | — | applied | partial | [SHEET](../../technologies/ssd1306-oled-ui/SHEET.md) | [app](applications/ssd1306-oled-ui.md) |
| `metermaster-adapter-http` | MeterMaster Adapter HTTP | F | — | observed | none | — | — |
| `embedded-web-ui` | Embedded Web (poll) | G | — | observed | none | — | — |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Adapter :8089 Contract | observed | Sheet wenn zweites Produkt-Adapter-Muster |
| OLED Feld-Lesbarkeit | Desk only | Foto/Evidence Feld |

## Signale ohne Eintrag

- OTA GitHub-Dropdown — Application B Hub/Web
- Alarm LED + Schwellwert — OLED-Application
