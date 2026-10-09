# Technology Sheet: ioBroker MeterMaster Adapter

```yaml
slug: iobroker-metermaster-adapter
title: ioBroker MeterMaster Adapter
primary: F
tags: [iobroker, nodejs]
type: component
status: active
seen_in: [iobroker-metermaster, esp32-metermaster, metermaster-app]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/iobroker-metermaster-2026-pilot
```

Nur Ebene **A**. Implementierung → [`applications/iobroker-metermaster-adapter.md`](../../projects/iobroker-metermaster/applications/iobroker-metermaster-adapter.md). Firmware-Client → [`esp32-metermaster`](../../projects/esp32-metermaster/).

## Kurzfassung

Produkt-Adapter für **Zählerablesungen** (Mobile App → HTTP → ioBroker States/History) plus optionales **ESP32-Display-Node-Management** auf einem eigenen HTTP-Port (typisch **8089**): Register, Config-Poll, Befehle — getrennt von ESP-Hub und Simple-API.

## Abgrenzung

- **Ist:** Adapter-HTTP-Contract für Readings + Node-Lifecycle; WebUI am Adapter-Port.
- **Ist nicht:** ESP-Hub `/api/register` :8093 (→ `esp-hub-telemetry` / `iobroker-esp-hub-adapter`); Simple-API :8087 (→ `iobroker-simple-api`); Android-App-Logik; OLED-Rendering (→ `ssd1306-oled-ui`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| App → Adapter | `POST /api/reading(s)`, `/api/import`, `GET /api/ping` | oft Basic Auth |
| Node → Adapter | `POST /api/register`, Config-Poll `/api/nodes/{MAC}/config` | Heartbeat ≠ Hub |
| Adapter → Node | Config / `cmd` (z. B. LED) | über States + HTTP |
| lateral | Browser WebUI | Data/Import/Logs/System/Nodes |
| oben | ioBroker Objects | Häuser/Wohnungen/Zähler + `nodes.{MAC}` |

## Typische Fallstricke (A)

| Claim | Status | Hinweis |
|-------|--------|---------|
| MeterMaster-Register = ESP-Hub-Register | `REJECTED` | anderer Port und Payload |
| Simple-API ersetzt Adapter-Readings | `REJECTED` | App spricht Produkt-API |
| ESP-Nodes sind Pflicht für den Adapter | `REJECTED` | optional; App allein reicht |
| Ein Port für Hub + MeterMaster + Simple-API | `REJECTED` | typisch 8093 / 8089 / 8087 |
| WebUI braucht dieselbe Auth wie Writes | `HYPOTHESIS` | oft View ohne Passwort, Writes geschützt |

## Transfer

Muster „Produkt-Adapter mit eigenem HTTP + optionalen Display-Nodes“. Für neue ähnliche Adapter: Ports und Register-Semantik klar von Hub trennen.

### Projektstart-Checkliste

- [ ] Port ≠ 8093 / ≠ 8087 dokumentieren
- [ ] Readings-API vs. Node-API in Application trennen
- [ ] Firmware-Client: welcher Poll (config vs. Simple-API vs. Hub)?
- [ ] Application + `seen_in` (Adapter **und** Firmware-Projekt)

## Referenzen

- [ioBroker.metermaster](https://github.com/MPunktBPunkt/ioBroker.metermaster) README API
- [esp32.MeterMaster](https://github.com/MPunktBPunkt/esp32.MeterMaster)

## Offene Fragen

- Einheitliches Auth-Modell für Node-Register im LAN?
