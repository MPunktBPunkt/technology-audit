# Method: Own-Link Motion Sensitivity

```yaml
slug: own-link-motion-sensitivity
title: Own-Link Motion Sensitivity
status: active
tags: [lab-only, field, rf-environment, validation]
```

## Zweck

Prüfen, ob kurzzeitige Änderungen des **eigenen WLAN-Links** (Router↔Node) durch Bewegung in der Nähe reproduzierbar messbar sind — **ohne** Presence-, CSI- oder Personenzählungs-Claim.

Einsetzen wenn: Assessment-Score (typisch 4 s / kleines RSSI-Fenster) Walk-bys verschluckt; Feinsignal nötig; Abgrenzung zu Proximity/CSI klarhalten.

## Voraussetzungen

- Firmware mit high-rate Own-Link-Ring + Session-Profil `motion` (oder äquivalent)
- Zwei Boards optional (Vergleich Mini/S3); fester AP/Router-Pfad
- Host-Tool zur Auswertung (z. B. `rf-motion-characterize`) oder manuelle σ/Δ-Rechnung
- Operator-Protokoll: eine Ruhekalibrierung + mind. ein Walk-by

## Ablauf

1. **Baseline-Lage** — Node fest, WLAN verbunden, Umgebung ruhig.
2. **Session `motion`** — Scans pausieren / Own-Link-Samplezeit ≈200 ms; Ring groß genug für Phasen.
3. **CAL** — 45–60 s still; μ und σ der Ruhe.
4. **W1** — 45–60 s dichter Vorbeigehen am Node (und zurück).
5. **W2** (optional) — Repeatability.
6. **Export** — Samples + Phase-Aggregates; Live-API nur Ausschnitt.
7. **Auswerten** — max\|Δ\| vs. CAL, SNR_motion ≈ excursion/σ; Mini↔S3 nur als Hinweis.

## Artefakte

- Session-JSON mit `motionRssi.samples` / Phase-Stats
- Kurz-README: μ/σ, max\|Δ\|, SNR, Pass/Fail ≥3σ
- Evidence-ID in Audit-Kampagne (Field ≠ Desk)

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Signal | max\|Δ\| ≥ ≈3·σ_CAL (SNR_motion ≳ 3) | Excursion im Ruheband |
| Claim-Disziplin | nur RSSI-Δ / Link-Beeinflussung | Presence / „Handy erkannt“ / CSI behauptet |
| Protokoll | CAL vor Walk-by; Stimulus dokumentiert | Score-Fenster als Motion-Ersatz verkauft |

## Fallstricke

- Score-/Observation-Pfad mit Motion-Ring vermischen
- Always-on Fine-Chart (`/api/rf/ownlink`) mit Session-Motion-Export verwechseln
- Schwachen Vorbeigeher oder weiten Abstand als Method-Fail der Hardware lesen
- Transfer auf andere Räume ohne neue CAL als FACT verkaufen

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| `esp32-rfmonitor` | Kampagne [`esp32-rfmonitor-2026-motion-delta`](../audits/esp32-rfmonitor-2026-motion-delta/); Upstream `docs/MOTION_SENSITIVITY.md` |
