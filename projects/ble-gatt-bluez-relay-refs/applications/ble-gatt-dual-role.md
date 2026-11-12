# Project Application: ble-gatt-dual-role in ble-gatt-bluez-relay-refs

```yaml
project_id: ble-gatt-bluez-relay-refs
tech_slug: ble-gatt-dual-role
status: active
sheet: ../../../technologies/ble-gatt-dual-role/SHEET.md
audit: ../../../audits/ble-gatt-bluez-relay-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Verstärkt: **BlueZ zwei HCI ≠ on-chip Dual-Role**. BluetoothInterceptor dokumentiert explizit, dass Concurrent Central+Peripheral auf einem Controller **nicht** garantiert ist und warnt bei gleichem Adapter.

## Evidenz (Desk)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Zwei Adapter empfohlen; Warnung wenn `--target-adapter` == `--clone-adapter` | `EVID-BZGATT-2026-11-12-005` | `FACT` |
| bluer liefert beide Rollen; Single-Adapter Concurrent = controller-dependent / unreliable | `EVID-BZGATT-2026-11-12-006` | `FACT` (DESIGN) |
| Zwei-HCI-Proxy ≠ Ein-Chip-Dual-Role Budget/Failure Modes | `EVID-BZGATT-2026-11-12-005` + Prior `…-060` | `REJECTED` Gleichsetzung |

**Prior CROSSREF:** btlejuice 2-Prozess/HCI (`EVID-BLEBR-2026-10-28-060`); Sheet-Fallstrick bereits `REJECTED`.
