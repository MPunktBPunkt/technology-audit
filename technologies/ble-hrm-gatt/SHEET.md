# Technology Sheet: BLE Heart Rate GATT (Central)

```yaml
slug: ble-hrm-gatt
title: BLE Heart Rate GATT (Central)
primary: C
tags: [esp-idf, streaming]
type: protocol
status: active
seen_in: [esp32-heartrate, esp32-ergo]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Projektpfade und Sensor-Quirks → jeweilige Application.

## Kurzfassung

Bluetooth LE Heart Rate Service (`0x180D`) mit Characteristic Heart Rate Measurement (`0x2A37`). Ein Central subscribed auf Notifies und parst Flags, BPM und optionale RR-Intervalle (Auflösung 1/1024 s laut Spec).

## Abgrenzung

- **Ist:** GATT-Profil für Puls-/RR-Daten von Wearables (und von Relays, die denselben Service spiegeln).
- **Ist nicht:** AVRCP/A2DP, FTMS Indoor-Bike-HR-Feld (`0x2AD2`), medizinische Zertifizierung, HRV-Analyse oberhalb der Roh-RR-Pipeline.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | App / Session-Pipeline | BPM, RR, Battery, RSSI |
| unten | BLE Stack (z. B. NimBLE) | Scan, Connect, GATT Subscribe |
| lateral | optional Peripheral-Relay | gleicher Service nach außen spiegeln |
| lateral | alternative HR-Quellen | z. B. FTMS `0x2AD2` HR-Bit — anderes Profil, anderer Slug |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Sensor Contact Bit ist überall gesetzt | `REJECTED` | Viele Gurte (u. a. Polar H9) liefern es nicht |
| Ein Gurt erlaubt beliebig viele gleichzeitige Centrals | `REJECTED` | H9 typischerweise single-link; Multi-Consumer braucht Relay (`ble-hr-relay`) |
| RR-Einheiten sind immer Millisekunden | `REJECTED` | Spec: 1/1024 s Einheiten |
| „HR vom Bike“ ist immer `0x180D` | `REJECTED` | Manche Trainer liefern HR nur in Indoor Bike Data |

## Varianten (A)

| Ansatz | Wann | Trade-off |
|--------|------|-----------|
| Direkter Central auf Gurt | Ein Consumer reicht | Einfach; blockiert andere Apps am Gurt |
| Central hinter HR-Relay | Mehrere Consumer (App + Node) | Extra Hop; braucht Peripheral-Budget |
| HR aus FTMS IBD | Bike speist Puls (z. B. GymLink) | Kein eigener `0x180D`-Link; andere Semantik |

## Transfer

Geeignet für ESP-/NimBLE-Gateways und Trainings-Nodes. Voraussetzung: Central-Rolle, Heap für Scan+Connection, klare Trennung Parser vs. UI. Bei Multi-Consumer: Sheet `ble-hr-relay` mitdenken.

## Referenzen

- [Bluetooth Heart Rate Service](https://www.bluetooth.com/specifications/specs/) (GATT HR)
- NimBLE-Arduino / ESP NimBLE Central-Docs

## Offene Fragen

- Welche weiteren Gurte außer Polar H9 verhalten sich bzgl. Flags/RR identisch?
- Wie stabil ist Session-Reconnect geräteübergreifend (Fenster, Backoff)?
