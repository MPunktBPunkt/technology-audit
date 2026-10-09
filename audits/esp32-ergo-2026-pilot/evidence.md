# Evidence — esp32-ergo-2026-pilot

Desk-Audit 2026-10-09 gegen Commit `edaeb19`. Rohdaten im Quellenrepo / ftmsprobe.

Basis: `https://github.com/MPunktBPunkt/esp32.ergo/blob/edaeb19/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-FTMS-2026-10-09-001` | Varon: kein Power Target; `0x2AD8` fehlt | `MEASURED` | [GERAETEPROFIL.md](https://github.com/MPunktBPunkt/esp32.ergo/blob/edaeb19/docs/ergometer/GERAETEPROFIL.md) |
| `EVID-FTMS-2026-10-09-002` | Control-Point-Success beweist keine Wirkung (`0x05`) | `MEASURED` | GERAETEPROFIL + [UPDATE_CAPS_FIX.md](https://github.com/MPunktBPunkt/esp32.ergo/blob/edaeb19/debug/UPDATE_CAPS_FIX.md) |
| `EVID-FTMS-2026-10-09-003` | Bridge Exclusive sperrt Coach-Last (409) | `INFERRED` | [BRIDGE.md](https://github.com/MPunktBPunkt/esp32.ergo/blob/edaeb19/docs/ergometer/BRIDGE.md) |
| `EVID-VARON-2026-10-09-001` | Resistance sint16 Zehntel, ~16 Stufen wirkend | `MEASURED` | GERAETEPROFIL |
| `EVID-VARON-2026-10-09-002` | Advertising oft ohne Name/Services; MAC merken | `MEASURED` | GERAETEPROFIL |
| `EVID-HRM-2026-10-09-001` | Strap/Relay über `HrClient`/`0x180D` | `FACT` | `src/ble/HrClient.*`, README |
| `EVID-RELAY-2026-10-09-001` | Dual-HR + Heartrate-Relay mit MyWhoosh bewährt | `INFERRED` | [STATE.md](https://github.com/MPunktBPunkt/esp32.ergo/blob/edaeb19/STATE.md) |
| `EVID-WEB-2026-10-09-001` | SSE `/events` in Firmware | `FACT` | `src/app/App.cpp` |
| `EVID-WEB-2026-10-09-002` | App-Partition ~75 % bei 0.3.24-dev | `MEASURED` | STATE.md |
| `EVID-HUB-2026-10-09-001` | `fwType: ergo`, Hub Port 8093 | `MEASURED` | STATE / platformio.ini |
| `EVID-HUB-2026-10-09-002` | OTA beide Richtungen bewährt | `INFERRED` | STATE.md |

## Offene Claims (noch ohne ID)

| Claim | Status | Hinweis |
|-------|--------|---------|
| MyWhoosh Bridge-Abnahme formal PASS | `UNKNOWN` | STATE offen |
| Nachtest 6 Crash unter Last | `UNKNOWN` | STATE offen |
| SIM-Passthrough implementiert | `UNKNOWN` | STATE: Code fehlt |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Desk-Pilot; FTMS + Varon neu; Heartrate-Sheets `seen_in`/`W3` gewachsen (keine Forks) |
