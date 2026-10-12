# Project Scope: esp-sdr-bridge (Fremd)

```yaml
project_id: esp-sdr-bridge
title: esp-sdr-bridge — IQS USB → SpyServer/rtl_tcp (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "7da8aea"
repos:
  - https://github.com/z2labs/esp-sdr-bridge
status: active
```

## Zweck

Host-Bridge für ESP-SDR **IQS**-Stream auf S3: USB Serial/JTAG → SpyServer + rtl_tcp. Vertieft `esp32-undoc-iq-rx` um kontinuierlichen FIR/DDC-Pfad und Host-Backend-Muster (G7).

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| z2labs/esp-sdr-bridge | Python Host Bridge | ja (Desk) |
| ESP-SDR `s3-iq-stream` / PR#4 | Firmware IQS | angrenzend (Evidence via Docs) |
| TX / Tone / Polar | — | **nein** |
| Eigene Remessung | — | FOLLOW-ON (Upstream MEASUREMENTS = INFERRED) |

## Nicht-Ziele

- Author-SNR als KB-`MEASURED` ohne Remessung
- Burst-only ESP32SDR mit IQS vermengen

## Prioritäten

1. Application auf `esp32-undoc-iq-rx`  
2. IQS1 Framing / Rates / USB-Bandwidth-Limits  
3. SpyServer vs rtl_tcp als laterale Backends
