# Technology Sheet: Ride BLE Display (Custom GATT)

```yaml
slug: ride-ble-display
title: Ride BLE Display (Custom GATT)
primary: C
tags: [esp-idf, arduino, fragile, lab-only]
type: pattern
status: active
seen_in: [open-bike-computer]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/open-bike-computer-2026-foreign
```

Nur Ebene **A**. Konkrete UUIDs, Ownership-Crypto, Map-Renderer, Board-Pins → Application.  
**Kein** Standard-FTMS/HRM und **kein** RSSI-Proximity-Hunt.

## Kurzfassung

ESP32 als **BLE-Peripheral-Display** für Fahrrad/Outdoor: Phone/Watch pushen Navigation, GPS-Position, Map-Settings und Workout-Frames über **custom GATT** (oft mit Ownership/Auth und Fallback-Framing). Display zeigt Live-Stats und Turn-by-Turn — Sensorik und Cloud liegen am Phone.

## Abgrenzung

- **Ist:** Custom Ride/Nav GATT + Auth/Session + Display.
- **Ist nicht:** FTMS (`bluetooth-ftms`); HRM (`ble-hrm-gatt`); BLE PCM Stream (`ble-pcm-notify-stream`); RSSI Hunt (`ble-rssi-proximity`); FTMS-Probe.
- **Grenzt an:** Manufacturer Adv + Device-ID; Offline-Map render (Application).

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | iOS/Watch Central | Auth vor Nav-Writes |
| lateral | Adv: ProtocolVersion + Flags + ID-Suffix | Multi-Device Discovery |
| unten | Custom Service/Chars; NVS owner state | Session envelope |
| UI | Display/Touch | optional |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Ride-Display ≡ FTMS Trainer | `REJECTED` | Custom ≠ Standard-Profile |
| Unauthenticated Nav/Map writes ok | `REJECTED` | Ownership/Auth zuerst |
| GATT-Cache ohne Fallback | `REJECTED` / Gate | Framed fallback (z. B. MAPR/GPSP) |
| Device-ID aus eFuse ohne Fail-Lock | `REJECTED` | Identity vs. Owner-Artefakte |
| Proximity-Hunt als Ride-Pattern | `REJECTED` | anderer Sheet |

### Projektstart-Checkliste

- [ ] Custom vs Standard-GATT (FTMS/HRM) geklärt
- [ ] Auth/Ownership vor Payload-Writes
- [ ] Adv Schema + Multi-Device Suffix
- [ ] GATT-Cache-Fallback geplant
- [ ] Application + `seen_in`

## Transfer

Für Phone-gesteuerte Outdoor-Displays mit eigener Session. Nicht still auf Fitness-Standard-GATT oder Scan-Hunt übertragen.

## Referenzen

- Pilot: [seichris/open-bike-computer](https://github.com/seichris/open-bike-computer) `docs/ble-protocol.md`
