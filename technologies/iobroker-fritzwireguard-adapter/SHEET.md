# Technology Sheet: ioBroker FritzWireguard Adapter

```yaml
slug: iobroker-fritzwireguard-adapter
title: ioBroker FritzWireguard Adapter
primary: F
tags: [iobroker, nodejs, vpn]
type: component
status: active
seen_in: [iobroker-fritzwireguard]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/iobroker-fritzwireguard-2026-pilot
```

Nur Ebene **A**. Implementierung → [`applications/iobroker-fritzwireguard-adapter.md`](../../projects/iobroker-fritzwireguard/applications/iobroker-fritzwireguard-adapter.md). TR-064 → [`fritzbox-tr064`](../fritzbox-tr064/SHEET.md).

## Kurzfassung

Adapter-Muster: **selektives WireGuard** zur entfernten FritzBox/LAN (`wg-quick`, Config-Sanitizer gegen Full-Tunnel/DNS-Hijack) plus **TCP-Localhost-Tunnels**, damit andere Adapter einzelne Remote-Dienste erreichen — ohne systemweiten Full-Tunnel.

## Abgrenzung

- **Ist:** VPN-Betrieb am ioBroker-Host, Tunnel-Manager, Adapter-WebUI/States.
- **Ist nicht:** TR-064-Protokoll selbst (→ `fritzbox-tr064`); WireGuard-Kryptographie-Spec; Site-to-Site-Router-Ersatz; Produkt-Adapter der Remote-Geräte (Kostal, …).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Adapter → OS | `wg-quick` / `wg` (sudo/caps) | Temp-Config, Interface-Name |
| Adapter → Remote-LAN | WireGuard Peer | AllowedIPs eng halten |
| lateral | TCP `127.0.0.1:localPort` | Pipe zu `remoteHost:remotePort` |
| optional | TR-064 zur Remote-FritzBox | über VPN-Route |
| oben | ioBroker States + Browser-UI | Status, Geräte, Tunnel-Stats |

## Typische Fallstricke (A)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Full-Tunnel (`0.0.0.0/0`) ist unkritisch auf dem ioBroker-Host | `REJECTED` | bricht oft lokalen SSH/Zugang |
| Gleiches LAN-Subnet lokal+remote → ganze `/24` routen | `REJECTED` | Host-/32 Routes; sonst asymmetrisch/lokal |
| DNS aus Client-`.conf` immer übernehmen | `REJECTED` | systemweiter DNS-Overwrite |
| TR-064 Pflicht für Tunnel | `REJECTED` | Tunnel unabhängig |
| VPN ohne Host-Privilegien (`NET_ADMIN`/sudo) | `REJECTED` | Kernel-Interface braucht Rechte |
| Ein Tunnel = Full-Site-VPN für alle Adapter | `REJECTED` | selektive localhost-Ports |

## Transfer

Überall, wo ein Smart-Home-Host wenige Remote-HTTP/Modbus-Endpunkte braucht, ohne den Default-Gateway umzuleiten. Consuming Adapter binden `127.0.0.1` oder dokumentierten Tunnel-Port.

### Projektstart-Checkliste

- [ ] Host: wireguard Paket + sudoers/`setcap` dokumentieren
- [ ] AllowedIPs-Strategie (Subnet vs. /32) festlegen
- [ ] Tunnel-Tabelle (localPort → remote) + Konfliktports
- [ ] TR-064 optional? Sheet `fritzbox-tr064` lesen
- [ ] Application + `seen_in`

## Referenzen

- [ioBroker.fritzwireguard](https://github.com/MPunktBPunkt/ioBroker.fritzwireguard)
- WireGuard: wireguard.com · AVM FRITZ!Box VPN

## Offene Fragen

- Einheitliche Port-Defaults für Tunnel-Konsumenten (Kostal etc.)?
