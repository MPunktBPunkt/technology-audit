# Project Application: esp-hub-telemetry in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Arduino-`esp-hub-base`-Familie: Heartbeat `fwType: rfmonitor`, RF-IO-Keys, Web- und Hub-OTA.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Hub-IO-Keys laut README | `EVID-HUB-2026-10-09-006` | `INFERRED` |
| `fwType=rfmonitor` | `EVID-HUB-2026-10-09-007` | `FACT` |

## Abweichungen

- IO-Schema RF-spezifisch (score, ap_count, ble_count, …) — nicht mit heartrate/ergo identisch.
