# Project Inventory: ESP32.esp-hub

```yaml
project_id: esp32-esp-hub
updated: 2026-10-28
reviewed_commit: eebbcd9
profile: firmware
pilot_order: [esp-hub-base-template, esp-hub-telemetry, esp-embedded-web-sse]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| AppCore + Ableiten-Zonen + Derived A/B | `esp-hub-base-template` | **wachsen** |
| Heartbeat schlank + PSRAM/CPU-Additive; Reply `name` | `esp-hub-telemetry` | **wachsen** |
| Status-UI + SSE + gzip-PROGMEM Pack | `esp-embedded-web-sse` | **wachsen** |
| WiFiManager Portal | `wifi-manager-captive` | observed |

Ursprung: [ESP32.esp-hub](https://github.com/MPunktBPunkt/ESP32.esp-hub) @ `eebbcd9`.  
Kampagne: [esp32-esp-hub-2026-1.10-validation](../../audits/esp32-esp-hub-2026-1.10-validation/) · Prior: [esp32-esp-hub-2026-pilot](../../audits/esp32-esp-hub-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp-hub-base-template` | Hub Base Template | J | `arduino` | applied | partial | [SHEET](../../technologies/esp-hub-base-template/SHEET.md) | [app](applications/esp-hub-base-template.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `iobroker` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | applied | partial | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | [app](applications/esp-embedded-web-sse.md) |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |
