# Project Scope: c5vrx (Fremd)

```yaml
project_id: c5vrx
title: C5VRX — ESP32-C5 5.8 GHz FPV Analog RX (Fremd)
updated: 2026-10-11
profile_hint: lab-tool
reviewed_commit: "C5VRX@6887fb3"
repos:
  - https://github.com/Twotoz/C5VRX
status: active
```

## Zweck

C5-Zelle der Undoc-I/Q-Matrix vertiefen: continuous MODEM_DIAG → on-device WBFM-Demod → CVBS. G7: geringer Host-Portbedarf (Zero-CPU Pixelpfad), aber starke Chip-Spezialisierung.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| Twotoz/C5VRX (+ `v5/`) | Firmware + Messdocs | ja (Desk) |
| Seeed XIAO ESP32-C5 | Referenzboard | angrenzend |
| ESPARGOS C5 burst | gleicher Dump-Familienzweig | angrenzend |
| Feld-FPV-Reichweite | — | **nein** (Author-Limits) |

## Nicht-Ziele

- Eigenes FPV-Video-Sheet (Demod ist Application)
- „Production proven“-Badge als Lab-FACT
- Transfer polar-TX oder APLL auf C5

## Prioritäten

1. Application unter `esp32-undoc-iq-rx`  
2. Continuous-C5 vs. Burst-C5 kontrastieren  
3. Native-AGC-Fallen als Fallstrick-Kandidaten
