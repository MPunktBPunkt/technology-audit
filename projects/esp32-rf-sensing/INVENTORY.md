# Project Inventory: esp32-rf-sensing (Planung)

```yaml
project_id: esp32-rf-sensing
updated: 2026-10-26
reviewed_commit: none
profile: planning
pilot_order: [wifi-csi-motion, esp-wifi-promiscuous-pcap, rf-environment-monitor]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md)) — Phase 0: **kein neues Sheet**.

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| CSI Amplitudes → Motion/Score (managed traffic) | `wifi-csi-motion` | **reuse** (ESPectre Desk) |
| Promiscuous Frame → Buffer → PCAP | `esp-wifi-promiscuous-pcap` | **reuse** + Abgrenzung Capture≠CSI≠CCA |
| Environment Score / Own-Link / Location | `rf-environment-monitor` | **Kontrast**; CSI/Promiscuous/CCA-as-airtime `REJECTED` bleiben |
| Own-Link Walk-by Method | `own-link-motion-sensitivity` | Kontrast-Method (≠ CSI) |
| Chip × CSI × Promiscuous × RX-meta × CCA | — | **Gap** → Phase 1 IDF/esp-csi |
| Passive CSI ohne kontrollierten TX | — | **Gap** → Phase 2 CSI-Tool |
| Traffic vs. Human Motion Kontamination | — | **Kill-Gap** → Phase 2 HeliosSm |
| Echte CCA / Energy-Detect API | — | **Gate** → Phase 1; sonst UNKNOWN/REJECTED als Messgegenstand |

Kampagne: [`esp32-rf-sensing-2026-desk`](../../audits/esp32-rf-sensing-2026-desk/).

## Übersicht

| Slug | Status | Coverage | Sheet | Application (dieses Projekt) |
|------|--------|----------|-------|------------------------------|
| `wifi-csi-motion` | documented | none | [SHEET](../../technologies/wifi-csi-motion/SHEET.md) | reuse via [`espectre` app](../espectre/applications/wifi-csi-motion.md) |
| `esp-wifi-promiscuous-pcap` | documented | none | [SHEET](../../technologies/esp-wifi-promiscuous-pcap/SHEET.md) | reuse via [`esp32-marauder` app](../esp32-marauder/applications/esp-wifi-promiscuous-pcap.md) |
| `rf-environment-monitor` | documented | none | [SHEET](../../technologies/rf-environment-monitor/SHEET.md) | Kontrast [`esp32-rfmonitor`](../esp32-rfmonitor/) |

Status `documented` = Sheet existiert; **keine** Application unter diesem Projekt bis Messvertrag steht (`planning`).

## Coverage-Lücken (Phase 0)

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| IDF Chip-Capability Matrix | nur Upstream-Claims in ESPectre Desk | Phase 1 Primärquelle |
| CCA / Energy Detect | kein KB-FACT als Mess-API | Phase 1 Gate |
| Passive CSI ohne eigenen TX | nicht in ESPectre-Kernvertrag | Phase 2 CSI-Tool |
| Traffic vs Motion Trennung | Upstream holdout ≠ kontrolliertes Traffic-Gate | Phase 2 HeliosSm |
| Eigenes Lab / Field | Desk only | nach Messvertrag |

## Signale ohne Eintrag

- Multi-Link Sensing, SenseFi-Benchmarks, Presence-Demos — P2 nur bei Kill-Bedarf
- esp-csi Router/Passive Demos — Phase 1 Desk
