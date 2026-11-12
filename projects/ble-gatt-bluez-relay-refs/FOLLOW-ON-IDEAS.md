# Follow-on ideas (aus ble-gatt-bluez-relay-refs)

```yaml
reuse_outcomes:
  reused: [ble-gatt-transparent-bridge, ble-gatt-dual-role, ble-gatt-observe-proxy]
  new: []
  not_helped: ["bluez_peripheral als volles BLE↔BLE-Relay — nur Peripheral-API"]
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Lab: ein vs. zwei HCI unter bluer Concurrent Central+Peripheral | Dual-Role + DESIGN open Q | Controller-Capability messen |
| Analyse-Sink: EventBus-Schema → KB JSONL Capture | observe-proxy | Minimales Capture-Schema |
| Peripheral-only Lab mit bluez_peripheral + eigener Central | bluez_peripheral | Building Block ohne Relay-Overhead |
| BD_ADDR Clone auf Clone-Adapter | `bt-bdaddr-rewrite` (Pack B) | DESIGN out-of-scope; separates Sheet |
| ESP Dual-Role Budget unverändert Gate | Dual-Role Sheet | Two-HCI Patterns nicht 1:1 portieren |
