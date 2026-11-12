# Project Application: esp-wifi-bt-coex in esp32-wifi-bt-coex-refs

```yaml
project_id: esp32-wifi-bt-coex-refs
tech_slug: esp-wifi-bt-coex
status: active
sheet: ../../../technologies/esp-wifi-bt-coex/SHEET.md
audit: ../../../audits/esp32-wifi-bt-coex-2026-foreign/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

Desk-Pin der **WiFi↔Classic-BT RF-Coex-Karte** für Downstream-Projekte, die auf einem
ESP32 gleichzeitig **WiFi-TCP** und **Classic/BLE-Controller** brauchen — insbesondere
als Wissenslücke hinter `esp32-bt-analyzer` **HCI_TCP**.

Dieses Fremd-Audit **misst nicht**. Eigenlab-Zahlen gehören nur als Kontrast hierher.

## Architektur / Datenfluss (Zielbild)

```text
[2.4 GHz RF] ──TDM (esp_coex_*)──┬── WiFi STA/SoftAP ── lwIP/TCP ──► Host (z.B. HCI_TCP)
                                 └── Classic/BLE Controller ── VHCI/Host ──► Capture/Stack

Alternative: UART HCI ──► Host (WiFi-Pfad entlastet same-chip Coex)
```

## Relevante Pfade (Upstream-Docs / IDF)

| Pfad / Artefakt | Rolle |
|-----------------|-------|
| IDF `api-guides/coexist` (ESP32) | TDM; SoftAP/STA×BT-Matrix; Core-Pin; `SW_COEXIST` |
| `components/esp_coex/.../esp_coexist.h` | Status-Bits A2DP; prefer deprecated; EXTERNAL |
| IDF Issues #12434, #1291 | Bluedroid Vendor HCI; historische Throughput-Hinweis |
| esp-faq coexistence | TDM; BLE Scan-Window Truncation |

## Konfiguration und Parameter

| Parameter | Desk-Lesart | Status |
|-----------|-------------|--------|
| `CONFIG_ESP_COEX_SW_COEXIST_ENABLE` | Pflicht für SW-Coex | `FACT` |
| SoftAP CONNECTED + BT | Guide **C1** (instabil) | `FACT` |
| STA Connected + BT Connected | Guide **Y** | `FACT` |
| WiFi-/BT-Task Core-Pin | unterschiedliche Cores | `FACT` (Guide) |
| `ESP_COEX_BT_ST_A2DP_STREAMING` 0x10 / `A2DP_PAUSED` 0x20 | Status-Bits set/clear | `FACT` |
| `esp_coex_prefer_t` | **DEPRECATED** → Status-Bits | `FACT` |
| EXTERNAL coex wires 1/2/3 | PTA-ähnlich request/priority/grant | `FACT` |
| Bluedroid A2DP → Vendor HCI `BTM_ConfigCoexStatus` | #12434 | `FACT` |
| Public Mess-Repos Coex+A2DP+WiFi thr. | — | **Gap** / absent |

## Ebene C — Projekt-Kontrast (nicht Fremd-Desk-Messung)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Guide SoftAP×BT = C1; STA×BT = Y | `EVID-WBTCOEX-2026-11-12-002`/`003` | `FACT` (Desk) |
| Kein Public-Repo systematisch Coex+A2DP+WiFi thr. | `EVID-WBTCOEX-2026-11-12-012` | `FACT` (Gap) |
| bt-analyzer: HCI_TCP ACL ~41–45 kB/s / 62-vs-37 Gate | Projekt-[STATUS](../../esp32-bt-analyzer/STATUS.md) | `MEASURED` **nur dort** |
| WiFi+BT controller-only ist der Bottleneck für HCI_TCP | Ableitung aus Lab-Kontrast + Desk-Karte | `INFERENCE` (Application) — **nicht** Fremd-Audit-FACT |

## Abweichungen vom „Lehrbuch“

- Historisches #1291 (prefer BT, ~1–5 Mbps WiFi RX) ist **Orientierung**, kein aktueller
  Throughput-SoT für jedes IDF-Release.
- SoftAP als HCI_TCP-AP + Classic gleichzeitig widerspricht der Guide-C1-Lesart —
  Downstream sollte STA bevorzugen oder UART-HCI erwägen.

## Offene Fragen

- Lab: HCI_TCP ACL-kB/s unter STA+BT vs SoftAP+BT (C1-Diskriminator)?
- Reicht Status-Bit-Tuning, oder ist UART-HCI die robustere Architektur?

## Verwandte Applications / Methods

- Abgrenzung: [`esp32-s3-usb-wifi-coex`](../../../technologies/esp32-s3-usb-wifi-coex/SHEET.md)
- Abgrenzung: [`bt-dual-mode-coex`](../../../technologies/bt-dual-mode-coex/SHEET.md)
- Kontrast-Projekt: [`esp32-bt-analyzer`](../../esp32-bt-analyzer/)
