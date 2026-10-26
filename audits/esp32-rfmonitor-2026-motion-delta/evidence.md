# Evidence — esp32-rfmonitor-2026-motion-delta

Desk+Feld-Nachzug 2026-10-26 @ `afcd137` (FW **1.10.2**) · Prior-Basis FW **1.5.0** @ `739c67a` · **standard_version 0.7.1**.

Basis: `https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/afcd137/`  
Prior-Kampagne: [`esp32-rfmonitor-2026-v2-validation`](../esp32-rfmonitor-2026-v2-validation/) (Evidence 2026-10-25 weiter gültig).

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-RF-2026-10-26-001` | Profil `motion`: Own-Link RSSI 200 ms; Scans pausiert; Phasen CAL/W1/W2; Score-Pfad ungeeignet für Walk-by | `FACT` | [MOTION_SENSITIVITY.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/afcd137/docs/MOTION_SENSITIVITY.md) · [STATE.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/afcd137/docs/STATE.md) |
| `EVID-RF-2026-10-26-002` | Küche Walk-by: Mini max\|Δ\|≈2.18 dB SNR≈5.2; S3 ≈1.98 dB SNR≈13.2 (≥3σ) | `FACT` (Field) | [kitchen-walkby](https://github.com/MPunktBPunkt/esp32.rfmonitor/tree/afcd137/docs/evidence/2026-10-26-kitchen-walkby) · [ruhe2](https://github.com/MPunktBPunkt/esp32.rfmonitor/tree/afcd137/docs/evidence/2026-10-26-kitchen-ruhe2) |
| `EVID-RF-2026-10-26-003` | Motion ≠ Presence / Personenzählung / „Handy als WLAN-Sender“ | `REJECTED` (als Claim) | MOTION_SENSITIVITY Audit-Framing · walkby README |
| `EVID-RF-2026-10-26-004` | Score-Char A–G: schwacher Stimulus → Score flach → FAIL erwartbar | `FACT` (Field) | [score-characterization](https://github.com/MPunktBPunkt/esp32.rfmonitor/tree/afcd137/docs/evidence/2026-10-25-score-characterization) · [SCORE_CHARACTERIZATION.md](https://github.com/MPunktBPunkt/esp32.rfmonitor/blob/afcd137/docs/SCORE_CHARACTERIZATION.md) |
| `EVID-RF-2026-10-26-005` | Per-Phase Aggregates überleben Ring-Wrap (1.9.1); Ring 180/300 | `FACT` | STATE 1.9.1 · SCORE_CHARACTERIZATION |
| `EVID-RF-2026-10-26-006` | Channel History + Multi-res Rings (raw/1m/15m) + Baseline Drift (1.8) | `FACT` | README Features · `/api/rf/history` · `/api/rf/channels/history` |
| `EVID-RF-2026-10-26-007` | AP Lifetime Tracking + Operator Alert ACK/Pin | `FACT` | Commit `6a61fa7` / README Features |
| `EVID-RF-2026-10-26-008` | Mini BLE scan hang fix + validation stack (1.6) | `FACT` | Commit `abf2675` |
| `EVID-WEB-2026-10-26-001` | Own-Link fein always-on Δ-Chart; `/api/rf/ownlink`; CAL/W1 UI | `FACT` (Lab/UI) | STATE 1.10.1–1.10.2 · README API |

## Prior (weiter gültig, Auszug)

| ID | Claim | Status |
|----|-------|--------|
| `EVID-RF-2026-10-25-001`…`007` | Score v2, Observation, Lab-Baseline, Proxies≠Airtime, Dual-Core/PSRAM | siehe [v2 evidence](../esp32-rfmonitor-2026-v2-validation/evidence.md) |
| `EVID-HUB-2026-10-25-001`/`002` | Hub-Contract v2 Device; Adapter `UNKNOWN` | unverändert |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Motion-Transfer andere Räume/Geometrien | `UNKNOWN` | Exit #5 Rest |
| ioBroker.esp-hub konsumiert `rf.alert` | `UNKNOWN` | Exit #6 |
| Mini↔S3 Score-Drift-Nachlauf | `UNKNOWN` | Upstream Next |
| Formaler 600 s-Dump unter scoreVersion 2 | `HYPOTHESIS` | Prior FOLLOW-ON |

## Feld-Kurzwerte (Küche Walk-by)

| Board | Ruhe σ | max \|Δ\| | SNR_motion |
|-------|--------|-----------|------------|
| Mini `.87` | ≈0.42 dB | ≈2.18 dB | ≈5.2 |
| S3 `.88` | ≈0.15 dB | ≈1.98 dB | ≈13.2 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-25 | v2-validation @ `739c67a` / 1.5.0 |
| 2026-10-25 | Char A–G + Kitchen idle/side-by-side (Upstream) |
| 2026-10-26 | Motion 1.10.x + Küche Ruhe/Walk-by; Kampagne motion-delta @ `afcd137` |
