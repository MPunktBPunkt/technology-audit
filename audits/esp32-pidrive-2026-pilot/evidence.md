# Evidence — esp32-pidrive-2026-pilot

Desk-Audit 2026-10-09 @ `b00e453` · **standard_version 0.6.3**.

Basis: `https://github.com/MPunktBPunkt/esp32.pidrive/blob/b00e453/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-MSC-2026-10-09-001` | TinyUSB MSC bei `ARDUINO_USB_MODE=0` | `FACT` | `platformio.ini`, `App.cpp` begin |
| `EVID-MSC-2026-10-09-002` | Geometrie Legacy/L0/L0-16M/L3 per Flag | `FACT` | `MscGeometry.h`, PIO envs |
| `EVID-PUMP-2026-10-09-001` | Framing UART ≡ TCP | `FACT` | `PumpServer.h` Kommentar + `PUMP.md` |
| `EVID-PUMP-2026-10-09-002` | Soft-Paging hält 4 MSC-Slots | `FACT` | `PUMP.md`, Bridge-Docstring |
| `EVID-HUB-2026-10-09-080` | Register: fwType pidrive, chipModel esp32s3 | `FACT` | `App.cpp` buildHeartbeat |
| `EVID-HUB-2026-10-09-081` | otaUrl aus Register → performOta | `FACT` | `HubClient.cpp` |
| `EVID-HUB-2026-10-09-082` | HUB-INTEGRATION nennt IDF; Build Arduino/PIO | `FACT` | Doc vs. `platformio.ini` |
| `EVID-WEB-2026-10-09-060` | SoftAP WebUI REST ohne SSE | `FACT` | `App.cpp` `server_.on("/api/…")` |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Feld-AV / Ohr am BMW | bei `pidrive` Pilot 2 | nicht hier verdoppeln |
| Sticky-ID3 ≤12 KiB überall eingehalten | `UNKNOWN` | Doku; Messreihe offen |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Firmware-Desk-Pilot Standard 0.6.3; Sheet `pump-control-link` |
