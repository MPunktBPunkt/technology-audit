# Project Application: ble-hr-relay in esp32.ergo

```yaml
project_id: esp32-ergo
tech_slug: ble-hr-relay
status: active
sheet: ../../../technologies/ble-hr-relay/SHEET.md
audit: ../../../audits/esp32-ergo-2026-pilot/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Ergo **implementiert kein** HR-Relay. Es ist **Consumer** des Nodes [`esp32.heartrate`](https://github.com/MPunktBPunkt/esp32.heartrate) (oder äquivalent): Relay hält den H9, Ergo und MyWhoosh sehen `0x180D`.

## Architektur / Datenfluss

```text
H9 → esp32.heartrate (Peripheral) → esp32.ergo HrClient
                                 └→ MyWhoosh (optional parallel)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| README Überblick | Architekturbegründung Relay |
| `HrClient` | sieht Relay wie Gurt |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Dual-HR + Heartrate-Relay mit MyWhoosh „auf Hardware bewährt“ | `EVID-RELAY-2026-10-09-001` | `INFERRED` (STATE.md) |

## Abweichungen vom „Lehrbuch“

- Transfer = **Deployment**-Muster (zweiter Node), nicht Code-Kopie in ergo.

## Offene Fragen

- Automatische Prefer-Relay-Discovery (Name/MAC-Policy)?

## Verwandte

- Application in [esp32-heartrate](../../esp32-heartrate/applications/ble-hr-relay.md)
