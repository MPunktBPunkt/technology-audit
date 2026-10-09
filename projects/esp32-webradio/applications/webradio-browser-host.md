# Project Application: webradio-browser-host in esp32.webradio

```yaml
project_id: esp32-webradio
tech_slug: webradio-browser-host
status: active
sheet: ../../../technologies/webradio-browser-host/SHEET.md
audit: ../../../audits/esp32-webradio-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R1
  reusability: W2
```

## Rolle im Projekt

ESP = UI + NVS (Sender/Fav/Podcasts) + RSS-Proxy; Browser = HTML5 Audio / Media Session. Discovery radio-browser.info. Explizit **kein** A2DP.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp32.webradio.ino` | Monolith |
| README API | `/api/stations|favorites|nowplaying|proxy` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Browser spielt Streams, nicht ESP-Audio | `EVID-WR-2026-10-09-001` | `FACT` |
| Kein A2DP (README) | `EVID-WR-2026-10-09-002` | `FACT` |
| `/api/proxy` RSS | `EVID-WR-2026-10-09-003` | `FACT` |
