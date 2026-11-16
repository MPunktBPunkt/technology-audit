# Status / Gate exits — esp32.bt-analyzer

```yaml
updated: 2026-11-16
fw: "0.3.20"
topology: HCI_TCP dual-leg (.131 phone · .87 car)
upstream_commit: 0352824   # + local 0.3.20 (writeAll retry, task notify, prefer_bt default, etch_codec, f20_sim, :8081 BMW Connected Lab)
car_next: Lab test `--hu-profile f20_sim` against OnePlus · Field B3 transparent RFCOMM relay (.131↔.87) for full 5298-B capabilities dump
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
| A6 HU link | MEASURED PASS | `FIELD_A6_HU_20261113T062824Z` · BMW 38304 / Numeric Comparison via `bt-pair-agent` |
| B1 HU SDP state A/B | MEASURED | `FIELD_B1_FROM_A6_20261113T062824Z` (decoded from A6 btsnoop) · SPP `0x1101` ch 6–10, `deca-fade` ch 5 · [`bmw-nbt-evo`](applications/bmw-nbt-evo.md) |
| HFP SLC .87 ↔ HU | MEASURED FIXED | `lab_hfp_stack.py hfp-off --apply` → 0× `AT+` in B2 (`FIELD_B2_20261113T154728Z`) |
| B2 / P0 BCL transport `.87` ↔ F20 SCN 6 | MEASURED PASS | `FIELD_P0_HOLD_20261115T132501Z` / `FIELD_BURST_20261115` · `HS v5/iid14/0x4000`, `SP2\|SP4`, WD `p50=159,5 ms`, `OPEN 4004` alone → `ACK 8` + silence |
| F20 Connected Etch + SAS + AM/RHMI/CDS | MEASURED | `DEEP_FORENSIC_ETCH_SAS_20261116` · sdbm-5381 hashes resolve 100 % of F20 headers (`_result_sas_certificate` 16 B, 559-B RSA-4096 `sas_login`, `_result_sas_login`, `_result_rhmi_getCapabilities` 5306 B, 37× CDS) |
| Full F20 HU Simulator (`f20_sim` + `:8081` BMW Lab UI) | TEST PASS (121/121) | `tools/etch_codec.py`, `controller/bmw_lab.py`, `tools/bcl_etch_stub.py` (`v0.3.20`) |

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
