# Technology Sheet: BLE GATT Dual-Role

```yaml
slug: ble-gatt-dual-role
title: BLE GATT Dual-Role (Central + Peripheral)
primary: C
tags: [esp-idf, nimble]
type: pattern
status: active
seen_in: [ble-gatt-bridge-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Konkrete Bridge-Semantik → `ble-gatt-transparent-bridge` / `ble-gatt-semantic-bridge` / Profil-Sheets.

## Kurzfassung

Ein Controller führt **gleichzeitig** BLE-Central (zu Sensor/Gerät) und BLE-Peripheral (zu App/Host) aus. Limitiert durch Connection-Budget, RAM, Stack-Scheduling und oft explizite Build-Flags (`MAX_CONNECTIONS`, Role-Enable). Bridge-Produkt braucht Dual-Role — Reverse gilt nicht: Dual-Role allein definiert keine Bridge.

## Abgrenzung

- **Ist:** Controller-/Stack-Muster Dual-Role + Budget/Contention/Init-Reihenfolge.
- **Ist nicht:** Profil-Spiegelung (HR/FTMS); GATT↔MQTT ohne Peripheral (`esp32-ble2mqtt`); Dual-Role über **zwei** HCI-Adapter (btlejuice-Architektur ≠ Ein-Chip-ESP).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | BLE Stack (NimBLE/Bluedroid/…) | Central + Peripheral (+ ggf. Observer) |
| oben | Bridge-Logik | Fanout / Semantic / Transparent |
| lateral | `MAX_CONNECTIONS` / ACL | Central-Links + Peripheral-Hosts |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| „ESP32 kann Dual-Role“ gilt Classic = S3 | `REJECTED` (als FACT) | Chip-/Build-Scope; heartrate Mini oft ohne Peripheral |
| `MAX_CONNECTIONS=1` reicht für Central+Peripheral+zweiten Host | `REJECTED` | Budget explizit planen (typ. ≥2–3) |
| Advertising bleibt nach Peripheral-Accept connectable | `HYPOTHESIS` | oft Restart nötig (siehe HR-Relay) |
| Server-GATT vor Central-Connect immer unproblematisch | `HYPOTHESIS` | Fremd: Reboot-before-advertise / Role-Init-Reihenfolge |
| Dual-Role-Contention „kickt“ Target-Link nie | `REJECTED` | Fremd-Kommentare/Watchdogs existieren deshalb |
| Zwei-HCI-Proxy = Ein-Chip-Dual-Role | `REJECTED` | andere Failure Modes |

## Transfer

Vor jedem Bridge-Folgeprojekt: Chip-Scope + Connection-Rechnung (1× Upstream + N Downstream). Profile separat wählen. Geschwister: `ble-hr-relay`, `bluetooth-ftms`.

### Projektstart-Checkliste

- [ ] Chip/Env Dual-Role belegt? (S3-Familie vs Classic Gate)
- [ ] `MAX_CONNECTIONS` ≥ Upstream + Downstream(+Spare)
- [ ] Advertising-Restart / Target-Reconnect-Policy
- [ ] Bridge-Typ: Transparent vs Semantic vs Fanout (eigene Sheets)
- [ ] Application + `seen_in`

## Referenzen

- Fremd-Desk: ChimeraBLE, iFitnessProxy, BleRemoteBrideg, esp32-ble-uart-mx @ Pins in `ble-gatt-bridge-refs`
- Eigen: esp32.heartrate S3 Relay, esp32.ergo FTMS Bridge

## Offene Fragen

- Classic ESP32: stabiles Dual-Role mit ≥2 Peripheral-Clients?
- Wann Reboot-before-GATT-Server nötig vs. Live-Init?
