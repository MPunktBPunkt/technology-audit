# Technology Sheet: MQTT Node Telemetry

```yaml
slug: mqtt-node-telemetry
title: MQTT Node Telemetry
primary: F
tags: [streaming]
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

Optionaler MQTT-Kanal für ESP-Nodes: Status/Events publishen und Kommandos subscribe — ergänzend oder alternativ zu Hub-HTTP, oft unter einem Namensraum pro Gerätefamilie.

## Abgrenzung

- **Ist:** MQTT Pub/Sub für Telemetrie/Kommandos.
- **Ist nicht:** ESP-Hub HTTP-Contract; Cloud-IoT-Plattformen; Message-Bus-Internals.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| MQTT ersetzt Hub-Register | `HYPOTHESIS` | oft parallel; unterschiedliche Konsumenten |
| Ein Topic-Schema für alle Nodes | `REJECTED` | Gerätefamilie im Pfad (`…/toolnode/<device>/…`) |
| Broker immer erreichbar | `REJECTED` | optional + Backoff wie Hub |

### Projektstart-Checkliste

- [ ] Parallel zu Hub oder statt Hub?
- [ ] Topic-Namespace + Payload-Schema
- [ ] Packet-Size / QoS Limits
- [ ] Application + `seen_in`

## Referenzen

- MQTT 3.1.1 / Broker unabhängig
- Beispiel: PubSubClient auf ESP

## Offene Fragen

- Einheitliches Command-Schema über Node-Familien?
