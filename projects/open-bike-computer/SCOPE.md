# Project Scope: open-bike-computer (Fremd)

```yaml
project_id: open-bike-computer
title: Open Bike Computer — Ride BLE Display (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "cd7ad00bb6c4f9566195cd44ab4d6a675518b94d"
repos:
  - https://github.com/seichris/open-bike-computer
status: active
```

## Zweck

Fremdrepo: **Handlebar-Display** (Waveshare ESP32-S3 AMOLED) empfängt Navigation/Workout über **Custom BLE** von iPhone/Watch — Auth/Ownership, gerahmte Map/GPS/Workout-Frames. Abgrenzung zu Standard-FTMS/HRM und zu BLE-Proximity-Hunt.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `esp32/` Firmware + BLE Protocol | Ride Display Peripheral | ja |
| iOS/Watch App (Bicino) | Phone/Watch Host | beobachtet (Kontrast) |
| Strava/Apple Health Cloud | — | **nein** (Produkt) |
| FTMS/HRM Standard-GATT | — | **Kontrast** Sheets |
| Offline OSM Map-Render | Board UI | Application |

## Nicht-Ziele

- App-Store-/Gesundheitsdaten-Beratung
- AGPL Map-Backend Vertiefung
- Secrets/Owner-Keys spiegeln

## Prioritäten

1. Sheet `ride-ble-display` + App
2. Kontrast `bluetooth-ftms` / `ble-hrm-gatt` / `ble-rssi-proximity`
