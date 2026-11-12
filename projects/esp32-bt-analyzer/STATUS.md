# Status / Gate exits — esp32.bt-analyzer

```yaml
updated: 2026-11-12
fw: "0.3.18"
topology: HCI_TCP dual-leg (.131 phone · .87 car)
upstream_commit: 0352824
car_next: A6 then B1 (docs/CAR_A6_B1.md in upstream)
```

Classification key: `FACT` · `MEASURED` · `INFERENCE` · `UNKNOWN` · `REJECTED`

## Gate matrix

| Gate | Exit class | Evidence / pin |
|------|------------|----------------|
| BT0–BT13 | MEASURED | prior labs |
| BT16 BENCHMARK | MEASURED PASS (20 B) | `LAB_BT16_20261104T161828Z` |
| BT18 GATT Client | MEASURED PASS MVP | `LAB_BT18_GATT_*` |
| BT18b HOGP Host | MEASURED PASS (peer stub) | `LAB_BT18_PROFILES_20261104T172742Z` |
| BT18c FTMS Client | MEASURED PASS (peer stub) | same · Success≠Wirkung |
| BT17 Classic | deferred | after real-device HOGP/FTMS |
| BT15 RF/Air | deferred | separate |
| HCI_TCP A1–A5 | MEASURED | upstream `docs/HCI_TCP.md` |
| 62-vs-37 ACL gate | MEASURED PASS_37 | ~41–45 kB/s `none` |
| BCL synth + RFCOMM Dummy | MEASURED (TEST) | `applications/bmw-bcl.md` |
| Dummy-HU SDP SPP | MEASURED (TEST) | `CANDIDATE_STRONG` lab only |
| A6 HU link / B1 real SDP | UNKNOWN | car runbook — channel X not 5 |

## Claim boundary

| Claim | Status |
|-------|--------|
| HCI = Air | **REJECTED** |
| Peer stub = real keyboard/ergometer | **REJECTED** |
| FTMS Write Success = Wirkung | **REJECTED** |
| Analyzer Core = Universal Host | **REJECTED** |

## Repro

```bash
python3 tools/lab_hogp_ftms.py
```
