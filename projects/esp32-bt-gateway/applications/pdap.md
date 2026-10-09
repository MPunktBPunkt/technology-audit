# Project Application: pdap in esp32.bt-gateway

```yaml
project_id: esp32-bt-gateway
tech_slug: pdap
status: draft
sheet: ../../../technologies/pdap/SHEET.md
audit: ../../../audits/esp32-bt-gateway-2026-planning/
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
```

## Rolle im Projekt (Design-B)

Client→Gateway-Vertrag: PCM + Metadata + Commands + optional Menu. Gateway ohne Quell-Semantik.

## Konfiguration (geplant)

| Claim | Status |
|-------|--------|
| PCM 44.1 / S16LE / Stereo am Pi erzwingen | `HYPOTHESIS` (Konzept) |
| Event-Namen an Pi `map_event()` anschlussfähig | `HYPOTHESIS` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| PDAP im Auto latenzstabil | — | `UNKNOWN` |

## Offene Fragen

- Framing/Protokollversion vor Phase 0 einfrieren

## Verwandte

- [bluetooth-a2dp](bluetooth-a2dp.md)
