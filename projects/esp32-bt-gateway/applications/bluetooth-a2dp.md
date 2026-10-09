# Project Application: bluetooth-a2dp in esp32.bt-gateway

```yaml
project_id: esp32-bt-gateway
tech_slug: bluetooth-a2dp
status: draft
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/esp32-bt-gateway-2026-planning/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt (Design-B)

ESP als **A2DP Source** zur HU; PCM kommt per PDAP vom Client. Kein Sink+Source gleichzeitig am ESP.

## Architektur / Datenfluss

```text
PiDrive PCM ──PDAP──▶ ESP Encode/SBC ──A2DP Source──▶ BMW Sink
```

## Relevante Pfade (Planung)

| Pfad | Rolle |
|------|-------|
| `docs/planung/KONZEPT.md` | Architektur |
| `docs/planung/PFLICHTENHEFT.md` | Anforderungen |
| `docs/planung/FLASH-BUDGET.md` | Stack-Größe (offen) |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Gateway-Pfad im Auto verifiziert | — | `UNKNOWN` (FW fehlt) |
| Coexistence STA+A2DP stabil | — | `UNKNOWN` (A17/Gate) |

## Offene Fragen

- A17: Bluedroid vs. BTstack?
- Buffer/Bitpool Defaults?

## Verwandte

- [avrcp](avrcp.md) · [pdap](pdap.md) · PiDrive Ist-Pfad BlueZ (Kontrast)
