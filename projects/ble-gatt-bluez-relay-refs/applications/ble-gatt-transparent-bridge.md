# Project Application: ble-gatt-transparent-bridge in ble-gatt-bluez-relay-refs

```yaml
project_id: ble-gatt-bluez-relay-refs
tech_slug: ble-gatt-transparent-bridge
status: active
sheet: ../../../technologies/ble-gatt-transparent-bridge/SHEET.md
audit: ../../../audits/ble-gatt-bluez-relay-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

BlueZ/bluer **byte-transparent** GATT-Clone: Target-Services spiegeln, Read/Write/Notify forwarden. Offensive Nutzung nur inventarisiert (kein How-to).

## Evidenz (Desk)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `connect_target` Central; `build_clone` Peripheral auf zweitem Adapter | `EVID-BZGATT-2026-11-12-001` | `FACT` |
| CharacteristicRead/Write/Notify Fun → remote forward | `EVID-BZGATT-2026-11-12-002` | `FACT` |
| CCCD lokal BlueZ; `--clone-descriptors` default off | `EVID-BZGATT-2026-11-12-003` | `FACT` |
| GAP/GATT 0x1800/0x1801 skip (Stack reserved) | `EVID-BZGATT-2026-11-12-004` | `FACT` |
| bluez_peripheral = Peripheral API, kein Relay | `EVID-BZGATT-2026-11-12-010` | `FACT` |

**Prior CROSSREF:** btlejuice two-HCI transparent (`EVID-BLEBR-2026-10-28-060/061`); ifit Interceptor (`EVID-BLEBR-2026-10-28-023`) — nicht neu auditiert.
