# Project Application: fritzbox-tr064 in iobroker.fritzwireguard

```yaml
project_id: iobroker-fritzwireguard
tech_slug: fritzbox-tr064
status: active
sheet: ../../../technologies/fritzbox-tr064/SHEET.md
audit: ../../../audits/iobroker-fritzwireguard-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

**Optionaler** TR-064-Client zur *entfernten* FritzBox über den WireGuard-Tunnel: WAN-IP/Uptime, DeviceInfo, Hostliste → `fritzbox.*` / `devices.*`. Kontrast zu [`esp32-network`](../../esp32-network/applications/fritzbox-tr064.md): dort lokal HTTPS :49443.

## Architektur / Datenfluss

```text
VPN up ──▶ SOAP HTTP config.fritzHost:fritzPort (Default 49000)
Same-subnet Risiko: lokale FritzBox antwortet statt Remote → UI filtert (0.2.35)
Tunnel bleiben nutzbar auch wenn TR-064 leer/falsch
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `Schnittstellen.md` §2 | Endpunkte WAN/Hosts/DeviceInfo |
| `README.md` Troubleshooting | same subnet / leere Hostliste |
| `io-package.json` | `fritzHost` / `fritzPort` Defaults |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Default Port 49000 HTTP über VPN | `EVID-FWG-2026-10-09-010` | `FACT` |
| Same-subnet kann lokale Box treffen | `EVID-FWG-2026-10-09-011` | `FACT` |
| TR-064 optional; Tunnel unabhängig | `EVID-FWG-2026-10-09-012` | `FACT` |

## Verwandte

- Sheet: [`fritzbox-tr064`](../../../technologies/fritzbox-tr064/SHEET.md)
- Lokal HTTPS: [`esp32-network` App](../../esp32-network/applications/fritzbox-tr064.md)
