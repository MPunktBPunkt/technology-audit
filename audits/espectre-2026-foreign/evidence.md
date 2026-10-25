# Evidence — espectre-2026-foreign

Desk 2026-10-25 · **standard_version 0.7.1** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/francescopace/espectre | `5866bff6aa3a8ac41ed70d2476c115ea6285b277` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-ESPECTRE-2026-10-25-001` | Wi-Fi CSI motion sensor; no camera/mic/radar; on-device motion+score; privacy/consent guide | `FACT` | README |
| `EVID-ESPECTRE-2026-10-25-002` | Production timing: `csi_target_pps` 100, window 1000 ms, eval 250 ms, ≥70 % slots; TemporalCsiSampler ≤1 pkt/slot | `FACT` | ALGORITHMS.md, temporal_csi_sampler.h |
| `EVID-ESPECTRE-2026-10-25-003` | Lightweight (2-feature statistical) vs HighAccuracy (8-feature MLP, `ml_weights.h`); AGC on | `FACT` | ALGORITHMS.md, high_accuracy_detector.h |
| `EVID-ESPECTRE-2026-10-25-004` | Traffic modes ping/dns/dns_tcp/wifi_raw/external; two-device peer Null Data; chip matrix C6/C5/C3/S3/S2/Classic | `FACT` | CSI.md, README |
| `EVID-ESPECTRE-2026-10-25-005` | Published performance report (holdout/selection replay metrics, 2026-10-21) | `FACT` | docs/performance/README.md |
| `EVID-ESPECTRE-2026-10-25-006` | Layers core→runtime→frontend (ESPHome/Native/Matter); Micro-ESPectre path | `FACT` | ARCHITECTURE.md, README |
| `EVID-ESPECTRE-2026-10-25-007` | License GPLv3 (+ commercial option); Espressif esp-csi community recognition claimed | `FACT` | README, LICENSE |
| `EVID-ESPECTRE-2026-10-25-008` | Does not identify/count people or prove empty room / replace certified safety systems | `FACT` | README |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-25 | Desk-Bootstrap CSI Motion Sheet + Kampagne 0.7.1 |
