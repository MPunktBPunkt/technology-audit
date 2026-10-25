# Project Inventory: esp-ble-finder (Fremd)

```yaml
project_id: esp-ble-finder
updated: 2026-10-25
reviewed_commit: "1a588119bb8d21a5aa939b6e0601585bcf448431"
profile: lab-tool
pilot_order: [ble-rssi-proximity, rf-environment-monitor]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| BLE Adv RSSI proximity hunt + bands/clicker | `ble-rssi-proximity` | **neu** + App |
| RF Environment Score / periodic scan | `rf-environment-monitor` | **Kontrast** |
| Ride BLE Display Custom GATT | `ride-ble-display` | **Kontrast** |
| Waveshare AMOLED 1.8 BSP | — | observed |

Kampagne: [`esp-ble-finder-2026-foreign`](../../audits/esp-ble-finder-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `ble-rssi-proximity` | BLE RSSI Proximity Hunt | H | applied | partial | [SHEET](../../technologies/ble-rssi-proximity/SHEET.md) | [app](applications/ble-rssi-proximity.md) |
| `rf-environment-monitor` | RF Environment Monitor | H | observed | none | [SHEET](../../technologies/rf-environment-monitor/SHEET.md) | — |

## Signale ohne Eintrag

- TCA9554 V2 panel reset — Board-HAL
