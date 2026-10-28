# Project Application: bt-dual-mode-coex in bt-classic-profile-refs

```yaml
project_id: bt-classic-profile-refs
tech_slug: bt-dual-mode-coex
status: active
sheet: ../../../technologies/bt-dual-mode-coex/SHEET.md
audit: ../../../audits/bt-classic-gaps-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| a2dpSink: Classic-only + BLE mem_release | `EVID-BTCL-2026-10-28-003` | `FACT` |
| EspBle: BTDM Dual-Host HCI broker, ESP32-only Classic | `EVID-BTCL-2026-10-28-013` | `FACT` |
| bthidbridge: BTDM mode for HID bridge | `EVID-BTCL-2026-10-28-060` | `FACT` |
| IDF classic examples default BR/EDR-only | `EVID-BTCL-2026-10-28-033` | `FACT` |
