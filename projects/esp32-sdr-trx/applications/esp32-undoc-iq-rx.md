# Project Application: esp32-undoc-iq-rx in esp32-sdr-trx

```yaml
project_id: esp32-sdr-trx
tech_slug: esp32-undoc-iq-rx
status: active
sheet: ../../../technologies/esp32-undoc-iq-rx/SHEET.md
audit: ../../../audits/esp32-sdr-trx-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

**S3-narrowband-RX ohne FPGA:** undokumentierter Dump → on-chip CIC/FIR → USB → `rtl_tcp` (`espdr-rx`). Kontrast zu h0m3us3r FPGA@80 Msps und zu ESPARGOS Multi-Chip-Bursts.

## Architektur / Datenfluss

```text
Wi-Fi PHY dump (~16 Msps)
  → on-chip CIC/FIR (250 or 333 ksps, int8 I/Q)
  → USB stream
  → Host rtl_tcp bridge
  → SDR++ / GNU Radio
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `firmware/src/` (`radio`, `dsp`, capture) | Dump + Decimation |
| `src/espdr/cli_rx.py` (u. a.) | `espdr-rx` Host |
| `NOTICE` | eSpDR-Ursprung |
| h0m3us3r `fpga/` / `docs/RADIO.md` | High-rate Provenance |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| S3 narrowband rtl_tcp RX im Release | `EVID-ESPTRX-RX-2026-10-11-001` | `FACT` |
| Tuning-Claim ~1.84–2.79 GHz | `EVID-ESPTRX-RX-2026-10-11-002` | `FACT` (README); Performance `UNKNOWN` |
| FPGA 80 Msps = anderer Transport-Pfad | `EVID-ESPTRX-RX-2026-10-11-003` | `FACT` (upstream eSpDR) |

## Verwandte Applications

- Sheet-Pilot: [`espargos-espsdr`](../../espargos-espsdr/applications/esp32-undoc-iq-rx.md)
- TX-Contract: [esp32-polar-phy-tx.md](esp32-polar-phy-tx.md)
