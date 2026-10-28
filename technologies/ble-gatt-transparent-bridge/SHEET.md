# Technology Sheet: Transparent GATT Bridge

```yaml
slug: ble-gatt-transparent-bridge
title: Transparent GATT Bridge (Byte Passthrough)
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

Nur Ebene **A**. Offensive Clone/MITM-Nutzung → Inventar, **keine** How-tos in der KB.

## Kurzfassung

Bridge leitet GATT-Attribute **byte-transparent** weiter (Notify/Indicate/Write, oft auch Read aus Cache), ohne Profil-Semantik. Typisch: GATT-Tabelle klonen oder 1:1 mappen; CCCD am Downstream steuert Host-Notify, Upstream-Subscribe oft **unabhängig** und dauerhaft.

## Abgrenzung

- **Ist:** Opaque Passthrough / GATT-Clone-Relay; generischer Central-Gateway zu Nicht-BLE (z. B. MQTT) als verwandtes Muster.
- **Ist nicht:** Semantic Re-Encode (FTMS→CPS); HR-Fanout mit festem `0x180D` (`ble-hr-relay`); Attack-Rezepte; Analyse-Observability-Dach (→ `ble-gatt-observe-proxy`); Endpoint-Impersonation (→ `bt-analysis-endpoint`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Upstream | Remote GATT (Central) | Discover → optional dump → subscribe |
| Downstream | Local GATT Server und/oder MQTT/UI | Mirror-Chars / Topics |
| lateral | Handle-/Positions-Mapping | Clone muss Char-Align halten |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Downstream-CCCD schreibt Upstream-CCCD mit | `REJECTED` | oft getrennte Pfade; Upstream dauerhaft subscribed |
| CCCD-Descriptors 1:1 vom Profil klonen | `HYPOTHESIS` / oft skip | Stack verwaltet 0x2902 lokal |
| Live-Read vom Target bei jedem Host-Read | `HYPOTHESIS` | viele Clones liefern Snapshot-Werte |
| Notify-Congestion ist gelöst wenn Relay existiert | `REJECTED` | ohne Queue/Drop-Policy = UNKNOWN |
| Handle-Layout egal für Android-Cache | `REJECTED` | Fremd: keepHandles / Handle-Patch-Diskussion |
| GATT↔MQTT-Gateway = BLE Peripheral Bridge | `REJECTED` | kein Dual-Role-Peripheral |

## Transfer

Nutzen wenn Folgeprojekt **beliebige** oder unbekannte Services spiegeln soll. Für Fitness-Apps mit erwarteter Semantik → `ble-gatt-semantic-bridge`. Dual-Role-Budget → `ble-gatt-dual-role`. Für **Device-Understanding** mit Logging → `ble-gatt-observe-proxy`; bei Encryption/Classic-Audio → `bt-analysis-endpoint` + Method `bt-passive-host-sniff`.

### Projektstart-Checkliste

- [ ] Transparent vs Semantic entschieden
- [ ] CCCD: Source-auto-sub vs Dest-driven dokumentieren
- [ ] Mapping: Position/UUID/Handle-Strategie
- [ ] Reconnect: Rediscover + Resubscribe?
- [ ] Offensive Clone nur Inventar — kein How-to in Sheets
- [ ] Application + `seen_in`

## Referenzen

- ChimeraBLE `mitm.cpp` / `clone.cpp` (Architektur)
- btlejuice `proxy.js` / `fake.js` (Zwei-HCI Relay-Architektur)
- esp32-ble2mqtt `ble.c` (Central-only Gateway-Kontrast)
- esp32-ble-uart-mx (festes transparentes `FFE0`)

## Offene Fragen

- Wann Snapshot-Read spezkonform genug vs. Live-Proxy-Read?
- Backpressure-Muster für Notify-Stürme auf ESP?
