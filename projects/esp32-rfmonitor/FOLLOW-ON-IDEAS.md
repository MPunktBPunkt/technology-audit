# Folgeprojekte (aus esp32.rfmonitor)

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Standort-Kalibrierung RF-Score / Location Profile | `rf-environment-monitor` | Feldserie (Pilot Exit #5) |
| Coexistence-Baseline für BT-Gateway | Score + Kanal-Heatmap + Snapshot | Kopplung Messplan |
| Alerting nur über Hub | `esp-hub-telemetry` | Schwellwerte + Contract v2 |
| Score v2 gegen v1-Rohdaten replayen | Observation Model (ab FW 1.2) | Assessment-Layer |
| Measurement Session Export | Observation + History | UI/API Session |

## Wissensfeedback 2026-10-25 (FW 1.2/1.3 Observability)

Aus Code-Arbeit + Lab-OTA an `esp32.rfmonitor` (Mini `.87`, S3 `.88` N8R2):

| Claim | Status | Hinweis |
|-------|--------|---------|
| `channel_load` / `congestion` = Airtime | `REJECTED` | AP-Count-Proxies; `kind=proxy` |
| Scan-Instrumentierung (Dauer, Fail-Rate, Duty) | `FACT` (Lab) | Mini/S3 1.2.0 verifiziert |
| `measurementQuality` getrennt vom Score | `FACT` (Lab) | DQ 100 nach Scan |
| PSRAM Caps auf S3 N8R2 | `FACT` (Lab) | braucht `qio_qspi` (nicht `qio_opi`) |
| Dual-Core RF-Worker Core 0 | `FACT` (Lab) | `workerRunning: true` |
| Location Profile / Deviation / Session | `FACT` (Lab) | 600 s Capture Mini+S3, 151 Samples; Evidence `esp32.rfmonitor/docs/evidence/2026-10-25-lab-baseline/` |
| Coexistence Snapshot API | `FACT` (Lab) | Snapshot JSON gesichert |
| Score v2 parallel zu v1 | `FACT` (Lab) | FW 1.4+; Formel in `RfScore.cpp` |
| Hub-Contract v2 (`rf.alert`) | `HYPOTHESIS`→Lab | FW 1.5 Heartbeat-Feld; ioBroker-Seite noch offen |
| Operator Timeline / WLAN-Filter | `FACT` (Lab) | FW 1.5 UI |

Nächste Revalidation gegen Standard **0.7.1** empfohlen (`esp32-rfmonitor-2026-v2-validation`). Feldserie an zweitem Standort für Exit #5 noch offen.
