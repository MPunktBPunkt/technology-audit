# Project Scope: iobroker.fritzwireguard

```yaml
project_id: iobroker-fritzwireguard
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/ioBroker.fritzwireguard
reviewed_commit: 829b455
profile: adapter
```

## Grenzen

| | |
|--|--|
| **In scope** | `main.js`, `lib/`, `Schnittstellen.md`, README, Admin/WebUI, wg-quick, Tunnel-Manager, TR-064-Client |
| **Nicht in scope** | FritzOS-Firmware; WireGuard-Protokoll-Spec jenseits Adapter-Betrieb; Ziel-Adapter-Logik (Kostal etc.) |
| **Runtime** | Linux-Host mit `wireguard` + sudoers für `wg`/`wg-quick`; WebUI Default **8094** |
| **Version** | 0.2.36 |

## Systeme

```text
Adapter ──wg-quick──▶ Kernel WG ──VPN──▶ Remote-LAN / FritzBox
Adapter ──TR-064 (optional, oft :49000 über VPN)──▶ FritzBox
Anderer Adapter ──TCP──▶ 127.0.0.1:localPort ──Tunnel──▶ remoteHost:remotePort
Browser ──WebUI/REST──▶ :8094
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **0.6.3**: Adapter-Sheet (WG+Tunnel), TR-064 wachsen (Remote/VPN ≠ lokal HTTPS), Link Kostalpiko.
