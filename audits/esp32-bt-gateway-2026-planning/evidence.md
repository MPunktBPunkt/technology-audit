# Evidence — esp32-bt-gateway-2026-planning

Profil **planning** @ `7a7e8a4`. Keine Firmware-Messungen; Claims aus Planungsdokumenten.

Basis: `https://github.com/MPunktBPunkt/esp32.bt-gateway/blob/7a7e8a4/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-AVRCP-2026-10-09-001` | NBT: Skip/Play als AVRCP; MENU/BACK lokal; Skip=Cursor-Workaround am Pi | `INFERRED` | [AVRCP-MOEGLICHKEITEN.md](https://github.com/MPunktBPunkt/esp32.bt-gateway/blob/7a7e8a4/docs/planung/AVRCP-MOEGLICHKEITEN.md) (referenziert PiDrive) |
| `EVID-HUB-2026-10-09-005` | Hub v0.5.12: otaUrl einmalig, USB flash @0x0, Register-Contract | `INFERRED` | [HUB-INTEGRATION.md](https://github.com/MPunktBPunkt/esp32.bt-gateway/blob/7a7e8a4/docs/planung/HUB-INTEGRATION.md) H-F1–H-F9 |
| `EVID-BTGW-2026-10-09-001` | Gegenbefunde P-F1–P-F5 in Planung verankert | `INFERRED` | [STATE.md](https://github.com/MPunktBPunkt/esp32.bt-gateway/blob/7a7e8a4/STATE.md) |
| `EVID-BTGW-2026-10-09-002` | Firmware nicht gestartet; A17/Q12 Blocker | `FACT` | STATE / README |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| A17 Host-Stack Wahl | `UNKNOWN` | OFFENE-PUNKTE |
| Phase −1 Browsing/Meta Messwerte | `UNKNOWN` | PHASE-0-MESSPLAN |
| Flash-Budget gemessen | `UNKNOWN` | Q12 |
| Coexistence STA+A2DP PASS | `UNKNOWN` | nach A17 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-09-15 | Upstream Planung V2.0+ / STATE |
| 2026-10-09 | Planning-Audit; Profile/Parität-Prozess; Sheets A2DP/AVRCP/PDAP |
