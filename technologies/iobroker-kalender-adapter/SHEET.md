# Technology Sheet: ioBroker Kalender Adapter

```yaml
slug: iobroker-kalender-adapter
title: ioBroker Calendar Adapter
primary: F
tags: [iobroker, nodejs]
type: component
status: active
seen_in: [iobroker-kalender]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/iobroker-kalender-2026-pilot
```

## Kurzfassung

Kalender-/Scheduler-Adapter: lokale Events + optionale **ICS-Feeds**, Zeit-Trigger die **ioBroker-States** und optional **Alexa** ansteuern — Web-Dashboard als Bedienfläche.

## Abgrenzung

- **Ist:** Event-Store, Trigger, ICS-Import, Ansage/State-Aktionen.
- **Ist nicht:** vollständiger CalDAV-Server; Alexa-Skill-Hosting; generisches Cron allein.

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| ICS ist bidirektional sync | `REJECTED` | typisch read-only Import |
| Zeitzone egal | `REJECTED` | system.config / Config pflegen |
| Trigger = nur UI-Erinnerung | `REJECTED` | State-Writes sind Kernnutzen |

### Projektstart-Checkliste

- [ ] Port / Timezone
- [ ] ICS-Quellen vs. lokale Events
- [ ] Alexa-Geräte-Discovery Abhängigkeiten
- [ ] Application + `seen_in`
