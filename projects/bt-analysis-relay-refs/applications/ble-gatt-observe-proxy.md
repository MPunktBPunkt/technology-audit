# Project Application: ble-gatt-observe-proxy in bt-analysis-relay-refs

```yaml
project_id: bt-analysis-relay-refs
tech_slug: ble-gatt-observe-proxy
status: active
sheet: ../../../technologies/ble-gatt-observe-proxy/SHEET.md
audit: ../../../audits/bt-analysis-relay-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Chimera: Dual-Role relayNotify + UART hex log | `EVID-BTAR-2026-10-28-001` | `FACT` |
| Chimera: CCCD Host onSubscribe log-only (Source≠Dest) | `EVID-BTAR-2026-10-28-002` | `FACT` |
| ble2mqtt: GATT→MQTT publish Analyse-Sink (Central-only) | `EVID-BTAR-2026-10-28-010` | `FACT` |
| uart-mx: Dual-Role Custom GATT serial observability | `EVID-BTAR-2026-10-28-020` | `FACT` |
