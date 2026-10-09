# Technology Sheet: LAN Device Inventory Scan

```yaml
slug: lan-device-inventory
title: LAN Device Inventory Scan
primary: H
tags: [lab-only]
type: pattern
status: active
seen_in: [esp32-network]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Kurzfassung

ESP scannt das **lokale IPv4-Subnetz** (TCP-Port-Proben, optional Ping), hält persistentes Geräteinventar (Label, Online, Uptime) und meldet Aggregates an Hub/Web. Optional Anreicherung über Router-APIs (z. B. TR-064).

## Abgrenzung

- **Ist:** IP/L4 Gerätefindung im Heimnetz.
- **Ist nicht:** RF-Environment-Monitor; ESP-NOW Peer-Discovery; Spektrumanalyse.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Gleicher Slug wie RF-Monitor | `REJECTED` | andere Schicht (siehe REUSE Scan-Tabelle) |
| Offene Ports = vollständige Identifikation | `REJECTED` | Heuristik; Labels manuell |
| Scan ohne Rate-Limit ist LAN-freundlich | `HYPOTHESIS` | Intervalle / Parallelität begrenzen |

### Projektstart-Checkliste

- [ ] Port-Set und Intervall
- [ ] Persistenz-Schlüssel (MAC vs. IP)
- [ ] Optional Router-Enrichment Sheet?
- [ ] Application + `seen_in`

## Referenzen

- Beispiel: esp32.network

## Offene Fragen

- ARP/mDNS als Ergänzung zu TCP-Proben?
