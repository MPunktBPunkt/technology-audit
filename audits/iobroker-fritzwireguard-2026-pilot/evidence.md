# Evidence — iobroker-fritzwireguard-2026-pilot

Desk-Audit 2026-10-09 @ `829b455` · **standard_version 0.6.3**.

Basis: `https://github.com/MPunktBPunkt/ioBroker.fritzwireguard/blob/829b455/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-FWG-2026-10-09-001` | wg-quick + sudoers Requirements | `FACT` | README Requirements |
| `EVID-FWG-2026-10-09-002` | TCP-Tunnel Manager Konzept | `FACT` | `Schnittstellen.md` §3 |
| `EVID-FWG-2026-10-09-003` | webPort Default 8094 | `FACT` | `io-package.json` native |
| `EVID-FWG-2026-10-09-004` | Config-Sanitizer DNS/Full-Tunnel | `FACT` | `Schnittstellen.md` §1.3 |
| `EVID-FWG-2026-10-09-010` | TR-064 Default Host/Port 49000 | `FACT` | `io-package.json` / Schnittstellen |
| `EVID-FWG-2026-10-09-011` | Same-subnet → lokale Box möglich | `FACT` | README Troubleshooting + 0.2.35 |
| `EVID-FWG-2026-10-09-012` | TR-064 optional | `FACT` | README Features |
| `EVID-FWG-2026-10-09-020` | Version 0.2.36 | `FACT` | `io-package.json` |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Catalog latest listing | `UNKNOWN` | Fork-Scan fehlte; Upstream prüfen |
| TR-064 HTTPS :49443 über VPN | `UNKNOWN` | Default noch 49000 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Adapter-Pilot; Sheet `iobroker-fritzwireguard-adapter` |
