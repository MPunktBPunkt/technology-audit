# Evidence — iobroker-kostalpiko-2026-pilot

Desk-Audit 2026-10-09 @ `e90c650` · **standard_version 0.6.3**.

Basis: `https://github.com/MPunktBPunkt/ioBroker.kostalpiko/blob/e90c650/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-PIKO-2026-10-09-001` | Interleaved Zellen String/L | `FACT` | `Schnittstellen.md` |
| `EVID-PIKO-2026-10-09-002` | Live und LogDaten nicht parallel; Nacht-Skip | `FACT` | `main.js` Kommentare/Flow |
| `EVID-PIKO-2026-10-09-003` | Catalog hat `kostal-piko-ba`, nicht `kostalpiko` | `FACT` | Fork `sources-dist.json` Scan |
| `EVID-PIKO-2026-10-09-004` | Auth pvserver/pvwr, latin1 | `FACT` | `Schnittstellen.md` |
| `EVID-PIKO-2026-10-09-005` | webPort Default 8092 | `FACT` | README + Schnittstellen |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Alle gelisteten PIKO-Modelle feldverifiziert | `UNKNOWN` | README „Supported/Tested“ |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Adapter-Pilot; Sheet `kostal-piko-http` |
