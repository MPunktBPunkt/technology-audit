# Technology Sheet: ESP-Hub Node Telemetry

```yaml
slug: esp-hub-telemetry
title: ESP-Hub Node Telemetry
primary: F
tags: [iobroker]
type: pattern
status: active
seen_in: [esp32-heartrate, esp32-ergo, esp32-ftmsprobe, esp32-bt-gateway, esp32-rfmonitor, esp32-toolnode, esp32-metermaster, esp32-webradio, esp32-io-control, esp32-communicator, esp32-network, esp32-esp-hub, iobroker-esp-hub, esp32-pidrive]
maturity:
  technology: R4
  implementation: R0
  field_evidence: R0
  reusability: W4
```

Nur Ebene **A** = **HTTP-Contract** (sprachneutral). Client-Firmware und Adapter-Server → Applications / ggf. `iobroker-esp-hub-adapter`.

## Kurzfassung

LAN-Hub-Muster: Nodes `POST /api/register` (mac, name, hwType, version, Metriken, `ios`); Antwort kann `interval` und einmalige `otaUrl` liefern. Identity oft über MAC/Name — `fwType` optional (neuere Nodes). Stack (Arduino, IDF, anderer HTTP-Client) ist austauschbar.

## Abgrenzung

- **Ist:** Node↔Hub Telemetrie-Contract + OTA-URL-Impuls.
- **Ist nicht:** Adapter-UI/USB/Compiler (→ `iobroker-esp-hub-adapter`); Simple-API; Produkt-Adapter-Ports; Cloud ohne LAN-Hub.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Node → Hub | `POST /api/register` | Heartbeat + ios |
| Hub → Node | Response `interval`, `otaUrl` | otaUrl typisch einmalig |
| optional | `GET /api/ota/check` | alternativer Poll |
| lateral | Web-UI am Node | Host/Port Config |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Hub ist immer erreichbar | `REJECTED` | Nodes brauchen lastOk/Backoff |
| Config-Änderungen dürfen bis zum nächsten Intervall warten | `HYPOTHESIS` | Oft schlechte UX; besser send-now |
| OTA aus Heartbeat-Response ist spezifiziert überall gleich | `UNKNOWN` | Adapter-Version prüfen (`Schnittstellen.md`) |
| Ein `fwType` reicht für alle Nodes | `REJECTED` | wo genutzt: pro Familie; Basis-Contract braucht keins |
| Hub-Anbindung erfordert Arduino-`esp-hub-base` | `REJECTED` | Contract ist HTTP |
| OTA-URL im Heartbeat ist dauerhaft gültig | `REJECTED` | Adapter löscht State nach Versand — sofort konsumieren |
| Hub-OTA funktioniert immer im Feld (Auto) | `REJECTED` | oft nur Heim-WLAN; lokaler Upload/Depot Stufe 2 |
| Produkt-Adapter-Register = ESP-Hub-Heartbeat | `REJECTED` | getrennte Ports (z. B. 8089 vs 8093) |
| Simple-API ersetzt `/api/register` | `REJECTED` | Henne-Ei bei nodes.* |
| Jeder Hub-Node sendet `fwType` | `REJECTED` | Spec/`Schnittstellen.md`: mac/name/hwType |
| Fehlendes `fwType` = kein Hub-Muster | `REJECTED` | |
| Contract ändert sich mit Programmiersprache | `REJECTED` | A ist HTTP/JSON; B ist C++ vs Node |
| Nested Domain-Blöcke (z. B. `rf.alert`) ersetzen den Basis-Heartbeat | `REJECTED` | Erweiterungen pro `fwType`; Basis bleibt mac/name/ios |
| Device-Contract-Doku = Adapter spiegelt Felder End-to-End | `REJECTED` | Adapter-Seite eigene Evidence |

## Transfer

Voraussetzung: Hub erreichbar im LAN (typisch :8093), dokumentierte `ios`-Keys pro Node. Für neue Nodes: Vorlage `esp-hub-base-template`. Adapter-Features (Flash, Compile) nicht in diesen Slug pressen. Optionale nested Domain-Contracts versionieren und im Adapter explizit spiegeln — nicht still annehmen.

### Projektstart-Checkliste

- [ ] Identity: `fwType` **oder** `name`/`hwType`/`mac` laut Spec
- [ ] Heartbeat-Keys + `ios` in Application
- [ ] Nested Domain-Contract? ID + Felder dokumentieren; Adapter-Exit separat
- [ ] otaUrl-Konsum (einmalig) implementieren
- [ ] Zweiter Produkt-Adapter? Ports trennen
- [ ] Application + `seen_in` (Client **und/oder** Adapter-Projekt)

## Referenzen

- [iobroker.esp-hub `Schnittstellen.md`](https://github.com/MPunktBPunkt/iobroker.esp-hub/blob/master/Schnittstellen.md)
- [ESP32.esp-hub](https://github.com/MPunktBPunkt/ESP32.esp-hub) Heartbeat-Tabelle

## Offene Fragen

- Einheitliches Meta-Schema der IO-Keys?
- Auth für `/api/register` (heute LAN-offen)?
