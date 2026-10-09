# Project Application: iobroker-simple-api in esp32.MeterMaster

```yaml
project_id: esp32-metermaster
tech_slug: iobroker-simple-api
status: active
sheet: ../../../technologies/iobroker-simple-api/SHEET.md
audit: ../../../audits/esp32-metermaster-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R1
  reusability: W2
```

## Rolle im Projekt

ESP als HTTP-Client: `GET …:8087/getPlainValue/{stateId}` für Zählerwerte. Registrierung/Config **nicht** über Simple-API (Henne-Ei) → Adapter :8089.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp32.MeterMaster.ino` | Poll / Ports |
| `docs/DATENAUSTAUSCH.md` | Contract |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Simple-API nur Werte lesen | `EVID-IOB-2026-10-09-001` | `FACT` |
| Register nicht via Simple-API | `EVID-IOB-2026-10-09-002` | `FACT` |
