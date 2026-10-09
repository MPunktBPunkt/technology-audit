# Project Inventory: esp32.io-control

```yaml
project_id: esp32-io-control
updated: 2026-10-09
reviewed_commit: c79dd3a
profile: firmware
pilot_order: [esp-lab-bus-tools, esp-embedded-web-sse, esp-hub-telemetry]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.2](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| GPIO/I2C/SPI/PWM Lab-UI | `esp-lab-bus-tools` | **neu** (Geschwister toolnode-Module) |
| SSE `/api/events` | `esp-embedded-web-sse` | wachsen |
| Hub Heartbeat ohne fwType | `esp-hub-telemetry` | wachsen |
| Pin-Schutz BOOT/USB/UART | `unter Lab-Tools` | Application |

Ursprung: [esp32.io-control](https://github.com/MPunktBPunkt/esp32.io-control).  
Kampagne: [esp32-io-control-2026-pilot](../../audits/esp32-io-control-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp-lab-bus-tools` | ESP Lab Bus / GPIO | H | `lab-only` | applied | partial | [SHEET](../../technologies/esp-lab-bus-tools/SHEET.md) | [app](applications/esp-lab-bus-tools.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | applied | partial | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | [app](applications/esp-embedded-web-sse.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Feldserie | Desk-Audit | Evidence nachziehen |

## Signale ohne Eintrag

- WiFiManager / NVS — observed-Familie
