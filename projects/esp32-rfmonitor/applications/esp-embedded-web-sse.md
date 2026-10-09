# Project Application: esp-embedded-web-sse in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: esp-embedded-web-sse
status: active
sheet: ../../../technologies/esp-embedded-web-sse/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Lab-UI: Gauge, Kanal-Heatmap, Charts, Event-Terminal, Config; SSE `/events`.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `/events` SSE vorhanden | `EVID-WEB-2026-10-09-003` | `FACT` |

## Abweichungen

- Kein Setup-Wizard in der Monitor-UI (Config-Tab); WiFiManager separat beim Erststart.
