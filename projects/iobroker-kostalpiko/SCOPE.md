# Project Scope: iobroker.kostalpiko

```yaml
project_id: iobroker-kostalpiko
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/ioBroker.kostalpiko
reviewed_commit: e90c650
profile: adapter
```

## Grenzen

| | |
|--|--|
| **In scope** | `main.js`, `Schnittstellen.md`, `lib/`, Admin/WebUI, PIKO-HTTP-Scraping, History/Yield |
| **Nicht in scope** | Kostal Cloud/Portal; fremder Adapter `kostal-piko-ba`; ESP-Hub |
| **Hardware** | Kostal PIKO 3.0–10.1 (lokaler Webserver) |
| **Runtime** | Node.js ≥22; WebUI Default **8092** (+1 pro Instanz) |
| **Version** | 0.6.32 (README-Badge) |

## Systeme

```text
Kostal PIKO ──HTTP Basic (index.fhtml / Inf.fhtml / LogDaten.dat)──▶ Adapter
Adapter ──States──▶ kostalpiko.N.*
Browser ──Dashboard──▶ :8092 (+N)
optional InfluxDB / Open-Meteo / E-Mail-Reports
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **0.6.3**: Device-Sheet `kostal-piko-http`, Adapter-Application, Catalog-Hinweis (≠ `kostal-piko-ba`).
