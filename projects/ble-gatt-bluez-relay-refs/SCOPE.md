# Project Scope: ble-gatt-bluez-relay-refs (Fremd)

```yaml
project_id: ble-gatt-bluez-relay-refs
title: BlueZ GATT Relay Delta (bluer two-adapter)
updated: 2026-11-12
profile_hint: lab-tool
reviewed_commit: "BluetoothInterceptor@4a10bcf bluez_peripheral@8174c15"
repos:
  - https://github.com/BrentWebEU/BluetoothInterceptor
  - https://github.com/spacecheese/bluez_peripheral
status: active
```

## Zweck

Desk-Delta: moderne **BlueZ/bluer** Two-Adapter GATT-Clone/Relay-Architektur (Rust) und Python Peripheral-Building-Block. Schließt die Lücke zwischen historischem btlejuice (noble/bleno) und heutigen BlueZ-D-Bus-APIs — **ohne** Attack-How-tos.

## Systeme und Grenzen

| Repo | Rolle im Audit | Im Scope? |
|------|----------------|-----------|
| BrentWebEU/BluetoothInterceptor @ `4a10bcf` | Rust+bluer; Central auf Adapter A, Peripheral-Clone auf Adapter B; Read/Write/Notify forward; EventBus | ja — **nur Architektur** |
| spacecheese/bluez_peripheral @ `8174c15` | Python BlueZ GATT Peripheral API (Advertisement, Service, Characteristic, Agent) | ja — Building Block, **kein** volles Relay |
| ianchi/ifit | bereits in `ble-gatt-bridge-refs` | **CROSSREF only** |
| btlejuice / ChimeraBLE | Kontrast Zwei-HCI vs on-chip | Querverweis Prior-Audit |

## Nicht-Ziele

- Attack-/MITM-Rezepte, Impersonation-Anleitungen, Unauthorized Access
- Neues Sheet `bluez-gatt-peripheral` (reuse `ble-gatt-transparent-bridge` / `ble-gatt-dual-role`)
- On-chip ESP Dual-Role Lab (bleibt Gate in Dual-Role-Sheet)
- BD_ADDR-Rewrite-Implementierung (→ Pack B / `bt-bdaddr-rewrite`)

## Prioritäten

1. Grow `ble-gatt-transparent-bridge` + `ble-gatt-dual-role` (Fallstrick BlueZ two-adapter ≠ on-chip)  
2. Optional Cross-Ref `ble-gatt-observe-proxy` (EventBus plaintext)  
3. Inventory: Interceptor = Relay; bluez_peripheral = Peripheral-API only  
