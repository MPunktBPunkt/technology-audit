# Evidence — esp32-rfmonitor-2026-v2-validation

Desk+Lab-Nachzug 2026-10-25 @ `739c67a` (FW **1.5.0**) · Lab-Baseline-Capture unter FW **1.3.0** · **standard_version 0.7.1**.

Basis: `https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/739c67a/`  
Lab-Artefakte: [`docs/evidence/2026-10-25-lab-baseline/`](https://github.com/MPunktBPunkt/esp32.rfmonitor/tree/739c67a/docs/evidence/2026-10-25-lab-baseline)

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-RF-2026-10-25-001` | Score v2 aktiv (`scoreVersion=2`); v1 parallel für Replay | `FACT` | [RF_SCORE.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/739c67a/docs/RF_SCORE.md) · [`RfScore.cpp`](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/739c67a/src/rf/RfScore.cpp) · `RFMON_SCORE_VERSION=2` |
| `EVID-RF-2026-10-25-002` | Observation = raw / derived(proxy) / assessment | `FACT` | [OBSERVATION_MODEL.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/739c67a/docs/OBSERVATION_MODEL.md) |
| `EVID-RF-2026-10-25-003` | Lab-Baseline Mini+S3, 600 s, 151 Samples, Location Profile | `FACT` (Lab) | [lab-baseline README](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/739c67a/docs/evidence/2026-10-25-lab-baseline/README.md) · JSON Snapshots |
| `EVID-RF-2026-10-25-004` | `measurementQuality` getrennt vom RF-Score | `FACT` (Lab) | OBSERVATION_MODEL + Session `avgQuality` |
| `EVID-RF-2026-10-25-005` | density/pressure/occupancy = **proxy**, nicht Airtime | `REJECTED` (als Physik) | RF_SCORE.md · OBSERVATION_MODEL `kind=proxy` |
| `EVID-RF-2026-10-25-006` | WLAN- und BLE-Scan nacheinander (shared radio) | `FACT` | README Hardware @ `739c67a` |
| `EVID-RF-2026-10-25-007` | Dual-Core RF-Worker + PSRAM-Caps (S3) | `FACT` (Lab) | Snapshot `hw.workerRunning` / `psram`; FOLLOW-ON Lab-Notiz |
| `EVID-HUB-2026-10-25-001` | Hub-Contract v2: nested `rf` + `rf.alert`, `fwType=rfmonitor` | `FACT` (Device-Doku) | [HUB_CONTRACT.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/739c67a/docs/HUB_CONTRACT.md) |
| `EVID-HUB-2026-10-25-002` | IO-Keys inkl. `rf_score_v1/v2`, `measurement_quality`, `location_deviation`, Alert-Flags | `FACT` (README) / Adapter-Spiegel `UNKNOWN` | README Hub-IO · HUB_CONTRACT |
| `EVID-WEB-2026-10-25-001` | Operator-UI: Timeline, WLAN-Filter, History-Fenster, Findings | `FACT` (Lab) | README Features v1.5 · UiPages |
| `EVID-RF-2026-10-09-001` | Score-Heuristik v1 dokumentiert (Baseline Freeze) | `FACT` | Prior Pilot — weiter gültig als v1-Referenz |
| `EVID-RF-2026-10-09-002` | Sequentieller WLAN/BLE-Scan | `FACT` | Prior — bestätigt durch `EVID-RF-2026-10-25-006` |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Score/Location an zweitem Standort stabil | `UNKNOWN` | Exit #5 |
| ioBroker.esp-hub konsumiert `rf.alert` / nested `rf` | `UNKNOWN` | Exit #6 |
| Score-v2 Lab-Serie mit FW ≥1.4 (Baseline war 1.3 / scoreVersion 1) | `HYPOTHESIS`→teilweise Lab | FOLLOW-ON: v2 parallel Lab; formaler 600 s-Dump noch v1 |

## Lab-Kurzwerte (Upstream)

| Board | Samples | Baseline Score | AP≈ | BLE≈ | ownRssi≈ |
|-------|---------|----------------|-----|------|----------|
| Mini `.87` | 151 | 96 | 3.0 | 0 | −48.3 |
| S3 `.88` | 151 | 93.4 | 3.8 | 11.6 | −31.9 |

BLE-Count 0 (Mini) vs. ~12 (S3): Antenne/Position/Scan-Fenster — kein Kill, relevant für Score-v2-Vergleich.

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Pilot Desk @ `95314cd` / FW 1.1.0 · Standard 0.6.0 |
| 2026-10-25 | Lab Observability 1.2–1.3 + Baseline Capture; Upstream Ship 1.5.0 @ `739c67a` |
| 2026-10-25 | Revalidation-Kampagne unter Standard 0.7.1 |
