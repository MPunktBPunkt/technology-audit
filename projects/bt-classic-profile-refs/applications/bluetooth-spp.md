# Project Application: bluetooth-spp in bt-classic-profile-refs

```yaml
project_id: bt-classic-profile-refs
tech_slug: bluetooth-spp
status: active
sheet: ../../../technologies/bluetooth-spp/SHEET.md
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
| BTClassicSPP: Server SCN0, SEC_NONE, single-client kick | `EVID-BTCL-2026-10-28-040` | `FACT` |
| EspBle: multi SPP server start_srv | `EVID-BTCL-2026-10-28-011` | `FACT` |
| IDF bt_spp_*: BR/EDR-only + SPP_ENABLED | `EVID-BTCL-2026-10-28-031` | `FACT` |
