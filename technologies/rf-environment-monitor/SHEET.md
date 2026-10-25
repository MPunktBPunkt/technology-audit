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
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Konkrete Score-Formel / IO-Keys → Application.

## Kurzfassung

Muster: stationärer Node scannt zyklisch WLAN- und/oder BLE-Umgebung, verdichtet Metriken (RSSI, Dichte, Kanalbelegung, Beacons) zu einem **RF-Score** und History/Events — für Infrastruktur-Überwachung, nicht für Spektrumanalyse oder Raum-Presence.

Geschwister: Einzweck-Monitor (`esp32.rfmonitor`) vs. RF als Modul in Modular-Firmware (`esp32.toolnode`) — gleicher Slug, kontrastierende Applications.

## Abgrenzung

- **Ist:** periodischer Environment-Scan + Heuristik-Score + Telemetrie.
- **Ist nicht:** Spektrumanalysator; Paket-Sniffer / Promiscuous-PCAP (→ `esp-wifi-promiscuous-pcap`); BT-Central zu einem Gurt/Bike; Presence mit Raumgenauigkeit; das Modul-Host-Framework (→ `esp-module-host`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | WiFi scan API + BLE Adv-Scan | oft **sequentiell** (ein Radio) |
| oben | Web-UI / Hub | Score, Listen, Events |
| lateral | Hub-Telemetrie | `fwType` spezfisch |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| WLAN- und BLE-Scan parallel ohne Qualitätseinbuße | `HYPOTHESIS` | ESP oft shared radio — nacheinander planen |
| RF-Score ist kalibrierte Messgröße | `REJECTED` | Heuristik; Versionieren und dokumentieren |
| Monitor = Connection-Central | `REJECTED` | Observer/Scanner-Rollen anders als GATT-Central-Produkt |
| Monitor = Marauder-Promiscuous/PCAP | `REJECTED` | anderer Contract → `esp-wifi-promiscuous-pcap` |
| Monitor = CSI-Motion Occupancy | `REJECTED` | anderer Contract → `wifi-csi-motion` |
| BLE-Scan ist Pflichtteil des Musters | `REJECTED` | WLAN-only (toolnode Mini, `ENABLE_BLE=0`) bleibt RF-Environment-Monitor |
| Einzweck-Firmware und Modul teilen keinen Slug | `REJECTED` | Geschwister → gleicher Slug, Applications kontrastieren |

## Transfer

Nützlich für Standort-Monitoring und Coexistence-Baselines. Score-Formel und Event-Taxonomie versionieren; nicht still mit Produkten mischen, die Links halten. Modular-Host und MQTT sind **andere** Sheets.

### Projektstart-Checkliste

- [ ] Scan-Intervall und Radio-Zeitbudget festlegen (WLAN vs. BLE)
- [ ] Score-Formel versionieren (docs + Evidence)
- [ ] Einzweck vs. Modul? → gleicher Slug, Application kontrastieren (kein Fork)
- [ ] Hub-IO-Keys + `fwType` dokumentieren
- [ ] Application + `seen_in` nachziehen

## Referenzen

- ESP WiFi scan / NimBLE scan APIs
- Beispiel Einzweck: [esp32.rfmonitor](https://github.com/MPunktBPunkt/esp32.rfmonitor) `docs/RF_SCORE.md`
- Beispiel Modul: [esp32.toolnode](https://github.com/MPunktBPunkt/esp32.toolnode) Scanner/RfHealth

## Offene Fragen

- Wie portabel ist die Heuristik zwischen Standorten ohne Kalibrierung?
