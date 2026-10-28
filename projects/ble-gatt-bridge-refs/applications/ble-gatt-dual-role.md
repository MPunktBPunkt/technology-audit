# Project Application: ble-gatt-dual-role in ble-gatt-bridge-refs

```yaml
project_id: ble-gatt-bridge-refs
tech_slug: ble-gatt-dual-role
status: active
sheet: ../../../technologies/ble-gatt-dual-role/SHEET.md
audit: ../../../audits/ble-gatt-bridge-refs-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Querschnitt: welche Fremdrepos Dual-Role **auf einem Chip** vs. Zwei-HCI realisieren; welche Budgets/Flags sichtbar sind.

## Evidenz (Desk)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Chimera Dual MITM + MAX_CONNECTIONS=3 Hinweis | `EVID-BLEBR-2026-10-28-001` | `FACT` |
| iFitnessProxy Dual FTMS Central + CPS Peripheral, MAX_CONN=2 | `EVID-BLEBR-2026-10-28-010` | `FACT` |
| BleRemoteBrideg Dual + explizite FSM | `EVID-BLEBR-2026-10-28-040` | `FACT` |
| uart-mx Dual + multi-peer | `EVID-BLEBR-2026-10-28-050` | `FACT` |
| ble2mqtt **kein** Dual-Role Peripheral | `EVID-BLEBR-2026-10-28-030` | `FACT` |
| btlejuice Dual über 2 Prozesse/HCI | `EVID-BLEBR-2026-10-28-060` | `FACT` |
