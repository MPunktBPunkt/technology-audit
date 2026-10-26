# Project Scope: esp32-rf-sensing (Planung)

```yaml
project_id: esp32-rf-sensing
title: ESP32 RF Sensing — Messvertrag Desk (Planung)
updated: 2026-10-26
profile: planning
reviewed_commit: none
reviewed_commit_note: "Kein eigenes Firmware-Repo; Desk aus KB-Reuse + Primärquellen (Phase 1+) und Fremd-Repos (Phase 2)."
status: active
```

## Zweck

Belastbare Technologie- und Evidence-Grundlage für ein **neues, eigenständiges** ESP32-RF-Sensing-Projekt ableiten. Zentrale Frage:

> Was ist die kleinste auditierbare ESP32-RF-Sensing-Plattform mit physikalisch sinnvollem, reproduzierbarem, offline analysierbarem Messvertrag?

Nicht: bestes Repo klonen · Feature-Sammlung · rfmonitor erweitern.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| Bestehende KB (Sheets/Apps/Evidence/Methods) | Phase 0 Reuse/Gap | ja |
| `espressif/esp-idf` WiFi CSI / Promiscuous / RX ctrl / CCA | Phase 1 Primärgate | ja (Desk) |
| `espressif/esp-csi` | Phase 1 Referenz | ja (Desk) |
| Fremd: CSI-Tool, wifi-radar-lab, HeliosSm | Phase 2 Kill-Fragen | ja (gezielt) |
| `esp32.rfmonitor` | Kontrast / Abgrenzung | nur Referenz — **kein** Umbau |
| ESPectre / Marauder | Reuse | ja — **kein** erneutes Voll-Audit |
| Eigenes Firmware-Repo | Engineering | erst nach Messvertrag |
| Presence / Person Count / Identity / Vitals / Localization | Produktclaims | **nein** bis Evidence trägt |

## Nicht-Ziele

- CSI / Promiscuous / CCA in `esp32.rfmonitor` nachziehen
- Neues Sheet nur weil ein Themengebiet existiert
- Dataset-/Weight-Spiegelung
- Offensive TX / Attack-How-tos
- Vollständiges Re-Audit von ESPectre oder Marauder

## Phasen

| Phase | Fokus | Exit |
|-------|--------|------|
| **0** | KB Reuse/Gap (diese Kampagne zuerst) | FACT-Inventar + Kill-Gaps für Phase 1/2 |
| **1** | ESP-IDF + esp-csi Gate | Chip × CSI × Promiscuous × RX-meta × CCA Matrix |
| **2** | CSI-Tool · radar-lab · HeliosSm | Traffic-vs-Motion + Capture-Contracts |
| **3** | Synthese | Messvertrag + Projektklasse A/B/C + Characterization-Method |

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| KB Reuse | `technologies/wifi-csi-motion`, `esp-wifi-promiscuous-pcap`, `rf-environment-monitor` | Phase 0 |
| Prior Audits | `audits/espectre-2026-foreign`, `esp32-marauder-2026-foreign`, `esp32-rfmonitor-*` | Phase 0 |
| Method Kontrast | `methods/own-link-motion-sensitivity` | ≠ CSI |
| IDF / esp-csi | GitHub Espressif | Phase 1 |
| Fremd P1 | CSI-Tool, radar-lab, HeliosSm | Phase 2 |

## Abgrenzung zu esp32.rfmonitor

| Bleibt im rfmonitor | Gehört nur ins neue Projekt (wenn Evidence) |
|---------------------|---------------------------------------------|
| Environment Scan, Own-Link RSSI, Score, Location, History, Hub | CSI Roh/Capture, Promiscuous Capture, CCA falls API-FACT, CSI-Processing, Multi-Link Sensing |

Grenze = **Messvertrag**, nicht Feature-Wunsch. `channel_*`=Airtime/CCA bleibt im RF-Monitor-Kontext `REJECTED`.

## Offene Scope-Fragen

- Projekt-ID Upstream: `esp32.rf-sensing` vs. `esp32.csi-sense`?
- Braucht Phase 3 eine neue Method Note (CSI characterization) oder reicht FOLLOW-ON?
