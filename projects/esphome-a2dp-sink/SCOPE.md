# Project Scope: esphome-a2dp-sink (Fremd)

```yaml
project_id: esphome-a2dp-sink
title: PxPert a2dp_sink — ESPHome A2DP Sink Component (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "4e6ab38"
repos:
  - https://github.com/PxPert/a2dp_sink
status: active
```

## Zweck

ESPHome-Custom-Component: A2DP Sink + Metadata/Volume/AVRCP-State als Entities — Integrationsmuster, nicht Gateway-Stack.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| PxPert/a2dp_sink | ESPHome hub/sensors/media_source | ja |
| Underlying pschatzmann stack note | Kontrast | angrenzend |
| S3 Classic A2DP | — | **nein** (README) |
