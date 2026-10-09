# Project Application: esp-embedded-web-sse in esp32.ergo

```yaml
project_id: esp32-ergo
tech_slug: esp-embedded-web-sse
status: active
sheet: ../../../technologies/esp-embedded-web-sse/SHEET.md
audit: ../../../audits/esp32-ergo-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Ride-/Coach-UI ist während BLE-Link die **einzige** Anzeige (Konsolendisplay aus). REST + SSE; UI wird per `tools/pio_pack_ui.py` gepackt.

## Architektur / Datenfluss

```text
Browser ──REST/SSE──▶ App.cpp / UiPages (packed)
Control-APIs ──▶ Limiter (einziger Schreibpfad); Bridge-Lock → 409
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/web/UiPages.h` / pack script | UI |
| `src/app/App.cpp` | Routes inkl. `/events` |
| `docs/ergometer/WEBINTERFACE.md` | Vertragsdoku |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `/events` SSE vorhanden | `EVID-WEB-2026-10-09-001` | `FACT` |
| Flash-Budget ~75 % App-Partition @ 0.3.24-dev | `EVID-WEB-2026-10-09-002` | `MEASURED` (STATE) |

## Abweichungen vom Heartrate-Projekt

- Deutlich größere UI (Ride, Bibliothek, Bridge-Status); Pack-Schritt Pflicht.
- Exklusiv-Steuerung Bridge spiegelt sich in API-Fehlercodes.

## Offene Fragen

- SSE unter Bridge+ERG-Last gemessen?

## Verwandte

- [esp-hub-telemetry](esp-hub-telemetry.md)
