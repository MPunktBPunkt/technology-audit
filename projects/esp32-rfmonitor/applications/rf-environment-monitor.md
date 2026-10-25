# Project Application: rf-environment-monitor in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: rf-environment-monitor
status: active
sheet: ../../../technologies/rf-environment-monitor/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-v2-validation/
maturity:
  technology: R3
  implementation: R4
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Permanenter Standort-Monitor: `RfScanner` (WLAN), `BleTracker` (Adv), `RfScore`/`RfAnalyzer` (Score v1∥v2 + DQ), Location Profile, MeasSession, Snapshot, History/Events, UI+Hub.

## Architektur / Datenfluss

```text
WiFi.scanNetworks ──▶ RfScanner ──┐
NimBLE Adv-Scan  ──▶ BleTracker ──┼──▶ observation (raw)
                                  │         │
                                  │         ▼
                                  │    derived (proxy: density/pressure/occupancy)
                                  │         │
                                  │         ▼
                                  └── assessment: scoreV1 ∥ scoreV2 + measurementQuality
                                            │
                     LocationProfile / MeasSession / Snapshot / Hub / SSE
```

WLAN und BLE **nacheinander** (README). Dual-Core RF-Worker (Core 0) wenn `RFMON_USE_DUAL_CORE`.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/rf/RfScanner.*` | WLAN-Scan + Instrumentierung |
| `src/rf/BleTracker.*` | BLE Adv / Beacons |
| `src/rf/RfScore.*` | Score v1 + v2 Parallel |
| `src/rf/RfAnalyzer.*` | Aggregation / Assessment |
| `src/rf/LocationProfile.*` | Standort-Baseline + Deviation |
| `src/rf/MeasSession.*` | Mess-Session Export |
| `src/core/HwCaps.*` | Caps / PSRAM / Dual-Core |
| `docs/RF_SCORE.md` | Formeln v1/v2 |
| `docs/OBSERVATION_MODEL.md` | Schichten |
| `docs/LOCATION_PROFILE.md` | Baseline / Session / Snapshot |
| `docs/evidence/2026-10-25-lab-baseline/` | Lab-JSON |

## Konfiguration

| Claim | Status |
|-------|--------|
| `FW_VERSION` 1.5.0 | `FACT` (`BuildFlags.h`) |
| `RFMON_SCORE_VERSION` 2 (v1 parallel) | `FACT` |
| Peripheral/Central disabled auf Mini (Scan-only) | `FACT` (`platformio.ini`) |
| Observation = raw / derived(proxy) / assessment | `FACT` |
| Mini: kein PSRAM, kleine Caps; S3: PSRAM → große Caps | `FACT` (Lab) |
| Location Deviation ≠ Score-Offset | `FACT` (Doku) |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Score v2 Formel + Parallel-v1 | `EVID-RF-2026-10-25-001` | `FACT` |
| Observation-Schichten dokumentiert | `EVID-RF-2026-10-25-002` | `FACT` |
| Lab-Baseline Mini+S3 600 s / 151 Samples | `EVID-RF-2026-10-25-003` | `FACT` (Lab) |
| measurementQuality ≠ rf_score | `EVID-RF-2026-10-25-004` | `FACT` (Lab) |
| Proxies ≠ Airtime | `EVID-RF-2026-10-25-005` | `REJECTED` (Physik) |
| Sequentieller WLAN/BLE-Scan | `EVID-RF-2026-10-25-006` | `FACT` |
| Dual-Core Worker + PSRAM Caps | `EVID-RF-2026-10-25-007` | `FACT` (Lab) |
| Score-Heuristik v1 (Freeze) | `EVID-RF-2026-10-09-001` | `FACT` |
| Feldkalibrierung Standort 2 | — | `UNKNOWN` (Exit #5) |

## Offene Fragen

- Score-v2 vs. v1 Diff an dichtem Standort (Lab hatte scoreVersion 1 im 600 s-Dump)?
- Radio-Duty und BLE-Fenster Mini vs. S3 systematisieren?

## Verwandte

- [esp-hub-telemetry](esp-hub-telemetry.md) · [esp-embedded-web-sse](esp-embedded-web-sse.md)
