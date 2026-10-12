# Project Scope: a2dpsinkhfpclient (Fremd)

```yaml
project_id: a2dpsinkhfpclient
title: a2dpSinkHfpClient — A2DP Sink + HFP + AVRC (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "db7ff2f"
repos:
  - https://github.com/walinsky/a2dpSinkHfpClient
status: active
```

## Zweck

Kompakte ESP-IDF-Component: A2DP Sink + HFP HF + explizite AVRC-API (play/pause/next/prev + Metadata-Struct) — Vergleich zu reinem A2DP+AVRCP.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| a2dpSinkHfpClient component | IDF ≥5.5 Classic audio+HF | ja |
| PBAP phonebook | side feature | observed |
| A2DP Source / Gateway-Rolle | — | **nein** |

## Nicht-Ziele

- Feld-Paarung NBT Evo als MEASURED behaupten
- Standalone-AVRCP ohne A2DP als Library-Fähigkeit behaupten

## Prioritäten

1. Sheets `bluetooth-a2dp` / `avrcp` wachsen lassen  
2. Stack-/Rollen-Kontraste dokumentieren  
3. Querverweis `esp32-bt-gateway`
