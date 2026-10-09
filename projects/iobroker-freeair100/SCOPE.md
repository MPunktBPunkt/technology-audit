# Project Scope: iobroker.freeair100

```yaml
project_id: iobroker-freeair100
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/iobroker.freeair100
reviewed_commit: 501f344
profile: adapter
```

## Grenzen

| | |
|--|--|
| **In scope** | `main.js`, `Schnittstellen.md`, Admin/WebUI :8096, Portal-Poll/Parsing |
| **Nicht in scope** | Geräte-Firmware; reverse-engineering fremder Keys als fertige Wahrheit |
| **Runtime** | Node.js; WebPort **8096**; Cloud freeair-connect.de |
| **Version** | 0.5.2 |

## Systeme

```text
freeair-connect.de (HTML / values.php AES) ──▶ Adapter Poll
Adapter ──States──▶ freeair100.0.*
Browser ──Dashboard──▶ :8096
```

## Ziel

Desk-Audit **0.6.3**: Portal-Sheet + Adapter-App; AES-Lücke als Coverage dokumentieren.
