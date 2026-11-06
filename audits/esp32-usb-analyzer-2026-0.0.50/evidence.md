# Evidence — esp32-usb-analyzer-2026-0.0.50

Lab 2026-11-02 · Upstream FW **0.0.50** @ `60244b3` (Controller **0.0.41**).  
Basis: `https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/`  
Prior Pilot-Evidence (0.0.35 @ `b2c9987`): [`../esp32-usb-analyzer-2026-pilot/evidence.md`](../esp32-usb-analyzer-2026-pilot/evidence.md)

Rohdaten bleiben im Quellenrepo — hier Claims + Links.

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBA-2026-11-02-001` | OTG MSC READ peak **917 kB/s** (chunk=8); sustained 3× **907–914 kB/s**; pattern fail **0** | `MEASURED` | [LAB_BASELINE_MEASURED.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_BASELINE_MEASURED.md) · [JSON T195715Z](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_BASELINE_20261102T195715Z.json) · [Capability Report](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/reports/2026-11-02-capability-audit-0.0.50.md) |
| `EVID-USBA-2026-11-02-002` | Single-sector MSC RTT p50 **~0.80 ms**; 8-sector p50 **~4.2 ms** | `MEASURED` | same Baseline |
| `EVID-USBA-2026-11-02-003` | WiFi TCP ESP↔ESP peak **332 kB/s** (2048 B×64); gaps **0** | `MEASURED` | same Baseline |
| `EVID-USBA-2026-11-02-004` | TCP sliding-window **pipeline** sweet spot ~**436 kB/s** (4096×win=8, FW 0.0.37); win≥16 cliff — noch ≪ USB | `MEASURED` | [LAB_TCP_PIPELINE_MEASURED.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_TCP_PIPELINE_MEASURED.md) |
| `EVID-USBA-2026-11-02-005` | Capability Audit **7/7**: Enum + MSC + TCP + sync-offset + BOT class-hook + Gate10 + Path-A-rejected | `MEASURED` | [LAB_CAPABILITY_AUDIT_MEASURED.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_CAPABILITY_AUDIT_MEASURED.md) · [JSON T195731Z](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_CAPABILITY_AUDIT_20261102T195731Z.json) |
| `EVID-USBA-2026-11-02-006` | Path A „GPIO19/20 am OTG = FS-Sniffer“ **FALSIFIED**; Path B external tap preferred; E1.1 ~2.1 Msps / 0 nutzbare Edges | `REJECTED` (Path A) / `MEASURED` (feasibility) | [LAB_GATE10A_FEASIBILITY.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_GATE10A_FEASIBILITY.md) · [E1.1](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_GATE10A_E11_GPIO_SAMPLE.md) |
| `EVID-USBA-2026-11-02-007` | Observer-effect OTG-Loop: Direct MSC ~844 kB/s vs WiFi MSC-proxy ~25 kB/s (Δ~151 ms) — **nicht** PC↔Stick-MITM | `MEASURED` (lab loop) | [LAB_OBSERVER_EFFECT_BASELINE.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_OBSERVER_EFFECT_BASELINE.md) |
| `EVID-USBA-2026-11-02-008` | Gate10 Perf Campaign **9/9** (Enum/MSC/TCP/PathA/E1.1/PathB-GPIO-lab/L0-sim/Observer/EP0-ctrl-neg 8/8); sync residual≈6952 µs = Offset only | `MEASURED` / hard-µs-lock `REJECTED` | [LAB_GATE10_PERF_CAMPAIGN.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_GATE10_PERF_CAMPAIGN.md) · [JSON T195737Z](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/evidence/LAB_GATE10_PERF_CAMPAIGN_20261102T195737Z.json) |
| `EVID-USBA-2026-11-02-009` | Soft-USB-Cycle / Soft-Unplug ≠ VBUS-Unplug; Live D+/D− und Path-B-soldered PHY **nicht** claimed | `REJECTED` / not claimed | Capability Report §5 · [GATE10_STATUS](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/60244b3/docs/GATE10_STATUS.md) · Handover 0.0.50 |
| `EVID-USBA-2026-11-02-010` | Lab boards unverändert: `.88` Host / `.89` Device · DUT `303a:1001` ANALYZER FS · Controller `:8080` 0.0.41 allowlisted proxy | `FACT` (lab inventory) | Capability Report §1 · LAB_INVENTORY |

## Vergleich Pilot → 0.0.50

| Kanal | Pilot 0.0.35 (`b2c9987`) | **0.0.50** (`60244b3`) |
|-------|-------------------------|-------------------------|
| USB MSC peak | ~934 kB/s | **917 kB/s** |
| USB sustained | ~934–937 | **907–914** |
| Pattern loss | 0 | **0** |
| TCP peak (campaign) | ~139 kB/s ack-each | **332 kB/s** |
| TCP pipeline (0.0.37) | — | bis ~**436 kB/s** (noch ≪ USB) |
| Path A sniffer | UNKNOWN / research | **REJECTED** |
| Observer-Loop | Exit offen | **MEASURED** (loop only) |
| Capability harness | — | **7/7** + Gate10 **9/9** |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Transparent MITM PC↔Stick | `UNKNOWN` | Observer-Loop ≠ Transparenz-FACT |
| Passives Live-D+/D− | `UNKNOWN` | Path-B HW offen (`009`) |
| Hard synchronized µs clocks | `REJECTED` until proven | Offset only (`008`) |
| HU AOA / BCL / MSC Feld | `UNKNOWN` | deferred; Fremd-DUT Visibility ≠ Wire-FACT |
| Mode-A ausreichend für sustained HU Bulk | `REJECTED` ohne SF bei aktuellem Δ | Coex + STORE_FORWARD |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-31 | Pilot Lab Baseline MSC/TCP AOA/Enum @ 0.0.35 |
| 2026-11-01 | 0.0.36–0.0.41: Ctrl-Neg, TCP pipeline, Gate10A Path-A kill, Observer, Path-B soft |
| 2026-11-02 | 0.0.50 Capability Audit 7/7 + frische Baseline; technology-audit Import @ `60244b3` |
