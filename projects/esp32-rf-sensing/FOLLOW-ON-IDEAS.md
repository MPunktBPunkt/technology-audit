# Folge (esp32-rf-sensing Planung)

| Idee | Baut auf | Wann |
|------|----------|------|
| Phase 2 HeliosSm Traffic-vs-Motion Gate | K7 | nach Phase-1 Exit |
| Phase 2 CSI-Tool Passiv-Capture | K5 | nach Phase 1 |
| Phase 2 radar-lab Instrument-Muster | K6 | nach Phase 1 |
| Characterization-Method CSI (roh → offline) | Messvertrag | Phase 3 / ≥2 Einsätze |
| Eigenes Lab vs ESPectre holdout | `wifi-csi-motion` | nach Messvertrag |
| Upstream-Repo Bootstrap | Projektklasse A/B | nach Decision |

## Wissensfeedback Phase 0–1 (2026-10-26)

| Claim | Status | Hinweis |
|-------|--------|---------|
| CSI-Motion ≠ Promiscuous ≠ RF-Environment | `FACT` (KB) | Sheets + Evidence |
| Packet-Count / channel_* ≠ CCA/Airtime | `REJECTED` (RF-Monitor) | nicht neu aufrollen |
| Own-Link Motion ≠ CSI Presence | `REJECTED` / Method | Kontrast |
| S3/C6 CSI+Promisc+RX-meta API-Matrix | `FACT` (Desk) | PHASE1 |
| Öffentliche CCA-Occupancy-API | `REJECTED` | P1-007 |
| S3 Non-HE ≠ C6 HE CSI/rx_ctrl | `FACT` | P1-002 |
| Traffic-Kontamination geklärt | `UNKNOWN` | Phase 2 HeliosSm |
