# Project Application: esp-hub-telemetry in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-v2-validation/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Arduino-`esp-hub-base`-Familie: Heartbeat `fwType: rfmonitor`, RF-IO-Keys, nested Hub-Contract v2 (`rf` + `rf.alert`), Web- und Hub-OTA.

## Ebene B (Device-Contract)

| Claim | Status |
|-------|--------|
| `fwType` bleibt `rfmonitor` | `FACT` |
| Contract-ID `rfmonitor-hub-v2` ab FW 1.5 | `FACT` ([HUB_CONTRACT.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/739c67a/docs/HUB_CONTRACT.md)) |
| Nested `rf`: score, scoreVersion, scoreV1/V2, measurementQuality, locationDeviation, alert.flags | `FACT` (Doku) |
| Alert-Hysterese on-device | `FACT` (Doku) |
| Flache IO-Keys bleiben (Kompatibilität) | `FACT` (README) |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Hub-IO-Keys laut README (erweitert) | `EVID-HUB-2026-10-25-002` | `FACT` (README) |
| Hub-Contract v2 Device-Seite | `EVID-HUB-2026-10-25-001` | `FACT` (Doku) |
| `fwType=rfmonitor` | `EVID-HUB-2026-10-09-007` | `FACT` |
| Adapter spiegelt `rf.alert` / nested `rf` | — | `UNKNOWN` (Exit #6) |

## Abweichungen

- IO-Schema RF-spezifisch — nicht mit heartrate/ergo identisch.
- Nested Domain-Contract ist **Erweiterung**, ersetzt nicht Basis-Heartbeat (`mac`/`name`/`ios`).
