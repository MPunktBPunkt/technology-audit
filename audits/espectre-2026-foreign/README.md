# Audit Campaign: espectre-2026-foreign

```yaml
id: espectre-2026-foreign
project_id: espectre
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "5866bff6aa3a8ac41ed70d2476c115ea6285b277"
reuse_outcomes:
  reused: [esp-wifi-promiscuous-pcap, rf-environment-monitor, mqtt-node-telemetry, esp-embedded-web-sse]
  new: [wifi-csi-motion]
  not_helped: []
  process: "Desk foreign CSI motion; no dataset mirror; contrast sniff/score; privacy noted"
```

## Ziel

[francescopace/espectre](https://github.com/francescopace/espectre) als Fremd-Upstream für **Wi-Fi-CSI-Motion-Sensing** (Echtzeit, Temporal Admission, on-device Detektoren inkl. kleinem NN) in die KB bringen — klar getrennt von Promiscuous/PCAP und RF-Score-Monitoren.

## Scope

[SCOPE](../../projects/espectre/SCOPE.md) — Desk only; keine Rohdaten-Spiegelung.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | `standard_version` 0.7.1 + lab-tool + Commit-Pin | erfüllt |
| 2 | Sheet `wifi-csi-motion` + App; Kontrast Sniff/RF | erfüllt |
| 3 | Grok-Punkte CSI / ML / hohe pps in Evidence | erfüllt |
| 4 | Keine Dataset/Weight-Spiegelung | erfüllt |
| 5 | C10–C12; C13 n/a Desk | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 7 | Eigenes Raum-Lab | offen (FOLLOW-ON) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neues Sheet? | = Promiscuous oder RF-Score? | `…-001`/`…-002` | Neuer Slug `wifi-csi-motion` | KNOWN BEFORE TEST |
| CSI-MLP → `mcu-ple-inference`? | LLM vs Feature-NN | `…-003` | Nein — getrennt | KNOWN BEFORE TEST |
| Marauder CSI reuse seen_in? | Gleiche Implementierung? | Marauder Inventar | Nein — nur Kontrast bis Vertiefung | KNOWN BEFORE TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-ESPECTRE-2026-10-25-002` | pps-Änderungen = Timing neu validieren; nicht „mehr = besser“ | KNOWN BEFORE TEST |
| `EVID-ESPECTRE-2026-10-25-003` | Lightweight vs HA: CPU/Flash vs Accuracy Tradeoff vor Default | KNOWN BEFORE TEST |
| `EVID-ESPECTRE-2026-10-25-004` | Traffic-Quelle und Chip-CSI-Gates vor Placement-Claims | KNOWN BEFORE TEST |
| `EVID-ESPECTRE-2026-10-25-001` | Privacy/Consent trotz „keine Kamera“ | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese:** Upstream liefert belastbare On-Device-CSI-Motion-Pipeline mit dokumentiertem Timing.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Nur Cloud-ML, keine On-Device-Detektoren | nicht eingetreten |
| 2 | Nur Promiscuous-Sniff ohne CSI-Amplitude-Pipeline | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Audit; eigene Raum-Metriken UNKNOWN ≠ STOP.
```

## Lessons → Transfer

- Hohe Sampling-Raten bei CSI brauchen **Temporal Admission**, sonst Excess/Jitter-Artefakte.
- „Keine Kamera“ ≠ Privacy-frei.
- Marauder-CSI und ESPectre teilen das Stichwort CSI, nicht den Produkt-Contract.

## Bezug

[INVENTORY](../../projects/espectre/INVENTORY.md) · [evidence](evidence.md)
