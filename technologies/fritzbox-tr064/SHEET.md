# Technology Sheet: FritzBox TR-064 Hostlist

```yaml
slug: fritzbox-tr064
title: FritzBox TR-064 Hostlist
primary: F
tags: []
type: protocol
status: active
seen_in: [esp32-network, iobroker-fritzwireguard]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Kurzfassung

Heimrouter-API (AVM TR-064): Hostliste, WAN-Status, DeviceInfo. Pfade unterscheiden sich: **lokal** oft **HTTPS :49443** (selbstsigniert); **über VPN** kann Legacy-**HTTP :49000** noch genutzt werden — immer die erreichbare Box prüfen.

## Abgrenzung

- **Ist:** TR-064 Hosts/WAN/DeviceInfo gegen FritzBox.
- **Ist nicht:** generisches UPnP; ESP-Hub; Simple-API; WireGuard/Tunnel-Betrieb (→ `iobroker-fritzwireguard-adapter`).

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Port 49000 HTTP immer offen | `REJECTED` | ab FritzOS ≥7.50 lokal oft nur HTTPS 49443 |
| Zertifikat immer vertrauenswürdig | `REJECTED` | selbstsigniert — Client muss insecure/TLS-Policy kennen |
| TR-064 ersetzt Subnetz-Scan | `HYPOTHESIS` | nur angemeldete Hosts; Scan findet andere Dienste |
| Gleiches Subnet lokal+remote → TR-064 trifft immer die Remote-Box | `REJECTED` | ohne enge Routes antwortet oft die lokale Box |
| TR-064 ist Pflicht für Remote-TCP-Zugriffe | `REJECTED` | Tunnels/VPN können ohne Hostliste laufen |

### Projektstart-Checkliste

- [ ] HTTPS:49443 vs. Legacy-HTTP :49000 (Pfad: lokal vs. VPN)
- [ ] Auth-Variante
- [ ] Same-subnet: welche Box antwortet?
- [ ] Merge-Strategie mit Scan-Inventar / Tunnel-Targets
- [ ] Application + `seen_in`

## Referenzen

- AVM TR-064
- Lokal: esp32.network · Remote/VPN: ioBroker.fritzwireguard

## Offene Fragen

- Welche Hostlist-Felder portabel über FritzOS-Versionen?
- Ob VPN-Clients HTTPS :49443 zuverlässig nutzen können?
