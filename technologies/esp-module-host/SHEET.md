# Technology Sheet: ESP Modular Tool Firmware

```yaml
slug: esp-module-host
title: ESP Modular Tool Firmware
primary: J
tags: [esp-idf]
type: pattern
status: active
seen_in: [esp32-toolnode]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Kurzfassung

Firmware-Muster: gemeinsamer Core (Config, Web/SSE, Hub, Events, History) plus **aktivierbare Module** hinter einem gemeinsamen Interface (`begin`/`loop`/Status/IO/Commands/Routes), gesteuert über Build-Flags und optional Setup-Wizard/Profile.

## Abgrenzung

- **Ist:** Modularisierung und Host-Lifecycle für Werkzeug-/Multi-Feature-Nodes.
- **Ist nicht:** die Fachmodule selbst (RF, I²C, …); Microservices; RTOS-App-Framework allgemein.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Module → Core | BaseModule-API | Status/IO in Hub-Payload einspeisen |
| Core → Platform | WiFi, HTTP, NVS, GPIO | Pin-Guard gegen Konflikte |
| Build | `ENABLE_*` Flags | Board-Profile |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Alle Module immer compilieren | `REJECTED` | Flash/RAM; Flags pro Env |
| Module dürfen Pins ungeprüft teilen | `REJECTED` | Claim/Guard nötig |
| Wizard ersetzt Build-Flags vollständig | `HYPOTHESIS` | oft beides: Compile-Zeit + Runtime-Enable |

## Transfer

Für Werkstatt-Nodes mit wählbarem Feature-Set. Fachwissen der Module in eigenen Sheets halten (z. B. `rf-environment-monitor`).

### Projektstart-Checkliste

- [ ] Module-Interface und Lifecycle skizzieren
- [ ] Build-Profile vs. Runtime-Enable klären
- [ ] Pin-Konfliktstrategie
- [ ] Fachmodule auf bestehende Tech-Slugs mappen (keine Forks)
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Beispiel: `esp32.toolnode` `docs/ARCHITECTURE.md`

## Offene Fragen

- Wie weit lässt sich das Interface über Arduino hinaus (IDF) portieren?
