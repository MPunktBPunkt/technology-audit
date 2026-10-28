# Evidence — esp32-esp-hub-2026-pilot

Desk-Audit 2026-10-09 @ `a03400a` · **standard_version 0.6.3**.

Basis: `https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/a03400a/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-BASE-2026-10-09-001` | Änderungszonen README | `FACT` | README Tabelle AB HIER… |
| `EVID-BASE-2026-10-09-002` | Bin-Namen {projekt}.{ver}.esp32.bin | `FACT` | README |
| `EVID-HUB-2026-10-09-070` | Heartbeat-Felder | `FACT` | README Heartbeat |
| `EVID-HUB-2026-10-09-071` | Identity ohne fwType | `FACT` | README + .ino buildHeartbeat |
| `EVID-WEB-2026-10-09-050` | SSE Status | `FACT` | .ino SSE + README |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Partition-Empfehlung im Feld verifiziert | `UNKNOWN` | Minimal SPIFFS |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Pilot Standard 0.6.3 |
| 2026-10-28 | Superseded by [`esp32-esp-hub-2026-1.10-validation`](../esp32-esp-hub-2026-1.10-validation/) (FW 1.10.5 @ `eebbcd9`, Standard 0.7.1) |
