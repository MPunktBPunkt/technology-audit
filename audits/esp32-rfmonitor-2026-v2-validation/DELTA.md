# AUDIT DELTA — esp32-rfmonitor Pilot → v2-validation

```yaml
prior: esp32-rfmonitor-2026-pilot
new: esp32-rfmonitor-2026-v2-validation
old_standard: "0.6.0"
new_standard: "0.7.1"
old_commit: 95314cd
new_commit: 739c67a
old_fw: "1.1.0"
new_fw: "1.5.0"
revalidated: 2026-10-25
```

Vergleich **Upstream-Update** (nicht nur Regelstand). Pilot blieb auf Desk @ 1.1.0; diese Kampagne zieht 1.2–1.5 Observability + Lab-Baseline nach.

## OLD AUDIT (0.6.0 @ 95314cd)

| Bereich | Stand |
|---------|--------|
| Claims | Score v1, sequentieller Scan, Hub `fwType=rfmonitor`, SSE |
| UNKNOWNs | Feldkalibrierung Exit #5; Observation-Schichten nur Hypothese |
| Sheets | `rf-environment-monitor` neu; Hub/Web wachsen |
| Evidence | 5 IDs (Desk) |
| Process gaps | Standard 0.6.0; keine C10–C13-Pflicht |

## NEW AUDIT (0.7.1 @ 739c67a)

| Bereich | Delta |
|---------|--------|
| neue FACTs | Score v2 + Parallel-v1; Observation raw/derived/assessment; measurementQuality; Location Profile + Deviation; Lab-Baseline Mini+S3; Dual-Core/PSRAM; Hub-Contract v2 Device-Doku; Operator Timeline |
| herabgestuft / geschärft | „Score kalibriert“ → Location Profile / Deviation; `channel_*` explizit Proxy |
| neue UNKNOWNs | Zweiter Standort; Hub-Adapter v2-Spiegel; formaler Score-v2-600 s-Dump |
| verworfene Transfers | Proxy → Airtime; Monitor → Spektrum/PCAP/Presence (unverändert REJECTED) |
| Cross-Project-Reuse | Geschwister toolnode-RF bestätigt; kein Sheet-Fork |

## Quantitativ

| Metrik | Pilot 0.6.0 | v2-validation 0.7.1 | Δ |
|--------|-------------|---------------------|---|
| Upstream FW | 1.1.0 | 1.5.0 | +Observability/Score/Hub/UI |
| Evidence-IDs (Kampagne) | 5 | 10+Prior | Lab + Contract |
| Offene Exits | Exit #5 | Exit #5 Rest + #6 Adapter | Lab-Teil geschlossen |
| `standard_gaps` | [0.6.1…] | keine | Parität 0.7.1 |

## Urteil

Stärkster Hebel: **Schichtenmodell Observation + versionierter Score + Location als eigene Achse** — macht den Pilot-UNKNOWN „Kalibrierung“ zu einem greifbaren Contract statt Score-Offset. Hub-Contract v2 ist Device-FACT; End-to-End bleibt Gate am Adapter.
