# Technology Sheet: ESP32 WiFi ↔ Classic Bluetooth RF Coexistence

```yaml
slug: esp-wifi-bt-coex
title: ESP32 WiFi ↔ Classic Bluetooth RF Coexistence (esp_coex_*)
primary: D
tags: [esp-idf, esp32, wifi, classic-bt, rf-coex]
type: pattern
status: active
seen_in: [esp32-wifi-bt-coex-refs, esp32-bt-analyzer]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/esp32-wifi-bt-coex-2026-foreign
```

Ebene **A**. SoftAP/STA-Pins und HCI_TCP-Entscheidungen → Application.
Desk: [`esp32-wifi-bt-coex-2026-foreign`](../../audits/esp32-wifi-bt-coex-2026-foreign/).

## Kurzfassung

Auf Original-ESP32 teilen sich **WiFi** und **Classic BT/BLE** den 2.4‑GHz-Pfad per
**TDM**. Espressif steuert das über Software-Coexistence (`CONFIG_ESP_COEX_SW_COEXIST_ENABLE`,
`esp_coex_*`, Status-Bits; optional EXTERNAL PTA-ähnliche Wires). SoftAP **CONNECTED**
mit BT ist Guide-seitig problematisch (**C1**); STA Connected + BT Connected ist
vorgesehen (**Y**). Status-Bits (z. B. A2DP Streaming) ersetzen deprecated Prefer-API;
Bluedroid setzt Streaming oft über Vendor HCI.

## Abgrenzung

- **Ist:** RF Software-Coex WiFi↔BT/BLE (TDM, Status-Bits, SoftAP/STA-Matrix, Core-Pin, EXTERNAL).
- **Ist nicht:** USB-OTG↔WiFi PHY ([`esp32-s3-usb-wifi-coex`](../esp32-s3-usb-wifi-coex/SHEET.md));
  Classic+BLE-only Budgets ([`bt-dual-mode-coex`](../bt-dual-mode-coex/SHEET.md) — WiFi ≠ BTDM);
  gemessener HCI_TCP-Throughput eines konkreten Analysators (Application/Lab).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | RF / PHY / Coex-Scheduler | TDM-Slices WiFi / BT / BLE |
| lateral | WiFi SoftAP / STA | SoftAP CONNECTED+BT = C1; STA+BT = Y |
| lateral | Classic / BLE Controller | A2DP Status-Bits; Vendor HCI |
| oben | App / Host (TCP, VHCI) | HCI_TCP konkurriert um WiFi-Slices |
| optional | EXTERNAL wires 1/2/3 | request / priority / grant (PTA-ähnlich) |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| `CONFIG_ESP_COEX_SW_COEXIST_ENABLE` nötig für SW-Coex | `FACT` | IDF Guide |
| SoftAP CONNECTED + BT = C1 (instabil) | `FACT` | IDF Guide-Matrix |
| STA Connected + BT Connected = Y | `FACT` | IDF Guide-Matrix |
| WiFi- und BT-Stacks auf unterschiedliche Cores pinnen | `FACT` | IDF Guide |
| `ESP_COEX_BT_ST_A2DP_STREAMING` 0x10 / `A2DP_PAUSED` 0x20 | `FACT` | `esp_coexist.h` |
| `esp_coex_prefer_t` aktuell empfehlen | `REJECTED` | DEPRECATED → Status-Bits |
| Bluedroid setzt A2DP-Streaming via Vendor HCI `BTM_ConfigCoexStatus` | `FACT` | IDF #12434 |
| Public Repos messen systematisch `esp_coex_*`+A2DP+WiFi thr. | `REJECTED` (Existenz) | Gap bleibt |
| Historisch: prefer BT → A2DP smooth; WiFi RX ~1–5 Mbps; AMPDU ↓ | `FACT` (historisch #1291) | kein Universal-SoT |
| BLE Scan-Window kann von WiFi gekürzt werden | `FACT` | esp-faq |
| USB↔WiFi-Sheet erklärt RF WiFi↔BT | `REJECTED` | andere Domäne |
| BTDM-Sheet ersetzt WiFi-Coex | `REJECTED` | Classic+BLE ≠ WiFi-TDM |
| Bessere WiFi-RSSI hebt Classic-ACL-Durchsatz | `REJECTED` | STA + Classic über HCI_TCP: ~3–4 kB/s (`wifi_ps` min/max) bzw. ~36–45 kB/s (`none`), unabhängig von −45/−85 dBm — [`esp32-bt-analyzer`](../../projects/esp32-bt-analyzer/applications/esp-wifi-bt-coex.md) |
| Externer Host (BlueZ via HCI) setzt A2DP-Status-Bit | `REJECTED` | nur On-Chip-Host (Bluedroid); sonst manuell `esp_coex_status_bit_set` (Wirkung `UNKNOWN`) |

## Transfer

Bei jedem ESP32-Projekt mit **WiFi-TCP + Classic/BLE gleichzeitig**:

1. SoftAP×BT vermeiden, wenn Guide-C1 gilt; STA bevorzugen.
2. `SW_COEXIST` + Core-Pin prüfen, bevor Throughput-Optimismus.
3. A2DP: Status-Bits / Bluedroid-Pfad, nicht Prefer-API.
4. Architekturentscheid: **UART HCI offload** vs. same-chip SoftAP/STA + `esp_coex_*`-Tuning.

### Projektstart-Checkliste

- [ ] Sheet gelesen (Abgrenzung USB / BTDM)
- [ ] SoftAP vs STA × BT gegen Guide-Matrix geprüft
- [ ] `CONFIG_ESP_COEX_SW_COEXIST_ENABLE` + Core-Pin im Build
- [ ] Prefer-API vermieden; Status-Bits / Stack-Verhalten verstanden
- [ ] UART-HCI vs same-chip Coex entschieden (oder Lab-Diskriminator geplant)
- [ ] Application + `seen_in`

## Referenzen

- ESP-IDF RF Coexistence Guide (ESP32)
- `esp_coexist.h` (Status-Bits, EXTERNAL, prefer deprecated)
- esp-idf Issues [#12434](https://github.com/espressif/esp-idf/issues/12434), [#1291](https://github.com/espressif/esp-idf/issues/1291)
- Espressif FAQ coexistence
- Audit Evidence: `EVID-WBTCOEX-2026-11-12-*`

## Offene Fragen

- Aktuelle IDF-Releases: WiFi-Throughput unter Classic A2DP bei STA+`SW_COEXIST` (Lab)?
- Wann EXTERNAL PTA vs. reines Software-Coex?
- Für Analyzer: ab welcher HCI_TCP-Last ist UART-HCI Pflicht trotz Coex-Tuning?
