# Technology Sheet: Bluetooth A2DP

```yaml
slug: bluetooth-a2dp
title: Bluetooth A2DP
primary: C
tags: [bluetooth-classic, streaming]
type: protocol
status: active
seen_in: [pidrive, esp32-bt-gateway]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/pidrive-2026-radio-bt
```

Nur Ebene **A**. Host-/Fahrzeugverhalten → Application C oder Host-Sheet.  
**Stack-Scope:** Profil ist spezseitig gemeinsam; **Implementierung** Pi BlueZ/PipeWire ≠ ESP Classic-Controller (Bluedroid/BTstack) — Evidence und Coexistence getrennt führen (G17-analog).

## Kurzfassung

Advanced Audio Distribution Profile: punkt-zu-punkt Streaming komprimierter Audio (typisch SBC) zwischen Source und Sink. Im Infotainment oft Source = Kopfhörer/Phone-Stack oder dedizierte Hardware; Sink = HU/Headset.

## Abgrenzung

- **Ist:** Classic-BT Audio-Transport (Source/Sink-Rollen).
- **Ist nicht:** AVRCP (Steuerung/Metadaten/Browse); BLE Audio; USB-Audio; Mix/Routing (PipeWire); stiller Transfer Pi-BlueZ-Evidence → ESP-Gateway.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | PCM/Encoder | festes Format oft erzwingen (z. B. 44.1/S16/Stereo) |
| unten | Classic BT Controller + Host-Stack | Bluedroid / BTstack / BlueZ |
| lateral | AVRCP | gleiche Gerätepaarung, anderes Profil |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| A2DP-Sink ohne Default-Route = hörbar | `REJECTED` | Streams/Card-Profil oft explizit setzen (PipeWire/pactl) |
| Jede Audioquelle folgt automatisch BT | `REJECTED` | Demods können eigenen ALSA-Pfad haben |
| BT und USB-Gadget-Output gleichzeitig | `HYPOTHESIS` | Produkt-Policy trennen |
| Ein Gerät kann gleichzeitig A2DP Sink und Source sein | `REJECTED` | Classic-Rollen schließen sich am ESP typischerweise aus |
| WiFi + Classic-BT Coexistence ist überall gratis | `HYPOTHESIS` | stack- und antennaabhängig — hartes Gate |
| Sink-Stabilität ist rein Codec-Sache | `REJECTED` | Buffering, Link-Supervision, Host-Policies dominieren oft |
| Pi BlueZ-Route beweist ESP-Gateway-A2DP | `REJECTED` | getrennte Stack-Evidence / Applications |

## Transfer

Geeignet wenn Audio-Pfad von fragilem Desktop-BT (BlueZ+PW) auf dedizierte Hardware wandert. PCM-Contract und Coexistence vor Feature-Fülle klären. PiDrive vs. `esp32-bt-gateway`: gleicher Slug, kontrastierende Applications.

### Projektstart-Checkliste

- [ ] Rolle Source vs. Sink festlegen (kein stilles Dual)
- [ ] Host-Stack benennen (BlueZ/PW vs. ESP Classic) — kein stiller Transfer
- [ ] Coexistence WiFi+BT als Gate, nicht als Nachgedanke
- [ ] AVRCP als eigenen Slug planen
- [ ] PipeWire/BlueZ-Routing und Profil `a2dp_sink` prüfen (Pi-Pfad)
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Bluetooth A2DP / SBC Spezifikationen (SIG)
- Projektplanung: `esp32.bt-gateway` Konzept (nicht Spec)

## Offene Fragen

- Welche Buffer-/Bitpool-Defaults für NBT-Evo-Sinks empirisch stabil sind?
