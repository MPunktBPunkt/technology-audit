# Evidence — esp32-sdr-trx-2026-foreign

Desk 2026-10-11 · **standard_version 0.6.6** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/jochenhammes/esp32-sdr-trx | `e1aebbf` |
| https://github.com/h0m3us3r/eSpDR | `f279bf8` |
| https://github.com/jochenhammes/eSpDR | (verweist auf esp32-sdr-trx; Desk-Provenance) |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-POLAR-2026-10-11-001` | TX-Protocol: LO 2320–2450 MHz, 4-byte freq/gain records, ops 40–46 | `FACT` | `firmware/protocol/transmit.h` |
| `EVID-POLAR-2026-10-11-002` | Built on eSpDR `f279bf8`; ESP32-S3; Claude coding assist disclosed | `FACT` | `NOTICE`, README |
| `EVID-POLAR-2026-10-11-003` | Release-TX = polar test-tone; raw I/Q TX on `research/iq-tx` only | `FACT` | README + research branch docs |
| `EVID-POLAR-2026-10-11-004` | Thermal drift / correction figures (Hz, °C) | `INFERRED` | `docs/transmitter.md` author Lab; nicht remessen |
| `EVID-ESPTRX-RX-2026-10-11-001` | Narrowband RX 250/333 ksps → rtl_tcp ohne FPGA | `FACT` | README + firmware/host |
| `EVID-ESPTRX-RX-2026-10-11-002` | RX tuning claim 1.84–2.79 GHz | `FACT` (claim); RF quality `UNKNOWN` | README |
| `EVID-ESPTRX-RX-2026-10-11-003` | Upstream eSpDR: 80 Msps + FPGA path exists | `FACT` | h0m3us3r repo tree/docs |
| `EVID-MATCH-2026-10-11-POLAR` | Neuer Slug nötig — nicht `esp32-apll-fm-tx` | `FACT` | Abgrenzung Band/Contract |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Absolute TX power / harmonics | `UNKNOWN` | Author: uncalibrated |
| Polar-TX auf C5/S31 | `UNKNOWN` | Gate |
| Fremde Lab-Reproduktion SSB-Bild | `UNKNOWN` | README-Screenshot = author |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-11 | Desk-Bootstrap aus Kandidatenliste; Sheets polar + undoc-iq |
