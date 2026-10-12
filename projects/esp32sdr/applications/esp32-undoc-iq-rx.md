# Project Application: esp32-undoc-iq-rx in esp32sdr

```yaml
project_id: esp32sdr
tech_slug: esp32-undoc-iq-rx
status: active
sheet: ../../../technologies/esp32-undoc-iq-rx/SHEET.md
audit: ../../../audits/esp32sdr-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Burst-Capture-RX auf S3 (ESPARGOS-Bypass): SRAM I/Q @ `0x3fcd0000`, Register `0x60033d5c`, Raten bis ~80/40/16 Msps; USB Serial/JTAG Transport + Waterfall-GUI. Zweites Board / peer messaging.

## Architektur / Datenfluss

```text
RF → baseband ADC → SRAM aperture → CAP16 pack
  → burst_serial (USB/UART) → gui waterfall / bit decoder
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `README.md` — receive chain | Register table, sample format |
| `main/targets/esp32s3/` | capture / display |
| `main/common/burst_serial.*` | USB/UART transport |
| `gui/server.py` | Waterfall host |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| S3 burst capture register path documented | `EVID-ESPSDR-RX-2026-10-12-001` | `FACT` |
| I/Q 10-bit in 32-bit word; CAP8 packing | `EVID-ESPSDR-RX-2026-10-12-002` | `FACT` |
| RX spectrum mirrored / −3 MHz spur quirks | `EVID-ESPSDR-RX-2026-10-12-003` | `INFERRED` (author) |
| Absolute sensitivity | — | `UNKNOWN` |

## Abweichungen

- High-rate burst ≠ esp-sdr-bridge IQS continuous FIR stream — gleicher Sheet-Slug, anderer Application-Pfad.
