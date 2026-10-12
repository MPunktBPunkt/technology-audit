# Project Application: bluetooth-a2dp in espble

```yaml
project_id: espble
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/espble-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

`EspBleClassic` A2DP Sink **und** Source auf **original ESP32** über namespaced Classic-only Bluedroid (`libespble_bluedroid_classic.a`), parallel zu NimBLE für BLE.

| Repo | Commit |
|------|--------|
| [tanakamasayuki/EspBle](https://github.com/tanakamasayuki/EspBle) | `56e288d` |

## Architektur / Datenfluss

```text
Sketch EspBleClassic
  → namespaced Bluedroid Classic host
  → HCI broker (optional dual-host with NimBLE)
  → A2DP Sink/Source stream APIs
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/EspBleClassicA2dp.cpp` / `EspBleClassicA2dpSource.cpp` | Sink/Source |
| `src/EspBleClassic.h` | Codec/stream types |
| `tests/peer/dual_host_a2dp/` | Dual-host soak |
| `README.md` Compatibility | Classic only on original ESP32 |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Classic A2DP only on original ESP32 | `EVID-ESPBLE-A2DP-2026-10-12-001` | `FACT` |
| Sink + Source classes present | `EVID-ESPBLE-A2DP-2026-10-12-002` | `FACT` |
| Dual-host BLE+Classic experimental | `EVID-ESPBLE-A2DP-2026-10-12-003` | `FACT` (README) |
