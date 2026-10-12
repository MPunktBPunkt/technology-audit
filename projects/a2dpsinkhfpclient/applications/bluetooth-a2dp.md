# Project Application: bluetooth-a2dp in a2dpsinkhfpclient

```yaml
project_id: a2dpsinkhfpclient
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/a2dpsinkhfpclient-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

A2DP **Sink** mit I2S-TX zu externem DAC; parallel HFP für Calls (I2S-RX Mic). IDF-Component Registry `walinsky/a2dpsinkhfpclient`.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/a2dpSink.c` / `a2dpSinkHfpHf.c` | Sink + orchestration |
| `include/a2dpSinkHfpHf.h` | Public config/API |
| `examples/minimal*` | Bring-up |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| A2DP Sink + I2S pins in config | `EVID-HFPCLI-A2DP-2026-10-12-001` | `FACT` |
| IDF component v5.5+ badge | `EVID-HFPCLI-A2DP-2026-10-12-002` | `FACT` |
