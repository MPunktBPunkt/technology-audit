# Project Scope: iobroker.esp-hub

```yaml
project_id: iobroker-esp-hub
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/iobroker.esp-hub
reviewed_commit: 8d3853c
profile: adapter
```

## Grenzen

| | |
|--|--|
| **In scope** | `main.js`, `Schnittstellen.md`, README (API, States, USB/LXC), `admin/`, `firmware/` |
| **Nicht in scope** | Node-Firmware-Logik; andere ioBroker-Adapter (MeterMaster, Simple-API) |
| **Hardware / Runtime** | Node.js ≥18 auf ioBroker-Host; optional USB-UART |
| **Version** | 0.5.12 |

## Systeme

```text
ESP Nodes ──HTTP :8093──▶ Adapter (register, firmware, ota, webrtc)
Adapter ──States──▶ ioBroker
Browser ──Dashboard / USB / Compile──▶ Adapter
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.3** (sprachneutraler Contract, Adapter-Profil, Navigations-Einstieg).
