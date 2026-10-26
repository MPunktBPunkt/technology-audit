# Technology Sheet: RF Environment Monitor

```yaml
slug: rf-environment-monitor
title: RF Environment Monitor
primary: H
tags: [esp-idf, lab-only]
type: pattern
status: active
seen_in: [esp32-rfmonitor, esp32-toolnode]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R1
  reusability: W3
```

Nur Ebene **A**. Konkrete Score-Formel / IO-Keys / Caps → Application.

## Kurzfassung

Muster: stationärer Node scannt zyklisch WLAN- und/oder BLE-Umgebung, trennt **Observation (raw)**, **Derived (proxy)** und **Assessment (Score + Datenqualität)**, hält optional ein **Standortprofil** (Deviation ≠ Score-Offset), optional **History/Drift** und optional ein **Own-Link-Feinsignal** (high-rate RSSI für Walk-by-Charakterisierung — **kein** Presence) und liefert Events/Telemetrie — für Infrastruktur-Überwachung, nicht für Spektrumanalyse oder Raum-Presence.

Geschwister: Einzweck-Monitor (`esp32.rfmonitor`) vs. RF als Modul in Modular-Firmware (`esp32.toolnode`) — gleicher Slug, kontrastierende Applications.

## Abgrenzung

- **Ist:** periodischer Environment-Scan + versionierte Heuristik-Scores + Telemetrie; Observation-Schichten; Standort-Δ als eigene Achse; optional Session-Profile (Feld/Char/Motion); optional Own-Link-Feinring.
- **Ist nicht:** Spektrumanalysator; Paket-Sniffer / Promiscuous-PCAP (→ `esp-wifi-promiscuous-pcap`); BLE RSSI Proximity Hunt (→ `ble-rssi-proximity`); CSI-Motion Occupancy (→ `wifi-csi-motion`); BT-Central zu einem Gurt/Bike; Presence mit Raumgenauigkeit; das Modul-Host-Framework (→ `esp-module-host`); kalibrierte physikalische Interferometrie.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | WiFi scan API + BLE Adv-Scan | oft **sequentiell** (ein Radio); Scan-Dauer/Fails instrumentieren |
| unten | Own-Link RSSI (optional) | high-rate Ring; Scans im Motion-Profil typisch pausiert |
| oben | Web-UI / Hub | Score(s), Quality, Listen, Events, optional nested Alert-Contract |
| lateral | Hub-Telemetrie | `fwType` / Domain-Contract spezfisch |
| lateral | Location Profile | Baseline-Capture; Deviation separat vom Absolute-Score |
| lateral | Session-Profile | Assessment vs. Characterization vs. Motion nicht vermischen |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| WLAN- und BLE-Scan parallel ohne Qualitätseinbuße | `HYPOTHESIS` | ESP oft shared radio — nacheinander planen |
| RF-Score ist kalibrierte Messgröße | `REJECTED` | Heuristik; versionieren; Standort über Profile/Deviation |
| `channel_*` / density / pressure = Airtime / CCA | `REJECTED` | Zähl-Proxies; als `kind=proxy` markieren |
| measurementQuality ersetzt / ist der Score | `REJECTED` | getrennte Achsen: Vertrauenswürdigkeit vs. Lage-Heuristik |
| Location Deviation = Score-Offset | `REJECTED` | Absolute Quality vs. Standort-Δ |
| Own-Link Motion = Presence / Personenzählung | `REJECTED` | nur Link-RSSI-Δ; Method `own-link-motion-sensitivity` |
| Assessment-Score-Fenster reicht für Walk-by-Zeitauflösung | `REJECTED` | typisch zu langsam/klein — eigenes Feinsignal |
| Schwacher Char-Stimulus = Score-Formel kaputt | `REJECTED` | FAIL der Stimulus-Qualität, nicht automatisch der Formel |
| Monitor = Connection-Central | `REJECTED` | Observer/Scanner-Rollen anders als GATT-Central-Produkt |
| Monitor = Marauder-Promiscuous/PCAP | `REJECTED` | anderer Contract → `esp-wifi-promiscuous-pcap` |
| Monitor = CSI-Motion Occupancy | `REJECTED` | anderer Contract → `wifi-csi-motion` |
| BLE-Scan ist Pflichtteil des Musters | `REJECTED` | WLAN-only (toolnode Mini, `ENABLE_BLE=0`) bleibt RF-Environment-Monitor |
| Einzweck-Firmware und Modul teilen keinen Slug | `REJECTED` | Geschwister → gleicher Slug, Applications kontrastieren |
| Eine Score-Version reicht für immer | `REJECTED` | parallel rechnen / `scoreVersion` führen (Replay) |

## Transfer

Nützlich für Standort-Monitoring und Coexistence-Baselines (Snapshot). Score-Formel und Event-Taxonomie versionieren; Proxies nicht als Physik verkaufen. Modular-Host und MQTT sind **andere** Sheets. Transfer an neuen Standort braucht Location Profile oder Feldserie — Score allein reicht nicht. Own-Link-Motion braucht neue CAL am Zielort; kein stiller Raum-Transfer.

### Projektstart-Checkliste

- [ ] Scan-Intervall und Radio-Zeitbudget festlegen (WLAN vs. BLE) — instrumentieren
- [ ] Score-Formel versionieren (`scoreVersion`; parallel halten für Replay)
- [ ] Observation: raw / derived(proxy) / assessment trennen
- [ ] `measurementQuality` separat vom Score
- [ ] Location Profile / Deviation vs. Absolute Score klären
- [ ] Session-Profile: Assessment vs. Characterization vs. Motion trennen
- [ ] Own-Link-Feinring? → Presence/CSI explizit **nicht** claimen; Method nutzen
- [ ] Einzweck vs. Modul? → gleicher Slug, Application kontrastieren (kein Fork)
- [ ] Hub-IO-Keys + `fwType` (+ optional nested Domain-Contract) dokumentieren
- [ ] Application + `seen_in` nachziehen
- [ ] Caps: PSRAM / Dual-Core / History-/Motion-Ring-Größen board-abhängig

## Referenzen

- ESP WiFi scan / NimBLE scan APIs
- Beispiel Einzweck: [esp32.rfmonitor](https://github.com/MPunktBPunkt/esp32.rfmonitor) `docs/RF_SCORE.md`, `docs/OBSERVATION_MODEL.md`, `docs/LOCATION_PROFILE.md`, `docs/MOTION_SENSITIVITY.md`, `docs/HUB_CONTRACT.md`
- Beispiel Modul: [esp32.toolnode](https://github.com/MPunktBPunkt/esp32.toolnode) Scanner/RfHealth
- Method: [`own-link-motion-sensitivity`](../../methods/own-link-motion-sensitivity.md)

## Offene Fragen

- Wie portabel ist die Heuristik zwischen Standorten ohne Location Profile?
- Reicht AP-Count-Proxy für Coexistence-Baseline, oder braucht es Hub-seitige Aggregation?
- Wann lohnt eine dritte Score-Version vs. nur Feature-Gewichte drehen?
- Wie weit trägt Own-Link-Motion über Küchen-Geometrie hinaus?
