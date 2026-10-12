# Project Scope: espble (Fremd)

```yaml
project_id: espble
title: EspBle — NimBLE + Classic A2DP/AVRCP CT/TG (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "56e288d"
repos:
  - https://github.com/tanakamasayuki/EspBle
status: active
```

## Zweck

Unified BLE (NimBLE) + Classic Bluedroid (namespaced) mit explizitem AVRCP CT/TG und A2DP Sink/Source — Dual-Host-Koexistenz experimental.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| EspBle BLE API | NimBLE across family | ja |
| EspBleClassic | A2DP/AVRCP/HFP/SPP/HID on original ESP32 | ja |
| S3 Classic A2DP | — | **nein** (kein BR/EDR) |
| Dual-host BLE+Classic | experimental | angrenzend |

## Nicht-Ziele

- Feld-Paarung NBT Evo als MEASURED behaupten
- Standalone-AVRCP ohne A2DP als Library-Fähigkeit behaupten

## Prioritäten

1. Sheets `bluetooth-a2dp` / `avrcp` wachsen lassen  
2. Stack-/Rollen-Kontraste dokumentieren  
3. Querverweis `esp32-bt-gateway`
