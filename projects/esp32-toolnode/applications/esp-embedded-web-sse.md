# Project Application: esp-embedded-web-sse in esp32.toolnode

```yaml
project_id: esp32-toolnode
tech_slug: esp-embedded-web-sse
status: active
sheet: ../../../technologies/esp-embedded-web-sse/SHEET.md
audit: ../../../audits/esp32-toolnode-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

PROGMEM-Web-UI, REST unter `/api/*` (system, rf, lab), SSE aus `esp-hub-base`-Familie (`/events`), plus Setup-Wizard `/wizard` und `/api/setup/*`.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| REST + SSE + Wizard API | `EVID-WEB-2026-10-09-010` | `FACT` |
