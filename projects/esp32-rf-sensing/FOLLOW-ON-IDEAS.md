# Folge (esp32-rf-sensing Planung)

| Idee | Baut auf | Wann |
|------|----------|------|
| Phase 3 Messvertrag + A/B/C | P0–P2 Constraints | nach Phase-2 Exit |
| Characterization-Method CSI (roh → offline) | Messvertrag | Phase 3 / ≥2 Einsätze |
| Method traffic-vs-motion controls (E1–E4-Analog) | K7 | Phase 3 / ≥1 eigener Einsatz |
| Eigenes Lab vs ESPectre holdout | `wifi-csi-motion` | nach Messvertrag |
| Upstream-Repo Bootstrap | Projektklasse A/B | nach Decision |
| Passiv Ambient Lab-Ausbeute | K5 Residual | optional nach Spec |

## Wissensfeedback Phase 0–2 (2026-10-26)

| Claim | Status | Hinweis |
|-------|--------|---------|
| CSI-Motion ≠ Promiscuous ≠ RF-Environment | `FACT` (KB) | Sheets + Evidence |
| Packet-Count / channel_* ≠ CCA/Airtime | `REJECTED` (RF-Monitor) | nicht neu aufrollen |
| Own-Link Motion ≠ CSI Presence | `REJECTED` / Method | Kontrast |
| S3/C6 CSI+Promisc+RX-meta API-Matrix | `FACT` (Desk) | PHASE1 |
| Öffentliche CCA-Occupancy-API | `REJECTED` | P1-007 |
| S3 Non-HE ≠ C6 HE CSI/rx_ctrl | `FACT` | P1-002 |
| Passiv = RX ohne eigenen TX; braucht Fremd-DATA | `FACT` | P2-001/002 |
| console_test Session/Label-Muster | `FACT` | P2-004; Radar-Demo ≠ Contract |
| Motion-Assessment ohne Traffic-Kontrollen | `REJECTED` | P2-008 |
| HeliosSm: lokal Motion ≫ UDP-Traffic auf Metriken | `FACT` (Desk-Repro) | P2-007; Transfer `UNKNOWN` |
