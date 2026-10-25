# Project Inventory: esp32-marauder (Fremd)

```yaml
project_id: esp32-marauder
updated: 2026-10-25
reviewed_commit: "9386f3c0348c171eb58ef2e1ce1f0c2f555ba30c"
profile: lab-tool
pilot_order: [esp-wifi-promiscuous-pcap, rf-environment-monitor, lan-device-inventory]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| WiFi Promiscuous + PCAP Double-Buffer + Packet-Rate | `esp-wifi-promiscuous-pcap` | **neu** + App |
| WLAN/BLE Environment-Score (Hub-Monitor) | `rf-environment-monitor` | **Kontrast** — kein `seen_in` (≠ Sniff) |
| ARP/Port-Scan CLI | `lan-device-inventory` | **Kontrast / partial** — observed |
| NimBLE Adv-Scan | — | observed (`ble-adv-scan`); ≠ `ble-hrm-gatt` |
| Dual-Band Kanal-Liste (C5, 51 Kanäle) | `esp-wifi-promiscuous-pcap` | Chip-Gate im Sheet |
| Double-Buffer + `portMUX` (hohe Rate) | `esp-wifi-promiscuous-pcap` | A-Fallstrick (≠ pinned Dual-Core-Worker) |
| Deauth / Beacon Spam / Attack-CLI | — | **observed only** — kein Sheet (Policy) |
| Evil Portal | — | out of KB |
| GPS / Wigle CSV | — | observed (Wardrive-Nebenrolle) |

Kampagne: [`esp32-marauder-2026-foreign`](../../audits/esp32-marauder-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp-wifi-promiscuous-pcap` | ESP WiFi Promiscuous + PCAP | H | applied | partial | [SHEET](../../technologies/esp-wifi-promiscuous-pcap/SHEET.md) | [app](applications/esp-wifi-promiscuous-pcap.md) |
| `rf-environment-monitor` | RF Environment Monitor | H | observed | none | [SHEET](../../technologies/rf-environment-monitor/SHEET.md) | — (Kontrast) |
| `lan-device-inventory` | LAN Device Inventory | H | observed | none | [SHEET](../../technologies/lan-device-inventory/SHEET.md) | — (Kontrast) |

## Nach Kategorie

### H — Test / Analyse

- `esp-wifi-promiscuous-pcap` (Kern)
- Kontrast: `rf-environment-monitor`, `lan-device-inventory`

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Eigene pps/Drop-Messung | Desk only | Lab authorized |
| Expliziter Dual-Core-Worker | im Upstream nicht als `xTaskCreatePinnedToCore` gefunden | UNKNOWN / nicht behaupten |
| BLE-Spam / Spoof | Policy | kein Sheet |
| C5 Dual-Band Lab | Chip-Gate Desk | FOLLOW-ON |

## Signale ohne Eintrag (bewusst)

- Offensive TX-Modi (`WIFI_ATTACK_*`, CLI `attack …`) — Produkt-Existenz, keine KB-Technik-A
- Evil Portal / Karma — nicht dokumentieren
- Flipper / CYD / M5 Board-HAL — Hardware-Matrix, kein Slug
- CSI Motion — observed; Kontrast-Sheet jetzt [`wifi-csi-motion`](../../technologies/wifi-csi-motion/SHEET.md) (ESPectre-Pilot); Marauder-Code nicht vertieft
- Remote ID — observed, Gate vor Sheet
