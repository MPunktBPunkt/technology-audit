# AUDIT DELTA — esp32-rfmonitor v2-validation → motion-delta

```yaml
prior: esp32-rfmonitor-2026-v2-validation
new: esp32-rfmonitor-2026-motion-delta
old_standard: "0.7.1"
new_standard: "0.7.1"
old_commit: 739c67a
new_commit: afcd137
old_fw: "1.5.0"
new_fw: "1.10.2"
revalidated: 2026-10-26
```

Vergleich **Upstream-Feature-Delta** (nicht Regelstand). v2-validation deckte Observation/Score-v2/Hub-v2/Lab-Baseline @ 1.5.0; diese Kampagne zieht 1.6–1.10.2 nach.

## OLD AUDIT (0.7.1 @ 739c67a / 1.5.0)

| Bereich | Stand |
|---------|--------|
| Claims | Observation-Schichten; Score v1∥v2; Location; Hub-Contract v2 Device; Lab-Baseline; Operator Timeline |
| UNKNOWNs | Standort 2; Hub-Adapter v2; formaler Score-v2-600 s-Dump |
| Sheets | `rf-environment-monitor` Observation/Location-Achse |
| Evidence | Lab Mini+S3 600 s; Desk Contract |
| Exits | #5 Rest, #6 Adapter offen |

## NEW AUDIT (0.7.1 @ afcd137 / 1.10.2)

| Bereich | Delta |
|---------|--------|
| neue FACTs | Session-Profile (`field`/`characterization`/`motion`/…); Own-Link 200 ms; Küchen Walk-by SNR≥5; Char A–G + Aggregates; Channel History multi-res; AP Lifetime + Alert ACK/Pin; Mini BLE-Hang-Fix 1.6; always-on Δ-Chart |
| herabgestuft / geschärft | Motion explizit ≠ Presence; Score-Pfad ≠ Walk-by-Zeitauflösung; schwacher Char-Stimulus = erwarteter FAIL |
| neue UNKNOWNs | Motion-Transfer andere Räume; Mini↔S3 Score-Drift-Nachlauf; Hub-Adapter (unverändert) |
| verworfene Transfers | Motion → CSI/Presence/Handy-als-WLAN-Sender; Char-FAIL → Score-Formel kaputt |
| Cross-Project-Reuse | Geschwister toolnode-RF unverändert; Motion bleibt Monitor-Application |

## Quantitativ

| Metrik | v2-validation | motion-delta | Δ |
|--------|---------------|--------------|---|
| Upstream FW | 1.5.0 | 1.10.2 | +History/Char/Motion/UI |
| Evidence-IDs (neu) | — | 9+ | Küche + Char + History |
| Offene Exits | #5 Rest + #6 | #5 teilweise + #6 | Küche |
| `standard_gaps` | keine | keine | — |

## Urteil

Stärkster Hebel: **Own-Link Motion als eigene Messklasse** (Method + Sheet-Abgrenzung) — verhindert Presence-Drift und erklärt, warum Score-v2 den Walk-by nicht ersetzt. Characterization und History machen Assessment/Operator-Contract feldfähiger, ohne das Observation-Modell umzubauen.
