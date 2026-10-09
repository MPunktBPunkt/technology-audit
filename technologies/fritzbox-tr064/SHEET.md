# Technology Sheet: FritzBox TR-064 Hostlist

```yaml
slug: fritzbox-tr064
title: FritzBox TR-064 Hostlist
primary: F
tags: []
type: protocol
status: active
seen_in: [esp32-network]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Kurzfassung

Heimrouter-API (AVM TR-064): Hostliste abfragen zur Anreicherung von LAN-Inventaren. Neuere FritzOS oft nur noch **HTTPS :49443** (selbstsigniert); Digest-Auth möglich.

## Abgrenzung

- **Ist:** TR-064 Hosts/Get… gegen FritzBox.
- **Ist nicht:** generisches UPnP; ESP-Hub; Simple-API.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Port 49000 HTTP immer offen | `REJECTED` | ab FritzOS ≥7.50 oft nur HTTPS 49443 |
| Zertifikat immer vertrauenswürdig | `REJECTED` | selbstsigniert — Client muss insecure/TLS-Policy kennen |
| TR-064 ersetzt Subnetz-Scan | `HYPOTHESIS` | nur angemeldete Hosts; Scan findet andere Dienste |

### Projektstart-Checkliste

- [ ] HTTPS:49443 vs. Legacy-HTTP
- [ ] Auth-Variante
- [ ] Merge-Strategie mit Scan-Inventar
- [ ] Application + `seen_in`

## Referenzen

- AVM TR-064
- Beispiel: esp32.network

## Offene Fragen

- Welche Hostlist-Felder portabel über FritzOS-Versionen?
