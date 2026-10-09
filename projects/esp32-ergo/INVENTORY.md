# Project Inventory: esp32.ergo

```yaml
project_id: esp32-ergo
updated: 2026-10-09
reviewed_commit: edaeb19
pilot_order: [bluetooth-ftms, hammer-varon-xtr, ble-hrm-gatt, esp-embedded-web-sse, esp-hub-telemetry]
```

Desk-Audit 2026-10-09 gegen `edaeb19`.  
Ursprungsrepo: [esp32.ergo](https://github.com/MPunktBPunkt/esp32.ergo) (read-only).  
Kampagne: [esp32-ergo-2026-pilot](../../audits/esp32-ergo-2026-pilot/).  
Taxonomie: [`docs/TAXONOMY.md`](../../docs/TAXONOMY.md).

**Wissenswachstum:** Slugs `ble-hrm-gatt`, `ble-hr-relay`, `esp-hub-telemetry`, `esp-embedded-web-sse` existierten aus `esp32-heartrate` — Sheets erweitert (`seen_in`, Fallstricke), **keine** Forks.

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `bluetooth-ftms` | Bluetooth FTMS | C | `esp-idf`, `streaming` | applied | partial | [SHEET](../../technologies/bluetooth-ftms/SHEET.md) | [app](applications/bluetooth-ftms.md) |
| `hammer-varon-xtr` | Hammer Varon XTR II | I | `field-verified` | applied | partial | [SHEET](../../technologies/hammer-varon-xtr/SHEET.md) | [app](applications/hammer-varon-xtr.md) |
| `ble-hrm-gatt` | BLE Heart Rate GATT | C | `esp-idf`, `streaming` | applied | partial | [SHEET](../../technologies/ble-hrm-gatt/SHEET.md) | [app](applications/ble-hrm-gatt.md) |
| `ble-hr-relay` | BLE HR-Relay | C | `esp-idf`, `streaming` | applied | partial | [SHEET](../../technologies/ble-hr-relay/SHEET.md) | [app](applications/ble-hr-relay.md) |
| `esp-embedded-web-sse` | Embedded Web REST + SSE | G | `streaming` | applied | partial | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | [app](applications/esp-embedded-web-sse.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `esp32-arduino-pio` | ESP32-S3 + PlatformIO | D | `esp-idf` | observed | none | — | — |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |
| `nvs-config-store` | NVS ConfigStore | E | — | observed | none | — | — |
| `session-archive` | SessionStore / Archiv | E | — | observed | none | — | — |
| `ftms-erg-control` | ERG/Limiter/PowerMap | D | `streaming` | observed | none | — | — |
| `github-actions-pio` | CI PlatformIO + native tests | H | — | observed | none | — | — |

Legende Status: `candidate` · `observed` · `documented` · `applied` · `transferred`  
Legende Coverage: `none` · `partial` · `full`

## Nach Kategorie

### C — Protokolle

`bluetooth-ftms`, `ble-hrm-gatt`, `ble-hr-relay`

### D — Embedded

`esp32-arduino-pio`, `ftms-erg-control`

### E — Speicher

`nvs-config-store`, `session-archive`

### F — Systemintegration

`esp-hub-telemetry`, `wifi-manager-captive`

### G — Steuerung / UI

`esp-embedded-web-sse`

### H — Test / Analyse

`github-actions-pio`

### I — Fahrzeug / Geräte

`hammer-varon-xtr`

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| `bluetooth-ftms` Bridge | MyWhoosh-Abnahme laut STATE offen | Lab-PASS + Evidence-IDs |
| `hammer-varon-xtr` | Nachtest 6 (Crash unter Last) offen | Feldnotiz |
| `ftms-erg-control` | nur observed | eigenes Sheet wenn Transferbedarf |
| shared Hub/Web | IO-Keys ergo vs heartrate | Schema-Abgleich im Hub-Repo |

## Signale ohne Eintrag

- ZWO-Import / WorkoutEngine — vorerst unter `ftms-erg-control`
- CPS/CSC Peripheral neben FTMS Bridge — bei Bedarf eigener Slug
