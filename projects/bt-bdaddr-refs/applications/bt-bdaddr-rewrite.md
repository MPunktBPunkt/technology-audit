# Project Application: bt-bdaddr-rewrite in bt-bdaddr-refs

```yaml
project_id: bt-bdaddr-refs
tech_slug: bt-bdaddr-rewrite
status: active
sheet: ../../../technologies/bt-bdaddr-rewrite/SHEET.md
audit: ../../../audits/bt-bdaddr-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Evidenz (Desk)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Vendor-spezifische Write-BD_ADDR (Ericsson/CSR/TI/BCM/Intel/Cypress/…) | `EVID-BDADDR-2026-11-12-001` | `FACT` |
| Kein Espressif in `vendor[]` | `EVID-BDADDR-2026-11-12-002` | `FACT` |
| ESP nutzt IDF MAC/Controller APIs statt `bdaddr` | `EVID-BDADDR-2026-11-12-003` | `FACT` (Abgrenzung) |
| Link-Key Invalidierung bei Address Change | `EVID-BDADDR-2026-11-12-004` | `INFERENCE` |
| HU/Peer-Reaktion auf Address Change | `EVID-BDADDR-2026-11-12-005` | `UNKNOWN` |
