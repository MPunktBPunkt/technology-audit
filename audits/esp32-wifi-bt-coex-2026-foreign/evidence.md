# Evidence — esp32-wifi-bt-coex-2026-foreign

Desk 2026-11-12 · **standard_version 0.7.1** · Profile `lab-tool` · keine
Builds, keine RF-/Throughput-Remessung, keine Root-Cause für bt-analyzer HCI_TCP.

## Quellen-Snapshots

| Repository / Artefakt | Pin / Desk | Vertiefter Pfad | Hinweis |
|----------------------|------------|-----------------|---------|
| ESP-IDF RF Coexistence Guide (ESP32) | docs desk 2026-11-12 | TDM WiFi/BT/BLE; SoftAP/STA×BT-Matrix; `SW_COEXIST`; Core-Pin | Primary D |
| esp-idf `esp_coexist.h` | IDF header symbols desk | `ESP_COEX_BT_ST_A2DP_STREAMING` 0x10; `A2DP_PAUSED` 0x20; set/clear; prefer deprecated; EXTERNAL 1/2/3 | Apache-2.0 |
| https://github.com/espressif/esp-idf/issues/12434 | `#12434` | Bluedroid Vendor HCI `BTM_ConfigCoexStatus` | A2DP streaming status |
| https://github.com/espressif/esp-idf/issues/1291 | `#1291` (historisch) | prefer BT; WiFi RX ~1–5 Mbps; AMPDU ↓ under coex | historisch |
| Espressif FAQ coexistence | FAQ page desk | TDM; BLE scan window truncated by WiFi | Abgrenzung zu USB-Coex |
| Public measurement projects | Search desk | `esp_coex_*` + Classic A2DP + WiFi throughput | **nicht gefunden** |
| esp32-bt-analyzer (Lokal, Kontrast) | STATUS HCI_TCP / 62-vs-37 | ~41–45 kB/s ACL | **nicht** Desk-Messung |

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-WBTCOEX-2026-11-12-001` | ESP32 RF Coex: WiFi/BT/BLE teilen RF per **TDM**-Slices. | `FACT` | IDF RF Coexistence Guide (ESP32) |
| `EVID-WBTCOEX-2026-11-12-002` | SoftAP **CONNECTED** + BT = Guide-Stufe **C1** (instabil / problematisch). | `FACT` | IDF Guide Matrix |
| `EVID-WBTCOEX-2026-11-12-003` | STA **Connected** + BT Connected = Guide **Y** (vorgesehen). | `FACT` | IDF Guide Matrix |
| `EVID-WBTCOEX-2026-11-12-004` | `CONFIG_ESP_COEX_SW_COEXIST_ENABLE` ist für Software-Coexistence erforderlich. | `FACT` | IDF Guide / Kconfig |
| `EVID-WBTCOEX-2026-11-12-005` | WiFi- und BT-Stacks auf **unterschiedliche Cores** pinnen (Guide-Empfehlung). | `FACT` | IDF Guide |
| `EVID-WBTCOEX-2026-11-12-006` | `ESP_COEX_BT_ST_A2DP_STREAMING` = 0x10; `ESP_COEX_BT_ST_A2DP_PAUSED` = 0x20; `esp_coex_status_bit_set` / `clear`. | `FACT` | `esp_coexist.h` |
| `EVID-WBTCOEX-2026-11-12-007` | `esp_coex_prefer_t` / Prefer-API ist **DEPRECATED** zugunsten von Status-Bits. | `FACT` | `esp_coexist.h` |
| `EVID-WBTCOEX-2026-11-12-008` | EXTERNAL Coex: Wire **1/2/3** ≈ request / priority / grant (PTA-ähnlich). | `FACT` | `esp_coexist.h` / Guide EXTERNAL |
| `EVID-WBTCOEX-2026-11-12-009` | Bluedroid setzt A2DP-Streaming-Coex-Status via Vendor HCI `BTM_ConfigCoexStatus` (#12434); keine Public-Messprojekt-Beispiele im Issue-Kontext. | `FACT` | IDF #12434 |
| `EVID-WBTCOEX-2026-11-12-010` | Historisch (#1291): prefer BT → A2DP smooth + WiFi TCP; WiFi RX ~**1–5 Mbps** bei smooth A2DP unter `SW_COEXIST`; AMPDU unter Coex reduziert. | `FACT` (historisch) | IDF #1291 |
| `EVID-WBTCOEX-2026-11-12-011` | FAQ: Coex ist TDM; **BLE Scan-Window** kann durch WiFi verkürzt werden. | `FACT` | Espressif FAQ coexistence |
| `EVID-WBTCOEX-2026-11-12-012` | Keine öffentlichen Repos gefunden, die systematisch `esp_coex_*` + Classic A2DP + WiFi-Throughput messen — **Gap bleibt**. | `FACT` (Absence) | Desk-Suche 2026-11-12 |

## SoftAP / STA × BT (Desk-Karte)

| WiFi | BT | Guide | Evidence |
|------|----|-------|----------|
| SoftAP CONNECTED | aktiv | **C1** | `002` |
| STA Connected | BT Connected | **Y** | `003` |
| SW Coex enable | — | Pflicht | `004` |
| Core-Pin WiFi ≠ BT | — | empfohlen | `005` |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| USB↔WiFi-Sheet erklärt RF WiFi↔BT | `REJECTED` | andere Domäne (`esp32-s3-usb-wifi-coex`) |
| BTDM-Sheet ersetzt WiFi-TDM | `REJECTED` | Classic+BLE ≠ WiFi (`bt-dual-mode-coex`) |
| Prefer-API aktuell empfehlen | `REJECTED` | `007` DEPRECATED |
| #1291 Mbps = aktueller Universal-SoT | `REJECTED` | historisch; Release-abhängig |
| bt-analyzer ~41–45 kB/s ACL als Fremd-Desk-`MEASURED` | `REJECTED` | nur Projekt-STATUS; Application darf `INFERENCE` |
| SoftAP×BT „stabil laut Guide“ | `REJECTED` | C1 |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Lab: SoftAP×BT vs STA×BT unter HCI_TCP ACL-Last | `UNKNOWN` | FOLLOW-ON |
| UART HCI vs getuntes STA+`esp_coex_*` Dominanz | `HYPOTHESIS` | Key Decision; Lab |
| Aktuelle IDF A2DP+WiFi Mbps | `UNKNOWN` | #1291 nicht ersetzen |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-11-12 | Fremd-Desk WiFi↔BT Coex; Gap HCI_TCP; Sheet `esp-wifi-bt-coex` |
