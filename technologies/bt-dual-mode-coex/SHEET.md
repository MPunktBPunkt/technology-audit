# Technology Sheet: BT Dual-Mode Coexistence (BTDM)

```yaml
slug: bt-dual-mode-coex
title: BT Dual-Mode Coexistence (Classic + BLE)
primary: C
tags: [esp-idf, classic-bt, ble]
type: pattern
status: active
seen_in: [bt-classic-profile-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Profil-Logik bleibt in HFP/SPP/HID/A2DP/GATT-Sheets.

## Kurzfassung

**BTDM**: ein Controller betreibt Classic BR/EDR und BLE gleichzeitig (oder zeitmultiplex). Limits: Connection-Slots, RAM, SCO+ACL, WiFi-Coex, Host-Architektur (ein Bluedroid vs. Dual-Host HCI-Broker). „Dual-Mode an“ ≠ alle Profile parallel stabil.

## Abgrenzung

- **Ist:** Controller-/Host-Coexistence-Muster, Budgets, Init-Modi (`BR_EDR_ONLY` / `BLE_ONLY` / `BTDM`).
- **Ist nicht:** einzelnes Profil; WiFi-only Coex ohne BT; S3-„Classic“ ohne Chip-Evidence.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | Controller | `ESP_BT_MODE_*`, mem_release |
| oben | Host(s) | Bluedroid und/oder NimBLE / BTstack VHCI |
| lateral | WiFi | SoftAP/STA Coex-Parameter |
| lateral | Audio SCO | Sync-Conn-Budget vs A2DP |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| IDF Classic-Examples = BTDM-Referenz | `REJECTED` | oft bewusst `BR_EDR_ONLY` |
| BLE mem_release + später BLE nutzen | `REJECTED` | Classic-only Pfad irreversibel bis Reset |
| EspBle Dual-Host auf S3 | `REJECTED` (Desk) | Classic an Original-ESP32 gebunden |
| BTDM in sdkconfig ⇒ App nutzt beide | `REJECTED` | z. B. HFP-Demo mit BTDM-Flag ohne BLE-Code |
| Unbegrenzte Classic+BLE+WiFi+SCO | `REJECTED` | Slots/Latenz/Queue-Overflows |
| Connection Interval egal bei HID Bridge | `REJECTED` | Fremd: 15 ms + Poll gegen Overflow |

## Transfer

Vor Gateway/Bridge: Matrix **Chip × Mode × Profile × WiFi**. Classic-Media-Sink oft Classic-only einfacher; BLE+Classic HID Bridge braucht BTDM+Coex-Heuristiken.

### Projektstart-Checkliste

- [ ] Chip: Classic vorhanden? (ESP32 vs S3 Gate)
- [ ] Mode: BR/EDR-only vs BTDM vs BLE-only
- [ ] Host: single Bluedroid vs Dual-Host Broker vs BTstack
- [ ] Profile-Kombination + SCO/ACL Budget
- [ ] WiFi parallel? Coex-Plan
- [ ] Application + `seen_in`

## Referenzen

- EspBle HCI-Broker; esp32-bthidbridge BTDM+HID Coex
- a2dpSinkHfpClient Classic-only mem_release
- ESP-IDF classic_bt sdkconfig.defaults; btstack ESP32 port

## Offene Fragen

- Messbare Coex-Matrix WiFi+A2DP+HFP+BLE GATT auf ESP32?
