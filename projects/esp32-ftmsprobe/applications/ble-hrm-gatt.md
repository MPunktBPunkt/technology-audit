# Project Application: ble-hrm-gatt in esp32.ftmsprobe

```yaml
project_id: esp32-ftmsprobe
tech_slug: ble-hrm-gatt
status: active
sheet: ../../../technologies/ble-hrm-gatt/SHEET.md
audit: ../../../audits/esp32-ftmsprobe-2026-pilot/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R3
  reusability: W3
```

## Rolle im Projekt

Dual-Scan/Connect: Bike + Polar H9 parallel (`dual`), Verbindungsbudget wie Produkt (§14 / `MAX_CONNECTIONS=3`).

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| H9 im Labor parallel zum Bike sichtbar/koppelbar | `EVID-HRM-2026-10-09-002` | `MEASURED` |

## Verwandte

- Sheet-Varianten Direct vs Relay (Relay hier nicht gebaut)
