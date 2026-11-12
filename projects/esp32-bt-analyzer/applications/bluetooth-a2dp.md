# Project Application: bluetooth-a2dp in esp32-bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
upstream: https://github.com/MPunktBPunkt/esp32.bt-analyzer
upstream_fw: ["0.3.16", "0.3.19"]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R2   # lab MEASURED: single path stable, dual relay audible but choppy
  reusability: W2
```

## Rolle im Projekt

A2DP **nicht** im Analyzer-Core, sondern in **BlueZ auf Linux** über zwei ESP32-Controller
(HCI über TCP). Messobjekt: Relay Phone → `.131` → BlueZ (Sink, decode) → BlueZ (Source,
encode) → `.87` → Kopfhörer. Stack-Scope laut Sheet: BlueZ-HCI-Host ≠ Bluedroid.

## Architektur / Datenfluss

```text
Phone ─A2DP─ .131 ─TCP─┐                                  ┌─TCP─ .87 ─A2DP─ headset
                       └─ BlueZ .108: sink → PCM → source ┘
```

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `docs/A2DP_RELAY.md` | Budget, Stack-Optionen, Schritte R0–R4 |
| `tools/a2dp_budget.py` | SBC-Rate je Bitpool; AVDTP Set Configuration aus btmon |
| `docs/evidence/LAB_HCI_TCP_A1A5_20261111T204600Z.*` | single path / dual relay |

## Ebene C — Evidence

| Claim | Evidence | Status |
|-------|----------|--------|
| Phone → `.131` A2DP über HCI TCP hörbar und stabil (single path, ~45 kB/s toHost Peak) | `LAB_HCI_TCP_A1A5_20261111T204600Z` | `MEASURED` |
| Dual relay Phone → `.131` → BlueZ → `.87` → Kopfhörer hörbar | same | `MEASURED` (abgehackt) |
| Ursache abgehackt = Coex-Budget, kein Queue-Bug | ring/drops + Sweeps ([`esp-wifi-bt-coex`](esp-wifi-bt-coex.md)) | `INFERENCE` |
| SBC joint stereo 44.1 kHz: bitpool 53 ≈ 328 kbit/s ≈ 42 kB/s auf HCI | `a2dp_budget.py` (SBC-Formel + RTP/L2CAP/ACL) | `FACT` (Rechnung) |
| Bitpool 35 ≈ 229 kbit/s ≈ 29 kB/s (≤ 80 % von 38 kB/s) | same | `FACT` (Rechnung) |
| PipeWire Source: bitpool bis 64 @44.1k, kein Config-Key, −2 bei Socket-Stau | PipeWire `spa/plugins/bluez5/a2dp-codec-sbc.c` (gelesen 2026-11-12) | `FACT` (Code) |
| bluez-alsa `--sbc-quality` begrenzt Source, nicht Sink-Caps | bluez-alsa `src/a2dp-sbc.c`, `bluealsad.8` (gelesen 2026-11-12) | `FACT` (Code/Doc) |
| Phone-Leg per Linux-Config drosselbar | beide Stacks | `REJECTED` (nur Sink-Caps-Patch) |
| Coex-Modus `a2dp` + Bitpool ≤ 35 ⇒ Relay ohne Aussetzer | R2–R4 offen | `UNKNOWN` |

## Epistemik

```text
YES:  Hörtest + Agent-Zähler; Bitraten-Rechnung; Stack-Verhalten aus Quellcode
NO:   Bluedroid-on-chip A2DP; Car-HU-A2DP; Air-Capture
```

## Lessons

- Zwei Legs auf zwei ESPs verdoppeln nicht das Budget pro Leg — jedes Leg trifft
  allein auf das Coex-Limit seines ESP.
- Für die BMW-Analyse (BCL über RFCOMM, AVRCP) ist das A2DP-Budget irrelevant;
  das Relay ist ein eigener Use Case.
