# Project Application: iobroker-fritzwireguard-adapter

```yaml
project_id: iobroker-fritzwireguard
tech_slug: iobroker-fritzwireguard-adapter
status: active
sheet: ../../../technologies/iobroker-fritzwireguard-adapter/SHEET.md
audit: ../../../audits/iobroker-fritzwireguard-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

**Node.js**-Adapter steuert WireGuard (`wg-quick`), sanitized Config (kein DNS/Full-Tunnel), optional Auto-Reconnect, TCP-Tunnel-Manager und WebUI/REST auf **8094**.

## Architektur / Datenfluss

```text
wgConfig (Admin) ──sanitize──▶ /tmp/…/wg-fritzwireguard.conf
wg-quick up/down + wg show (Poll)
tunnels[] ──▶ 127.0.0.1:localPort pipe ▶ remoteHost:remotePort
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `main.js` | Adapter-Kern |
| `lib/` | WG / Tunnel / TR-064 Hilfen |
| `Schnittstellen.md` | Fünf Schnittstellen |
| `README.md` / `README.de.md` | Betrieb, sudoers, AllowedIPs |
| `io-package.json` | native Defaults (webPort 8094) |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| webPort | 8094 | `FACT` |
| Interface-Name | `wg-fritzwireguard` | `FACT` (Schnittstellen) |
| Sanitizer | entfernt DNS, `0.0.0.0/0`, `::/0` | `FACT` |
| Same subnet | AllowedIPs Host-/32 empfohlen | `FACT` (README) |
| Tunnel-Beispiel | 8085 → Kostal :80 | `FACT` (Schnittstellen) |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| wg-quick + sudoers Pflicht | `EVID-FWG-2026-10-09-001` | `FACT` |
| TCP-Tunnel localhost → remote | `EVID-FWG-2026-10-09-002` | `FACT` |
| WebUI :8094 | `EVID-FWG-2026-10-09-003` | `FACT` |

## Verwandte

- Sheet: [`iobroker-fritzwireguard-adapter`](../../../technologies/iobroker-fritzwireguard-adapter/SHEET.md)
- TR-064: [`fritzbox-tr064`](fritzbox-tr064.md)
- Konsument: [`iobroker-kostalpiko`](../../iobroker-kostalpiko/)
