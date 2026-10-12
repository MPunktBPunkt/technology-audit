# Project Scope: esp32-a2dp-codecs (Fremd)

```yaml
project_id: esp32-a2dp-codecs
title: ESP32 A2DP Sink Multi-Codec Forks (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "cfint@bf8b482 WillyBilly06@f4eb125"
repos:
  - https://github.com/cfint/esp32-a2dp-sink
  - https://github.com/WillyBilly06/ESP32-A2DP-SINK-WITH-CODECS-UPDATED
status: active
```

## Zweck

Multi-Codec-A2DP-Sinks (AAC/aptX/LDAC/Opus/…) als **Implementation-Varianten** von `bluetooth-a2dp` — Gates PSRAM/IDF-Fork/BlueZ-Cache; AVRCP parallel observed.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| cfint/esp32-a2dp-sink | IDF 5.1.4-a2dp-codecs fork path | ja |
| WillyBilly06/…CODECS-UPDATED | IDF 5.5.2 internal-RAM path | ja |
| Stock Espressif SBC-only | Kontrast | angrenzend |
| Antennen-/Feld-Audioqualität | — | FOLLOW-ON |

## Nicht-Ziele

- Pro Codec einen Sheet-Slug
- Patched IDF als KB-Default für Gateway
