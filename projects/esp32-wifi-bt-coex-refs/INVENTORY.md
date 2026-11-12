# Project Inventory: esp32-wifi-bt-coex-refs

```yaml
project_id: esp32-wifi-bt-coex-refs
updated: 2026-11-12
reviewed_commit: "desk-docs-2026-11-12"
profile: lab-tool
pilot_order: [esp-wifi-bt-coex]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel | Aktion |
|--------|------|--------|
| WiFi↔BT/BLE RF TDM + `esp_coex_*` | `esp-wifi-bt-coex` | **neu** |
| Classic+BLE Budgets / Init-Modi | `bt-dual-mode-coex` | **Abgrenzung** (WiFi ≠ BTDM) |
| S3 USB-OTG↔WiFi PHY | `esp32-s3-usb-wifi-coex` | **Abgrenzung** (USB ≠ RF) |
| SoftAP CONNECTED + BT = C1 | Evidence Desk | FACT Guide |
| STA Connected + BT Connected = Y | Evidence Desk | FACT Guide |
| A2DP status bits / Vendor HCI | Evidence Desk | FACT Header + #12434 |
| Historische WiFi-RX unter A2DP | Evidence Desk | FACT #1291 (historisch) |
| Systematische Public-Mess-Repos | — | **Gap** (`UNKNOWN` / absent) |
| bt-analyzer HCI_TCP ACL ~41–45 kB/s | Application Kontrast | `INFERENCE` nur dort |

Kampagne: [esp32-wifi-bt-coex-2026-foreign](../../audits/esp32-wifi-bt-coex-2026-foreign/).

## Quelle × Claim-Cluster

| Quelle | Cluster | Epistemik |
|--------|---------|-----------|
| IDF RF Coexistence Guide (ESP32) | TDM; SoftAP C1; STA+BT Y; `SW_COEXIST`; Core-Pin | `FACT` |
| `esp_coexist.h` | `A2DP_STREAMING` 0x10 / `A2DP_PAUSED` 0x20; set/clear; prefer deprecated; EXTERNAL 1/2/3 | `FACT` |
| IDF #12434 | Bluedroid setzt Streaming via Vendor HCI `BTM_ConfigCoexStatus` | `FACT` |
| IDF #1291 | prefer BT → smooth A2DP + WiFi TCP; RX ~1–5 Mbps; AMPDU reduziert | `FACT` (historisch) |
| esp-faq coexistence | TDM; BLE Scan-Window kann von WiFi gekürzt werden | `FACT` |
| Public measurement projects | `esp_coex_*` + Classic A2DP + WiFi throughput | **nicht gefunden** |

## SoftAP / STA × BT (Guide-Karte, Desk)

| WiFi-Zustand | BT aktiv | Guide-Lesart |
|--------------|----------|--------------|
| SoftAP **CONNECTED** | Classic/BLE | **C1** — instabil / problematisch |
| STA **Connected** | BT Connected | **Y** — vorgesehen / unterstützt |
| Coex-Software | — | `CONFIG_ESP_COEX_SW_COEXIST_ENABLE` erforderlich |
| Stack-Pinning | — | WiFi- und BT-Stacks auf **unterschiedliche Cores** |

## Übersicht Sheets

| Slug | Status | Coverage | Sheet | Application |
|------|--------|----------|-------|-------------|
| `esp-wifi-bt-coex` | applied | partial | [SHEET](../../technologies/esp-wifi-bt-coex/SHEET.md) | [app](applications/esp-wifi-bt-coex.md) |
| `bt-dual-mode-coex` | documented | none | [SHEET](../../technologies/bt-dual-mode-coex/SHEET.md) | Abgrenzung only |
| `esp32-s3-usb-wifi-coex` | documented | none | [SHEET](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md) | Abgrenzung only |

## Entscheidungsskizze (für Downstream)

| Option | WiFi-RF-Coex-Last | Wann sinnvoll |
|--------|------------------|---------------|
| **UART HCI** (Controller/Host getrennt, Capture/Host off-chip oder UART) | entlastet same-chip WiFi↔BT TDM | HCI_TCP über WiFi kollidiert mit Classic-Last |
| **Same-chip SoftAP/STA + `esp_coex_*`** | volle TDM-Tuning-Pflicht | WiFi und BT müssen auf einem Chip bleiben; SoftAP×BT meiden |
