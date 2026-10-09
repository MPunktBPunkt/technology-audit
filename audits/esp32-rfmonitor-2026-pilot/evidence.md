# Evidence — esp32-rfmonitor-2026-pilot

Desk-Audit 2026-10-09 @ `95314cd` · **standard_version 0.6.0**.

Basis: `https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/95314cd/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-RF-2026-10-09-001` | RF-Score-Heuristik v1 dokumentiert | `FACT` | [RF_SCORE.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/95314cd/docs/RF_SCORE.md) |
| `EVID-RF-2026-10-09-002` | WLAN- und BLE-Scan nacheinander | `FACT` | README Hardware |
| `EVID-HUB-2026-10-09-006` | Hub-IO-Keys RF-Metriken | `INFERRED` | README Hub-IO |
| `EVID-HUB-2026-10-09-007` | `fwType: rfmonitor` | `FACT` | README |
| `EVID-WEB-2026-10-09-003` | SSE `/events` | `FACT` | `App.cpp` / README API |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Score kalibriert an festem Standort | `UNKNOWN` | Exit 5 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Pilot unter Standard 0.6.0 (`standard_version` eingeführt) |
