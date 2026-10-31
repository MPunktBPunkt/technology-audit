# Project Inventory: esp32.usb-analyzer

```yaml
project_id: esp32-usb-analyzer
updated: 2026-10-31
reviewed_commit: b2c9987
profile: lab-tool
pilot_order: [usb-dual-esp-observe-proxy, usb-msc, esp-usb-host, usb-aoa]
```

Desk+Lab-Audit 2026-10-31 @ `b2c9987` (FW **0.0.35**).  
Ursprungsrepo: [esp32.usb-analyzer](https://github.com/MPunktBPunkt/esp32.usb-analyzer) (read-only).  
Kampagne: [esp32-usb-analyzer-2026-pilot](../../audits/esp32-usb-analyzer-2026-pilot/).  
Method: [usb-otg-loop-baseline](../../methods/usb-otg-loop-baseline.md).  
Reuse: [docs/REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md).

**Match (Signal → Slug):**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Dual-ESP Host+Device + Debian Control / Capture | `usb-dual-esp-observe-proxy` | **neu** (Pilot) |
| MSC Device gadget + BOT class-hook | `usb-msc` | wachsen (Lab Application) |
| ESP OTG Host enum / MSC / HID / AOA Host | `esp-usb-host` | wachsen (erste Lab-MEASURED Application) |
| AOA 51→52→53 + accessory VID/PID | `usb-aoa` | wachsen (OTG-Loop Lab) |
| BCL 8-byte BE Framing über AOA-Bulk | `bmw-bcl` | wachsen — **Lab Rohr**, nicht HU-Wire |
| USB↔WiFi Datenrate Mode A | `esp32-s3-usb-wifi-coex` | Application (Bottleneck MEASURED) |
| YD-ESP32-S3 N8R2 / OTG PHY | `esp32-s3-silicon` | Application light |
| Hub register / OTA Stufe A | `esp-hub-telemetry` | Application light |
| Node Web UI / SSE | `esp-embedded-web-sse` | observed |
| HID interrupt inject/observe | — | Signal unter Host/Device Apps; kein eigener Slug |
| Debian Lab UI `:8080` | — | Teil von `usb-dual-esp-observe-proxy` (B) |

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `usb-dual-esp-observe-proxy` | Dual-ESP USB Observe/Proxy Lab | H | `lab-only`, `usb`, `esp32s3` | applied | partial | [SHEET](../../technologies/usb-dual-esp-observe-proxy/SHEET.md) | [app](applications/usb-dual-esp-observe-proxy.md) |
| `usb-msc` | USB Mass Storage Class | C | `usb-device`, `lab-only` | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |
| `esp-usb-host` | ESP32 USB Host OTG | C | `usb-host`, `esp32s3` | applied | partial | [SHEET](../../technologies/esp-usb-host/SHEET.md) | [app](applications/esp-usb-host.md) |
| `usb-aoa` | USB AOA | C | `usb-host`, `lab-only` | applied | partial | [SHEET](../../technologies/usb-aoa/SHEET.md) | [app](applications/usb-aoa.md) |
| `bmw-bcl` | BMW BCL Framing | H | `automotive`, `lab-only` | applied | partial | [SHEET](../../technologies/bmw-bcl/SHEET.md) | [app](applications/bmw-bcl.md) |
| `esp32-s3-usb-wifi-coex` | S3 USB↔WiFi Coex | D | `wifi`, `usb` | applied | partial | [SHEET](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md) | [app](applications/esp32-s3-usb-wifi-coex.md) |
| `esp32-s3-silicon` | S3 Silicon / Board | D | `esp32s3` | applied | partial | [SHEET](../../technologies/esp32-s3-silicon/SHEET.md) | [app](applications/esp32-s3-silicon.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `iobroker` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | observed | none | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | — |

## Nach Kategorie

### C — Protokolle

- `usb-msc`, `esp-usb-host`, `usb-aoa` — applied / partial (OTG-Loop MEASURED)

### D — Embedded

- `esp32-s3-usb-wifi-coex`, `esp32-s3-silicon` — applied / partial

### F / G — Integration / UI

- `esp-hub-telemetry` — applied light · `esp-embedded-web-sse` — observed

### H — Test / Analyse

- `usb-dual-esp-observe-proxy`, `bmw-bcl` (Lab-Framing only)

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Transparent MITM + Observer-effect | Gate 4 Claim nicht erfüllt | Kontroll-Host Baseline Method |
| Hard Sync µs | nur Offset-Estimate | Gate 8 weiter / REJECT hard-lock |
| L0 D+/D− | Gate 10 | Research-Track, kein Sheet-Inflation |
| HU AOA/BCL Wire | Lab ≠ Feld | hu-probe / AOA-Kampagne getrennt |
| Store-and-Forward | vor Gate 4/5 deferred | `STORE_FORWARD.md` Upstream |
| Debian Web UI Application | observed Pattern | App nur bei Transferbedarf |

## Signale ohne Eintrag

- RGB/WS2812 Identify — Board-UI, kein Slug
- Soft-composite MSC+Vendor+HID — Implementation unter Device-Apps
- Capture schema `docs/schemas/` — Teil des Observe-Proxy Sheets
