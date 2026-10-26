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
phase: 0
reviewed_commit: none
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
  process: "Phase 0 KB Reuse/Gap only; keine neuen Sheets; Phase 1 IDF-Gate vorgeschlagen."
  decisions_touched:
    - reuse-espectre-wifi-csi-motion
    - reuse-marauder-promiscuous-abgrenzung
    - keep-rfmonitor-cca-airtime-rejected
    - defer-cca-until-idf-api-fact
```

## Ziel

Desk-Grundlage für die kleinste **auditierbare** ESP32-RF-Sensing-Plattform: Messvertrag aus Evidence, nicht Repo-Ranking. Phase 0 = Reuse/Gap gegen bestehende KB; danach IDF-Gate (Phase 1) und gezielte Fremd-Kill-Fragen (Phase 2).

## Scope

Siehe [SCOPE](../../projects/esp32-rf-sensing/SCOPE.md).

- **Im Scope Phase 0:** Inventar bestehender Sheets/Apps/Evidence/Methods; FACT-Liste; Gaps; Kill-/Gate-Fragen für Phase 1/2.
- **Nicht:** erneutes Voll-Audit ESPectre/Marauder; neue Sheets ohne Evidence; Code; rfmonitor-Features.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| P0.1 | Kampagne + SCOPE/INVENTORY Stub | erfüllt |
| P0.2 | Reuse-Tabelle Sheets/Apps/Evidence/Methods | erfüllt → [PHASE0](PHASE0.md) · [evidence](evidence.md) |
| P0.3 | FACT-Liste für RF-Sensing-Thema aus KB | erfüllt |
| P0.4 | Gap-Liste + Kill/Gate für Phase 1/2 | erfüllt |
| P0.5 | Keine neuen Sheets in Phase 0 | erfüllt |
| P1.1 | Chip × CSI × Promiscuous × RX-meta × CCA Matrix (IDF/esp-csi) | offen |
| P1.2 | CCA nur weiterführen wenn IDF-API-FACT — sonst UNKNOWN/REJECTED | offen |
| P2.1 | CSI-Tool / radar-lab / HeliosSm nur auf Kill-Fragen | offen |
| P2.2 | HeliosSm: keine Motion ohne Traffic-Kontamination geprüft | offen |
| P3.1 | Messvertrag + Projektklasse A/B/C Decision | offen |

## Decision Trace (Phase 0)

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| ESPectre erneut voll auditieren? | Fehlt KB-Contract CSI-Motion? | `EVID-RFSENSE-P0-001` | Nein — Reuse `wifi-csi-motion` | `KNOWN BEFORE TEST` |
| Marauder erneut voll auditieren? | Fehlt Promiscuous-Capture-Abgrenzung? | `EVID-RFSENSE-P0-002` | Nein — Reuse + Kontrast | `KNOWN BEFORE TEST` |
| CCA als Messgegenstand jetzt Sheet? | IDF-API-FACT in KB? | `EVID-RFSENSE-P0-004` | Nein — Gate Phase 1; RF-Monitor Airtime-`REJECTED` bleibt | `KNOWN BEFORE TEST` |
| Neues Sheet in Phase 0? | Trägt Evidence einen neuen Contract? | `EVID-RFSENSE-P0-005` | Nein | `KNOWN BEFORE TEST` |
| Nächstes Gate | Was blockiert Messvertrag? | `EVID-RFSENSE-P0-006` | Phase 1: IDF Chip×API Matrix | `DISCOVERED DURING TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-RFSENSE-P0-001` | Motion-/Presence-Claims an `wifi-csi-motion` Fallstricke binden; Person-Count `REJECTED` | `RETROFIT` |
| `EVID-RFSENSE-P0-002` | Capture≠CSI≠CCA in jedem Phase-1/2 Claim wiederholen | `RETROFIT` |
| `EVID-RFSENSE-P0-003` | Own-Link Method nicht als CSI-Substitute verkaufen | `KNOWN BEFORE TEST` |
| `EVID-RFSENSE-P0-004` | Packet-Count / channel_* nie als CCA labeln | `KNOWN BEFORE TEST` |

## Kill-Kriterien

**Hypothese Phase 0:** Bestehende KB reicht, um CSI / Promiscuous / RF-Environment sauber zu trennen und die echten Messvertrags-Gaps zu benennen — ohne neue Sheets.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | KB vermischt CSI und Promiscuous in einem Sheet | nicht eingetreten (getrennte Slugs) |
| 2 | RF-Monitor behandelt CCA-as-airtime als FACT | nicht eingetreten (`REJECTED`) |
| 3 | Keine benennbaren Phase-1/2 Gates aus Gaps | nicht eingetreten → siehe PHASE0 |

## Genutzte Methoden / Assets

| Asset | Pfad |
|-------|------|
| Sheet CSI Motion | [`wifi-csi-motion`](../../technologies/wifi-csi-motion/SHEET.md) |
| Sheet Promiscuous | [`esp-wifi-promiscuous-pcap`](../../technologies/esp-wifi-promiscuous-pcap/SHEET.md) |
| Sheet RF Environment | [`rf-environment-monitor`](../../technologies/rf-environment-monitor/SHEET.md) |
| Method Own-Link | [`own-link-motion-sensitivity`](../../methods/own-link-motion-sensitivity.md) |
| Prior | [`espectre-2026-foreign`](../espectre-2026-foreign/) · [`esp32-marauder-2026-foreign`](../esp32-marauder-2026-foreign/) |

## Ergebnisse Phase 0

- [PHASE0.md](PHASE0.md) — Reuse/FACT/Gap/Kill
- [evidence.md](evidence.md)
- **Phase-0 Exit:** erfüllt → Stop vor Phase 1 (siehe unten)

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Desk KB-Reuse | `EVID-RFSENSE-P0-001`…`006` | INVENTORY + diese Kampagne |

## Offene Punkte (nach Phase 0)

- Phase 1 starten: ESP-IDF + esp-csi Capability Matrix
- CCA nur bei API-FACT fortführen
- Phase 2 HeliosSm als Traffic-vs-Motion-Gate

---

## Phase-1 Gate (Vorschlag — noch nicht ausgeführt)

**Auftrag:** Primärquellen `espressif/esp-idf` + `espressif/esp-csi` Desk-lesen.

**Pflichtausgabe:** Matrix `Chip × CSI × Promiscuous × RX metadata × CCA` mit Status `FACT` / `UNKNOWN` / `REJECTED` und Datei-/Doc-Beleg.

**CCA-Regel:** Ohne belastbare IDF-API-/Messsemantik → Messgegenstand `UNKNOWN` oder `REJECTED` (nicht Sheet).

**Nicht in Phase 1:** HeliosSm/CSI-Tool Vertiefung; neue Motion-Claims; rfmonitor-Umbau.
