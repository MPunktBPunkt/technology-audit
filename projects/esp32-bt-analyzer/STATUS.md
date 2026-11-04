# Status / Gate exits — esp32.bt-analyzer

```yaml
updated: 2026-11-04
fw: "0.2.9"
topology: F_ONCHIP
upstream_commit: 542eed6
```

Classification key: `FACT` · `MEASURED` · `INFERENCE` · `UNKNOWN` · `REJECTED`

## Gate matrix (project green candidate)

| Gate | Exit class | Evidence / pin |
|------|------------|----------------|
| BT0–BT3 | MEASURED | onchip.ready, VHCI HCI frames |
| BT4 | MEASURED | `:9753` BTAC |
| BT5–BT6 | MEASURED | PSRAM 512 · `lab_run_gates` drops_delta=0 |
| BT7–BT8 | MEASURED | JSONL + PCAPNG LINKTYPE 201 |
| BT9 | MEASURED | leConnected Central↔Peripheral |
| BT10 | MEASURED | classicDiscoverable + Write_Local_Name + inquiry HCI |
| BT11–BT13 | MEASURED | peer/long/stress in `LAB_GATES_BT5_13_*` |
| L2 ATT probe | MEASURED (bounded) | `/api/bt/gatt/read-name` · ≠ Air / ≠ full GATT |
| BT16 CAPABILITY | MEASURED | connected + ATT + HCI traffic |
| BT16 BENCHMARK | NOT YET GREEN | needs file/app gap = 0 across matrix |
| BT14 | **ready for external review** | gate-result → GATE_EXITS (fixed) |
| BT15 | deferred | RF/Air separate |
| BT17 Classic audio | deferred after BT19 | separate Bluedroid flavor |
| BT19 timeline | scaffold | clock-offset estimation · not PTP |

## Claim boundary (must stay)

| Claim | Status |
|-------|--------|
| HCI capture = RF/Air | **REJECTED** |
| Classic BR/EDR on ESP32-S3 on-chip | **REJECTED** |
| Thin ATT name read = full GATT stack | **REJECTED** (L2 probe only) |

## Repro

```bash
cd esp32.bt-analyzer
python3 tools/lab_run_gates.py
python3 tools/lab_gate_exits.py   # refresh MEASURED markdown
```
