# Project Application: usb-dual-esp-observe-proxy in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: usb-dual-esp-observe-proxy
status: active
sheet: ../../../technologies/usb-dual-esp-observe-proxy/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-pilot/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

Kernmuster: ESP-A Host + ESP-B Device + Debian Control/UI. Liefert Lab-Capture, Integrity-APIs und Proxy-Slices — Claim-Disziplin über Gates 0–10.

## Architektur / Datenfluss

```text
DUT/Stick ──USB──▶ ESP Host (.88) ──WiFi:9752──▶ ESP Device (.89) ──USB──▶ PC/Host
                         │                            │
                         └──────── Debian :9750/:8080 ┘
                              discovery + dual capture
```

OTG-Loop (Host OTG ↔ Device OTG) ist die **Baseline-Topologie**; MITM-Wiring ist getrennt.

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/analyzer-node/` | Dual env `analyzer-s3-host` / `analyzer-s3-device` |
| `controller/` | Discovery `:9750`, capture proxy |
| `web/` | Lab UI `:8080` dual lanes |
| `docs/CAPTURE.md`, `docs/schemas/` | Event schema / layers |
| `tools/lab_*.py` | Mess- und Verify-Scripts |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| FW | 0.0.35 | `FACT` |
| Timestamp domain | `local_per_node` | `FACT` (B) · `EVID-USBA-2026-10-31-014` |
| Capture layers | L1 class/app — not L0 | `FACT` · `EVID-USBA-2026-10-31-017` |
| Lab IPs | `.88` Host / `.89` Device / `.187` controller | `FACT` · `EVID-USBA-2026-10-31-016` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| OTG-Loop MSC/TCP Baseline | `EVID-USBA-2026-10-31-001`…`005`/`015` | `MEASURED` (lab) |
| Dual capture timeline | Gate-7 docs | `MEASURED` (lab UI) |
| Transparent MITM | `EVID-USBA-2026-10-31-017` | not claimed |
| HU Feld | — | `UNKNOWN` / out of scope |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-31 Baseline | USB ≫ WiFi Mode-A; integrity clean nach Fill-Fix |
| 2026-10-31 Gates | Gate-7 timeline slice; MITM transparency offen |

## Abweichungen vom „Lehrbuch“

Analyzer-Marketing vs. Epistemic: „Protocol Analyzer“ hier = Class-Layer Lab, nicht Wire-Sniffer.

## Offene Fragen

- Observer-effect Baseline Definition?
- SF-* Timing vs. weiter windowed TCP?

## Verwandte Applications / Methods

- Method [`usb-otg-loop-baseline`](../../../methods/usb-otg-loop-baseline.md)
- Apps `usb-msc`, `esp-usb-host`, `usb-aoa`
