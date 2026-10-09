# Technology Sheet: MeterMaster Android App

```yaml
slug: metermaster-android-app
title: MeterMaster Android App
primary: G
tags: [mobile]
type: component
status: active
seen_in: [metermaster-app]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/metermaster-app-2026-pilot
```

## Kurzfassung

Local-first Mobile-App für Versorgungszähler (Häuser/Wohnungen/Ablesungen/Fotos/Export) mit **optionalen** Smart-Home-Backends — ioBroker-Produkt-Adapter ist einer von mehreren Opt-ins.

## Abgrenzung

- **Ist:** Mobile Erfassung + lokale Persistenz + optionale Exporte/Sync.
- **Ist nicht:** ioBroker-Adapter (→ `iobroker-metermaster-adapter`); ESP-OLED; Cloud-Account-Pflicht.

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| App braucht immer ioBroker | `REJECTED` | offline-first |
| Adapter-Quellcode gehört ins App-Repo | `REJECTED` | Submodule/eigene Repos |
| Privacy-Landing = App-Source | `REJECTED` | getrenntes MeterMaster-Repo |

### Projektstart-Checkliste

- [ ] Welche Backends (ioBroker/MQTT/…) wirklich nötig?
- [ ] Adapter-Contract Port/Auth lesen
- [ ] Submodule-Pins vs. Live-Releases
- [ ] Application + `seen_in`
