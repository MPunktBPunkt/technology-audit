# Audit Campaign: esp32-rfmonitor-2026-motion-delta

```yaml
id: esp32-rfmonitor-2026-motion-delta
project_id: esp32-rfmonitor
started: 2026-10-26
ended: null
status: active
profile: firmware
standard_version: "0.7.1"
standard_gaps: []
prior_audit: esp32-rfmonitor-2026-v2-validation
reviewed_commit: afcd137
upstream_pin:
  repo: https://github.com/MPunktBPunkt/esp32.rfmonitor
  commit: "afcd137"
  fw_version: "1.10.2"
  prior_fw: "1.5.0"
  prior_commit: "739c67a"
reuse_outcomes:
  reused:
    - rf-environment-monitor
    - esp-hub-telemetry
    - esp-embedded-web-sse
  new:
    - own-link-motion-sensitivity
    - field-session-profiles
    - score-characterization-a-g
    - channel-history-multires
    - ap-lifetime-alert-ack
  not_helped:
    - "Own-Link Motion = Presence / Personenzählung"
    - "Score-Pfad (4 s / 12er-Fenster) für Walk-by-Zeitauflösung"
    - "Schwacher Stimulus als Score-Char-Pass"
  process: "Upstream 1.5.0→1.10.2 Delta unter 0.7.1; v2-validation Exits #1–#4 übernommen; Küche schließt Standort-2 teilweise; Hub-Adapter weiter offen."
  decisions_touched:
    - fact-motion-ownlink-measurable-kitchen
    - reject-motion-as-presence
    - fact-score-char-needs-strong-stimulus
    - fact-phase-aggregates-survive-ring-wrap
```

## Ziel

Delta-Revalidation von `esp32.rfmonitor` **1.5.0 → 1.10.2**: Session-Profile, Score-Characterization A–G, Channel-History, AP-Lifetime/ACK, **Own-Link Motion Sensitivity** (CAL/W1/W2) + Küchen-Evidence. Sheet/Apps/Method nachziehen; Presence-Drift verhindern.

## Scope

Siehe [SCOPE](../../projects/esp32-rfmonitor/SCOPE.md).

- **Im Scope:** FW 1.6–1.10.2 Desk+Feld (Küche); Motion Own-Link; Characterization; History/Drift; Operator AP-Events; Method `own-link-motion-sensitivity`.
- **Nicht im Scope:** CSI / Promiscuous / Presence-Claims; Spektrum; toolnode-Modulpfad; ioBroker-Adapter-Implementierung von `rf.alert` (Exit #6 weiter offen); Mini↔S3 Score-Drift-Nachlauf (Upstream Next).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Kampagne `standard_version: "0.7.1"` + Pin `afcd137` / FW 1.10.2 | erfüllt |
| 2 | Sheet `rf-environment-monitor`: Motion≠Presence, Session-Profile, History-Achse | erfüllt |
| 3 | Applications + Evidence auf 1.10.2; Prior-v2 Evidence weiter gültig | erfüllt |
| 4 | Method Note `own-link-motion-sensitivity` + Küchen Walk-by/Ruhe verlinkt | erfüllt |
| 5 | Zweiter Standort (Pilot/v2 Exit #5 Rest): Küche als Feldstandort | teilweise (Motion FACT; Score-Transfer beliebiges Zimmer `UNKNOWN`) |
| 6 | Hub-Adapter Contract v2 (`rf.alert`) | offen (übernommen) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Motion = Own-Link-Feinsignal, nicht Presence | Misst 200 ms RSSI Walk-by reproduzierbar? | `EVID-RF-2026-10-26-002` | Sheet-Fallstrick Presence `REJECTED`; Method anlegen | `DISCOVERED DURING TEST` (Küche) |
| Score-Pfad ungeeignet für Walk-by | Reicht 4 s/12er-Fenster? | `EVID-RF-2026-10-26-001` | Eigenes Session-Profil `motion` | `KNOWN BEFORE TEST` (MOTION_SENSITIVITY) |
| Characterization braucht starken Stimulus | Schwacher Reiz → Score flach? | `EVID-RF-2026-10-26-004` | FAIL erwartbar; Aggregates + Ring-Größe | `DISCOVERED DURING TEST` |
| Ring-Wrap ohne Aggregates verliert A–G | Überleben Phase-Stats Wrap? | `EVID-RF-2026-10-26-005` | 1.9.1 Aggregates Pflicht für Char-Export | `DISCOVERED DURING TEST` |
| Küche ≠ Lab schließt Standort-2 teilweise | Zweiter Ort mit Evidence? | `EVID-RF-2026-10-26-002` + idle/side-by-side | Exit #5 teilweise; Raum-Transfer offen | `DISCOVERED DURING TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-RF-2026-10-26-001` | Clients/UI labeln Motion nicht als Presence/CSI; Scan-Pause im Profil `motion` beachten | `KNOWN BEFORE TEST` |
| `EVID-RF-2026-10-26-002` | Claims nur RSSI-Δ / SNR_motion; keine Personenzählung | `RETROFIT` |
| `EVID-RF-2026-10-26-003` | Abgrenzung zu `ble-rssi-proximity` / `wifi-csi-motion` im Sheet halten | `KNOWN BEFORE TEST` |
| `EVID-RF-2026-10-26-004` | Char-Protokoll: Stimulus-Stärke dokumentieren; FAIL bei schwachem Reiz nicht als Score-Bug lesen | `DISCOVERED DURING TEST` |
| `EVID-RF-2026-10-26-005` | Export/Auswertung Phase-Aggregates bevorzugen, nicht nur Sample-Ring | `DISCOVERED DURING TEST` |
| `EVID-WEB-2026-10-26-001` | Own-Link-Chart: Δ vs. absolut; `/api/rf/ownlink` always-on ≠ Session-Motion-Ring | `RETROFIT` |

## Kill-Kriterien

**Hypothese:** High-rate Own-Link (200 ms) liefert am Küchenstandort reproduzierbare Walk-by-Signale (SNR_motion ≥ 3) ohne CSI — und bleibt klar von Presence getrennt.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Walk-by max\|Δ\| ≤ Ruhe-σ (kein ≥3σ-Signal) an Mini **und** S3 | nicht eingetreten (`EVID-RF-2026-10-26-002`) |
| 2 | Motion-UI/Doku als Presence oder „Handy erkannt“ verkauft | `REJECTED` als Claim (`EVID-RF-2026-10-26-003`) — kein FW-Kill |
| 3 | Score-Char A–E ohne starken Stimulus als Pass gewertet | Fail korrekt dokumentiert (`EVID-RF-2026-10-26-004`) |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Own-Link Motion Sensitivity | [`methods/own-link-motion-sensitivity.md`](../../methods/own-link-motion-sensitivity.md) |
| Score Characterization A–G | Upstream `docs/SCORE_CHARACTERIZATION.md` + `tools/rf-characterize` (Method-Note optional später) |

## Bezug Inventar

- `rf-environment-monitor` — wachsen (Motion, Session-Profile, History)
- `esp-embedded-web-sse` — Own-Link-Chart / Session-APIs
- `esp-hub-telemetry` — unverändert Device-v2; Adapter Exit #6

## Ergebnisse

- [DELTA](DELTA.md) · [evidence](evidence.md)
- Sheet: [`rf-environment-monitor`](../../technologies/rf-environment-monitor/SHEET.md)
- Apps: [`applications/`](../../projects/esp32-rfmonitor/applications/)
- Upstream Evidence: [kitchen-motion](https://github.com/MPunktBPunkt/esp32.rfmonitor/tree/afcd137/docs/evidence/2026-10-26-kitchen-motion) · [ruhe2](https://github.com/MPunktBPunkt/esp32.rfmonitor/tree/afcd137/docs/evidence/2026-10-26-kitchen-ruhe2) · [walkby](https://github.com/MPunktBPunkt/esp32.rfmonitor/tree/afcd137/docs/evidence/2026-10-26-kitchen-walkby) · [char A–G](https://github.com/MPunktBPunkt/esp32.rfmonitor/tree/afcd137/docs/evidence/2026-10-25-score-characterization)

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Küche Walk-by 1.10.x | `EVID-RF-2026-10-26-002` | App RF + Sheet Fallstrick Presence |
| Motion-Profil Doku | `EVID-RF-2026-10-26-001` | Method + App |
| Char A–G schwach | `EVID-RF-2026-10-26-004` | App + FOLLOW-ON |
| Aggregates 1.9.1 | `EVID-RF-2026-10-26-005` | App |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact.

## Lessons → Transfer

- Own-Link-Feinsignal ist eine **eigene Messklasse** neben Assessment-Score — nicht denselben Pfad zwingen.
- Characterization falsifiziert Stimulus-Qualität, nicht automatisch die Score-Formel.
- Zweiter Standort (Küche) stützt Motion-FACT; Score-Portabilität bleibt profile-gebunden.

## Offene Punkte nach Abschluss

- Exit #6: ioBroker.esp-hub Contract-v2-Spiegelung
- Score-Transfer / Drift Mini↔S3 Nachlauf (Upstream Next)
- Optional: Method Note `rf-score-characterization`
- Raum-/Geometrie-Transfer Motion (`UNKNOWN`)
