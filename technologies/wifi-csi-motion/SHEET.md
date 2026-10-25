# Technology Sheet: Wi-Fi CSI Motion Sensing

```yaml
slug: wifi-csi-motion
title: Wi-Fi CSI Motion Sensing
primary: H
tags: [esp-idf, lab-only, fragile, wifi]
type: pattern
status: active
seen_in: [espectre]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/espectre-2026-foreign
```

Nur Ebene **A**. Raumgeometrie, HA-Entities, Board-Pins → Application.  
**Privacy:** Motion/Presence aus Wi-Fi kann Routinen offenbaren — Consent und lokaler Betrieb sind Teil des Contracts, nicht optionaler Nachsatz.

## Kurzfassung

Bewegungs-/Belegungshinweise aus **Channel State Information (CSI)** bestehender Wi-Fi-Links: Subcarrier-Amplituden (typisch HT20) werden in Echtzeit erfasst, zeitlich auf ein festes pps-Raster **admittiert** und von einem lokalen Detektor (statistisch oder kleines NN) zu Motion/Score verdichtet — ohne Kamera, Mikrofon oder Radar-Hardware.

## Abgrenzung

- **Ist:** CSI-Capture + Quality/Normalize + Temporal Admission + Motion-Detector; managed Traffic zur CSI-Erzeugung.
- **Ist nicht:** Promiscuous Frame-Dump/PCAP (`esp-wifi-promiscuous-pcap`); AP-Listen-RF-Score (`rf-environment-monitor`); Person-ID/People-Count; LLM-Inference (`mcu-ple-inference`); Safety-zertifizierte Alarmanlage.
- **Grenzt an:** ESP-IDF CSI / esp-csi Ökosystem; MQTT/HTTP Occupancy-Frontends (App).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | Wi-Fi STA + CSI Callback | AGC oft an; Chip-Gates |
| lateral | Traffic Generator (ping/dns/null-data/external) | steuert nutzbare CSI-Rate |
| Mitte | Temporal Sampler (max 1 Sample/Slot) | `csi_target_pps` |
| oben | Motion state / score / Occupancy entity | lokal |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| CSI-Motion ≡ Packet-Sniffer/PCAP | `REJECTED` | Amplituden-Pipeline ≠ Frame-Capture |
| CSI-Motion ≡ RF-Environment-Score | `REJECTED` | anderer Contract |
| Beliebige pps ohne Admission = bessere Detection | `REJECTED` | Excess/Drops; Timing am Target-Raster |
| Alle ESP32-Chips gleiche CSI/ACK-Fähigkeit | `REJECTED` | Chip-/Rev-Gates (Upstream Compatibility) |
| Detektor beweist leeren Raum / zählt Personen | `REJECTED` | nur Radio-Änderungen |
| Cloud nötig für Inference | `REJECTED` | On-device möglich |
| CSI-MLP ≡ On-Device-LLM | `REJECTED` | Feature-MLP ≠ PLE-LLM |
| Privacy egal weil „keine Kamera“ | `REJECTED` | Routinen/Abwesenheit können sichtbar werden |

### Projektstart-Checkliste

- [ ] Chip + Band (2.4 HT20 vs C5 5 GHz) gegen Upstream-Compatibility
- [ ] `csi_target_pps` + Window; Admission verstehen
- [ ] Traffic-Quelle (internal vs external / peer)
- [ ] Detector-Profil: Lightweight vs High-Accuracy Tradeoff
- [ ] Consent / lokaler Betrieb / Roh-CSI optional halten
- [ ] Application + `seen_in`; Kontrast Sniff/Score-Sheets

## Transfer

Für raumbezogene Occupancy ohne Kamera, HA/Matter-Sensoren, Lab-Validierung von Wi-Fi-Sensing. Nicht still auf Sniff/Deauth-Toolkits oder LLM-Edge übertragen.

## Referenzen

- Espressif [esp-csi](https://github.com/espressif/esp-csi) (Community-Bezug)
- Pilot: [francescopace/espectre](https://github.com/francescopace/espectre) (`docs/CSI.md`, `ALGORITHMS.md`)

## Offene Fragen

- Welche Mindest-Luftzeit-Budgets bei mehreren Sensoren auf einem Kanal?
- Wann Peer-Null-Data besser als AP-Pfad ist (Placement)?
