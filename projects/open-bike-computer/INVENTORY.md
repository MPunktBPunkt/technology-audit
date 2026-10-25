# Project Inventory: open-bike-computer (Fremd)

```yaml
project_id: open-bike-computer
updated: 2026-10-25
reviewed_commit: "cd7ad00bb6c4f9566195cd44ab4d6a675518b94d"
profile: lab-tool
pilot_order: [ride-ble-display, bluetooth-ftms, ble-hrm-gatt]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Custom BLE ride/nav/workout display + ownership auth | `ride-ble-display` | **neu** + App |
| FTMS Trainer GATT | `bluetooth-ftms` | **Kontrast** |
| BLE HRM | `ble-hrm-gatt` | **Kontrast** |
| BLE RSSI proximity hunt | `ble-rssi-proximity` | **Kontrast** (Sibling) |
| AMOLED Waveshare profiles | — | observed (Board-HAL) |

Kampagne: [`open-bike-computer-2026-foreign`](../../audits/open-bike-computer-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `ride-ble-display` | Ride BLE Display (Custom GATT) | C | applied | partial | [SHEET](../../technologies/ride-ble-display/SHEET.md) | [app](applications/ride-ble-display.md) |
| `bluetooth-ftms` | Bluetooth FTMS | C | observed | none | [SHEET](../../technologies/bluetooth-ftms/SHEET.md) | — |
| `ble-hrm-gatt` | BLE HRM GATT | C | observed | none | [SHEET](../../technologies/ble-hrm-gatt/SHEET.md) | — |

## Signale ohne Eintrag

- Locked PlatformIO bootstrap / immutable runtime — Ops
- map-platform AGPL backend — out of desk-FW scope
