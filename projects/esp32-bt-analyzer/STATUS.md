# Status / Gate exits — esp32.bt-analyzer

```yaml
updated: 2026-11-04
fw: "0.3.2"
topology: F_ONCHIP
upstream_commit: b006324
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
