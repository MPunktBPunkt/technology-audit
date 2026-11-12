# Project Application: esp-wifi-bt-coex in esp32-bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: esp-wifi-bt-coex
status: active
sheet: ../../../technologies/esp-wifi-bt-coex/SHEET.md
upstream: https://github.com/MPunktBPunkt/esp32.bt-analyzer
upstream_fw: ["0.3.17", "0.3.18", "0.3.19"]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R2   # lab MEASURED on real D1 Mini ESP32 (HCI agent); coex API 0.3.19 effect UNKNOWN
  reusability: W2
```

## Rolle im Projekt

D1 Mini ESP32 als **reiner Controller** (`hci-agent-esp32`): VHCI ↔ WiFi TCP `:9754` ↔
Linux `/dev/vhci` ↔ BlueZ. WiFi STA und Classic BR/EDR laufen gleichzeitig auf einem
Radio; der Host-Stack (BlueZ) sitzt **nicht** auf dem Chip. Damit fehlt dem
ESP-Coex-Scheduler jede Profil-Information (A2DP-Streaming etc.).

## Architektur / Datenfluss

```text
Phone ─BR/EDR─ ESP32 controller ═ coex ═ WiFi STA ─TCP :9754─ hci_tcp_bridge.py → /dev/vhci → BlueZ (.108)
```

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `firmware/analyzer-node/src/agent/HciTcpAgent.cpp` | `/api/hci/wifi_ps`, `/api/hci/coex` (0.3.19) |
| `tools/lab_hci_tcp_62_37_gate.py` | sustained vs peak ACL (ESP↔ESP l2test 672 B) |
| `tools/lab_hci_coex_ab.py` | A/B per coex mode (0.3.19) |
| `docs/evidence/LAB_HCI_TCP_WIFI_PS_SWEEP_*` | wifi_ps sweeps (repeater / router) |
| `docs/evidence/LAB_HCI_TCP_62_37_GATE_20261112T061010Z.*` | PASS_37 |

## Ebene C — Evidence

| Claim | Evidence | Status |
|-------|----------|--------|
| Sustained ACL `wifi_ps=min`/`max` ≈ 3–4 kB/s per ESP | `LAB_HCI_TCP_WIFI_PS_SWEEP_20261111T202605Z`, `…_ROUTER_20261111T221956Z` | `MEASURED` |
| Sustained ACL `wifi_ps=none` ≈ 36–45 kB/s per ESP | same + `LAB_HCI_TCP_62_37_GATE_20261112T061010Z` | `MEASURED` |
| Better WiFi RSSI (−45 vs −85 dBm) raises BT ACL | router vs repeater sweep | `REJECTED` (coex-bound, not backhaul) |
| Larger controller→host ring raises rate | ringPeak ≤ ~19 % of 24 KiB, drops 0 | `REJECTED` |
| Classic page/ACL bring-up flaky under `none` cold | sweeps T2/T3 | `MEASURED`; recipe: connect under `min`, then `none` |
| `min` after a `none` session re-throttles immediately | T5 sticky | `REJECTED` (label ≠ duty cycle until radio reset) |
| ~62 kB/s sustained | 62/37 gate | `REJECTED` (short-window artefact) |
| BlueZ-hosted A2DP sets ESP coex A2DP status | design | `REJECTED` — only an on-chip host (Bluedroid) does |
| `ESP_COEX_BT_ST_A2DP_STREAMING` / `PREFER_BT` raise sustained ACL | `lab_hci_coex_ab.py` pending | `UNKNOWN` |

## Transfer

- Bei jedem „ESP als Remote-Controller“-Aufbau (HCI über WiFi) zuerst das Coex-Budget
  messen; es begrenzt jede Classic-Nutzlast (A2DP SBC bitpool 53 ≈ 42 kB/s ≈ Budget).
- `esp_coex_preference_set` ist in ESP-IDF 5.x deprecated; Nachfolger
  `esp_coex_status_bit_set()` (IDF 5.5 `esp_coexist.h`, `FACT` Header).
- Laut Desk [`esp32-wifi-bt-coex-2026-foreign`](../../../audits/esp32-wifi-bt-coex-2026-foreign/)
  gibt es keine öffentlichen Durchsatz-Messprojekte; diese Sweeps sind die beste
  verfügbare Evidenz. Ausweg ohne Coex: UART-HCI
  ([`esp-hci-uart-controller`](../../../technologies/esp-hci-uart-controller/SHEET.md)).

## Epistemik

```text
YES:  ESP↔ESP ACL über HCI TCP, Agent-Zähler, wifi_ps-Varianten, zwei APs
NO:   Air-Capture; Bluedroid-on-chip Coex (anderer Host); Wirkung der Coex-API (noch nicht gemessen)
```
