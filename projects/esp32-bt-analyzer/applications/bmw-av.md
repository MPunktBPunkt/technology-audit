# Project Application: bmw-av in esp32-bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: bmw-av
status: active
sheet: ../../../technologies/bmw-av/SHEET.md
maturity:
  technology: R2
  implementation: R1
  field_evidence: R3
  reusability: W2
updated: 2026-11-23
audit: ../../../audits/bmw-av-session-control-vs-audio-2026-11-21/
```

## Rolle im Projekt

Misst und dokumentiert den **Etch-AV Control-Pfad** der Connected Music-Session
(`av_create` → ENTERTAINMENT → PLAY) und hält die **Audio-Boundary** offen, bis
Dual-Plane-Evidence vorliegt.

## Ebene C — Evidence

| Claim | Evidence | Status |
|-------|----------|--------|
| AV create/request/granted/PLAY in B3 | `FIELD_B3_GATEB_…/forensic/AV_EVENTS.json` | `FIELD FACT` |
| PLAY anchor `P@0x000315a6` | PLAY_BOUNDARY_SKIM / Timeline | `FIELD FACT` |
| post-PLAY bulk on dest 4004 | same | `FIELD FACT` |
| bulk = audio | — | `NOT PROVEN` |
| audible | Operator note | `NOT OBSERVED` |

## Next

Dual-Plane field protocol (BCL/Etch + audio candidate plane) — see sheet +
[`esp32-bt-analyzer-b3-relay-topology-2026-11-21`](../../../audits/esp32-bt-analyzer-b3-relay-topology-2026-11-21/).
