# Project Scope: iobroker.kalender

```yaml
project_id: iobroker-kalender
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/iobroker.kalender
reviewed_commit: d515fb6
profile: adapter
```

## Grenzen

| | |
|--|--|
| **In scope** | `main.js`, Schnittstellen REST :8095, Events/Geburtstage/ICS/Alexa |
| **Nicht in scope** | Alexa-Adapter-Quellcode; Google OAuth jenseits ICS |
| **Runtime** | Node; WebPort **8095** |
| **Version** | 0.6.0 |

## Systeme

```text
Browser ──REST/UI──▶ :8095 ──States/Trigger──▶ ioBroker (+ Alexa-Geräte)
Externe Kalender ──ICS URL──▶ Adapter (read-only)
```
