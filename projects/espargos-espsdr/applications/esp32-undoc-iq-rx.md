# Project Application: esp32-undoc-iq-rx in espargos-espsdr

```yaml
project_id: espargos-espsdr
tech_slug: esp32-undoc-iq-rx
status: active
sheet: ../../../technologies/esp32-undoc-iq-rx/SHEET.md
audit: ../../../audits/espargos-espsdr-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Pilot-Application für die **Multi-Chip-Matrix**: Burst/FFT-Capture auf vielen Targets; Spezialmodi S3-IQS und S31-Stream; Host WebSDR/Soapy/Bridges. CardputerADV-SDR = Downstream-Port (UI/Audio), gleicher PHY-Contract.

| Repo | Commit | Rolle |
|------|--------|-------|
| [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr) | `e74f2a4` | Firmware + targets |
| [ESPARGOS/SoapyESPSDR](https://github.com/ESPARGOS/SoapyESPSDR) | `6f2cc72` | S31 continuous Host |
| [fedaykinofdune/CardputerADV-SDR](https://github.com/fedaykinofdune/CardputerADV-SDR) | `aa4737d` | S3 Board-Port |

## Architektur / Datenfluss

```text
Undocumented modem sample dump
  → SRAM packing / on-device FFT or decimation
  → UART | USB Serial/JTAG | HS USB | Gigabit Eth
  → WebSDR / Soapy / esp-sdr-bridge / on-device UI
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `firmware-targets.json` | Chip-Profile inkl. S31 preview |
| `main/targets/*/receiver.c` | per-chip RX |
| Docs `iq-stream.md` / `s31-streaming.md` | Continuous Protokolle |
| Cardputer `main/boards/cardputer/` | Port UI/audio |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Multi-chip support table (C5/S31/…) | `EVID-ESPSDR-2026-10-11-001` | `FACT` |
| Public firmware RX-only; TX withheld | `EVID-ESPSDR-2026-10-11-002` | `FACT` |
| S3 IQS rates 15.625–250 kSa/s | `EVID-ESPSDR-2026-10-11-003` | `FACT` (doku) |
| S31 up to 20/40 MSa/s experimental | `EVID-ESPSDR-2026-10-11-004` | `FACT` (doku); quality `UNKNOWN` |
| Cardputer = Port nicht neues PHY | `EVID-ESPSDR-2026-10-11-005` | `FACT` |

## Verwandte Applications

- [`c5vrx`](../../c5vrx/applications/esp32-undoc-iq-rx.md) — C5 continuous FPV
- [`esp32-sdr-trx`](../../esp32-sdr-trx/applications/esp32-undoc-iq-rx.md) — S3 narrowband rtl_tcp
