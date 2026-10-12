# Evidence — esp-sdr-bridge-2026-foreign

Desk 2026-10-12 · **standard_version 0.6.6** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/z2labs/esp-sdr-bridge | `7da8aea` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-BRIDGE-2026-10-12-001` | IQS serial commands + IQS1 header/CRC in bridge.py | `FACT` | `src/esp_sdr_bridge/bridge.py` |
| `EVID-BRIDGE-2026-10-12-002` | Rates 250/125/62.5 kS/s; USB ~0.65 MB/s | `FACT` | README |
| `EVID-BRIDGE-2026-10-12-003` | 87 min soak 0 CRC / 0 SpyServer gaps | `INFERRED` | docs/MEASUREMENTS.md |
| `EVID-BRIDGE-2026-10-12-004` | PLL spur when LO on 20 MHz grid | `INFERRED` | README/MEASUREMENTS |
| `EVID-BRIDGE-2026-10-12-005` | Tune 2204–2804 MHz; fs/4 IF | `FACT` | README |
| `EVID-BRIDGE-2026-10-12-006` | Dual servers SpyServer+rtl_tcp | `FACT` | bridge.py argparse |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| SNR-Zahlen reproduzierbar | `UNKNOWN` | VSG60 author setup |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-12 | Desk Application auf undoc-iq-rx |
