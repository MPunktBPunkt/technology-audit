# Audit Campaign: esp32-rfmonitor-2026-v2-validation

```yaml
id: esp32-rfmonitor-2026-v2-validation
project_id: esp32-rfmonitor
started: 2026-10-25
ended: 2026-10-26
status: closed
profile: firmware
standard_version: "0.7.1"
standard_gaps: []
prior_audit: esp32-rfmonitor-2026-pilot
superseded_by: esp32-rfmonitor-2026-motion-delta
reviewed_commit: 739c67a
upstream_pin:
  repo: https://github.com/MPunktBPunkt/esp32.rfmonitor
  commit: "739c67a"
  fw_version: "1.5.0"
  lab_baseline_fw: "1.3.0"
reuse_outcomes:
  reused:
    - rf-environment-monitor
    - esp-hub-telemetry
    - esp-embedded-web-sse
  new:
    - observation-raw-derived-assessment
    - rf-score-v2-parallel-replay
    - location-profile-vs-absolute-score
    - hub-contract-v2-rf-alert
  not_helped:
    - "RF-Score als kalibrierte Messgröße ohne Standortprofil"
    - "channel_load / congestion = Airtime"
  process: "Upstream 1.1.0→1.5.0 Desk+Lab unter 0.7.1 geschlossen; Nachzug 1.6–1.10.2 → motion-delta; Exit #5 Rest/Küche + #6 Adapter dort."
  decisions_touched:
    - fact-score-v2-active-parallel-v1
    - fact-measurement-quality-separate
    - reject-proxy-as-airtime
    - hub-v2-device-side-fact-adapter-unknown
```

## Ziel

Revalidation von `esp32.rfmonitor` nach Observability-/Score-v2-/Hub-Contract-v2-Update (FW **1.5.0** @ `739c67a`) unter **Audit-Standard 0.7.1**. Sheet/Apps/Evidence nachziehen; Pilot-Lücken schließen, wo Lab belegt.

## Scope

Siehe [SCOPE](../../projects/esp32-rfmonitor/SCOPE.md).

- **Im Scope:** Observation Model, RF-Score v1+v2, Location/Session/Snapshot, Hub-Contract v2 (Device-Seite), Lab-Baseline 2026-10-25, Operator-UI-Signale, Dual-Core/PSRAM-Caps.
- **Nicht im Scope:** Spektrumanalyse; toolnode-Modulpfad; ioBroker-Adapter-Implementierung von `rf.alert`; Presence; zweiter Feldstandort (Exit #5 Rest).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Kampagne `standard_version: "0.7.1"` + Reuse-Outcomes | erfüllt |
| 2 | Sheet `rf-environment-monitor` um Observation/Score-v2/Location-Achse gewachsen | erfüllt |
| 3 | Applications + Evidence auf `739c67a` / FW 1.5.0 | erfüllt |
| 4 | Lab-Baseline Mini+S3 verlinkt (Upstream Evidence) | erfüllt |
| 5 | Feldserie an ≥1 weiterem Standort (Pilot Exit #5 Rest) | übernommen → [`motion-delta`](../esp32-rfmonitor-2026-motion-delta/) (Küche teilweise) |
| 6 | Hub-Adapter spiegelt Contract v2 (`rf.alert`) | übernommen → [`motion-delta`](../esp32-rfmonitor-2026-motion-delta/) Exit #6 |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Score v2 aktiv, v1 parallel | Formel + `RFMON_SCORE_VERSION=2`? | `EVID-RF-2026-10-25-001` | Sheet: versionierte Assessment-Schicht; Replay möglich | `KNOWN BEFORE TEST` (Doku) / Lab bestätigt |
| Proxies ≠ Airtime | Sind density/pressure/occupancy gemessen? | `EVID-RF-2026-10-25-005` | `REJECTED` als Physik-Claim | `KNOWN BEFORE TEST` |
| measurementQuality ≠ Score | Getrennte Achse? | `EVID-RF-2026-10-25-004` | Checklist + Hub-Keys getrennt führen | `DISCOVERED DURING TEST` (Lab 1.2/1.3) |
| Location Δ ≠ Score-Offset | Standortprofil separat? | `EVID-RF-2026-10-25-003` | Absolute Quality vs. Standort-Δ | `DISCOVERED DURING TEST` |
| Hub v2 Device-FACT | Heartbeat `rf.alert` im Repo? | `EVID-HUB-2026-10-25-001` | Application wachsen; Adapter-Seite Gate | `KNOWN BEFORE TEST` (Doku 1.5) |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-RF-2026-10-25-001` | Clients lesen `scoreVersion` / `scoreV1`+`scoreV2`; nicht still v1-Formel annehmen | `RETROFIT` |
| `EVID-RF-2026-10-25-002` | UI/Hub nutzen `observation`/`derived`/`assessment` oder markieren Legacy-Flachkeys | `RETROFIT` |
| `EVID-RF-2026-10-25-005` | Kein Label „Airtime“/„CCA“ für `channel_pressure_proxy` | `KNOWN BEFORE TEST` |
| `EVID-HUB-2026-10-25-001` | Adapter: nested `rf` + Alert-Flags optional; Basis-Contract bleibt `fwType`+`ios` | `RETROFIT` |

## Kill-Kriterien

**Hypothese:** RF-Score v2 + Observation Model machen den Standort-Monitor ohne weiteres Lab übertragbar und ersetzen Standortkalibrierung.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Score ohne Location Profile als „kalibriert“ behauptet wird | `REJECTED` (Doku) — kein Kill der FW, Kill der Fehlinterpretation |
| 2 | Lab zeigt Score-Stabilität nur an einem Standort; Transfer an Standort 2 scheitert | übernommen (Exit #5 → motion-delta) |
| 3 | Hub-Contract v2 ohne Adapter-Spiegelung als End-to-End-FACT verkauft wird | Gate übernommen (Exit #6 → motion-delta) |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk+Lab belegen Contract/Heuristik am festen Lab-Standort; falsifizierbarer Transfer-Kill braucht zweiten Standort (Exit #5) — nicht als „kein Test nötig“ lesen.
```

## Bezug

[INVENTORY](../../projects/esp32-rfmonitor/INVENTORY.md) · [evidence](evidence.md) · [DELTA](DELTA.md) · Prior: [`esp32-rfmonitor-2026-pilot`](../esp32-rfmonitor-2026-pilot/) · Nachfolger: [`esp32-rfmonitor-2026-motion-delta`](../esp32-rfmonitor-2026-motion-delta/) · Standard: [`VERSION`](../../VERSION) `0.7.1`

## Lessons

- Observation + versionierter Score + Location-Achse machen „Kalibrierung“ zu einem Contract statt Score-Offset.
- Desk @ 1.1 reichte nicht; Lab-Baseline schließt Desk→Lab, nicht Standort-Transfer.
- Upstream-Feature-Sprung 1.5→1.10 braucht eigene Delta-Kampagne — nicht still in dieser Kampagne nachziehen.
- Offene Exits (#5 Standort, #6 Adapter) bewusst an Nachfolger übergeben statt Kampagne künstlich offen zu halten.

## Offene Punkte

- Übernommen von [`esp32-rfmonitor-2026-motion-delta`](../esp32-rfmonitor-2026-motion-delta/): Exit #5 Rest (Küche teilweise), Exit #6 Hub-Adapter
- Optional: Method Note Score-Replay (v1-Features → v2)
