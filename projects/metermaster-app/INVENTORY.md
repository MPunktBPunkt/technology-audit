# Project Inventory: MeterMaster-App

```yaml
project_id: metermaster-app
updated: 2026-10-09
reviewed_commit: 80e3fe0
profile: ops-field
pilot_order: [metermaster-android-app, iobroker-metermaster-adapter]
```

**Reuse / Match:**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Local-first Zähler-App + HTTP zum Adapter | `metermaster-android-app` | **neu** |
| Adapter :8089 | `iobroker-metermaster-adapter` | Application-Verweis (existiert) |
| ESP OLED | `ssd1306-oled-ui` / esp32-metermaster | Querverweis |
| Landing MeterMaster (Privacy) | — | observed Ops, kein Sheet |

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `metermaster-android-app` | MeterMaster Android | G | `mobile` | applied | partial | [SHEET](../../technologies/metermaster-android-app/SHEET.md) | [app](applications/metermaster-android-app.md) |
| `iobroker-metermaster-adapter` | MeterMaster Adapter | F | `iobroker` | documented | partial | [SHEET](../../technologies/iobroker-metermaster-adapter/SHEET.md) | [Adapter](../iobroker-metermaster/applications/iobroker-metermaster-adapter.md) |
