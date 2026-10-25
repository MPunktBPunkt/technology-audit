# Project Scope: esp-ble-finder (Fremd)

```yaml
project_id: esp-ble-finder
title: ESP BLE Finder — RSSI Proximity Hunt (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "1a588119bb8d21a5aa939b6e0601585bcf448431"
repos:
  - https://github.com/khlebobul/esp_ble_finder
status: active
```

## Zweck

Fremdrepo: **BLE Advertisement Scan → RSSI-Proximity-Hunt** (findphone-Muster) mit UI-Bands, Sparkline und Clicker. Abgrenzung zu RF-Environment-Monitor und zu Ride-BLE-Display/GATT-Profiles.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| NimBLE Adv Scan + proximity mapping | Hunt | ja |
| LVGL UI + speaker clicker | Feedback | Application |
| GATT Connect / Pairing | — | **nein** |
| RF Environment Score | — | **Kontrast** `rf-environment-monitor` |
| Ride Display Custom GATT | — | **Kontrast** `ride-ble-display` |

## Nicht-Ziele

- Stalking-/Überwachungs-How-tos; nur Desk-Pattern
- Board-Treiber als Universal-Sheet
- Asset-Mirrors

## Prioritäten

1. Sheet `ble-rssi-proximity` + App
2. Kontrast Environment-Monitor und Ride-Display
