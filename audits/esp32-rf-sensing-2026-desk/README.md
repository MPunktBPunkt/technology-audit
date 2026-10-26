# Audit Campaign: esp32-rf-sensing-2026-desk

```yaml
id: esp32-rf-sensing-2026-desk
project_id: esp32-rf-sensing
started: 2026-10-26
ended: null
status: active
profile: planning
standard_version: "0.7.1"
standard_gaps: []
phase: 1
reviewed_commit: none
primary_pins:
  esp-idf: "master@d35ea02 + docs stable v6.1"
  esp-csi: "master@8633d67"
reuse_outcomes:
  reused:
    - wifi-csi-motion
    - esp-wifi-promiscuous-pcap
    - rf-environment-monitor
    - own-link-motion-sensitivity
  new: []
  not_helped:
    - "CSI/Promiscuous/CCA in esp32.rfmonitor nachziehen"
    - "Voll-Reaudit ESPectre oder Marauder"
    - "CCA/Channel-Occupancy als IDF-Messgegenstand"
    - "esp-csi full-series CSI auf jedem Chip"
  process: "Phase 0 KB Reuse/Gap; Phase 1 IDF/esp-csi Capability-Gate — CCA REJECTED; keine neuen Sheets."
  decisions_touched:
    - reuse-espectre-wifi-csi-motion
    - reuse-marauder-promiscuous-abgrenzung
    - keep-rfmonitor-cca-airtime-rejected
    - reject-cca-as-public-idf-measurement
    - separate-s3-nonhe-vs-c6-he-csi-paths
```

## Ziel

Desk-Grundlage für die kleinste **auditierbare** ESP32-RF-Sensing-Plattform: Messvertrag aus Evidence, nicht Repo-Ranking. Phase 0 = Reuse/Gap gegen bestehende KB; danach IDF-Gate (Phase 1) und gezielte Fremd-Kill-Fragen (Phase 2).

## Scope

Siehe [SCOPE](../../projects/esp32-rf-sensing/SCOPE.md).

- **Im Scope Phase 0:** Inventar bestehender Sheets/Apps/Evidence/Methods; FACT-Liste; Gaps; Kill-/Gate-Fragen für Phase 1/2.
- **Im Scope Phase 1:** ESP-IDF + esp-csi Capability-/API-Matrix (CSI, Promiscuous, RX-meta, CCA-Gate); S3 vs C6 trennen.
- **Nicht:** erneutes Voll-Audit ESPectre/Marauder; Community-Repo-Tiefe (Phase 2); neue Sheets ohne Evidence; Code; rfmonitor-Features; A/B/C-Zwang.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| P0.1 | Kampagne + SCOPE/INVENTORY Stub | erfüllt |
| P0.2 | Reuse-Tabelle Sheets/Apps/Evidence/Methods | erfüllt → [PHASE0](PHASE0.md) · [evidence](evidence.md) |
| P0.3 | FACT-Liste für RF-Sensing-Thema aus KB | erfüllt |
| P0.4 | Gap-Liste + Kill/Gate für Phase 1/2 | erfüllt |
| P0.5 | Keine neuen Sheets in Phase 0 | erfüllt |
| P1.1 | Chip × CSI × Promiscuous × RX-meta × CCA Matrix (IDF/esp-csi) | erfüllt → [PHASE1](PHASE1.md) |
| P1.2 | CCA nur weiterführen wenn IDF-API-FACT — sonst UNKNOWN/REJECTED | erfüllt: **REJECTED** als Messgegenstand |
| P1.3 | K1–K4 Desk geschlossen oder Residual benannt | erfüllt |
| P1.4 | Keine neuen Sheets in Phase 1 | erfüllt |
| P2.1 | CSI-Tool / radar-lab / HeliosSm nur auf Kill-Fragen | offen |
| P2.2 | HeliosSm: keine Motion ohne Traffic-Kontamination geprüft | offen |
| P3.1 | Messvertrag + Projektklasse A/B/C Decision | offen |

## Decision Trace (Phase 0 + 1)

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| ESPectre erneut voll auditieren? | Fehlt KB-Contract CSI-Motion? | `EVID-RFSENSE-P0-001` | Nein — Reuse `wifi-csi-motion` | `KNOWN BEFORE TEST` |
| Marauder erneut voll auditieren? | Fehlt Promiscuous-Capture-Abgrenzung? | `EVID-RFSENSE-P0-002` | Nein — Reuse + Kontrast | `KNOWN BEFORE TEST` |
| CCA als Messgegenstand Sheet? | Öffentliche IDF-API mit Semantik? | `EVID-RFSENSE-P1-007` | **Nein — REJECTED**; Proxy nicht CCA nennen | `DISCOVERED DURING TEST` |
| S3/C6 CSI gleich behandeln? | Gleicher Config/rx_ctrl-Pfad? | `EVID-RFSENSE-P1-002` | Nein — Non-HE vs HE | `DISCOVERED DURING TEST` |
| Amp/Phase als Roh-API? | Felder in `wifi_csi_info_t`? | `EVID-RFSENSE-P1-004` | Nein — Derived aus I/Q | `KNOWN BEFORE TEST` |
| Neues Sheet Phase 0/1? | Neuer Contract? | `EVID-RFSENSE-P0-005` | Nein | `KNOWN BEFORE TEST` |
| Nächstes Gate | Was bleibt für Messvertrag? | `EVID-RFSENSE-P1-009` + K5–K7 | Phase 2: Passiv/Instrument/Traffic-vs-Motion | `DISCOVERED DURING TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-RFSENSE-P0-001` | Motion-/Presence-Claims an `wifi-csi-motion` Fallstricke binden; Person-Count `REJECTED` | `RETROFIT` |
| `EVID-RFSENSE-P0-002` | Capture≠CSI≠CCA in jedem Phase-2 Claim wiederholen | `RETROFIT` |
| `EVID-RFSENSE-P0-003` | Own-Link Method nicht als CSI-Substitute verkaufen | `KNOWN BEFORE TEST` |
| `EVID-RFSENSE-P1-007` | Packet-Count / channel_* / noise_floor nie als CCA labeln | `DISCOVERED DURING TEST` |
| `EVID-RFSENSE-P1-002` | CSI/rx_ctrl Parser chip-spezifisch (S3 classic vs C6 HE) | `DISCOVERED DURING TEST` |
| `EVID-RFSENSE-P1-004` | Nur I/Q+len als RAW; Features/Detector getrennt versionieren | `RETROFIT` |

## Kill-Kriterien

**Hypothese Phase 0:** Bestehende KB reicht, um CSI / Promiscuous / RF-Environment sauber zu trennen und die echten Messvertrags-Gaps zu benennen — ohne neue Sheets.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | KB vermischt CSI und Promiscuous in einem Sheet | nicht eingetreten (getrennte Slugs) |
| 2 | RF-Monitor behandelt CCA-as-airtime als FACT | nicht eingetreten (`REJECTED`) |
| 3 | Keine benennbaren Phase-1/2 Gates aus Gaps | nicht eingetreten → siehe PHASE0 |

**Hypothese Phase 1:** IDF legt fest, welche Rohbeobachtungen S3/C6 wirklich liefern und welche Occupancy-/CCA-Claims schon API-seitig fallen.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 4 | Öffentliche CCA-Occupancy-API existiert klar dokumentiert | nicht eingetreten → Messgegenstand `REJECTED` |
| 5 | S3 und C6 teilen identisches CSI/rx_ctrl Layout | widerlegt → getrennte Pfade `FACT` |

## Genutzte Methoden / Assets

| Asset | Pfad |
|-------|------|
| Sheet CSI Motion | [`wifi-csi-motion`](../../technologies/wifi-csi-motion/SHEET.md) |
| Sheet Promiscuous | [`esp-wifi-promiscuous-pcap`](../../technologies/esp-wifi-promiscuous-pcap/SHEET.md) |
| Sheet RF Environment | [`rf-environment-monitor`](../../technologies/rf-environment-monitor/SHEET.md) |
| Method Own-Link | [`own-link-motion-sensitivity`](../../methods/own-link-motion-sensitivity.md) |
| Prior | [`espectre-2026-foreign`](../espectre-2026-foreign/) · [`esp32-marauder-2026-foreign`](../esp32-marauder-2026-foreign/) |

## Ergebnisse

- [PHASE0.md](PHASE0.md) — Reuse/FACT/Gap/Kill · **Exit erfüllt**
- [PHASE1.md](PHASE1.md) — Capability-Matrix · K1–K4 · **Exit erfüllt**
- [evidence.md](evidence.md)

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Desk KB-Reuse | `EVID-RFSENSE-P0-001`…`006` | INVENTORY + diese Kampagne |
| Desk IDF/esp-csi | `EVID-RFSENSE-P1-001`…`009` | PHASE1 + INVENTORY Gaps |

## Offene Punkte (nach Phase 1)

- Phase 2: K5 CSI-Tool (Passiv), K6 radar-lab (Instrument), **K7 HeliosSm** (Traffic vs Motion)
- CCA nicht wiederbeleben
- A/B/C-Messvertrag erst nach Phase 2

---

## Phase-2 Gate (Vorschlag — noch nicht ausgeführt)

Nur Residuals aus [PHASE1](PHASE1.md) §8: Passiv-CSI, Offline-Instrument-Muster, Traffic-Kontamination. Keine CCA-Renaissance; keine Community-Vollaudits.
