# Technology Sheet: HID Cross-Transport Bridge (HOGP ↔ Classic)

```yaml
slug: hid-cross-transport-bridge
title: HID Cross-Transport Bridge (HOGP ↔ Classic)
primary: C
tags: [esp-idf, classic-bt, ble]
type: pattern
status: active
seen_in: [bt-classic-profile-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
```

Nur Ebene **A**. Profil-Basics → `bluetooth-hid`; Dual-Mode → `bt-dual-mode-coex`.

## Kurzfassung

Bridge zwischen **BLE HID Host (HOGP)** und **Classic HID Device** (oder umgekehrt): Report Descriptor und Report-Bytes werden transportübergreifend weitergereicht, damit Legacy-Hosts (PC) ein BLE-Gamepad/Keyboard als Classic-HID sehen. Kein generisches GATT-Clone — HID-Rollen und SDP/GATT-Maps sind spezifik.

## Abgrenzung

- **Ist:** Cross-Transport HID Report-Passthrough + Output-Rückkanal.
- **Ist nicht:** Semantic GATT A→B (`ble-gatt-semantic-bridge`); Transparent GATT Clone; A2DP; HFP.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Upstream | BLE HID Host | Scan 0x1812 / Appearance |
| Downstream | Classic HID Device | SDP Descriptor + Input |
| rück | Output/Feature | Rumble/LED → BLE SET_REPORT |
| lateral | BTDM | beide Transports gleichzeitig |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| depth-1 latest-wins Queue für Keyboard OK | `REJECTED` | droppt Tasten; Gamepad eher ok |
| Descriptor unverändert immer kompatibel | `HYPOTHESIS` | optionale Battery-Mutation |
| Event-driven Forward im HID-Callback sicher | `HYPOTHESIS`/`REJECTED` | Fremd: BTC-Queue → Poll-Task |
| Classic HID Host Example ersetzt Bridge | `REJECTED` | IDF liefert Device-Example |
| Bridge ohne BTDM | `REJECTED` | braucht beide Links |

## Transfer

Nur wenn Legacy-Classic-Host und BLE-Peripheral gekoppelt werden müssen. Sonst reines HOGP oder reines Classic. Coex-Checkliste Pflicht.

### Projektstart-Checkliste

- [ ] Richtung HOGP→Classic vs Classic→HOGP
- [ ] Device-Klasse (Gamepad vs Keyboard) → Queue-Politik
- [ ] Output/Rumble-Pfad getestet?
- [ ] BTDM + Interval/Poll Coex
- [ ] `bluetooth-hid` + `bt-dual-mode-coex` gelesen
- [ ] Application + `seen_in`

## Referenzen

- anarsoul/esp32-bthidbridge

## Offene Fragen

- Classic→HOGP Richtung produktiv belegt?
