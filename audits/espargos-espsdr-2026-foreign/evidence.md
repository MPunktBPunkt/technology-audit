# Evidence — espargos-espsdr-2026-foreign

Desk 2026-10-11 · **standard_version 0.6.6** · Profile `lab-tool`.

| Quelle | Commit / Snapshot |
|--------|-------------------|
| https://github.com/ESPARGOS/esp-sdr | `e74f2a4` |
| https://github.com/ESPARGOS/SoapyESPSDR | `6f2cc72` |
| https://github.com/fedaykinofdune/CardputerADV-SDR | `aa4737d` |
| https://espargos.net/espsdr | Snapshot 2026-10-11 |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-ESPSDR-2026-10-11-001` | Chip-Tabelle inkl. C5, S3, S31; P4 unsupported; H21/H4 WIP | `FACT` | README + `firmware-targets.json` |
| `EVID-ESPSDR-2026-10-11-002` | Public firmware implements RX only; TX possible but withheld | `FACT` | README / site |
| `EVID-ESPSDR-2026-10-11-003` | S3 IQS continuous decimated USB 15.625–250 kSa/s | `FACT` | README section |
| `EVID-ESPSDR-2026-10-11-004` | S31 stream up to 20 MSa/s USB / 40 MSa/s Eth (experimental, DC peak) | `FACT` (doku) | README + Soapy repo |
| `EVID-ESPSDR-2026-10-11-005` | CardputerADV-SDR = downstream port of esp-sdr | `FACT` | Cardputer README/import |
| `EVID-ESPSDR-2026-10-11-006` | C5 listed with 5 GHz band capability in project docs | `FACT` | README |
| `EVID-MATCH-2026-10-11-IQ` | Neuer RX-Slug; nicht in APLL-FM-Sheet mischen | `FACT` | Index vor Audit |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Absolute sensitivity / ENOB | `UNKNOWN` | kein KB-Lab |
| S31 production quality | `UNKNOWN` | experimental |
| Public TX path details | `UNKNOWN` | withheld |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-11 | Desk-Bootstrap; Sheet `esp32-undoc-iq-rx` |
