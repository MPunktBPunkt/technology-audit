# Project Inventory: esp32.ftmsprobe

```yaml
project_id: esp32-ftmsprobe
updated: 2026-10-11
reviewed_commit: 70c3c25
profile: lab-tool
pilot_order: [ble-http-gatt-probe, bluetooth-ftms, hammer-varon-xtr, esp-hub-telemetry]
```

Desk-Audit 2026-10-09 @ `70c3c25`; Revalidation **0.6.6** 2026-10-11.  
Ursprungsrepo: [esp32.ftmsprobe](https://github.com/MPunktBPunkt/esp32.ftmsprobe) (read-only).  
Kampagne: [esp32-ftmsprobe-2026-pilot](../../audits/esp32-ftmsprobe-2026-pilot/) · [DELTA](../../audits/esp32-ftmsprobe-2026-pilot/DELTA.md).  
Method: [ftms-capability-probe](../../methods/ftms-capability-probe.md).  
Reuse: [docs/REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md).

**Match (Signal → Slug):**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| HTTP-GATT-Sonde | `ble-http-gatt-probe` | neu (Pilot) |
| FTMS Caps/Wirkung | `bluetooth-ftms` | wachsen |
| Varon-Lauf | `hammer-varon-xtr` | wachsen (Host) |
| Dual-Env probe / probe-s3 | — | Chip-/Build-Scope in Apps |
| Hub/OTA/HR | bestehende Slugs | Applications |
| Web/SSE Sonde | `esp-embedded-web-sse` | observed (kein App-Zwang) |

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
| Weitere Bikes | nur Varon belegt | Method erneut fahren (kein Sheet-Ausweiten) |
| Dual-Link Classic vs S3 | Budget dokumentiert, Env-Parität offen | pro Env belegen (G17) |

## Signale ohne Eintrag

- ProbeGuard Deadman — Teil von `ble-http-gatt-probe`
- `ble-host-precheck.sh` — Host-BlueZ-Check, Method-Hinweis
