# Project Inventory: esp32.bt-gateway

```yaml
project_id: esp32-bt-gateway
updated: 2026-10-09
reviewed_commit: 7a7e8a4
profile: planning
pilot_order: [bluetooth-a2dp, avrcp, pdap, esp-hub-telemetry, bmw-nbt-evo]
```

**Profil:** `planning` ([AUDIT-PROFILES](../../docs/AUDIT-PROFILES.md)) — keine Firmware; Status bewusst ≤ `documented`.

**Reuse / Match:**

| Signal (Planung) | Slug | Aktion |
|------------------|------|--------|
| A2DP Source | `bluetooth-a2dp` | Sheet neu (Spec/Muster) |
| AVRCP Target / Browse | `avrcp` | Sheet neu (war PiDrive-Kandidat) |
| PDAP PCM+Control | `pdap` | Sheet neu (Muster) |
| ESP-Hub OTA/Register | `esp-hub-telemetry` | **gewachsen** (IDF-Client, einmalige otaUrl) |
| BMW NBT als Sink/Controller | `bmw-nbt-evo` | `seen_in` + Design-App |
| ESP-IDF / Classic ESP32 | `esp32` | observed, noch kein Sheet-Zwang |

Ursprungsrepo: [esp32.bt-gateway](https://github.com/MPunktBPunkt/esp32.bt-gateway).  
Kampagne: [esp32-bt-gateway-2026-planning](../../audits/esp32-bt-gateway-2026-planning/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `bluetooth-a2dp` | Bluetooth A2DP | C | `bluetooth-classic`, `streaming` | documented | none | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | [app](applications/bluetooth-a2dp.md) |
| `avrcp` | AVRCP | C | `bluetooth-classic`, `metadata` | documented | none | [SHEET](../../technologies/avrcp/SHEET.md) | [app](applications/avrcp.md) |
| `pdap` | PDAP WiFi PCM/Control | J | `streaming` | documented | none | [SHEET](../../technologies/pdap/SHEET.md) | [app](applications/pdap.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | documented | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `bmw-nbt-evo` | BMW NBT Evo Host | I | `automotive`, `field-verified` | documented | none | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | [app](applications/bmw-nbt-evo.md) |
| `esp32-idf-classic` | ESP32 Classic + IDF | D | `esp-idf` | observed | none | — | — |
| `wifi-bt-coex` | WiFi + Classic-BT Coexistence | F | — | candidate | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| A17 Host-Stack | Entscheidung offen | OFFENE-PUNKTE / Phase −1 |
| Phase −1 Browsing/Meta | ungemessen | PHASE-0-MESSPLAN |
| Flash-Budget | Q12 Build-Host fehlt | FLASH-BUDGET.md Messung |
| Coexistence | Gate nach Stack | BETRIEBSMODI |

## Signale ohne Eintrag

- Pairing-WebUI — Teil Hub/Betriebsmodi
- PiDrive-Depot lokales OTA — Application Hub Stufe 2
