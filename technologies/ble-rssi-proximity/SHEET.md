# Technology Sheet: BLE RSSI Proximity Hunt

```yaml
slug: ble-rssi-proximity
title: BLE RSSI Proximity Hunt
primary: H
tags: [esp-idf, lab-only]
type: pattern
status: active
seen_in: [esp-ble-finder]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/esp-ble-finder-2026-foreign
```

Nur Ebene **A**. Konkrete Board-UI, Target-Name-Strings, Clicker-Pins → Application.  
**RSSI ≠ Distanz** in Metern; Bands sind Heuristik.

## Kurzfassung

Muster: kontinuierlicher **BLE Advertisement Scan**, Filter auf Name/Addr oder „stärkstes Adv“, **EMA/Hold** gegen Target-Hopping, Abbildung RSSI → Proximity-Band / Fill / Audio-Click-Rate — „wärmer/kälter“-Hunt, kein GATT-Connect.

## Abgrenzung

- **Ist:** Adv-Scan + RSSI-Heuristik + Hunt-UI/Feedback.
- **Ist nicht:** RF Environment Score (`rf-environment-monitor`); Ride Display GATT (`ride-ble-display`); Promiscuous/PCAP; Raum-Presence mit Meter-Genauigkeit.
- **Grenzt an:** findphone-ähnliche UX; Mute während Hunt.

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | NimBLE/IDF Adv Scan | kein Connect nötig |
| lateral | Target filter (name substring / addr) | Compile-time oft |
| oben | UI bands + optional audio clicker | Application |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| RSSI = exakte Distanz (m) | `REJECTED` | Band-Heuristik; Multipath |
| Hunt ≡ Environment-Monitor Score | `REJECTED` | andere Produktabsicht |
| Ständig Target wechseln ohne Hold | `REJECTED` / Gate | Lock + dB-Hysterese |
| GATT Connect für Hunt nötig | `REJECTED` | Adv reicht |
| Mute stoppt Scan | `REJECTED` | nur Feedback |

### Projektstart-Checkliste

- [ ] Hunt vs Environment-Monitor geklärt
- [ ] Target-Filter und Lock/Hysterese
- [ ] RSSI-Bounds dokumentiert (nicht als Meter verkaufen)
- [ ] Application + `seen_in`

## Transfer

Für physische „suche das Gerät“-Lab-Tools. Nicht als Presence-Meter oder Ride-Protokoll still übertragen.

## Referenzen

- Inspiration: [ben-z/findphone](https://github.com/ben-z/findphone)
- Pilot: [khlebobul/esp_ble_finder](https://github.com/khlebobul/esp_ble_finder)
