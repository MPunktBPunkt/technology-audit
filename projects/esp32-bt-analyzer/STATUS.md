# Status / Gate exits — esp32.bt-analyzer

```yaml
updated: 2026-11-12
fw: "0.3.19"
topology: HCI_TCP dual-leg (.131 phone · .87 car)
upstream_commit: 0352824   # + local 0.3.19 changes (coex API, a2dp_budget, framer session-init), not yet pushed
car_next: A6 then B1 (docs/CAR_A6_B1.md in upstream) — blocked by weak car WiFi
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
| 62-vs-37 ACL gate | MEASURED PASS_37 | ~41–45 kB/s `none` · [`esp-wifi-bt-coex`](applications/esp-wifi-bt-coex.md) |
| A2DP single path (Phone → `.131`) | MEASURED | stable · [`bluetooth-a2dp`](applications/bluetooth-a2dp.md) |
| A2DP dual relay (Phone → `.131` → BlueZ → `.87` → headset) | MEASURED (choppy) | coex budget ≈ SBC bitpool 53 |
| Coex API `/api/hci/coex` (0.3.19) | UNKNOWN | code only; A/B `lab_hci_coex_ab.py` pending |
| BCL synth + RFCOMM Dummy | MEASURED (TEST) | `applications/bmw-bcl.md` |
| BCL framer session-init `12 34 56 78` | TEST (host) | desk expectation BclCarLink, not HU wire |
| Dummy-HU SDP SPP | MEASURED (TEST) | `CANDIDATE_STRONG` lab only |
| B0.7 Dummy-HU SPP + A2DP sink, answers session init | UNKNOWN | tool `lab_bcl_dummy_hu_a2dp.py` + host tests; not yet run on .108 |
| A6 HU link / B1 real SDP | UNKNOWN | car runbook — channel X not 5; car WiFi too weak on first try |

## Claim boundary

| Claim | Status |
|-------|--------|
| HCI = Air | **REJECTED** |
| Peer stub = real keyboard/ergometer | **REJECTED** |
| FTMS Write Success = Wirkung | **REJECTED** |
| Analyzer Core = Universal Host | **REJECTED** |
| Better WiFi RSSI raises BT ACL rate | **REJECTED** (coex-bound) |
| Dual A2DP relay = transparent audio proxy | **REJECTED** (two terminated links, BlueZ decode/encode) |

## Repro

```bash
python3 tools/lab_hogp_ftms.py
python3 tools/lab_hci_tcp_62_37_gate.py   # on .108, bridges up
python3 tools/lab_hci_coex_ab.py          # fw ≥ 0.3.19
```
