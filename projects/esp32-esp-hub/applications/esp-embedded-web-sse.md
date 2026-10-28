# Project Application: esp-embedded-web-sse in esp32-esp-hub

```yaml
project_id: esp32-esp-hub
tech_slug: esp-embedded-web-sse
status: active
sheet: ../../../technologies/esp-embedded-web-sse/SHEET.md
audit: ../../../audits/esp32-esp-hub-2026-1.10-validation/
maturity:
  technology: R3
  implementation: R4
  field_evidence: R3
  reusability: W3
```

## Rolle im Projekt

Status-SPA aus `web/index.html` als gzip-PROGMEM; SSE Live; OTA-Upload. Pack-Pipeline ist Teil des Ableiten-Standards.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp-hub-base/web/index.html` | UI-Quelle |
| `esp-hub-base/tools/pack_ui.py` | → `UiPagesGz.h` |
| `esp-hub-base/src/core/WebUi.cpp` | gzip-Header, SSE `/events`, `/api/status` |
| `docs/update/WEBUI_GZ.md` | Pack-Vertrag |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| gzip PROGMEM Pack | `EVID-WEB-2026-10-28-001` | `FACT` |
| SSE Status-UI | `EVID-WEB-2026-10-28-002` | `FACT` |
