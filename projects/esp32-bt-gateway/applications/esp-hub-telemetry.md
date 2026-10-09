# Project Application: esp-hub-telemetry in esp32.bt-gateway

```yaml
project_id: esp32-bt-gateway
tech_slug: esp-hub-telemetry
status: draft
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-bt-gateway-2026-planning/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt (Design-B)

**Dünner IDF-HubClient** (kein Arduino-`esp-hub-base`): Register, einmalige `otaUrl`-Persistenz, USB-Flash merged @0x0, Stufe-2 lokales OTA ohne Hub im Auto.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `docs/planung/HUB-INTEGRATION.md` | H-F1–H-F9 verifiziert gegen Hub v0.5.12 |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Hub-Contract v0.5.12 Fakten H-F1–H-F9 | `EVID-HUB-2026-10-09-005` | `INFERRED` (Planungsdoku, Code-Verifikation dokumentiert) |
| Firmware OTA im Auto über Hub | — | `REJECTED` als Anforderung — Stufe 2 lokal (R24) |

## Abweichungen von Arduino-Nodes

- IDF-only; Compile-Tab Hub irrelevant
- Classic-BT schließt volles esp-hub-base aus

## Verwandte

- Sheet-Wachstum: IDF-Client / einmalige otaUrl Fallstricke
