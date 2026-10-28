# Project Application: ble-gatt-transparent-bridge in ble-gatt-bridge-refs

```yaml
project_id: ble-gatt-bridge-refs
tech_slug: ble-gatt-transparent-bridge
status: active
sheet: ../../../technologies/ble-gatt-transparent-bridge/SHEET.md
audit: ../../../audits/ble-gatt-bridge-refs-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Byte-Passthrough / GATT-Clone und Central-Gateway-Kontrast. Offensive Nutzung nur inventarisiert.

## Evidenz (Desk)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Chimera: wireRelays Source-sub; Host onSubscribe log-only | `EVID-BLEBR-2026-10-28-002` | `FACT` |
| Chimera: notify/write passthrough | `EVID-BLEBR-2026-10-28-003` | `FACT` |
| ble2mqtt: CCCD register + queued write; GATTS off | `EVID-BLEBR-2026-10-28-031` | `FACT` |
| uart-mx: festes FFE0 transparent | `EVID-BLEBR-2026-10-28-051` | `FACT` |
| btlejuice: setGattHandlers + FakeDevice keepHandles | `EVID-BLEBR-2026-10-28-061` | `FACT` |
