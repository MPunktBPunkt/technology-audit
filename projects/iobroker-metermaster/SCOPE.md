# Project Scope: iobroker.metermaster

```yaml
project_id: iobroker-metermaster
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/ioBroker.metermaster
reviewed_commit: be89348
profile: adapter
```

## Grenzen

| | |
|--|--|
| **In scope** | `main.js`, README-API, `admin/`, WebUI :8089, Node-Register/Config/Cmd |
| **Nicht in scope** | Android-App-Code ([MeterMaster](https://github.com/MPunktBPunkt/MeterMaster)); ESP-Firmware-Logik (→ [`esp32-metermaster`](../esp32-metermaster/)); Simple-API :8087; ESP-Hub :8093 |
| **Runtime** | Node.js / js-controller ≥6; Port Default **8089** |
| **Version** | 0.9.12 (`io-package.json`) |

## Systeme

```text
Android MeterMaster App ──HTTP Basic Auth──▶ Adapter :8089 (/api/reading…)
ESP32 OLED Nodes ──POST /api/register + config poll──▶ Adapter :8089
Adapter ──States──▶ metermaster.0.* (+ nodes.{MAC}.*)
Browser ──WebUI──▶ :8089 (Data / Import / Logs / System / Nodes)
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **0.6.3**: Adapter-Sheet, Abgrenzung zu Hub/Simple-API, Querverweis Firmware.
