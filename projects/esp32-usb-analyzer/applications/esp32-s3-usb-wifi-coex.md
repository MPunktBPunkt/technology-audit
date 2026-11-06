# Project Application: esp32-s3-usb-wifi-coex in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: esp32-s3-usb-wifi-coex
status: active
sheet: ../../../technologies/esp32-s3-usb-wifi-coex/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-0.0.50/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

Mode-A Datenplane läuft **USB + WiFi STA gleichzeitig**. Lab quantifiziert den **Durchsatz-Engpass** (TCP ≪ USB MSC) — separates Thema von PHY-Kill-Hypothesen aus hu-probe. Pipeline (0.0.37) hebt TCP, schließt die Lücke aber nicht.

## Architektur / Datenfluss

```text
USB OTG MSC (~0.92 MB/s)  vs  WiFi TCP Mode-A (~0.33 MB/s campaign peak; pipeline ~0.44 MB/s @4096×8)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `tools/lab_integrity_test.py`, `lab_perf_sweep.py` | TCP rates / pipeline |
| `tools/lab_baseline_campaign.py` | Combined campaign |
| `tools/lab_capability_audit.py` | TCP integrity sample (gaps=0) |
| GATE4 / LAB_TCP_PIPELINE | windowed + pipeline modes |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| TCP peak campaign **332 kB/s** (0.0.50) | `EVID-USBA-2026-11-02-003` | `MEASURED` |
| Pipeline sweet spot ~**436 kB/s** (0.0.37); win≥16 cliff | `004` | `MEASURED` |
| USB MSC peak ~**0.92 MB/s** | `001` | `MEASURED` |
| Mode-A reicht für USB Nutzrate | H2 Kill | `REJECTED` still |
| „USB Bulk kills WiFi“ als Desk-FACT | Sheet | `REJECTED` still — hier Rate-Bottleneck, nicht Death |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-31 | Kill H2: Mode-A ack-each (~139 kB/s) reicht nicht |
| 2026-11-01 | Pipeline +45 % vs barrier windowed — immer noch ≪ USB |
| 2026-11-02 | Campaign peak 332 kB/s; Capability TCP gaps=0 |

## Offene Fragen

- Coex discrimination A–D unter sustained proxy load?
- Store-and-Forward Pflicht vor HU Bulk?

## Verwandte Applications / Methods

- [`usb-wifi-coex-discrimination`](../../../methods/usb-wifi-coex-discrimination.md)
- hu-probe Coex Application
