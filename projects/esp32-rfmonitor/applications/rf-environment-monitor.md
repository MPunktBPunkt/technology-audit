# Project Application: rf-environment-monitor in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: rf-environment-monitor
status: active
sheet: ../../../technologies/rf-environment-monitor/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

Permanenter Standort-Monitor: `RfScanner` (WLAN), `BleTracker` (Adv), `RfAnalyzer` (Score/Breakdown), History/Events, UI+Hub.

## Architektur / Datenfluss

```text
WiFi.scanNetworks ──▶ RfScanner ──┐
NimBLE Adv-Scan  ──▶ BleTracker ──┼──▶ RfAnalyzer (score) ──▶ History / Events / Hub / SSE
```

WLAN und BLE **nacheinander** (README).

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/rf/RfScanner.*` | WLAN-Scan |
| `src/rf/BleTracker.*` | BLE Adv / Beacons |
| `src/rf/RfAnalyzer.*` | Score |
| `docs/RF_SCORE.md` | Heuristik v1 |

## Konfiguration

| Claim | Status |
|-------|--------|
| `FW_VERSION` 1.1.0 | `FACT` |
| Score-Formel wie RF_SCORE.md | `FACT` (Doku=Code-Intent) |
| Peripheral/Central disabled auf Mini (Scan-only) | `FACT` (`platformio.ini`) |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Score-Heuristik v1 dokumentiert | `EVID-RF-2026-10-09-001` | `FACT` |
| Sequentieller WLAN/BLE-Scan | `EVID-RF-2026-10-09-002` | `FACT` (README) |
| Feldkalibrierung an Standort X | — | `UNKNOWN` |

## Offene Fragen

- Breakdown-Stabilität über Tage?

## Verwandte

- [esp-hub-telemetry](esp-hub-telemetry.md) · [esp-embedded-web-sse](esp-embedded-web-sse.md)
