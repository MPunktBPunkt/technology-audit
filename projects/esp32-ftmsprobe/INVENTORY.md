# Project Inventory: esp32.ftmsprobe

```yaml
project_id: esp32-ftmsprobe
updated: 2026-10-09
reviewed_commit: 70c3c25
pilot_order: [ble-http-gatt-probe, bluetooth-ftms, hammer-varon-xtr, esp-hub-telemetry]
```

Desk-Audit 2026-10-09 @ `70c3c25`.  
Ursprungsrepo: [esp32.ftmsprobe](https://github.com/MPunktBPunkt/esp32.ftmsprobe) (read-only).  
Kampagne: [esp32-ftmsprobe-2026-pilot](../../audits/esp32-ftmsprobe-2026-pilot/).  
Method: [ftms-capability-probe](../../methods/ftms-capability-probe.md).  
Reuse: [docs/REUSE.md](../../docs/REUSE.md).

**Match (Signal → Slug):** HTTP-GATT-Sonde → **neu** `ble-http-gatt-probe`; FTMS Caps/Wirkung → `bluetooth-ftms`; Varon-Lauf → `hammer-varon-xtr`; Hub/OTA/WiFi/SSE/HR → bestehende Slugs.

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `ble-http-gatt-probe` | HTTP BLE-GATT-Sonde | H | `esp-idf`, `lab-only` | applied | partial | [SHEET](../../technologies/ble-http-gatt-probe/SHEET.md) | [app](applications/ble-http-gatt-probe.md) |
| `bluetooth-ftms` | Bluetooth FTMS | C | `esp-idf`, `streaming` | applied | partial | [SHEET](../../technologies/bluetooth-ftms/SHEET.md) | [app](applications/bluetooth-ftms.md) |
| `hammer-varon-xtr` | Hammer Varon XTR II | I | `field-verified`, `lab-only` | applied | partial | [SHEET](../../technologies/hammer-varon-xtr/SHEET.md) | [app](applications/hammer-varon-xtr.md) |
| `ble-hrm-gatt` | BLE HR GATT | C | `esp-idf` | applied | partial | [SHEET](../../technologies/ble-hrm-gatt/SHEET.md) | [app](applications/ble-hrm-gatt.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | observed | none | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | — |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |
| `esp32-arduino-pio` | PlatformIO ESP32 | D | `esp-idf` | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Web/SSE | observed, UI lab-only | Application wenn Transferbedarf |
| Codec `tools/ftms.py` | Referenz für Ergo | in FTMS-Application verlinken |
| Weitere Bikes | nur Varon belegt | Method erneut fahren |

## Signale ohne Eintrag

- ProbeGuard Deadman — Teil von `ble-http-gatt-probe`
- `ble-host-precheck.sh` — Host-BlueZ-Check, Method-Hinweis
