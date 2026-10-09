# Evidence — esp32-ftmsprobe-2026-pilot

Desk-Audit 2026-10-09 @ `70c3c25`. Rohdaten: `docs/ergometer/scan-20260910/` im Quellenrepo.

Basis: `https://github.com/MPunktBPunkt/esp32.ftmsprobe/blob/70c3c25/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-PROBE-2026-10-09-001` | Varon-Scan 2026-09-10 inkl. Rohordner | `MEASURED` | [scan-20260910/](https://github.com/MPunktBPunkt/esp32.ftmsprobe/tree/70c3c25/docs/ergometer/scan-20260910) · [ERGEBNISBERICHT](https://github.com/MPunktBPunkt/esp32.ftmsprobe/blob/70c3c25/docs/ergometer/ERGEBNISBERICHT.md) |
| `EVID-PROBE-2026-10-09-002` | Direkter OTA/Deploy bei offenen BLE-Links abgelehnt | `INFERRED` | README Deployment |
| `EVID-PROBE-2026-10-09-003` | Panic-Pfad Control `08 01` + Disconnect | `FACT` | README API |
| `EVID-VARON-2026-10-09-003` | Gerät TC174 / ASR / MAC im Lab | `MEASURED` | ERGEBNISBERICHT §2 |
| `EVID-HRM-2026-10-09-002` | Polar H9 parallel scanbar/koppelbar | `MEASURED` | ERGEBNISBERICHT Kurzfazit |
| `EVID-HUB-2026-10-09-003` | Firmware-Schema `ftmsprobe.<ver>.<family>.bin` | `FACT` | README / deploy.sh |
| `EVID-HUB-2026-10-09-004` | NVS `esphub` überlebt Familienwechsel | `INFERRED` | README Erstflash |

Geteilte FTMS/Varon-Claims (ergo-Kampagne): `EVID-FTMS-2026-10-09-001/002`, `EVID-VARON-2026-10-09-001` — Ursprung Messung hier.

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Zweites Nicht-Varon-Gerät mit gleicher Method | `UNKNOWN` | Exit 6 |
| Sim `0x11` Wirkungsmessung vollständig | `UNKNOWN` | ERGEBNISBERICHT Option |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-09-10 | Lab-Lauf Varon (Upstream) |
| 2026-10-09 | Import in technology-audit; Method + Probe-Pattern; REUSE-Prozess |
