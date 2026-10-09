# Project Application: esp-hub-telemetry in iobroker-esp-hub

```yaml
project_id: iobroker-esp-hub
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/iobroker-esp-hub-2026-pilot/
maturity:
  technology: R4
  implementation: R3
  field_evidence: R2
  reusability: W4
```

## Rolle im Projekt

**Server-Seite** desselben Contracts wie die ESP-Clients. Sprache Node.js — Sheet A unverändert. Spec: `Schnittstellen.md` (mac/name/hwType, ios; Response interval/otaUrl).

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Spec POST /api/register | `EVID-HUB-2026-10-09-080` | `FACT` |
| otaUrl einmalig | `EVID-HUB-2026-10-09-081` | `FACT` |
| Stack Node ≠ neuer Slug | `EVID-HUB-2026-10-09-082` | `FACT` (Prozess 0.6.3) |
