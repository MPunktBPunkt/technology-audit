# Project Application: esp-hub-telemetry in esp32.ftmsprobe

```yaml
project_id: esp32-ftmsprobe
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-ftmsprobe-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Gleicher Hub-Client-Pattern (`fwType` Sonde/Familie `ftmsprobe`), OTA über Hub oder direkt; NVS-Namespace `esphub` teilt Config mit anderen Nodes auf demselben Chip.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Hub-OTA-Schema `ftmsprobe.<ver>.<family>.bin` | `EVID-HUB-2026-10-09-003` | `FACT` (README/deploy) |
| NVS `esphub` überlebt Firmware-Familienwechsel | `EVID-HUB-2026-10-09-004` | `INFERRED` (README) |

## Abweichungen

- OTA während offener BLE-Links: direkter Deploy lehnt ab (Messschutz).
