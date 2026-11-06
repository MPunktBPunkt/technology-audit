# Project Application: usb-dual-esp-observe-proxy in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: usb-dual-esp-observe-proxy
status: active
sheet: ../../../technologies/usb-dual-esp-observe-proxy/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-0.0.50/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

Kernmuster: ESP-A Host + ESP-B Device + Debian Control/UI. Liefert Lab-Capture, Integrity-APIs, Proxy-Slices, Capability-/Gate10-Harness — Claim-Disziplin über Gates 0–10.

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
| `controller/` | Discovery `:9750`, capture proxy, allowlist lab proxy 0.0.41 |
| `web/` | Lab UI `:8080` dual lanes |
| `docs/CAPTURE.md`, `docs/schemas/` | Event schema / layers |
| `tools/lab_capability_audit.py` | Soft-Lab Regression 7/7 |
| `tools/lab_observer_effect.py` | Observer-Loop Baseline |
| `tools/lab_l0_feasibility.py` | Path-A Feasibility |
| `tools/lab_*.py` | Weitere Mess-/Verify-Scripts |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| FW | **0.0.50** (Host+Device) · Controller **0.0.41** | `FACT` |
| Timestamp domain | `local_per_node` + offset estimate | `FACT` (B) · `EVID-USBA-2026-11-02-008` |
| Capture layers | L1 class/app — not Live-L0 | `FACT` · `009` |
| Lab IPs | `.88` Host / `.89` Device / controller `:8080` | `FACT` · `010` |
| Path A sniffer | falsified | `REJECTED` · `006` |
| Observer-Loop | Direct≪Proxy Δ MEASURED | `MEASURED` · `007` (not MITM) |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| OTG-Loop MSC/TCP Baseline 0.0.50 | `EVID-USBA-2026-11-02-001`…`003` | `MEASURED` (lab) |
| Capability Harness 7/7 + Gate10 9/9 | `005` / `008` | `MEASURED` |
| Path A GPIO Sniffer | `006` | `REJECTED` |
| Observer-Loop Proxy Δ | `007` | `MEASURED` (otg_loop only) |
| Transparent MITM PC↔Stick | `009` | not claimed |
| HU Feld | — | `UNKNOWN` / out of scope |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-31 Baseline | USB ≫ WiFi Mode-A; integrity clean nach Fill-Fix |
| 2026-11-01 Gate10A | Path A tot; Path B preferred |
| 2026-11-02 Capability | Soft-Perf-Raum kalibriert; nächster Gewinn außerhalb Soft-MSC |

## Abweichungen vom „Lehrbuch“

Analyzer-Marketing vs. Epistemic: „Protocol Analyzer“ hier = Class-Layer Lab, nicht Wire-Sniffer. Soft Path-B/L0-Sim ≠ Live-D+/D−.

## Offene Fragen

- Kontroll-Host Definition für Transparenz jenseits OTG-Loop?
- Path-B Hardware Bring-up Priorität vs. Feld?

## Verwandte Applications / Methods

- Method [`usb-otg-loop-baseline`](../../../methods/usb-otg-loop-baseline.md)
- Apps `usb-msc`, `esp-usb-host`, `usb-aoa`
