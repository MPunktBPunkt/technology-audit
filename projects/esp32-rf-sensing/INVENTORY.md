# Project Inventory: esp32-rf-sensing (Planung)

```yaml
project_id: esp32-rf-sensing
updated: 2026-10-26
reviewed_commit: none
profile: planning
pilot_order: [wifi-csi-motion, esp-wifi-promiscuous-pcap, rf-environment-monitor]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md)) — Phase 0–2: **kein neues Sheet**.

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| CSI Amplitudes → Motion/Score (managed traffic) | `wifi-csi-motion` | **reuse** (ESPectre Desk) |
| Promiscuous Frame → Buffer → PCAP | `esp-wifi-promiscuous-pcap` | **reuse** + Abgrenzung Capture≠CSI≠CCA |
| Environment Score / Own-Link / Location | `rf-environment-monitor` | **Kontrast**; CSI/Promiscuous/CCA-as-airtime `REJECTED` bleiben |
| Own-Link Walk-by Method | `own-link-motion-sensitivity` | Kontrast-Method (≠ CSI) |
| Chip × CSI × Promiscuous × RX-meta × CCA | — | Phase 1 **geschlossen** Desk; CCA `REJECTED` |
| Passive CSI ohne kontrollierten TX | — | Phase 2 **K5 geschlossen** (Definition); Lab-Ausbeute offen |
| Traffic vs. Human Motion Kontamination | — | Phase 2 **K7**: Assessment ohne Kontrollen `REJECTED` |
| Instrument Session/Offline | — | Phase 2 **K6**: Muster `FACT`; Spec Phase 3 |

Kampagne: [`esp32-rf-sensing-2026-desk`](../../audits/esp32-rf-sensing-2026-desk/).

## Übersicht

| Slug | Status | Coverage | Sheet | Application (dieses Projekt) |
|------|--------|----------|-------|------------------------------|
| `wifi-csi-motion` | documented | none | [SHEET](../../technologies/wifi-csi-motion/SHEET.md) | reuse via [`espectre` app](../espectre/applications/wifi-csi-motion.md) |
| `esp-wifi-promiscuous-pcap` | documented | none | [SHEET](../../technologies/esp-wifi-promiscuous-pcap/SHEET.md) | reuse via [`esp32-marauder` app](../esp32-marauder/applications/esp-wifi-promiscuous-pcap.md) |
| `rf-environment-monitor` | documented | none | [SHEET](../../technologies/rf-environment-monitor/SHEET.md) | Kontrast [`esp32-rfmonitor`](../esp32-rfmonitor/) |

Status `documented` = Sheet existiert; **keine** Application unter diesem Projekt bis Messvertrag steht (`planning`).

## Coverage-Lücken

| Bereich | Status | Nächster Schritt |
|---------|--------|------------------|
| IDF Chip-Capability Matrix S3/C6 | **geschlossen** Desk → [PHASE1](../../audits/esp32-rf-sensing-2026-desk/PHASE1.md) | Lab optional |
| CCA / Energy Detect als Mess-API | **`REJECTED`** (öffentlich) | nicht weiterführen |
| Passive CSI ohne eigenen TX | **Definition geschlossen** → [PHASE2](../../audits/esp32-rf-sensing-2026-desk/PHASE2.md) | Lab-Ausbeute; Traffic-Quelle spezifizieren |
| Traffic vs Motion Trennung | **Gate geschlossen**: ohne Kontrollen `REJECTED` | Phase 3 Messvertrag + ggf. Method |
| Instrument Session/Offline | **Muster geschlossen** | Phase 3 Spec (Drops/Clock/Replay) |
| Eigenes Lab / Field | Desk only | nach Messvertrag |

## Signale ohne Eintrag

- Multi-Link Sensing, SenseFi-Benchmarks, Presence-Demos — P2 nur bei Kill-Bedarf
- Method „CSI traffic-vs-motion controls“ — Kandidat Phase 3, nicht angelegt
