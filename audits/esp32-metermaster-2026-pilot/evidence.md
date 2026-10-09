# Evidence — esp32-metermaster-2026-pilot

Desk-Audit 2026-10-09 @ `60fa14b` · **standard_version 0.6.1**.

Basis: `https://github.com/MPunktBPunkt/esp32.MeterMaster/blob/60fa14b/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-IOB-2026-10-09-001` | Simple-API getPlainValue :8087 | `FACT` | [DATENAUSTAUSCH.md](https://github.com/MPunktBPunkt/esp32.MeterMaster/blob/60fa14b/docs/DATENAUSTAUSCH.md) |
| `EVID-IOB-2026-10-09-002` | Register nicht via Simple-API (Henne-Ei) | `FACT` | DATENAUSTAUSCH.md |
| `EVID-HUB-2026-10-09-020` | Ports 8087 / 8089 / 8093 | `FACT` | `.ino` Defaults + DATENAUSTAUSCH |
| `EVID-HUB-2026-10-09-021` | Hub-Heartbeat separat (`sendEspHubHeartbeat`) | `FACT` | `esp32.MeterMaster.ino` |
| `EVID-OLED-2026-10-09-001` | U8G2_SSD1306_64X48_ER | `FACT` | `.ino` Konstruktor |
| `EVID-OLED-2026-10-09-002` | 4 Stile + Carousel | `FACT` | README / `.ino` |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| OLED im Feld gut lesbar (Umgebungslicht) | `UNKNOWN` | Exit 5 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Pilot; Triple-HTTP + OLED Sheets; Standard 0.6.1 |
