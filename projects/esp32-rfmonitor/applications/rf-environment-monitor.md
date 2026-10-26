# Project Application: rf-environment-monitor in esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
tech_slug: rf-environment-monitor
status: active
sheet: ../../../technologies/rf-environment-monitor/SHEET.md
audit: ../../../audits/esp32-rfmonitor-2026-motion-delta/
maturity:
  technology: R3
  implementation: R4
  field_evidence: R3
  reusability: W3
```

## Rolle im Projekt

Permanenter Standort-Monitor: `RfScanner` (WLAN), `BleTracker` (Adv), `RfScore`/`RfAnalyzer` (Score v1∥v2 + DQ), Location Profile, MeasSession (Profile `field` / `characterization` / `motion` / …), Snapshot, History/Events, Own-Link-Feinring, UI+Hub.

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
         LocationProfile / History(multi-res) / AP Lifetime / Alerts
                                            │
         MeasSession ── field | characterization(A–G) | motion(CAL/W1/W2)
                                            │
         Own-Link fein (always-on 200 ms) + Motion-Ring (Session)
                                            │
                              Snapshot / Hub / SSE / Operator-UI
```

WLAN und BLE **nacheinander** (README). Dual-Core RF-Worker (Core 0) wenn `RFMON_USE_DUAL_CORE`. Im Profil `motion` Scans praktisch pausiert.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/rf/RfScanner.*` | WLAN-Scan + Instrumentierung |
| `src/rf/BleTracker.*` | BLE Adv / Beacons |
| `src/rf/RfScore.*` | Score v1 + v2 Parallel |
| `src/rf/RfAnalyzer.*` | Aggregation / Assessment / Own-Link |
| `src/rf/LocationProfile.*` | Standort-Baseline + Deviation |
| `src/rf/MeasSession.*` | Mess-Session + Profile/Phasen |
| `src/core/HwCaps.*` | Caps / PSRAM / Dual-Core |
| `docs/RF_SCORE.md` | Formeln v1/v2 |
| `docs/OBSERVATION_MODEL.md` | Schichten |
| `docs/LOCATION_PROFILE.md` | Baseline / Session / Snapshot |
| `docs/MOTION_SENSITIVITY.md` | Own-Link Walk-by |
| `docs/SCORE_CHARACTERIZATION.md` | Protokoll A–G |
| `docs/evidence/2026-10-25-*` | Lab + Char + Kitchen idle |
| `docs/evidence/2026-10-26-kitchen-*` | Motion Ruhe/Walk-by |
| `tools/rf-characterize` · `tools/rf-motion-characterize` | Host-Auswertung |

## Konfiguration

| Claim | Status |
|-------|--------|
| `FW_VERSION` 1.10.2 | `FACT` (`BuildFlags.h`) |
| `RFMON_SCORE_VERSION` 2 (v1 parallel) | `FACT` |
| Peripheral/Central disabled auf Mini (Scan-only) | `FACT` (`platformio.ini`) |
| Observation = raw / derived(proxy) / assessment | `FACT` |
| Mini: kein PSRAM, kleine Caps; S3: PSRAM → große Caps | `FACT` (Lab) |
| Location Deviation ≠ Score-Offset | `FACT` (Doku) |
| Session-Profile inkl. `motion` / `characterization` | `FACT` |
| Motion-Ring Mini 900 / S3 1500; Fine-Ring 300 | `FACT` (STATE) |

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
| Motion-Profil / Own-Link 200 ms | `EVID-RF-2026-10-26-001` | `FACT` |
| Küche Walk-by SNR≳5 Mini+S3 | `EVID-RF-2026-10-26-002` | `FACT` (Field) |
| Motion ≠ Presence | `EVID-RF-2026-10-26-003` | `REJECTED` (Claim) |
| Char A–G schwacher Stimulus FAIL | `EVID-RF-2026-10-26-004` | `FACT` (Field) |
| Phase-Aggregates vs. Ring-Wrap | `EVID-RF-2026-10-26-005` | `FACT` |
| Channel History multi-res | `EVID-RF-2026-10-26-006` | `FACT` |
| AP Lifetime + Alert ACK/Pin | `EVID-RF-2026-10-26-007` | `FACT` |
| Mini BLE hang fix 1.6 | `EVID-RF-2026-10-26-008` | `FACT` |
| Motion-Transfer anderer Raum | — | `UNKNOWN` (Exit #5 Rest) |

## Offene Fragen

- Score-v2 vs. v1 Diff an dichtem Standort (Lab hatte scoreVersion 1 im 600 s-Dump)?
- Mini↔S3 Score-Drift-Nachlauf?
- Motion-CAL-Portabilität jenseits Küche?

## Verwandte

- [esp-hub-telemetry](esp-hub-telemetry.md) · [esp-embedded-web-sse](esp-embedded-web-sse.md)
- Method: [`own-link-motion-sensitivity`](../../../methods/own-link-motion-sensitivity.md)
