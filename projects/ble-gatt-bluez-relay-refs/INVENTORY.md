# Project Inventory: ble-gatt-bluez-relay-refs

```yaml
project_id: ble-gatt-bluez-relay-refs
updated: 2026-11-12
reviewed_commit: "BluetoothInterceptor@4a10bcf bluez_peripheral@8174c15"
profile: lab-tool
pilot_order: [ble-gatt-transparent-bridge, ble-gatt-dual-role]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Two-HCI Central+Peripheral Clone + byte forward | `ble-gatt-transparent-bridge` | **wachsen** (Fallstrick BlueZ/bluer) |
| Zwei Adapter ≠ Ein-Chip Dual-Role | `ble-gatt-dual-role` | **wachsen** (BluetoothInterceptor Evidence) |
| EventBus hex/JSON plaintext Read/Write/Notify | `ble-gatt-observe-proxy` | **optional Cross-Ref** |
| Python Advertisement/Service/Characteristic/Agent | — | Building Block observed; kein neues Sheet |
| ifit Interceptor | Prior `ble-gatt-bridge-refs` | **CROSSREF only** |

Kampagne: [ble-gatt-bluez-relay-2026-foreign](../../audits/ble-gatt-bluez-relay-2026-foreign/).

## Repo-Kurzinventar

| Repo @ commit | Roles | Bridge-Pattern | CCCD / Observability |
|---------------|-------|----------------|----------------------|
| BluetoothInterceptor `4a10bcf` | Dual **über 2 HCI** (`--target-adapter` Central, `--clone-adapter` Peripheral) | Transparent GATT clone + Read/Write/Notify forward | CCCD lokal BlueZ (`CharacteristicNotify`); `--clone-descriptors` default off; **EventBus** plaintext hex |
| bluez_peripheral `8174c15` | **Peripheral only** | kein Relay | Advertisement + Service + Characteristic + Agent API |

## Übersicht Sheets

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `ble-gatt-transparent-bridge` | Transparent GATT Bridge | C | applied | partial | [SHEET](../../technologies/ble-gatt-transparent-bridge/SHEET.md) | [app](applications/ble-gatt-transparent-bridge.md) |
| `ble-gatt-dual-role` | BLE GATT Dual-Role | C | applied | partial | [SHEET](../../technologies/ble-gatt-dual-role/SHEET.md) | [app](applications/ble-gatt-dual-role.md) |
| `ble-gatt-observe-proxy` | Observe Proxy | C | documented | partial | [SHEET](../../technologies/ble-gatt-observe-proxy/SHEET.md) | — (Prior: bt-analysis-relay-refs; EventBus Cross-Ref only) |
