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
  field_evidence: R1   # HU SDP + B2-A accept ch5/6 MEASURED; BCL payload still UNKNOWN
  reusability: W2
updated: 2026-11-13
```

## Rolle im Projekt

**Lab messkette for BCL-over-BT**, not HU wire FACT. Validates that HCI-TCP →
BlueZ → RFCOMM → streaming 8-byte BCL framer works end-to-end with a **synthetic**
stream (hu-probe CaC1) and that a Dummy-HU can advertise SPP for B1 rehearsal.

Real F20 / NBT Evo SDP/BCL remain **UNKNOWN** until car A6/B1/B2.

**Messbedingung (Secondary):** Während A6/B1/B2 SDP- und RFCOMM-Captures **MyBMW und
AAIdrive deaktivieren** (Force-Stop / nicht parallel), sonst SPP-/BCL-Kanal-Contention —
[`supra-idrive6-android-auto-2026-secondary`](../../../audits/supra-idrive6-android-auto-2026-secondary/)
(`EVID-SUPRA-2026-11-13-003`/`004`). Zustand im Protokoll dokumentieren.

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
| Framer erkennt Phone→HU Session-Init `12 34 56 78` an Frame-Grenzen (sonst sticky PayloadTooLarge durch len=0x5678) | host tests `TestSessionInit` (0.3.19) | `TEST` — Erwartung aus [`bmw-bcl-handshake`](../../bimmergestalt-idrive-refs/applications/bmw-bcl-handshake.md) |
| Dummy-HU muss A2DP-Senke **und** SPP-Server sein, sonst versucht die App kein RFCOMM | [`bmw-bcl-rfcomm`](../../bimmergestalt-idrive-refs/applications/bmw-bcl-rfcomm.md) (`EVID-BCLRF-2026-11-12-005`) → B0.7 `lab_bcl_dummy_hu_a2dp.py` | `FACT` (BclCarLink) · synth PASS · external MyBMW/AAIdrive `NO_RFCOMM` |
| MyBMW + AAIdrive open RFCOMM to Dummy-HU after re-pair (A2DP+SPP gate up) | `LAB_BCL_DUMMY_HU_A2DP_20261112T172006Z` | early `NO_RFCOMM` = **eligibility symptom** — superseded by phone BCL PASS below |
| Real HU offers SPP | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` — ch 6–10 SPP `0x1101`, ch 5 Vendor-UUID `deca-fade` ([bmw-nbt-evo](bmw-nbt-evo.md)) |
| HU opens SPP/BCL in state A (idle, no phone app) | `FIELD_B1_FROM_A6_20261113T062824Z` | `REJECTED` for state A — only HFP RFCOMM in 192 s |
| Phone can open HU ch 6 (`0x1101`) and ch 5 (`deca-fade`); HU UA, no payload | `FIELD_B2_20261113T154728Z` | `MEASURED` transport; BCL `UNKNOWN` |
| HU dials our observe-only SPP in state A (Apps/HFP off) | `FIELD_B2B_20261113T1653Z` | `REJECTED` inbound |
| Real HU speaks BCL on that SPP | — | `UNKNOWN` (next: state C/D ± controlled TX) |
| BclCarLink (`createRfcommSocketToServiceRecord(0x1101)`) would land on HU ch 6 | SDP order + B2-A ch 6 accept | `INFERENCE` strengthened — transport path exists |
| Lab RFCOMM channel 5 = BMW channel | — | `REJECTED` as claim (HU ch 5 exists but is `deca-fade`, not `0x1101` — number coincidence) |
| Lab can advertise F20-shaped SDP (ch5 `deca-fade` + ch6 `0x1101`) | `LAB_F20_SDP_MIRROR_20261113T174006Z` | `MEASURED` (LAB_TEST); ch7–10 identical `0x1101` blocked by BlueZ ProfileManager |
| OnePlus + MyBMW/AAIdrive vs answering Dummy (ch6 HANDSHAKE-ready, BMW 38304 CoD) | `LAB_BMW_SIM_20261113T181344Z` | early negative; later same night **PASS** |
| `b2a-tx` controlled INIT → Dummy HANDSHAKE (no KNOCK) | `LAB_B2A_TX_20261113T2157Z` | `MEASURED` (LAB_TEST) — validates BclCarLink TX-first order; F20 pending |
| OnePlus AAIdrive/MyBMW → Dummy full BCL (INIT→HS→SELECTPROTO(2)→OPEN 5001/4004→PKCS7→WD≈2.5s) | `LAB_PHONE_BCL_20261113T2201Z` + `_DECODE` | `MEASURED` — UI „verbunden mit BMW“; Wire ≠ BclCarLink@7cfd959 (SP/WD) |
| Wrong Dummy CoD → DEADBEEF+UUID probe instead of INIT | `LAB_COD_AB_BOUNCE_20261113T2355Z` · `LAB_EVENING_COD_GATE_*` · `LAB_L3_NO_HS_*` | `MEASURED` — needs ACL bounce; A2DP transport stayed idle (eof ≠ A2DP drop) |
| No WD pong → phone CLOSE 5001 @~38s; echo keeps ≥96s | `LAB_WD_PONG_20261114T0001Z` vs LAB_A2DP_CORR | `MEASURED` — lab Dummy should `--echo-watchdog` |
| BclCarLink@7cfd959 pin-drift explains wire SP(2)/WD 2.5s | desk vs wire | `REJECTED` as proven — AAIdrive uses MyBMW proxy; keep desk as structural ref only |
| HU ch5 `deca-fade` | public iAP2/MFi UUID + `BCL_BT.md` | `FACT` (identity) — **not** BCL endpoint; H-D dropped |

## Epistemik

```text
YES:  own lab can advertise SPP and decode synthetic BCL over RFCOMM
YES:  Phone (MyBMW/AAIdrive) opens RFCOMM+BCL to Dummy when CoD/SPP/A2DP/HS gate OK
YES:  Wire markers diverge from BclCarLink@7cfd959 (SELECTPROTO(2), WD≈2.5s)
YES:  Wrong CoD → DEADBEEF+UUID probe (not INIT)
NO:   NBT Evo / F20 wire BCL FACT
NO:   channel 5 as BMW BCL expectation
YES:  HU SDP measured (F20, state A/B): SPP 0x1101 ch 6–10, deca-fade ch 5
```

Desk CROSSREF (roles / source matrix): pidrive `HU-Technical-Facts.md` §10.1–10.4 ·
`bmw-bcl-rfcomm-role-2026-desk` · BimmerGestalt inventory.

## Next (car)

A6 link `.87`↔HU (**MEASURED** 2026-11-13) → B1 state A/B decoded from the A6 capture (`tools/btsnoop_decode.py`)
→ HFP AG off (`tools/lab_hfp_stack.py`, HU otherwise reopens RFCOMM every 20–35 s)
→ **B2-A** ch 6 and ch 5 (phone/ESP initiate) **+ B2-B** (HU initiate, `.87` observe-only SPP server).
Upstream runbook `docs/CAR_FIELD_1H.md`.
F20 RFCOMM initiator = **UNKNOWN** until SABM measured; B2-A negative ≠ BCL absent.
See upstream `docs/CAR_A6_B1.md` · method `docs/analysis/BCL_RFCOMM_TWO_MODE_20261113.md`.
Optional lab: B0.7 with **BclCarLink**; B2-B observe-only mode on ProfileManager (not AAIdrive alone).

**B1/B2 checklist addendum:** Phone: MyBMW + AAIdrive off (baseline); note if Connected Classic remains;
no parallel nbt-aad session if testing BCL; no BCL TX during B2-B before classification.
Secondary contention is a known confounder, not a BCL decoder / not F20-[B].
