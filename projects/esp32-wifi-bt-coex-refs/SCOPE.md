# Project Scope: esp32-wifi-bt-coex-refs (Fremd)

```yaml
project_id: esp32-wifi-bt-coex-refs
title: ESP32 WiFi ↔ Classic Bluetooth RF Coexistence (esp_coex_*)
updated: 2026-11-12
profile_hint: lab-tool
reviewed_commit: "desk-docs-2026-11-12"
repos:
  - https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/coexist.html
  - https://github.com/espressif/esp-idf (esp_coexist.h / RF Coexistence)
  - https://github.com/espressif/esp-idf/issues/12434
  - https://github.com/espressif/esp-idf/issues/1291
  - https://github.com/espressif/esp-faq (coexistence)
status: active
```

## Zweck

Desk-Navigationskarte für **Software-RF-Coexistence** auf ESP32 (Original): WiFi und
Classic BT/BLE teilen sich den 2.4‑GHz-Pfad per **TDM** (`esp_coex_*`,
`CONFIG_ESP_COEX_SW_COEXIST_ENABLE`, Status-Bits, optional EXTERNAL PTA-ähnliche Wires).

**Trigger-Wissenslücke:** `esp32-bt-analyzer` streamt HCI über **WiFi TCP** (`HCI_TCP`),
während der On-Chip-Controller Classic/BLE bedient — öffentliche Messprojekte zu
`esp_coex_*` + Classic A2DP + WiFi-Throughput fehlen; Gap bleibt.

## Systeme und Grenzen

| Quelle | Muster | Im Scope? |
|--------|--------|-----------|
| ESP-IDF RF Coexistence Guide (ESP32) | TDM-Slices; SoftAP/STA×BT-Matrix; Core-Pin | ja |
| `esp_coexist.h` / Status-Bits / EXTERNAL | A2DP_STREAMING/PAUSED; prefer deprecated; wire 1/2/3 | ja |
| IDF #12434 | Bluedroid Vendor HCI `BTM_ConfigCoexStatus` | ja |
| IDF #1291 (historisch) | prefer BT; WiFi RX ~1–5 Mbps bei smooth A2DP | ja |
| Espressif FAQ coexistence | TDM; BLE-Scan-Window vs WiFi | ja |
| Public Repos mit systematischer Coex-Messung | A2DP + WiFi throughput + `esp_coex_*` | **nicht gefunden** (Gap) |
| `esp32-bt-analyzer` Lab (HCI_TCP ACL kB/s) | Eigenmessung | nur **Kontrast** in Application (`INFERENCE`); dieses Fremd-Audit **misst nicht** |

## Nicht-Ziele

- [`esp32-s3-usb-wifi-coex`](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md) — USB-PHY/BBPLL, nicht RF WiFi↔BT
- [`bt-dual-mode-coex`](../../technologies/bt-dual-mode-coex/SHEET.md) — Classic+BLE (BTDM), nicht WiFi-TDM
- Root-Cause / Fix für bt-analyzer Throughput; Lab-Re-Messung in dieser Kampagne
- Attack / Offensive RF; SoftAP-Härtung als Produktclaim

## Prioritäten

1. Sheet `esp-wifi-bt-coex` (Primary **D**) + SoftAP/STA×BT-Stabilitätskarte  
2. Status-Bit- / Bluedroid-Pfad vs. deprecated `esp_coex_prefer_t`  
3. Entscheidungsrahmen: **UART HCI** (WiFi-Coex entlasten) vs. same-chip SoftAP/STA + `esp_coex_*`  
4. FOLLOW-ON Messplan (nicht Exit dieser Kampagne)
