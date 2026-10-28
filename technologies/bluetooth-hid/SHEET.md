# Technology Sheet: Bluetooth HID (Classic + HOGP Kontrast)

```yaml
slug: bluetooth-hid
title: Bluetooth HID (Classic Device/Host)
primary: C
tags: [esp-idf, classic-bt]
type: protocol
status: active
seen_in: [bt-classic-profile-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Cross-Transport BLE↔Classic → `hid-cross-transport-bridge`.

## Kurzfassung

**Classic HID**: Device (Peripheral, Report Descriptor in SDP) und/oder Host über L2CAP Control/Interrupt. **HOGP** (BLE HID over GATT, Service `0x1812`) ist verwandt im Report-Modell, aber anderer Transport. Report-Typen Input/Output/Feature und Boot vs Report Protocol gelten profilübergreifend — APIs nicht.

## Abgrenzung

- **Ist:** Classic HID Device/Host Contracts; Report Descriptor; GET/SET_REPORT; Output (z. B. LEDs/Rumble).
- **Ist nicht:** HOGP-Implementierungsdetail allein; A2DP; generisches GATT; Cross-Transport-Bridge (eigenes Sheet).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Device → Host | Interrupt Input Reports | Maus/Keyboard/Gamepad |
| Host → Device | Output / Feature / SET_REPORT | LEDs, Rumble |
| lateral | SDP / GATT | Descriptor Classic vs HOGP Map |
| lateral | CoD / Appearance | Discovery-Filter |

## Classic vs HOGP (Wahl)

| Kriterium | Classic HID | HOGP (BLE) |
|-----------|-------------|------------|
| Host-Ökosystem | Desktop/Alt-Stacks | Mobile/modern |
| Chip | BR/EDR nötig | BLE reicht |
| Latency/Sniff | Host-Sniff-Fallen | Connection Interval |
| Bridge zu Legacy PC | oft Classic Device | ggf. Cross-Transport |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| HID Device API = HID Host API | `REJECTED` | getrennte Rollen |
| Report Descriptor egal für Kompatibilität | `REJECTED` | Host parst strikt |
| SET_REPORT immer Success-Handshake | `HYPOTHESIS` | Fremd: Bluedroid-Workarounds |
| IDF liefert Classic HID **Host**-Example | `REJECTED` (Desk) | Mouse = Device-only |
| Keyboard/Mouse und Gamepad gleiche Queue-Strategie | `REJECTED` | depth-1 latest-wins droppt Keys |
| HOGP und Classic HID byte-identisch austauschbar | `HYPOTHESIS` | oft ja für Reports, nicht für Transport-State |

## Transfer

Gamepad/Keyboard-Produkte: Rolle zuerst. Desktop-Legacy: Classic Device. Mobile: HOGP. Beide Welten → Cross-Transport-Sheet.

### Projektstart-Checkliste

- [ ] Rolle Device vs Host vs Bridge
- [ ] Transport Classic vs HOGP vs beide
- [ ] Descriptor-Quelle (fest vs kopiert)
- [ ] Output/Feature-Pfad (Rumble/LED)
- [ ] Queue-Politik Input (Gamepad vs Keyboard)
- [ ] Application + `seen_in`

## Referenzen

- ESP-IDF `bt_hid_mouse_device`
- EspBle Classic HID; btstack `hid_device.c` / `hid_host.c`
- esp32-bthidbridge (Bridge → anderes Sheet)

## Offene Fragen

- Stabiler Classic HID Host auf ESP-Bluedroid ohne Community-Hilfe?
