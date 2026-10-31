# Project Application: esp32-s3-usb-wifi-coex in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: esp32-s3-usb-wifi-coex
status: active
sheet: ../../../technologies/esp32-s3-usb-wifi-coex/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-pilot/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

Mode-A Datenplane läuft **USB + WiFi STA gleichzeitig**. Lab quantifiziert den **Durchsatz-Engpass** (TCP ≪ USB MSC) — separates Thema von PHY-Kill-Hypothesen aus hu-probe.

## Architektur / Datenfluss

```text
USB OTG MSC (~0.93 MB/s)  vs  WiFi TCP Mode-A (~0.14 MB/s ack-each, ~0.26 MB/s window=8)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `tools/lab_integrity_test.py`, `lab_perf_sweep.py` | TCP rates |
| `tools/lab_baseline_campaign.py` | Combined campaign |
| GATE4 window notes | windowed bulk |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| TCP peak ~139 kB/s ack-each | `EVID-USBA-2026-10-31-003` | `MEASURED` |
| window=8 ~0.26 MB/s; window=16 can regress | `015` | `MEASURED` |
| USB MSC peak ~0.93 MB/s | `001` | `MEASURED` |
| „USB Bulk kills WiFi“ als Desk-FACT | Sheet | `REJECTED` still — hier Rate-Bottleneck, nicht Death |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-31 | Kill H2: Mode-A ack-each reicht nicht für USB Nutzrate |

## Offene Fragen

- Coex discrimination A–D unter sustained proxy load?
- Store-and-Forward Pflicht vor HU Bulk?

## Verwandte Applications / Methods

- [`usb-wifi-coex-discrimination`](../../../methods/usb-wifi-coex-discrimination.md)
- hu-probe Coex Application
