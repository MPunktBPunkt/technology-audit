# Audit Campaign: esp32-usb-analyzer-2026-0.0.50

```yaml
id: esp32-usb-analyzer-2026-0.0.50
project_id: esp32-usb-analyzer
started: 2026-11-02
ended: 2026-11-02
status: closed
reviewed_commit: 60244b3
profile: lab-tool
standard_version: "0.7.1"
prior_audit: esp32-usb-analyzer-2026-pilot
upstream_pin:
  repo: https://github.com/MPunktBPunkt/esp32.usb-analyzer
  commit: "60244b3"
  fw_version: "0.0.50"
  controller: "0.0.41"
  lab_baseline: "LAB_BASELINE_20261102T195715Z"
reuse_outcomes:
  reused: [usb-dual-esp-observe-proxy, usb-msc, esp-usb-host, esp32-s3-usb-wifi-coex, usb-otg-loop-baseline]
  new: []
  process: "0.0.35→0.0.50 Lab MEASURED import; Capability-Harness + Path-A-Kill + Observer-Baseline; TCP-Pipeline Delta"
  decisions_touched: [otg-loop-baseline-stable, path-a-gpio-sniffer-falsified, tcp-pipeline-still-below-usb, observer-loop-not-mitm]
  cycles_avoided: [more-msc-sweeps-instead-of-path-b-hw, gpio19-20-as-fs-sniffer]
```

## Ziel

Nach großem Upstream-Update (0.0.35→**0.0.50**) frische OTG-/TCP-/Capability-Messungen in die KB holen; Pilot-Claims revalidieren; Path-A-Falsifikation und Observer-Loop-Baseline verankern — **ohne** Live-L0-, Path-B-PHY- oder HU-Wire-Claims.

## Scope

Siehe [SCOPE.md](../../projects/esp32-usb-analyzer/SCOPE.md). Upstream FW **0.0.50** @ `60244b3` (Host `.88` + Device `.89` gleicher FW; Controller **0.0.41**). Messungen 2026-11-02T19:57Z OTG-Loop + WiFi TCP + Gate10-Perf.

**Im Scope:** MSC Integrity/Rate, TCP Integrity, Enum-Outcome, BOT class-hook, Path-A-Rejection, Observer-Loop, Capability-Harness 7/7, Gate10 soft 9/9.

**Nicht im Scope:** passives Live-D+/D−, gelötetes Path-B-Frontend, BMW-HU-Wire, USB-IF, HS, transparentes PC↔Stick-MITM.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SCOPE/INVENTORY auf `60244b3` / 0.0.50 | erfüllt |
| 2 | Evidence-IDs auf Upstream `LAB_*` 2026-11-02 | erfüllt |
| 3 | Apps `usb-msc` / Coex / Observe-Proxy mit neuen Zahlen | erfüllt |
| 4 | Sheet `usb-dual-esp-observe-proxy` Path-A + Observer + Harness | erfüllt |
| 5 | Method `usb-otg-loop-baseline` + Capability-Harness-Hinweis | erfüllt |
| 6 | `ta-assist check` grün | erfüllt (0 Errors, 2026-11-02) |
| 7 | Transparent MITM / Live-L0 / HU | bewusst deferred (Pilot Exit 7/8) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| OTG-Baseline 0.0.50 ≈ Pilot | Pattern-fail / Rate-Kollaps seit 0.0.35? | `EVID-USBA-2026-11-02-001` | Nein — USB ~917 kB/s, failB=0; Band bestätigt | MEASURED |
| TCP-Pipeline schließt USB-Lücke? | Peak TCP ≥ Peak MSC? | `EVID-USBA-2026-11-02-003` / `004` | Nein — 332≪917 kB/s; H2 bleibt tot | MEASURED |
| Path A GPIO = FS-Sniffer? | GPIO19/20 unter OTG nutzbar? | `EVID-USBA-2026-11-02-006` | **REJECTED** — interne PHY-Pins | KNOWN BEFORE / Lab bestätigt |
| Observer-Proxy = transparent MITM? | Loop-Baseline ⇒ PC↔Stick? | `EVID-USBA-2026-11-02-007` | **REJECTED** — nur OTG-Loop Δ | KNOWN BEFORE TEST |
| Weitere MSC-Sweeps als P0? | Soft-Perf-Raum erschöpft? | Upstream Capability-Bericht §6 | Ja für Soft-Lab — nächster Gewinn Path-B/Feld | DISCOVERED DURING TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-USBA-2026-11-02-001` | Vor Rate-Claims: beide Nodes gleiche analyzer-FW; Fremd-DUT ≠ `lab_sector_v1`-Pattern | KNOWN BEFORE TEST |
| `EVID-USBA-2026-11-02-006` | Kein Design das GPIO19/20 am S3-OTG als Packet-Sniffer verkauft | DISCOVERED DURING TEST (Gate10A) |
| `EVID-USBA-2026-11-02-007` | Observer-Zahlen nur mit Topologie-Tag `otg_loop`; nicht als MITM-Transparenz | KNOWN BEFORE TEST |
| `EVID-USBA-2026-11-02-005` | Soft-USB-Cycle / Soft-Unplug ≠ VBUS-Unplug in Docs & UI | KNOWN BEFORE TEST |
| `EVID-USBA-2026-11-02-008` | Controller-Sync = Offset-Schätzung; residual_us nicht als Hard-Lock lesen | RETROFIT (Pilot 014) |

## Kill-Kriterien

**Hypothese H1 (Revalidation):** Dual-ESP OTG-Loop liefert unter 0.0.50 weiterhin bit-integre MSC READ bei ~0.9 MB/s.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Pattern-fail Bytes > 0 bei chunk≤8, clean LBA, gleicher FW | nicht eingetreten (`001`) |
| 2 | Peak ≪ Pilot-Band (<~0.7 MB/s ohne Erklärung) | nicht eingetreten |

**Hypothese H2 (Revalidation):** Mode-A/Pipeline schließt USB-MSC-Nutzrate.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | TCP peak ≪ USB MSC peak | **Kill getroffen** — 332 vs 917 kB/s |

**Hypothese H3:** Path A (CPU-GPIO an OTG-Pins) ist FS-Packet-Sniffer.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Feasibility sagt `pathA_snifferOk=false` / interne PHY | **Kill getroffen** (`006`) |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| OTG-Loop Baseline (+ Capability Harness) | [`usb-otg-loop-baseline`](../../methods/usb-otg-loop-baseline.md) |
| BOT Command Observation | [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md) |
| USB↔WiFi Discrimination | [`usb-wifi-coex-discrimination`](../../methods/usb-wifi-coex-discrimination.md) |

## Bezug Inventar

[INVENTORY](../../projects/esp32-usb-analyzer/INVENTORY.md) · [evidence](evidence.md) · Prior: [`esp32-usb-analyzer-2026-pilot`](../esp32-usb-analyzer-2026-pilot/)

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Capability 7/7 + Baseline 0.0.50 | `001`…`005` | `applications/usb-msc.md`, Coex, Observe-Proxy |
| Path A falsified | `006` | Sheet `usb-dual-esp-observe-proxy` |
| Observer-Loop | `007` | Sheet + App Observe-Proxy |
| Gate10 soft 9/9 | `008` | SCOPE Coverage-Lücken / FOLLOW-ON |

## Ergebnisse

| Artefakt | Pfad |
|----------|------|
| Gewachsen | `usb-dual-esp-observe-proxy`, `usb-msc` App, Coex App, Method Baseline |
| Upstream Bericht | `docs/reports/2026-11-02-capability-audit-0.0.50.md` |
| Rohdaten | `LAB_CAPABILITY_AUDIT_*`, `LAB_BASELINE_20261102T195715Z.json`, `LAB_GATE10_PERF_CAMPAIGN_20261102T195737Z.json` |

## Lessons → Transfer

- USB-MSC Soft-Ceiling bleibt ~**0.90–0.93 MB/s** über FW-Spanne 0.0.14→0.0.50 — Stack, nicht Wire.
- TCP Mode-A stieg ~139→**~332 kB/s** (Pipeline 0.0.37) — immer noch Bottleneck vs USB.
- Path A ist **tot** als Sniffer-Idee; Path-B-HW ist der nächste messbare L0-Schritt.
- Observer-Proxy-Δ auf dem OTG-Loop ist MEASURED — Transparenz-Claim bleibt getrennt.
- `lab_capability_audit.py` ist das Regressionstor vor Releases (7/7 inkl. Gate10).

## Offene Punkte nach Abschluss

- Live Path-B PHY / echte `.l0samp` Korrelation n≥100
- Transparent MITM mit Kontroll-Host (nicht nur Loop)
- HU/Feld AOA·MSC (Analyzer + hu-probe/pidrive)
- Power-Cycle-Persistenz ≠ Soft-Reboot (Upstream Handover P0)
