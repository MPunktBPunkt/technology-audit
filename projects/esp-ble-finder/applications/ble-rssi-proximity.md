# Project Application: ble-rssi-proximity in esp-ble-finder

```yaml
project_id: esp-ble-finder
tech_slug: ble-rssi-proximity
status: active
sheet: ../../../technologies/ble-rssi-proximity/SHEET.md
audit: ../../../audits/esp-ble-finder-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle

findphone-Port auf Waveshare ESP32-S3-Touch-AMOLED-1.8: Auto-Scan, RSSI-Dots/Fill, Status-Bands, Speaker-Clicker mit Mute.

| Repo | Commit |
|------|--------|
| [khlebobul/esp_ble_finder](https://github.com/khlebobul/esp_ble_finder) | `1a588119` |

## Datenfluss

```text
NimBLE Adv Scan → device list (RSSI, name, addr)
  → filter TARGET_NAME / TARGET_ADDR (compile-time)
  → lock + SWITCH_DB hysteresis + EMA
  → proximity_strength/band (−50…−95 dBm bounds)
  → LVGL face + clicker_update
```

## Pfade

| Pfad | Rolle |
|------|-------|
| `main/main.c` | Scan, hunt lock, UI |
| `main/proximity.h` | Bounds, bands, click interval |
| `main/target.h` | Name/Addr filter |
| `main/clicker.*` | Speaker feedback |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Adv scan hunt; TARGET_NAME; mute keeps hunt | `EVID-BLEFIND-2026-10-25-001` | `FACT` |
| Proximity −50…−95 dBm; bands; click 70–1000 ms | `EVID-BLEFIND-2026-10-25-002` | `FACT` |
| Board 368×448 AMOLED 1.8 + NimBLE | `EVID-BLEFIND-2026-10-25-003` | `FACT` |
