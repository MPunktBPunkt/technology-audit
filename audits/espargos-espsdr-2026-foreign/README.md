# Audit Campaign: espargos-espsdr-2026-foreign

```yaml
id: espargos-espsdr-2026-foreign
project_id: espargos-espsdr
started: 2026-10-11
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "esp-sdr@e74f2a4 SoapyESPSDR@6f2cc72 CardputerADV-SDR@aa4737d"
reviewed_snapshot: "2026-10-11"
source_url: "https://espargos.net/espsdr"
reuse_outcomes:
  reused: [rtl-sdr, hw-path-gate]
  new: [esp32-undoc-iq-rx]
  not_helped: []
  process: "chip matrix desk; C5/S31 as UNKNOWN quality; no TX code"
```

## Ziel

ESPARGOS ESP-SDR als Primärquelle für **chipabhängige I/Q-Dump-Capabilities** (inkl. C5/S31) und Host-Portabilität (G7).

## Scope

[SCOPE](../../projects/espargos-espsdr/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 + lab-tool | erfüllt |
| 2 | Sheet `esp32-undoc-iq-rx` + Matrix C5/S31 | erfüllt |
| 3 | Application esp-sdr + Soapy + Cardputer-Port | erfüllt |
| 4 | TX withheld ≠ Implementierungs-FACT | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-11) |
| 6 | Lab Signalqualität S31 | offen |

## Lessons → Transfer

- C5 und S31 gehören in die Matrix (nicht nur Classic/S3).
- Multi-Repo-Familie: ein Sheet, mehrere Applications/Ports.
- Site-TX-Hinweis ohne Code = `UNKNOWN`/withheld.

## Bezug

[INVENTORY](../../projects/espargos-espsdr/INVENTORY.md) · [evidence](evidence.md) · [`c5vrx-2026-foreign`](../c5vrx-2026-foreign/) · [`esp32-sdr-trx-2026-foreign`](../esp32-sdr-trx-2026-foreign/)
