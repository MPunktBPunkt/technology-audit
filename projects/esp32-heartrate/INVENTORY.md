# Project Inventory: esp32.heartrate

```yaml
project_id: esp32-heartrate
updated: 2026-10-11
reviewed_commit: 72acae4
profile: firmware
pilot_order: [ble-hrm-gatt, ble-hr-relay, esp-embedded-web-sse, esp-hub-telemetry]
```

Desk-Audit-Lauf 2026-10-08, Nacharbeit/Re-Audit 2026-10-09; Revalidation **0.6.6** 2026-10-11 (Chip-Scope Relay, Geschwister).

Ursprungsrepo: [esp32.heartrate](https://github.com/MPunktBPunkt/esp32.heartrate) (read-only).  
Kampagne: [esp32-heartrate-2026-pilot](../../audits/esp32-heartrate-2026-pilot/) · [DELTA](../../audits/esp32-heartrate-2026-pilot/DELTA.md).  
Taxonomie: Primary A–J wie in [`docs/TAXONOMY.md`](../../docs/TAXONOMY.md).

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| BLE HR Central / Polar H9 | `ble-hrm-gatt` | Sheet + App |
| Dual-Role Relay | `ble-hr-relay` | **Chip-Scope S3**; Classic Mini unsupported |
| REST + SSE WebUI | `esp-embedded-web-sse` | Sheet + App |
| Hub Heartbeat / OTA | `esp-hub-telemetry` | Sheet + App (HTTP-A) |
| RR/Session/LittleFS | observed | kein Sheet ohne Transferbedarf (G19) |
| Geschwister ergo / ftmsprobe | dieselben Slugs | wachsen, keine Forks |

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `ble-hrm-gatt` | BLE Heart Rate GATT (Central) | C | `esp-idf`, `streaming` | applied | partial | [SHEET](../../technologies/ble-hrm-gatt/SHEET.md) | [app](applications/ble-hrm-gatt.md) |
| `ble-hr-relay` | BLE HR-Relay (Peripheral) | C | `esp-idf`, `streaming` | applied | partial | [SHEET](../../technologies/ble-hr-relay/SHEET.md) | [app](applications/ble-hr-relay.md) |
| `esp-embedded-web-sse` | Embedded Web REST + SSE | G | `streaming` | applied | partial | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | [app](applications/esp-embedded-web-sse.md) |
| `esp-hub-telemetry` | ESP-Hub Heartbeat / OTA / Export | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `esp32-arduino-pio` | ESP32 + PlatformIO Arduino | D | `esp-idf` | observed | none | — | — |
| `wifi-manager-captive` | WiFiManager Captive Portal | F | — | observed | none | — | — |
| `nvs-config-store` | NVS ConfigStore | E | — | observed | none | — | — |
| `littlefs-session-archive` | LittleFS Session-Archiv | E | — | observed | none | — | — |
| `rr-quality-pipeline` | RR / BeatTimeline / Quality | D | `streaming` | observed | none | — | — |
| `web-ota` | Web- und Hub-OTA | F | — | observed | none | — | — |
| `mdns-discovery` | mDNS `hr-*.local` | F | — | observed | none | — | — |
| `github-actions-pio` | GitHub Actions PlatformIO-Matrix | H | — | observed | none | — | — |

Legende Status: `candidate` · `observed` · `documented` · `applied` · `transferred`  
Legende Coverage: `none` · `partial` · `full`

## Nach Kategorie

### A — Empfang

—

### B — Audio

—

### C — Protokolle

`ble-hrm-gatt`, `ble-hr-relay`

### D — Embedded

`esp32-arduino-pio`, `rr-quality-pipeline`

### E — Speicher / Formate

`nvs-config-store`, `littlefs-session-archive`

### F — Systemintegration

`esp-hub-telemetry`, `wifi-manager-captive`, `web-ota`, `mdns-discovery`

### G — Steuerung / UI

`esp-embedded-web-sse`

### H — Test / Analyse

`github-actions-pio`

### I — Fahrzeug / Geräte

—

### J — Architektur

noch kein eigener Slug (Session/Producer-Consumer in Applications)

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| `ble-hrm-gatt` | Lab/README Polar H9; keine Evidence-Rohlogs im Repo | Feldnotiz + Continuity-KPIs vs. PFLICHTENHEFT |
| `ble-hr-relay` | Abnahmekriterien 1–15 dokumentiert, nicht als PASS protokolliert | Lab-Lauf nRF Connect + zweiter Consumer (S3) |
| Classic dual-role | S3-Evidence nicht übertragbar | Gate / eigene Messung — kein Sheet-Ausweiten |
| `esp-hub-telemetry` | Schnittstelle beschrieben; Hub-Repo out of scope | Sample-Heartbeat gegen laufenden Hub |
| observed-only Slugs | kein Sheet-Priorität im Pilot | Sheets bei Transferbedarf + Gate (G19) |

## Signale ohne Eintrag

- Soft-Auto Session-Modi (Rest/Alltag/Training/Recovery) — vorerst unter `rr-quality-pipeline` / Web-UI belassen
- HistoryStore Ringbuffer — Teil von `rr-quality-pipeline`
