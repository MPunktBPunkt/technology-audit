# Project Application: esp-embedded-web-sse in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: esp-embedded-web-sse
status: active
sheet: ../../../technologies/esp-embedded-web-sse/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-v2-validation/
maturity:
  technology: R3
  implementation: R4
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Lab-/Operator-UI: Gauge, Kanal-Heatmap, **RF Timeline**, WLAN-Filter/Sortierung, History-Zeitfenster, Findings, Event-Terminal, Config; SSE `/events`; Web-OTA.

## API (Auswahl)

| Endpoint | Rolle |
|----------|-------|
| `/api/status`, `/api/rf/*` | Status + Observation |
| `/api/location/*`, `/api/session/*` | Baseline / Session |
| `/events` | SSE |
| `/ota` | Web-OTA |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `/events` SSE vorhanden | `EVID-WEB-2026-10-09-003` | `FACT` |
| Operator Timeline / Filter / Findings (FW 1.5) | `EVID-WEB-2026-10-25-001` | `FACT` (Lab) |

## Abweichungen

- Kein Setup-Wizard in der Monitor-UI (Config-Tab); WiFiManager separat beim Erststart.
