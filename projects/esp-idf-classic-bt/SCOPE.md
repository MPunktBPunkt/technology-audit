# Project Scope: esp-idf-classic-bt (Fremd)

```yaml
project_id: esp-idf-classic-bt
title: ESP-IDF classic_bt — Official A2DP/AVRCP Examples (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "86f72d0"
repos:
  - https://github.com/espressif/esp-idf
status: active
```

## Zweck

Vendor-SoT für Bluedroid Classic: a2dp_sink_stream*, avrcp_ct_metadata, avrcp_ct_cover_art (1.6), avrcp_absolute_volume — Targets ESP32 (+ S31 Flag).

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| examples/.../classic_bt/avrcp_* | CT metadata, cover art, abs volume | ja |
| examples/.../a2dp_sink_stream* | A2DP Sink (+AAC variants) | ja |
| a2dp_source* | Source examples | angrenzend |
| Volles IDF außerhalb classic_bt | — | **nein** |

## Nicht-Ziele

- Feld-Paarung NBT Evo als MEASURED behaupten
- Standalone-AVRCP ohne A2DP als Library-Fähigkeit behaupten

## Prioritäten

1. Sheets `bluetooth-a2dp` / `avrcp` wachsen lassen  
2. Stack-/Rollen-Kontraste dokumentieren  
3. Querverweis `esp32-bt-gateway`
