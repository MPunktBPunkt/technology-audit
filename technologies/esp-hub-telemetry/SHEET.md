# Technology Sheet: ESP-Hub Node Telemetry

```yaml
slug: esp-hub-telemetry
title: ESP-Hub Node Telemetry
primary: F
tags: [esp-idf]
type: pattern
status: active
seen_in: [esp32-heartrate, esp32-ergo, esp32-ftmsprobe, esp32-bt-gateway, esp32-rfmonitor, esp32-toolnode, esp32-metermaster]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

## Kurzfassung

LAN-Hub-Muster: Nodes senden periodische HTTP-Heartbeats (`fwType`, Metriken, Status), empfangen optional OTA-URLs und posten Session-/Export-Payloads. Hub bleibt separates System; Audit betrifft die Node-Schnittstelle.

## Abgrenzung

- **Ist:** Node→Hub Telemetrie + Steuerimpulse (OTA, Export).
- **Ist nicht:** Cloud-Sync ohne Hub; vollständige Hub-Implementierung.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Hub HTTP API | Heartbeat, session-export, OTA-URL |
| unten | Config / Sensor-State | `fwType`, live metrics, node-spezifische IO-Keys |
| lateral | Web-UI Config | Host/Port, oft sofortiger Heartbeat nach Save |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Hub ist immer erreichbar | `REJECTED` | Nodes brauchen lastOk/Backoff |
| Config-Änderungen dürfen bis zum nächsten Intervall warten | `HYPOTHESIS` | Oft schlechte UX; besser send-now |
| OTA aus Heartbeat-Response ist spezifiziert überall gleich | `UNKNOWN` | Projekt-/Hub-Version prüfen |
| Ein `fwType` reicht für alle Nodes | `REJECTED` | Pro Node-Familie eigener Typ (`heartrate`, `ergo`, …) und IO-Schema |
| Hub-Anbindung erfordert Arduino-`esp-hub-base` | `REJECTED` | Contract ist HTTP; IDF-/dünner Client reicht (Register, otaUrl-Pull, `ios`) |
| OTA-URL im Heartbeat ist dauerhaft gültig | `REJECTED` | typisch einmalig konsumiert — sofort persistieren |
| Hub-OTA funktioniert immer im Feld (Auto) | `REJECTED` | oft nur Heim-WLAN; lokaler Upload/Depot als Stufe 2 |
| Produkt-Adapter-Register = ESP-Hub-Heartbeat | `REJECTED` | oft getrennte Ports/Contracts (z. B. MeterMaster 8089 vs. Hub 8093); Hub nur Dashboard-Sichtbarkeit |
| Simple-API ersetzt `/api/register` | `REJECTED` | Simple-API liest States; Register legt nodes.* erst an (Henne-Ei) |

## Transfer

Wiederkehrendes Muster in ESP-Node-Familien. Voraussetzung: stabile Hub-URL im LAN, dokumentierte IO-Keys **pro** `fwType`. Client-Code oft ähnlich; Payload-Builder projektspezifisch (Application B). Stack (Arduino vs. ESP-IDF) ist austauschbar solange der **HTTP-Contract** stimmt.

### Projektstart-Checkliste

- [ ] `fwType` festlegen (nicht Familien vermischen)
- [ ] Heartbeat-Payload-Keys dokumentieren (Application)
- [ ] Zweiter Produkt-Adapter? Ports/Contracts trennen (Hub ≠ Simple-API ≠ Adapter)
- [ ] OTA: Hub-Pull (einmalige URL) vs. lokaler Upload; Auto ohne Hub-Route bedenken
- [ ] USB-Flash-Erwartungen (merged image / Adresse) mit Hub-UI abgleichen
- [ ] NVS-Namespace-Kompatibilität zu Geschwister-Nodes prüfen
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Projektspezifisch: iobroker.esp-hub (externes Repo)
- HTTP JSON Heartbeat-Konventionen der jeweiligen Node-Familie

## Offene Fragen

- Einheitliches Meta-Schema der IO-Keys über Node-Typen?
- Authentifizierung/Trust im LAN?
