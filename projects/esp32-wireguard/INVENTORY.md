# Inventory — esp32-wireguard

```yaml
project_id: esp32-wireguard
updated: 2026-11-27
profile: firmware
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| esp-hub-base Ableiten / OTA / Web | `esp-hub-base-template` | wachsen |
| BaseModule + UiTab (D-022) | `esp-module-host` | wachsen |
| WireGuard-Client (trombik) | `esp-wireguard` | wachsen (Referenz-FW) |
| Hub Telemetrie / Firmware-Push | `esp-hub-telemetry` | observed |

Ursprung: [esp32.wireguard](https://github.com/MPunktBPunkt/esp32.wireguard).

## Übersicht

| Slug | Status | Sheet | Application |
|------|--------|-------|-------------|
| `esp-hub-base-template` | applied | [SHEET](../../technologies/esp-hub-base-template/SHEET.md) | [app](applications/esp-hub-base-template.md) |
| `esp-module-host` | applied | [SHEET](../../technologies/esp-module-host/SHEET.md) | [app](applications/esp-module-host.md) |
| `esp-wireguard` | applied | [SHEET](../../technologies/esp-wireguard/SHEET.md) | [app](applications/esp-wireguard.md) |
