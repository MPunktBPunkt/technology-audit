# Project Application: bmw-bcl in esp32-bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: bmw-bcl
status: active
sheet: ../../../technologies/bmw-bcl/SHEET.md
upstream: https://github.com/MPunktBPunkt/esp32.bt-analyzer
upstream_commits: [0322f2d, 0352824]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0   # lab TEST only — real HU still UNKNOWN
  reusability: W2
```

## Rolle im Projekt

**Lab messkette for BCL-over-BT**, not HU wire FACT. Validates that HCI-TCP →
BlueZ → RFCOMM → streaming 8-byte BCL framer works end-to-end with a **synthetic**
stream (hu-probe CaC1) and that a Dummy-HU can advertise SPP for B1 rehearsal.

Real F20 / NBT Evo SDP/BCL remain **UNKNOWN** until car A6/B1/B2.

## Architektur / Datenfluss (lab)

```text
Dummy-HU .87 ──RFCOMM── .131 / BlueZ .108 ──HCI TCP── capture
     │                      │
     │ ProfileManager SPP   └─ bcl_sdp_probe / bcl_framer
     └─ "BMW Connected" ch.5 (lab only — not BMW channel expectation)
```

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `tools/bcl_framer.py` | streaming BCL framer (desk header contract) |
| `tools/lab_bcl_synth_stream.py` | offline + RFCOMM synth lab |
| `tools/lab_bcl_dummy_hu_sdp.py` | ProfileManager SPP Dummy-HU |
| `tools/bcl_sdp_probe.py` | B1 SDP probe |
| `docs/CAR_A6_B1.md` | car runbook A6→B1 |
| `docs/evidence/LAB_BCL_SYNTH_STREAM_*` | synth + RFCOMM evidence |
| `docs/evidence/LAB_BCL_DUMMY_HU_SDP_20261112T062151Z.*` | Dummy-HU `CANDIDATE_STRONG` |

## Ebene C — Evidence

| Claim | Evidence | Status |
|-------|----------|--------|
| Framer: HANDSHAKE/DATA(`SYNTH01`)/UNKNOWN + sticky PayloadTooLarge | `LAB_BCL_SYNTH_STREAM_20261112T060144Z` | `MEASURED` (synthetic) |
| Synth BCL bytes survive RFCOMM over HCI TCP | `LAB_BCL_SYNTH_STREAM_20261112T060654Z` | `MEASURED` (lab Dummy) |
| Dummy-HU SPP `0x1101` / name BMW Connected / RFCOMM 5 visible via sdptool | `LAB_BCL_DUMMY_HU_SDP_20261112T062151Z` | `MEASURED` (lab Dummy) |
| Real HU offers SPP/BCL | — | `UNKNOWN` |
| Lab RFCOMM channel 5 = BMW channel | — | `REJECTED` as claim |

## Epistemik

```text
YES:  own lab can advertise SPP and decode synthetic BCL over RFCOMM
NO:   NBT Evo / F20 wire FACT
NO:   channel 5 as BMW expectation (measure X from SDP)
```

## Next (car)

A6 link `.87`↔HU → B1 SDP (UUID / name / **channel X**) → only then B2 RFCOMM payload.
See upstream `docs/CAR_A6_B1.md`.
