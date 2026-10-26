# Folgeprojekte (aus esp32.rfmonitor)

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Motion in anderem Raum/Geometrie | `own-link-motion-sensitivity` | Exit #5 Rest |
| Hub-Adapter Contract v2 | `esp-hub-telemetry` | Exit #6 — `rf.alert` spiegeln |
| Mini↔S3 Score-Drift-Nachlauf | Score v2 + Location | Upstream Next |
| Score v2 gegen v1-Rohdaten replayen | Observation Model | Method Note optional |
| Method Note Score-Characterization A–G | `rf-characterize` | optional bei 2. Einsatz |
| Coexistence-Baseline für BT-Gateway | Snapshot + Pressure-Proxy | Messplan koppeln |
| Motion-Export streaming | große Ringe | Upstream optional |

## Wissensfeedback 2026-10-26 (FW 1.6–1.10.2)

Aus Upstream Ship + Küchen-/Char-Evidence @ `afcd137` und Desk-Delta-Kampagne:

| Claim | Status | Hinweis |
|-------|--------|---------|
| Own-Link 200 ms misst Walk-by (Küche, Mini+S3) | `FACT` (Field) | SNR_motion ≳ 5 |
| Motion = Presence / Personenzählung | `REJECTED` | Method + Sheet |
| Score-Pfad (4 s) für Walk-by-Zeitauflösung | `REJECTED` | eigenes Profil |
| Char A–G schwacher Stimulus = FAIL | `FACT` (Field) | kein Score-Bug |
| Phase-Aggregates überleben Ring-Wrap | `FACT` | 1.9.1 |
| Channel History multi-res + Drift | `FACT` | 1.8 |
| AP Lifetime + Alert ACK/Pin | `FACT` | Operator |
| Hub-Contract v2 Device | `FACT` (Doku) | Adapter offen |
| Prior 1.5 Observation/Score-v2/Location | `FACT` | v2-validation |

Kampagne: [`esp32-rfmonitor-2026-motion-delta`](../../audits/esp32-rfmonitor-2026-motion-delta/).
