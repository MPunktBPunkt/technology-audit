# Status / Gate exits — esp32.bt-analyzer

```yaml
updated: 2026-11-04
fw: "0.3.1"
topology: F_ONCHIP
upstream_commit: c251b6c
```

Classification key: `FACT` · `MEASURED` · `INFERENCE` · `UNKNOWN` · `REJECTED`

## Gate matrix (project green candidate)

| Gate | Exit class | Evidence / pin |
|------|------------|----------------|
| BT0–BT3 | MEASURED | onchip.ready, VHCI HCI frames |
| BT4 | MEASURED | `:9753` BTAC · drain blocked while BTAC owns ring |
| BT5–BT6 | MEASURED | PSRAM 512 · `lab_run_gates` drops_delta=0 |
| BT7–BT8 | MEASURED | JSONL + PCAPNG LINKTYPE 201 · `resync` ≠ `gaps` |
| BT9 | MEASURED | leConnected Central↔Peripheral |
| BT10 | MEASURED | classicDiscoverable + Write_Local_Name + inquiry HCI |
| BT11–BT13 | MEASURED | peer/long/stress in `LAB_GATES_BT5_13_*` |
| L2 ATT probe | MEASURED (bounded) | `/api/bt/gatt/read-name` · ≠ Air / ≠ full GATT |
| BT16 CAPABILITY | MEASURED | connected + ATT + HCI |
| BT16 BENCHMARK | **MEASURED PASS** (20 B matrix) | `LAB_BT16_20261104T161828Z` |
| BT18 GATT Client Flavor | **MEASURED PASS** MVP | `LAB_BT18_GATT_20261104T171044Z` · STIMULUS · ≠ full GATT |
| BT14 | **ready for external review** | gate-result → GATE_EXITS |
| BT15 | deferred | RF/Air separate |
| HOGP / FTMS Flavors | deferred | after BT18 |
| BT17 Classic audio | deferred | after HOGP/FTMS · `.87` only |
| BT19 timeline | MEASURED scaffold | clock-offset estimation · PTP=NO |

## Claim boundary (must stay)

| Claim | Status |
|-------|--------|
| HCI capture = RF/Air | **REJECTED** |
| Classic BR/EDR on ESP32-S3 on-chip | **REJECTED** |
| Thin ATT / BT18 MVP = full GATT stack | **REJECTED** |
| Universal HID / A2DP host | **REJECTED** (Flavor path only) |
| kB/s without loss split = benchmark | **REJECTED** |

## Repro

```bash
cd esp32.bt-analyzer
python3 tools/lab_gatt_client.py
python3 tools/lab_gate_exits.py
```
