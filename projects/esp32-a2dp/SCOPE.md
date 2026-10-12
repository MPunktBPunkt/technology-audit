# Project Scope: esp32-a2dp (Fremd)

```yaml
project_id: esp32-a2dp
title: ESP32-A2DP — Classic A2DP/AVRCP Library (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "a9e946a"
repos:
  - https://github.com/pschatzmann/ESP32-A2DP
status: active
```

## Zweck

Referenz-Implementierung für **ESP Classic Bluetooth A2DP Sink/Source + AVRCP** (Bluedroid) in die KB ziehen — Kontrast zu Pi BlueZ/PipeWire und direkte Vorarbeit für `esp32-bt-gateway`.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| pschatzmann/ESP32-A2DP | Arduino/IDF-Library Sink+Source+AVRCP | ja (Desk) |
| AudioTools / Legacy I2S | Output-Backend | angrenzend |
| ESP32-S3/C3 BLE-only | — | **nein** (Gate: kein Classic BR/EDR) |
| Feld-Paarung NBT Evo | — | FOLLOW-ON / Gateway |

## Nicht-Ziele

- HFP/HSP oder standalone AVRCP ohne A2DP als belegt behaupten (Upstream: nicht supported)
- Pi-BlueZ-Evidence still auf ESP übertragen
- AAC/Multi-Codec ohne IDF-Versionsgate als universell behaupten

## Prioritäten

1. Sheets `bluetooth-a2dp` / `avrcp` um ESP-Bluedroid-Contracts wachsen lassen  
2. Chip-Scope: Classic ESP32 (+ Upstream-Flag ESP32-S31) vs. S3-REJECTED  
3. Source vs. Sink als getrennte Rollen in Applications  
4. Querverweis Gateway-Planung
