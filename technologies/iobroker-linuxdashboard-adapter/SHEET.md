# Technology Sheet: ioBroker Linux Dashboard Adapter

```yaml
slug: iobroker-linuxdashboard-adapter
title: ioBroker Linux Dashboard Adapter
primary: F
tags: [iobroker, linux-userspace]
type: component
status: active
seen_in: [iobroker-linuxdashboard]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/iobroker-linuxdashboard-2026-pilot
```

## Kurzfassung

Adapter als **Browser-Shell zum Linux-Host**: Live-Metriken plus operative Flächen (Dateien, Services, Pakete, Logs, optionale Befehle) — typisch **ohne HTTP-Auth**, daher nur vertrauenswürdiges LAN.

## Abgrenzung

- **Ist:** Host-Ops-UI + REST am Adapter-Port.
- **Ist nicht:** Kubernetes/Proxmox-UI; Remote-SSH-Ersatz mit Zero-Trust; Windows.

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Kein Auth = LAN-sicher genug immer | `REJECTED` | laterale Bewegung / offene Ports |
| Command-Execution immer nötig | `REJECTED` | whitelist/disable |
| filemanagerRoot=/ unkritisch | `REJECTED` | Schreibzugriff = Host-Compromise |
| Metrics-API = volle Shell | `REJECTED` | getrennte Capability-Flächen |

### Projektstart-Checkliste

- [ ] Port + Firewall / bind
- [ ] allowCommandExecution + Whitelist
- [ ] filemanagerRoot eingrenzen
- [ ] Application + `seen_in`
