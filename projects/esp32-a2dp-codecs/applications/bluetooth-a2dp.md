# Project Application: bluetooth-a2dp in esp32-a2dp-codecs

```yaml
project_id: esp32-a2dp-codecs
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/esp32-a2dp-codecs-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle

Zwei Fork-Linien für A2DP **Sink** mit erweiterten Codecs auf Classic ESP32:

| Repo | Commit | Besonderheit |
|------|--------|--------------|
| [cfint/esp32-a2dp-sink](https://github.com/cfint/esp32-a2dp-sink) | `bf8b482` | AAC/aptX/LDAC/Opus/LC3plus; **AAC→PSRAM**; custom IDF branch |
| [WillyBilly06/ESP32-A2DP-SINK-WITH-CODECS-UPDATED](https://github.com/WillyBilly06/ESP32-A2DP-SINK-WITH-CODECS-UPDATED) | `f4eb125` | IDF 5.5.2; **internal SRAM** main branch; native wrapper + EQ/BLE extras |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Codecs beyond SBC need patched IDF/external libs | `EVID-CODEC-2026-10-12-001` | `FACT` |
| AAC requires PSRAM (cfint) | `EVID-CODEC-2026-10-12-002` | `FACT` |
| WillyBilly main: no PSRAM required claim | `EVID-CODEC-2026-10-12-003` | `FACT` (README) |
| Linux BlueZ codec cache must be cleared | `EVID-CODEC-2026-10-12-004` | `FACT` (cfint README) |
