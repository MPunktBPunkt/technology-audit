# Technology Sheet: ioBroker ESP-Hub Adapter

```yaml
slug: iobroker-esp-hub-adapter
title: ioBroker ESP-Hub Adapter
primary: F
tags: [iobroker, nodejs]
type: component
status: active
seen_in: [iobroker-esp-hub]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

## Kurzfassung

ioBroker-Adapter als **Zentrale** der ESP-Hub-Familie: HTTP :8093 (Register, Firmware-Depot, OTA-Push), Geräte-States, Browser-Dashboard, optional USB-Flash (esptool), arduino-cli-Compile, Seriell-Monitor, WebRTC-Signaling-Relay.

## Abgrenzung

- **Ist:** Adapter-Produkt + Betriebsflächen um den Hub-Contract herum.
- **Ist nicht:** der HTTP-Register-Contract allein (→ `esp-hub-telemetry`); Simple-API; MeterMaster-Adapter (→ `iobroker-metermaster-adapter`); Node-Firmware.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | ESP Nodes | `/api/register`, `/firmware/*`, OTA |
| oben | ioBroker Objects/States | `devices.<MAC>.*` |
| lateral | Host-OS | USB `ttyUSB*`, esptool, arduino-cli |
| lateral | Browser | Dashboard, WebRTC Signaling `/api/webrtc` |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Adapter = nur State-Spiegel | `REJECTED` | Flash/Compile/OTA/WebRTC sind Kernnutzen |
| USB in LXC ohne Geräte-Passthrough | `REJECTED` | Major `c 188:*`, by-id Mounts |
| otaUrl-State bleibt nach Versand stehen | `REJECTED` | Adapter leert nach Heartbeat-Response |
| Register-API braucht Auth im Heimnetz | `HYPOTHESIS` | Spec: offen; Risiko dokumentieren |
| WebRTC-Signaling = Medienrelay | `REJECTED` | nur Signaling; Media peer-to-peer Browser |

### Projektstart-Checkliste

- [ ] Port 8093 + Firmware-Ablage
- [ ] State-Baum MAC-Normalisierung
- [ ] USB/Compile nur wenn Host das hergibt
- [ ] Contract-Änderungen → Sheet `esp-hub-telemetry` mitpflegen
- [ ] Application + `seen_in`

## Referenzen

- Repo iobroker.esp-hub · `Schnittstellen.md`

## Offene Fragen

- Multi-Instance / mehrere Hub-Ports?
