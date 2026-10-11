# Project Scope: esp32-sdr-trx (Fremd)

```yaml
project_id: esp32-sdr-trx
title: ESP32-S3 SDR Transceiver — polar PHY TX + narrowband RX (Fremd)
updated: 2026-10-11
profile_hint: lab-tool
reviewed_commit: "esp32-sdr-trx@e1aebbf eSpDR@f279bf8"
reviewed_commit_note: Desk; jochenhammes/eSpDR auf esp32-sdr-trx verwiesen — kanonisch esp32-sdr-trx
repos:
  - https://github.com/jochenhammes/esp32-sdr-trx
  - https://github.com/h0m3us3r/eSpDR
  - https://github.com/jochenhammes/eSpDR
status: active
```

## Zweck

S3-Universal-RF-Kandidat verstehen: undokumentierter I/Q-RX (decimated, kein FPGA) plus **polarer** PHY-TX — klar getrennt von Classic APLL-UKW und von ESPARGOS Multi-Chip-RX.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| jochenhammes/esp32-sdr-trx | Kanonischer maintained Fork (RX+TX) | ja (Desk) |
| h0m3us3r/eSpDR | Ursprung Dump + FPGA@80 Msps | ja (Provenance) |
| jochenhammes/eSpDR | Historischer Narrowband/TX-Research | angrenzend |
| `research/iq-tx` | Raw I/Q TX / LoRa | angrenzend (nicht Release) |
| Antennen-Feld-TX | — | **nein** (Desk; Legal) |
| Eigene Lab-Remessung | — | FOLLOW-ON |

## Nicht-Ziele

- Author-Thermal-Hz als KB-`MEASURED` übernehmen
- APLL-Sheet auf S3 ausweiten
- Raw-I/Q-TX als produktiven Contract behaupten

## Prioritäten

1. Sheet `esp32-polar-phy-tx` (S3-only) + Application  
2. RX an `esp32-undoc-iq-rx` matchen (Reuse)  
3. Epistemic: Code-Pfad = FACT; Performance = author-reported / UNKNOWN  
4. Kontrast zu `esp32-apll-fm-tx`
