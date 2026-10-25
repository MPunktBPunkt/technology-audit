# Project Application: ride-ble-display in open-bike-computer

```yaml
project_id: open-bike-computer
tech_slug: ride-ble-display
status: active
sheet: ../../../technologies/ride-ble-display/SHEET.md
audit: ../../../audits/open-bike-computer-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle

ESP32-S3 Handlebar-Computer (Waveshare AMOLED 1.75/2.06): BLE Peripheral für Bicino iOS/Watch — Nav, Map, Workout; Ownership v2 (P-256 ECDH).

| Repo | Commit |
|------|--------|
| [seichris/open-bike-computer](https://github.com/seichris/open-bike-computer) | `cd7ad00b` |

## Datenfluss

```text
iPhone/Watch Central
  → Adv service 9D7B3F30-…-1800 + mfg payload (ver 2, flags, ID suffix)
  → Auth char → owner key (ECDH/HKDF; compare code)
  → Nav/Map/GPS/Workout/RAUT chars (or framed 2A6E fallback)
  → Display: live stats, TBT, offline map
```

## Pfade

| Pfad | Rolle |
|------|-------|
| `docs/ble-protocol.md` | GATT/Auth/Framing Spec |
| `esp32/` | Firmware + board profiles |
| `tools/build_firmware.py` | Locked PlatformIO bootstrap |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Custom service + Adv protocol v2 + ownership auth | `EVID-BIKE-2026-10-25-001` | `FACT` |
| Framed fallback MAPR/GPSP/MSET/WTLM/RAUT | `EVID-BIKE-2026-10-25-002` | `FACT` |
| Boards: Waveshare AMOLED 1.75/2.06 | `EVID-BIKE-2026-10-25-003` | `FACT` |
