# Technology Sheet: BT BD_ADDR Rewrite (Vendor HCI)

```yaml
slug: bt-bdaddr-rewrite
title: Bluetooth BD_ADDR Rewrite (Vendor-Specific HCI)
primary: C
tags: [bluetooth, hci, foreign-desk]
type: technology
status: active
seen_in: [bt-bdaddr-refs]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

Nur Ebene **A**. Desk aus Host-Tool `bdaddr`. **Keine** Impersonation-/Attack-How-tos.

## Kurzfassung

Viele Bluetooth-Controller erlauben das Setzen der lokalen **BD_ADDR** nur über **herstellerspezifische** HCI-Vendor-Commands (nicht über ein universelles Standard-HCI-Command). Das Tool `thxomas/bdaddr` mappt Manufacturer-ID → Vendor-Write (+ optional Reset). **Espressif fehlt** in der Vendor-Tabelle — ESP nutzt Stack-/Controller-APIs (`esp_base_mac_addr_set` u. ä.), nicht dieses Host-Tool.

## Abgrenzung

- **Ist:** Vendor-HCI Write-BD_ADDR Muster; Manufacturer-Tabelle; Kontrast ESP MAC-APIs.
- **Ist nicht:** BLE Identity-Resolve; Link-Key-Management-Spec; ESP Dual-Role Bridge; Attack-Rezept für Spoofing.
- **Grenzt an:** BlueZ Clone-Adapter MAC-Frage in BluetoothInterceptor DESIGN (out-of-scope dort) → dieses Sheet.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Ein HCI-Opcode schreibt BD_ADDR auf allen Controllern | `REJECTED` | Vendor-Tabelle (CSR/TI/Intel/Cypress/…) |
| `bdaddr` unterstützt Espressif/ESP32 | `REJECTED` | kein Espressif in `vendor[]` @ `53dae3f` |
| ESP setzt Adresse wie CSR via Host-`bdaddr` | `REJECTED` | ESP: `esp_base_mac_addr_set` / Controller-APIs |
| Adresswechsel invalidiert alle Link-Keys automatisch | `INFERENCE` | üblich erwartet; Tool belegt es nicht |
| HU / Peer akzeptiert geklonte BD_ADDR immer | `UNKNOWN` | Feldreaktion nicht gemessen |

## Transfer

Nutzen wenn Folgeprojekt Adapter-Identität unter BlueZ/Linux ändern will (Dongle mit unterstütztem Manufacturer). Für **ESP32**: IDF MAC-APIs, nicht `bdaddr`. Für GATT-Clone mit Bonding: Adress-Clone ist separates Gap (BluetoothInterceptor DESIGN Q2).

### Projektstart-Checkliste

- [ ] Manufacturer-ID des Controllers bekannt?
- [ ] In `bdaddr` Vendor-Tabelle? Sonst anderer Pfad
- [ ] ESP? → IDF APIs, nicht dieses Tool
- [ ] Link-Key / Bonding-Folgen als INFERENCE markieren
- [ ] Peer/HU-Reaktion = UNKNOWN bis Lab/Field
- [ ] Application + `seen_in`

## Referenzen

- thxomas/bdaddr @ `53dae3f` — `bdaddr.c` `vendor[]`
- Cross-Ref: BluetoothInterceptor DESIGN §4 MAC clone out-of-scope
- ESP-IDF: `esp_base_mac_addr_set` (Kontrast, kein Pin dieses Audits)

## Offene Fragen

- Welche USB-Dongles im Lab-Inventar haben unterstützte Manufacturer-IDs?
- HU-Reaktion auf BD_ADDR-Wechsel am Analyse-Adapter?
