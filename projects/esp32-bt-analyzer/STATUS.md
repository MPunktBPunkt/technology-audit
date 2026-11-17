# Status / Gate exits — esp32.bt-analyzer

```yaml
updated: 2026-11-17
fw: "0.3.20"
topology: HCI_TCP dual-leg (.131 phone · .87 car)
upstream_commit: 4b24cf4   # dual 0.3.20 align; P0–P2 in-process PASS; USB→.131 Air PARTIAL (WD abort); dual-ESP Air FAIL
audits:
  - ../../../audits/esp32-bt-analyzer-f20-connected-2026-11-17/
  - ../../../audits/bimmergestalt-rhmi-checkresource-2026-11-17/
car_next: W0 Watchdog Air stabil → W1 checkResource → W2 digest-matched setResource → W3 initialize → W4 setData(447) → W5 paced Action; Resource-Auth = P0 blocker
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
| Full F20 HU Simulator (`f20_sim` + `:8081` BMW Lab UI) | TEST PASS (121/121 → 127 w/ P0–P2) | `tools/etch_codec.py`, `controller/bmw_lab.py`, `tools/bcl_etch_stub.py` (`v0.3.20`) |
| Etch Tiny-Int codec fix (0x00–0x7F / 0xC0–0xFF) | MEASURED | Lab `LIVE_1741`: 40 Modelle / 80 Tracks / 0 Fehler — `DEEP_FORENSIC_RHMI_SCREENMIRROR_20261117` §5 |
| A2DP ≠ RHMI | MEASURED | Lab `LAB_RHMI_BROWSE_20261116T2002Z` (0 setData) vs Feld `FIELD_RHMI_BROWSE_20261117` (21 setData ACK) |
| Feld RHMI Browse + YouTube + Screen-Mirror-Kandidat | MEASURED / STRONG | `19188` Spotify→YouTube; SE typ `0x5A6F115C`; ~216 KiB burst — Deep Forensic 2026-11-17 |
| P0–P2 in-process (SE 213, digest whitelist, menu upload) | TEST PASS | `LAB_P0_P2_RESULT_20261117` |
| FW 0.3.20 dual-align + USB→`.131` Air | PARTIAL | `LAB_P0P2_FW0320_RESULT_20261117` — AM+checkResource TX; abort `wd_echo_miss_limit`; dual-ESP FAIL |
| Resource-Authorization (F20 digest whitelist) | OPEN (Hauptblocker) | Desk SHA-256 Digests; Lab stub PASS; Feld Auth fremder Bytes unbewiesen |

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
