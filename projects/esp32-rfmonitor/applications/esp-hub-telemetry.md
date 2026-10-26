# Project Application: esp-hub-telemetry in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-motion-delta/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Arduino-`esp-hub-base`-Familie: Heartbeat `fwType: rfmonitor`, RF-IO-Keys (inkl. Radio-Duty-Fenster), nested Hub-Contract v2 (`rf` + `rf.alert`), Web- und Hub-OTA. Motion Own-Link ist **Session/UI**, nicht zwingend Hub-IO.

## Ebene B (Device-Contract)

| Claim | Status |
|-------|--------|
| `fwType` bleibt `rfmonitor` | `FACT` |
| Contract-ID `rfmonitor-hub-v2` ab FW 1.5 | `FACT` ([HUB_CONTRACT.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/afcd137/docs/HUB_CONTRACT.md)) |
| Nested `rf`: score, scoreVersion, scoreV1/V2, measurementQuality, locationDeviation, alert.flags | `FACT` (Doku) |
| Alert-Hysterese on-device; Operator ACK/Pin lokal | `FACT` (Doku/Features) |
| Flache IO-Keys bleiben (Kompatibilität) | `FACT` (README) |
| Radio-Duty 5 m / 1 h / Lifetime in IO | `FACT` (README 1.10) |

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
- Motion-Samples gehören nicht zum Hub-Heartbeat-Minimum.
