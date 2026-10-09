# Project Application: esp-hub-telemetry in esp32.webradio

```yaml
project_id: esp32-webradio
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-webradio-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

Heartbeat `/api/register` mit `ios`: favoriten, sender, nowStation, nowTitle. **Kein `fwType`** — Identity über mac/name/hwType.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Hub-IO nowStation/nowTitle | `EVID-HUB-2026-10-09-030` | `FACT` |
| Kein fwType im Payload | `EVID-HUB-2026-10-09-031` | `FACT` |
