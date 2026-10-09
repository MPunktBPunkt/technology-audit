# Project Application: esp-hub-telemetry in esp32.ergo

```yaml
project_id: esp32-ergo
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-ergo-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

`HubClient` mit `fwType: ergo`, Heartbeat, OTA beide Richtungen, Session-Bezug. Gleicher Client-Pattern wie heartrate, **anderer** Payload/`fwType`.

## Architektur / Datenfluss

```text
HubClient.loop → sendHeartbeat (builder aus App)
Hub → OTA URL → performOta
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/core/HubClient.*` | Client |
| `platformio.ini` | `HUB_PORT_DEFAULT=8093` |
| `STATE.md` | Hub `192.168.178.113:8093` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `fwType: ergo` in Betrieb | `EVID-HUB-2026-10-09-001` | `MEASURED` (STATE/README) |
| OTA beide Richtungen bewährt | `EVID-HUB-2026-10-09-002` | `INFERRED` (STATE) |

## Abweichungen vom Heartrate-Projekt

- Andere IO-Keys / Metriken (Leistung, Stufe, Modi) — Schema nicht identisch.
- Sheet A: `fwType` pro Familie (Wachstumseintrag).

## Offene Fragen

- Gemeinsames Hub-Schema-Dokument?

## Verwandte

- [esp32-heartrate Hub-Application](../../esp32-heartrate/applications/esp-hub-telemetry.md)
