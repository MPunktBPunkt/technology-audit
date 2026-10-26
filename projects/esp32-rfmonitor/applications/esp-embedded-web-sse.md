# Project Application: esp-embedded-web-sse in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: esp-embedded-web-sse
status: active
sheet: ../../../technologies/esp-embedded-web-sse/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-motion-delta/
maturity:
  technology: R3
  implementation: R4
  field_evidence: R3
  reusability: W3
```

## Rolle im Projekt

Lab-/Operator-UI: Gauge, Kanal-Heatmap, **RF Timeline**, WLAN-Filter/Sortierung, History-Zeitfenster, Findings, **Own-Link Δ-/Absolut-Chart**, Session-Profile/Phasen (Char A–G, Motion CAL/W1/W2), Event-Terminal, Config; SSE `/events`; Web-OTA.

## API (Auswahl)

| Endpoint | Rolle |
|----------|-------|
| `/api/status`, `/api/rf/*` | Status + Observation |
| `/api/rf/ownlink?n=` | Always-on Fine-RSSI |
| `/api/rf/history?res=` | Multi-res History |
| `/api/rf/channels/history` | Channel-Druck über Zeit |
| `/api/location/*`, `/api/session/*` | Baseline / Session |
| `/api/session/motion?n=` | Live Motion-Ausschnitt |
| `/events` | SSE |
| `/ota` | Web-OTA |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `/events` SSE vorhanden | `EVID-WEB-2026-10-09-003` | `FACT` |
| Operator Timeline / Filter / Findings (FW 1.5) | `EVID-WEB-2026-10-25-001` | `FACT` (Lab) |
| Own-Link fein Δ-Chart always-on (1.10.x) | `EVID-WEB-2026-10-26-001` | `FACT` (Lab/UI) |

## Abweichungen

- Kein Setup-Wizard in der Monitor-UI (Config-Tab); WiFiManager separat beim Erststart.
- Always-on `/api/rf/ownlink` ≠ voller Session-Motion-Export.
