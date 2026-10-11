# Technology Sheet: BLE HR-Relay (Peripheral Bridge)

```yaml
slug: ble-hr-relay
title: BLE HR-Relay (Peripheral Bridge)
primary: C
tags: [esp-idf, streaming]
type: pattern
status: active
seen_in: [esp32-heartrate, esp32-ergo]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/esp32-heartrate-2026-pilot
```

Nur Ebene **A**. Build-Flags und Env-Namen → Application.  
**Chip-Scope:** Belegte Dual-Role-Relay-Evidence in dieser KB = **ESP32-S3** (Familie `heartrate-s3` / vergleichbare Connection-Budgets). **Classic ESP32** (z. B. D1 Mini mit `PERIPHERAL_DISABLED` / `MAX_CONNECTIONS=1`): Relay **nicht** als FACT übertragbar — `UNKNOWN` bis eigene Evidence/Gate. Controller-`MAX_CONNECTIONS` und RAM sind Teil des Scopes.

## Kurzfassung

Muster: ein Gerät empfängt HR/RR als BLE Central und bietet denselben Heart Rate Service als Peripheral an weitere Consumer an („ein Sensor, mehrere Listener“), ohne den Originalgurt mehrfach zu koppeln.

## Abgrenzung

- **Ist:** Protokoll-Brücke / GATT-Server-Spiegelung für `0x180D`/`0x2A37` auf Controllern mit ausreichendem Dual-Role-/Connection-Budget.
- **Ist nicht:** FTMS-Bridge (Indoor Bike ↔ App); proprietäre Fitness-Cloud; Ersatz für Multi-Connect im Sensor selbst; stiller Transfer S3-Relay → Classic-Mini ohne Evidence.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Consumer (Phone, Bike Computer, Trainings-Node) | NOTIFY auf `0x2A37` |
| unten | Quell-Central / Parser | Rohbytes oder normalisierte HR/RR |
| lateral | Connection-Budget des Controllers | Central + N Peripheral-Links |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Advertising bleibt nach erstem Peripheral-Connect automatisch connectable | `HYPOTHESIS` | Stack-abhängig; oft expliziter Restart nötig |
| Notify aus dem BLE-Callback ist immer sicher | `REJECTED` | Besser Einspeisung aus App-Loop (Reentrancy/Heap) |
| Beliebig viele Relay-Clients | `REJECTED` | Controller-`MAX_CONNECTIONS` begrenzt |
| Relay muss imselben Firmware-Binary stecken wie der Consumer | `REJECTED` | Kann eigenständiger Node sein; Consumer sieht normales `0x180D` |
| „ESP32 kann HR-Relay“ gilt für Classic wie S3 | `REJECTED` (als FACT) | Chip-Scope: belegte Familie = S3; Classic Mini in heartrate = unsupported |
| S3-`MAX_CONNECTIONS=3` gilt auf jedem ESP32 | `UNKNOWN` / Gate | Build- und Controller-Grenze; eigene Evidence nötig |

## Transfer

Nützlich wenn Sensoren single-link sind und mehrere Apps/Nodes gleichzeitig Puls brauchen (z. B. Trainer-App + Coach-Node). Vermeiden auf Chips ohne genug Connections/RAM. Geschwister: `esp32-ergo` (Consumer/Bridge-Kontext), `esp32-heartrate` (Relay-Host auf S3).

### Projektstart-Checkliste

- [ ] Chip / Env: Dual-Role-Budget belegt? (S3-Familie vs. Classic Mini)
- [ ] Consumer vs. Implementierer klären (externer Node möglich)
- [ ] Connection-Budget / Advertising-Restart beachten
- [ ] Notify nicht aus BLE-Callback speisen
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Bluetooth HR Service (wie `ble-hrm-gatt`)
- NimBLE multi-connection / advertising notes

## Offene Fragen

- Byte-identische Weiterleitung vs. Re-Encode: wann ist was spezkonform genug?
- Idle-Policies: Central-Link halten solange Peripheral-Subscriber existieren?
- Classic ESP32: Dual-Role-Relay mit ≥2 Peripheral-Clients messbar/stabil? (Gate — kein Sheet-Ausweiten vorher)
