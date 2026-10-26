# Folge (esp32-rf-sensing Planung)

| Idee | Baut auf | Wann |
|------|----------|------|
| Phase 1 IDF/esp-csi Capability Matrix | Phase-0 Gaps | nach Phase-0 Exit |
| Phase 2 HeliosSm Traffic-vs-Motion Gate | Kill-Gap | nach Phase 1 |
| Characterization-Method CSI (roh → offline) | Messvertrag | Phase 3 / ≥2 Einsätze |
| Eigenes Lab vs ESPectre holdout | `wifi-csi-motion` | nach Messvertrag |
| Upstream-Repo Bootstrap | Projektklasse A/B | nach Decision |

## Wissensfeedback Phase 0 (2026-10-26)

| Claim | Status | Hinweis |
|-------|--------|---------|
| CSI-Motion ≠ Promiscuous ≠ RF-Environment | `FACT` (KB) | Sheets + Evidence |
| Packet-Count / channel_* ≠ CCA/Airtime | `REJECTED` (RF-Monitor) | nicht neu aufrollen |
| Own-Link Motion ≠ CSI Presence | `REJECTED` / Method | Kontrast |
| Chip×CSI×CCA Matrix IDF-belegt | `UNKNOWN` | Phase 1 |
| Traffic-Kontamination geklärt | `UNKNOWN` | Phase 2 HeliosSm |
