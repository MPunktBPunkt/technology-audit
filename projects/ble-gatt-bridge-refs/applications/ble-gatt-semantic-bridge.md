# Project Application: ble-gatt-semantic-bridge in ble-gatt-bridge-refs

```yaml
project_id: ble-gatt-bridge-refs
tech_slug: ble-gatt-semantic-bridge
status: active
sheet: ../../../technologies/ble-gatt-semantic-bridge/SHEET.md
audit: ../../../audits/ble-gatt-bridge-refs-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Profil A→B Mapping inkl. Control-Point und Exclusive-Muster.

## Evidenz (Desk)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| iFitnessProxy FTMS→CPS re-encode | `EVID-BLEBR-2026-10-28-011` | `FACT` |
| ifit Custom→FTMS + CP opcodes/indicate | `EVID-BLEBR-2026-10-28-021` | `FACT` |
| ifit FTMS poll-notify loop (kein Upstream-Notify-Zwang) | `EVID-BLEBR-2026-10-28-022` | `FACT` |
| BleRemoteBrideg HID semantic + HOGP CP | `EVID-BLEBR-2026-10-28-041` | `FACT` |
