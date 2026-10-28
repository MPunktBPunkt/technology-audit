# Project Inventory: ble-gatt-bridge-refs

```yaml
project_id: ble-gatt-bridge-refs
updated: 2026-10-28
reviewed_commit: "multi-2026-10-28"
profile: lab-tool
pilot_order: [ble-gatt-dual-role, ble-gatt-transparent-bridge, ble-gatt-semantic-bridge]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Dual-Role Central+Peripheral Budget/Contention | `ble-gatt-dual-role` | **neu** |
| Byte-Passthrough GATT Clone/Relay + CCCD-Unabhängigkeit | `ble-gatt-transparent-bridge` | **neu** |
| Profil A→B Re-Encode (FTMS→CPS, Custom→FTMS, HID→HID) | `ble-gatt-semantic-bridge` | **neu** |
| HR Notify-Fanout | `ble-hr-relay` | **wachsen** (Cross-Ref) |
| FTMS + Control Point / Exclusive | `bluetooth-ftms` | **wachsen** (Cross-Ref) |
| GATT Central Probe | `ble-http-gatt-probe` | reused (Kontrast) |
| CPS Measurement Encode | `ble-cps-gatt` | **candidate** (kein Sheet) |
| Fixed UART `FFE0` Tunnel | — | observed only |

Kampagne: [ble-gatt-bridge-refs-2026-foreign](../../audits/ble-gatt-bridge-refs-2026-foreign/).

## Repo-Kurzinventar

| Repo @ commit | Roles | Bridge-Pattern | Profile | CCCD-Modell |
|---------------|-------|----------------|---------|-------------|
| ChimeraBLE `2330423` | Dual | Transparent clone + notify/write proxy | Opaque GATT + HID decode log | Source auto-sub; dest stack-CCCD; **keine Sync** |
| iFitnessProxy `1c24f58` | Dual | **Semantic** FTMS→CPS | FTMS→CPS | Bike sub once; Watch stack; keine Sync |
| ifit `d29ca88` | Dual (Host) | Semantic Custom→FTMS; CP indicate; Interceptor transparent custom | Custom 128-bit + FTMS | Interceptor: both sides; FTMS: poll≠CCCD-upstream |
| esp32-ble2mqtt `e66ec5a` | **Central only** | Transparent GATT↔MQTT | Beliebig (typed MQTT) | CCCD write queued; kein BLE Peripheral |
| BleRemoteBrideg `958da7c` | Dual | Semantic HID + CP (HOGP) | HID 0x1812 | Upstream native CCCD; dest subscribe events; Bond CCCD store |
| esp32-ble-uart-mx `3451904` | Dual + multi-peer | Transparent fixed `FFE0` UART | Custom FFE0 | BLE2902 + registerForNotify |
| btlejuice `981b2e3` | Dual **über 2 HCI** | Transparent full GATT relay/clone | Beliebig | Fake subscribe → proxy notify enable |

## Übersicht Sheets

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `ble-gatt-dual-role` | BLE GATT Dual-Role | C | applied | partial | [SHEET](../../technologies/ble-gatt-dual-role/SHEET.md) | [app](applications/ble-gatt-dual-role.md) |
| `ble-gatt-transparent-bridge` | Transparent GATT Bridge | C | applied | partial | [SHEET](../../technologies/ble-gatt-transparent-bridge/SHEET.md) | [app](applications/ble-gatt-transparent-bridge.md) |
| `ble-gatt-semantic-bridge` | Semantic GATT Bridge | C | applied | partial | [SHEET](../../technologies/ble-gatt-semantic-bridge/SHEET.md) | [app](applications/ble-gatt-semantic-bridge.md) |
| `ble-hr-relay` | BLE HR-Relay | C | documented | partial | [SHEET](../../technologies/ble-hr-relay/SHEET.md) | — (siehe heartrate/ergo) |
| `bluetooth-ftms` | Bluetooth FTMS | C | documented | partial | [SHEET](../../technologies/bluetooth-ftms/SHEET.md) | — (siehe ergo/ftmsprobe) |
| `ble-cps-gatt` | BLE CPS | C | candidate | none | — | — |
