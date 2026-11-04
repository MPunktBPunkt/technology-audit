# Status / Gate exits — esp32.bt-analyzer

```yaml
updated: 2026-11-04
fw: "0.3.0"
topology: F_ONCHIP
upstream_commit: 07532b3
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
| BT11–BT13 | MEASURED | peer/long/stress in `LAB_GATES_BT5_13_20261104T162638Z` |
| L2 ATT probe | MEASURED (bounded) | `/api/bt/gatt/read-name` · ≠ Air / ≠ full GATT |
| BT16 CAPABILITY | MEASURED | connected + ATT + HCI |
| BT16 BENCHMARK | **MEASURED PASS** (20 B matrix) | `LAB_BT16_20261104T161828Z` · Notify@200 B still CAPABILITY-only |
| BT14 | **ready for external review** | gate-result → GATE_EXITS |
| BT15 | deferred | RF/Air separate |
| BT17 Classic audio | deferred after BT19 | separate Bluedroid flavor · not thin host |
| BT19 timeline | MEASURED scaffold | clock-offset estimation · PTP=NO · shared_clock=NO |

## Claim boundary (must stay)

| Claim | Status |
|-------|--------|
| HCI capture = RF/Air | **REJECTED** |
| Classic BR/EDR on ESP32-S3 on-chip | **REJECTED** |
| Thin ATT name read = full GATT stack | **REJECTED** (L2 probe only) |
| Universal HID / A2DP host | **REJECTED** (analyzer ≠ host) |
| kB/s without loss split = benchmark | **REJECTED** |

## Repro

```bash
cd esp32.bt-analyzer
python3 tools/lab_run_gates.py
python3 tools/lab_bt16_throughput.py --modes notify,write --mtus 23,247 --payloads 20 --duration 30 --repeats 2
python3 tools/lab_gate_exits.py
python3 tools/lab_multi_node_timeline.py --seconds 15
```
