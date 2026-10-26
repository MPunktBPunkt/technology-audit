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
phase: 2
reviewed_commit: none
primary_pins:
  esp-idf: "master@d35ea02 + docs stable v6.1"
  esp-csi: "master@8633d67"
  csi_tool: "StevenMHernandez/ESP32-CSI-Tool@cce5b1a"
  helios: "HeliosSm/wifi-sensing-csi-network-traffic@3f374b5"
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
    - "console_test Radar Presence/Move als Messvertrag"
    - "Motion-Assessment ohne Traffic-Kontrollgruppen"
  process: "P0 KB; P1 IDF Gate CCA REJECTED; P2 K5–K7 Kill — Passiv definiert, Instrument-Muster, Traffic-Kontrollen Pflicht; keine neuen Sheets."
  decisions_touched:
    - reuse-espectre-wifi-csi-motion
    - reuse-marauder-promiscuous-abgrenzung
    - keep-rfmonitor-cca-airtime-rejected
    - reject-cca-as-public-idf-measurement
    - separate-s3-nonhe-vs-c6-he-csi-paths
    - map-k6-to-esp-csi-console-test
    - reject-motion-assessment-without-traffic-controls
```

## Ziel

Desk-Grundlage für die kleinste **auditierbare** ESP32-RF-Sensing-Plattform: Messvertrag aus Evidence, nicht Repo-Ranking. Phase 0 = Reuse/Gap; Phase 1 = IDF-Gate; Phase 2 = gezielte Fremd-Kill-Fragen (kein Voll-Audit).

## Scope

Siehe [SCOPE](../../projects/esp32-rf-sensing/SCOPE.md).

- **Im Scope Phase 0:** Inventar bestehender Sheets/Apps/Evidence/Methods; FACT-Liste; Gaps; Kill-/Gate-Fragen für Phase 1/2.
- **Im Scope Phase 1:** ESP-IDF + esp-csi Capability-/API-Matrix (CSI, Promiscuous, RX-meta, CCA-Gate); S3 vs C6 trennen.
- **Im Scope Phase 2:** Nur K5 CSI-Tool · K6 Instrument-Muster (esp-csi console_test) · **K7 HeliosSm** Traffic-vs-Motion.
- **Nicht:** erneutes Voll-Audit ESPectre/Marauder; Community-Volltiefe; neue Sheets ohne Evidence; Code; rfmonitor-Features; A/B/C-Zwang; Experimentplanung in Phase 2.

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
| P2.1 | CSI-Tool / radar-lab / HeliosSm nur auf Kill-Fragen | erfüllt → [PHASE2](PHASE2.md) |
| P2.2 | HeliosSm: keine Motion ohne Traffic-Kontamination geprüft | erfüllt: Assessment ohne Kontrollen **`REJECTED`** |
| P2.3 | Keine neuen Sheets in Phase 2 | erfüllt |
| P3.1 | Messvertrag + Projektklasse A/B/C Decision | offen |

## Decision Trace (Phase 0–2)

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| ESPectre erneut voll auditieren? | Fehlt KB-Contract CSI-Motion? | `EVID-RFSENSE-P0-001` | Nein — Reuse `wifi-csi-motion` | `KNOWN BEFORE TEST` |
| Marauder erneut voll auditieren? | Fehlt Promiscuous-Capture-Abgrenzung? | `EVID-RFSENSE-P0-002` | Nein — Reuse + Kontrast | `KNOWN BEFORE TEST` |
| CCA als Messgegenstand Sheet? | Öffentliche IDF-API mit Semantik? | `EVID-RFSENSE-P1-007` | **Nein — REJECTED**; Proxy nicht CCA nennen | `DISCOVERED DURING TEST` |
| S3/C6 CSI gleich behandeln? | Gleicher Config/rx_ctrl-Pfad? | `EVID-RFSENSE-P1-002` | Nein — Non-HE vs HE | `DISCOVERED DURING TEST` |
| Amp/Phase als Roh-API? | Felder in `wifi_csi_info_t`? | `EVID-RFSENSE-P1-004` | Nein — Derived aus I/Q | `KNOWN BEFORE TEST` |
| Passiv ohne eigenen TX? | CSI-Tool `passive` Design? | `EVID-RFSENSE-P2-001` | Ja definiert; braucht Fremd-DATA | `DISCOVERED DURING TEST` |
| Radar-UI als Instrument-Contract? | Raw vs Presence-Demo? | `EVID-RFSENSE-P2-005` | Nein — nur Session/Label-Muster reuse | `DISCOVERED DURING TEST` |
| Motion ohne Traffic-Kontrollen? | HeliosSm E1–E4 + Repro? | `EVID-RFSENSE-P2-008` | **REJECTED** als Assessment | `DISCOVERED DURING TEST` |
| Neues Sheet Phase 0–2? | Neuer Contract? | `EVID-RFSENSE-P0-005` / `P2-010` | Nein | `KNOWN BEFORE TEST` |
| Nächstes Gate | Was bleibt? | P2 Residuals | Phase 3 Synthese Messvertrag (kein A/B/C hier) | `DISCOVERED DURING TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-RFSENSE-P0-001` | Motion-/Presence-Claims an `wifi-csi-motion` Fallstricke binden; Person-Count `REJECTED` | `RETROFIT` |
| `EVID-RFSENSE-P0-002` | Capture≠CSI≠CCA in jedem Claim wiederholen | `RETROFIT` |
| `EVID-RFSENSE-P0-003` | Own-Link Method nicht als CSI-Substitute verkaufen | `KNOWN BEFORE TEST` |
| `EVID-RFSENSE-P1-007` | Packet-Count / channel_* / noise_floor nie als CCA labeln | `DISCOVERED DURING TEST` |
| `EVID-RFSENSE-P1-002` | CSI/rx_ctrl Parser chip-spezifisch (S3 classic vs C6 HE) | `DISCOVERED DURING TEST` |
| `EVID-RFSENSE-P1-004` | Nur I/Q+len als RAW; Features/Detector getrennt versionieren | `RETROFIT` |
| `EVID-RFSENSE-P2-002` | Passiv-Claims: Traffic-Quelle Dritter spezifizieren | `DISCOVERED DURING TEST` |
| `EVID-RFSENSE-P2-005` | Presence/Move-Demo nicht als Messvertrag zitieren | `DISCOVERED DURING TEST` |
| `EVID-RFSENSE-P2-008` | Motion-Assessment nur mit Traffic-Kontrollgruppen | `DISCOVERED DURING TEST` |

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

**Hypothese Phase 2:** Fremd-Repos beantworten Passiv, Instrument-Muster und Traffic-vs-Motion, ohne Voll-Audits.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 6 | „Passiv“ = TX-frei und ohne Fremd-Frames CSI | widerlegt → braucht OFDM-DATA Dritter |
| 7 | console_test Radar = auditfester Presence-Contract | widerlegt → Demo; nur Session-Muster |
| 8 | Motion-Assessment ohne Traffic-Kontrollen haltbar | widerlegt → **`REJECTED`** (K7) |

## Genutzte Methoden / Assets

| Asset | Pfad |
|-------|------|
| Sheet CSI Motion | [`wifi-csi-motion`](../../technologies/wifi-csi-motion/SHEET.md) |
| Sheet Promiscuous | [`esp-wifi-promiscuous-pcap`](../../technologies/esp-wifi-promiscuous-pcap/SHEET.md) |
| Sheet RF Environment | [`rf-environment-monitor`](../../technologies/rf-environment-monitor/SHEET.md) |
| Method Own-Link | [`own-link-motion-sensitivity`](../../methods/own-link-motion-sensitivity.md) |
| Prior | [`espectre-2026-foreign`](../espectre-2026-foreign/) · [`esp32-marauder-2026-foreign`](../esp32-marauder-2026-foreign/) |
| Fremd P2 | ESP32-CSI-Tool · esp-csi console_test · HeliosSm |

## Ergebnisse

- [PHASE0.md](PHASE0.md) — Reuse/FACT/Gap/Kill · **Exit erfüllt**
- [PHASE1.md](PHASE1.md) — Capability-Matrix · K1–K4 · **Exit erfüllt**
- [PHASE2.md](PHASE2.md) — K5–K7 Kill · **Exit erfüllt**
- [evidence.md](evidence.md)

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Desk KB-Reuse | `EVID-RFSENSE-P0-001`…`006` | INVENTORY + diese Kampagne |
| Desk IDF/esp-csi | `EVID-RFSENSE-P1-001`…`009` | PHASE1 + INVENTORY Gaps |
| Desk Fremd Kill | `EVID-RFSENSE-P2-001`…`010` | PHASE2 + INVENTORY Gaps |

## Offene Punkte (nach Phase 2)

- **Phase 3:** Messvertrag-Synthese + A/B/C Decision (separater Lauf)
- CCA nicht wiederbeleben
- Motion-Assessment nur mit Traffic-Kontrollgruppen (E1–E4-Analog)
- Method-Kandidat traffic-vs-motion controls — erst nach Spec/Einsatz
- Keine Experimentplanung in diesem Lauf

---

## Phase-3 Gate (Vorschlag — noch nicht ausgeführt)

Constraints aus P1+P2 als Input: Roh = CSI I/Q + Promisc + RX-meta; Erzeugung managed oder dokumentierte Fremdquelle; Instrument = Session RAW+Labels ohne Presence-Produkt; Assessment nur mit Traffic-Kontrollen. Dann erst A/B/C.
