# Evidence — esp32-communicator-2026-pilot

Desk-Audit 2026-10-09 @ `429f20e` · **standard_version 0.6.2**.

Basis: `https://github.com/MPunktBPunkt/esp32.communicator/blob/429f20e/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-NOW-2026-10-09-001` | ESP-NOW+WiFi gleicher Kanal | `FACT` | README + .ino Kommentar |
| `EVID-NOW-2026-10-09-002` | WebRTC Media via Hub, Call via ESP-NOW | `FACT` | README Features |
| `EVID-WEB-2026-10-09-030` | SSE /api/sse | `FACT` | README API |
| `EVID-HUB-2026-10-09-050` | Hub ios peers/sent/recv | `FACT` | buildHeartbeat() |
| `EVID-HUB-2026-10-09-051` | Kein fwType | `FACT` | buildHeartbeat() |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Reichweite ~200 m Freifeld | `UNKNOWN` | nicht gemessen hier |
| Secure Context für Kamera im LAN | `HYPOTHESIS` | README Hinweis |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Pilot unter Standard 0.6.2 |
