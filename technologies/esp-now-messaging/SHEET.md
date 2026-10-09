# Technology Sheet: ESP-NOW Messaging

```yaml
slug: esp-now-messaging
title: ESP-NOW Messaging
primary: C
tags: [esp-idf]
type: protocol
status: active
seen_in: [esp32-communicator]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Kurzfassung

Direktfunk zwischen ESPs (Broadcast/Unicast, Peer-Discovery) **ohne Router**, oft **parallel zu STA-WiFi** auf demselben Kanal. Payload klein (≈250 B); geeignet für Chat/Signale, nicht für Medienstreams.

## Abgrenzung

- **Ist:** ESP-NOW Datagramme + Peer-Liste.
- **Ist nicht:** BLE GATT; TCP Mesh; A2DP; LAN-Subnet-Scan.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| ESP-NOW unabhängig vom WiFi-Kanal | `REJECTED` | folgt typisch dem STA-Kanal; BSSID-Lock |
| WiFi + ESP-NOW immer verlustfrei parallel | `HYPOTHESIS` | Timing/Heap; Watchdog beachten |
| Pakete > ~250 B ohne Fragmentierung | `REJECTED` | Hard-Limit |
| Anruf-Audio läuft über ESP-NOW | `REJECTED` | oft nur Klingel-Signal; Media = Browser/WebRTC |

### Projektstart-Checkliste

- [ ] Gleicher Kanal / BSSID-Strategie
- [ ] Packet-Schema versionieren
- [ ] Discovery-Intervall
- [ ] Application + `seen_in`

## Referenzen

- Espressif ESP-NOW
- Beispiel: esp32.communicator

## Offene Fragen

- Encryption/LMK in Hobby-Messenger-Setups?
