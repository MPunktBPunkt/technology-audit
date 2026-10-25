# Folgeprojekte (aus esp32.rfmonitor)

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Feldserie zweiter Standort | `rf-environment-monitor` | Exit #5 |
| Coexistence-Baseline für BT-Gateway | Snapshot + Pressure-Proxy | Messplan koppeln |
| Hub-Adapter Contract v2 | `esp-hub-telemetry` | Exit #6 — `rf.alert` spiegeln |
| Score v2 gegen v1-Rohdaten replayen | Observation Model | Method Note optional |
| Measurement Session CSV / Acknowledge | Session + UI | optional Upstream |

## Wissensfeedback 2026-10-25 (FW 1.2–1.5)

Aus Code-Arbeit + Lab-OTA (Mini `.87`, S3 `.88` N8R2) und Desk-Revalidation @ `739c67a`:

| Claim | Status | Hinweis |
|-------|--------|---------|
| `channel_load` / `congestion` = Airtime | `REJECTED` | AP-Count-Proxies; `kind=proxy` |
| Scan-Instrumentierung (Dauer, Fail-Rate, Duty) | `FACT` (Lab) | Mini/S3 1.2.0+ |
| `measurementQuality` getrennt vom Score | `FACT` (Lab) | |
| PSRAM Caps auf S3 N8R2 | `FACT` (Lab) | `qio_qspi` (nicht `qio_opi`) |
| Dual-Core RF-Worker Core 0 | `FACT` (Lab) | `workerRunning: true` |
| Location Profile / Deviation / Session | `FACT` (Lab) | 600 s Capture; Upstream Evidence |
| Score v2 parallel zu v1 | `FACT` | FW 1.4+; aktiv in 1.5 |
| Hub-Contract v2 (`rf.alert`) Device | `FACT` (Doku) | Adapter-Seite offen |
| Operator Timeline / WLAN-Filter | `FACT` (Lab) | FW 1.5 UI |

Kampagne: [`esp32-rfmonitor-2026-v2-validation`](../../audits/esp32-rfmonitor-2026-v2-validation/).
