# Technology Matrix — ESP32 RF Sensing Ansätze

```yaml
campaign: esp32-rf-sensing-2026-desk
artifact: TECHNOLOGY-MATRIX.md
date: 2026-10-26
mode: desk-decision-matrix
standard_version: "0.7.1"
project_decision: none
lab_path: frozen
instrument_artifact: not_a_decision
new_code: false
commit: for-external-review
```

## 1. Scope / Ziel

**Ziel:** entscheiden, **ob und welcher** technische Ansatz einen weiteren Experiment-/Projektpfad überhaupt rechtfertigt.

**Nicht-Ziel:** Projekt bauen · Firmware · Hardware · A0/C1 · rfmonitor ändern · CSI-Instrument weiterentwickeln · Produktarchitektur.

**Eingefrorener Kontext:** P0–P2 committed; P3-Plan/Instrument uncommitted Artefakt; **keine** CSI- oder Projektentscheidung bisher.

**Entscheidungsregel (GO-Kandidat):** Messgröße klar · Rohdaten verfügbar · Offline-Auswertung möglich · Sensing-Hypothese zumindest plausibel gestützt · keine offene fundamentale Killerfrage.  
Ein GO-Kandidat ist **keine** Projektentscheidung — nur: „weiterverfolgen als möglichen Pfad“.

---

## 2. Bewertungsmethode

| Regel | |
|-------|--|
| Epistemik | Jede belastende Aussage: `FACT` · `INFERENCE` · `HYPOTHESIS` · `UNKNOWN` · `REJECTED` |
| Quellenpriorität | (1) ESP-IDF/Espressif · (2) offizielle Repo-Doku · (3) Wissenschaft/Dataset-Repro · (4) OSS-Implementierung · (5) sonstiges nur ergänzend |
| Reuse | Bestehende KB/Kampagnen-Evidence; **kein** Neu-Vollaudit |
| Verbot | Unbelegte Vollständigkeits-Kandidaten; CCA erneut „öffnen“ |

**Verdict-Stufen je Kandidat:** `GO` (Shortlist Experimentpfad) · `FURTHER AUDIT` · `NO-GO`.

---

## 3. Evidenzstatus (Inputs)

| Pool | Inhalt | Reife |
|------|--------|-------|
| PHASE1 / `EVID-RFSENSE-P1-*` | IDF CSI / Promisc / RX-meta / CCA-Gate S3↔C6 | Desk-Primärquelle |
| PHASE2 / `EVID-RFSENSE-P2-*` | CSI-Tool Passiv; console_test Muster; HeliosSm Traffic×Motion | Desk + Dataset-Repro |
| Sheets | `wifi-csi-motion` · `esp-wifi-promiscuous-pcap` · `rf-environment-monitor` | R1–R3 / field gemischt |
| Prior Audits | ESPectre · Marauder · rfmonitor v2 + motion-delta | Foreign/Field Desk |
| Method | `own-link-motion-sensitivity` | Field Walk-by (Küche) |
| Instrument-Artefakt 2026-10-26 | A0 FAIL (D1 fehlt) | **nicht** als Technologie-Evidenz werten |

**HeliosSm (P2-006/007) — korrekte Lesart:** In **einem** kontrollierten C6-Testbed mit Upstream-Pipeline: Motion-Metriken ≫ Traffic-only; Pearson r(Mbps, var_movil)≈0.02.  
Das ist ein **Hinweis**, dass kinematische CSI-Derived-Größen dort von UDP-Last unterscheidbar waren — **kein** Transfer auf unsere Hardware, **kein** Presence-Beweis, **kein** Projekt-GO (`EVID-RFSENSE-P2-008/009`).

---

## 4. Kandidatenmatrix (Überblick)

| ID | Kandidat | Rolle | Verdict |
|----|----------|-------|---------|
| **T1** | Wi-Fi CSI (I/Q → Derived → optional Assessment) | Multipath-/Channel-State Sensing | **GO** (Experimentpfad) |
| **T2** | Promiscuous Frame Capture (+ PCAP) | Frame-Observation / Lab-Capture | **NO-GO** als Sensing; **GO** nur als Capture-Hilfspfad |
| **T3** | RX-Metadaten (RSSI, noise_floor, …) | Per-packet Radio-Meta | **FURTHER AUDIT** (allein schwach; oft Beiwerk) |
| **T4** | Own-Link high-rate RSSI | Link-Feinsignal / Walk-by Char | **GO** (enger Kontrast-/Char-Pfad) |
| **T5** | Environment Scan / Score | Heuristik-Monitoring | **NO-GO** für RF-Sensing-Messvertrag |
| **T0** | CCA / Channel Occupancy | — | **NO-GO** (`REJECTED`, nicht offen) |

T4/T5 nur aufgenommen, weil in KB/Prior-Audits belegt — keine neuen Erfindungen.

---

## 5. Detaillierte Bewertung

### T0 — CCA / Channel Occupancy (**geschlossen**)

| Kriterium | Bewertung | Status |
|-----------|-----------|--------|
| Messgröße | Öffentliche busy-time / energy-detect Zeitreihe | **`REJECTED`** — keine API in geprüften IDF-WiFi-Quellen (`P1-007`) |
| Proxies als CCA | Packet-Count / `channel_*` | **`REJECTED`** Label (`P0-004`, RF-Monitor) |
| Verdict | **NO-GO** | nicht erneut auditieren |

---

### T1 — Wi-Fi CSI

| Kriterium | Bewertung | Status / Beleg |
|-----------|-----------|----------------|
| Physikalische Messgröße | Subcarrier Channel Response bei RX (I/Q) | `FACT` IDF Vendor Features (`P1-004`) |
| Rohdaten | `buf` Imag/Real `int8` + `len` | `FACT` |
| Metadaten | `rx_ctrl` (rssi, noise_floor, channel, ts, …) + MAC | `FACT` (`P1-006`) |
| Auflösung / Granularität | Event-getrieben pro empfangenem Packet; Rate = Traffic×Admission | `FACT` braucht RX; Lab-pps `UNKNOWN` hier |
| Passiv (ohne eigenen TX) | Implementierbar (CSI-Tool NULL+Promisc) | `FACT` Design (`P2-001`); Ausbeute `UNKNOWN` |
| Externe Funkquelle | Ja — eigene managed TX **oder** Fremd-OFDM-DATA | `FACT` (`P1` Erzeugung; `P2-002`) |
| Abhängigkeit eigener Traffic | Typisch hoch für stabile Rate (ESPectre/esp-csi) | `FACT` Upstream-Muster |
| Abhängigkeit fremder Traffic | Bei Passiv: ja | `FACT` |
| Traffic vs Umwelt/Motion | HeliosSm: Motion ≫ UDP-Traffic auf Derived; r≈0.02 | `FACT` lokal Repro (`P2-007`); Transfer **`UNKNOWN`**; Assessment ohne Kontrollen **`REJECTED`** (`P2-008`) |
| Reproduzierbarkeit | Upstream-Datasets/Tools ja; **unser** Lab | Desk-Tools `FACT`; eigenes Lab **`UNKNOWN`** (A0-Artefakt nicht zählen) |
| Offline-Analyse | CSV/I/Q → Amp/Phase/Features | `FACT` Muster (CSI-Tool, HeliosSm, esp-csi logs) |
| Hardware | `SOC_WIFI_CSI_SUPPORT`; S3≠C6 Config/rx_ctrl | `FACT` (`P1-001/002`); nicht alle Chips (`P1-008`) |
| Primärquellen | IDF CSI Docs/API; esp-csi | `FACT` |
| Experimentelle Evidenz | ESPectre Desk; HeliosSm Repro; Sheet R1/field R0 | gemischt; eigenes Field **`UNKNOWN`** |
| Evidenzqualität | API stark; Sensing-Hypothese mittel (fremd/lokal); Transfer schwach | — |
| Implementierungsaufwand | Mittel–hoch (Chip-Parser, Traffic-Kontrolle, Drops) | `INFERENCE` |
| Auditierbarkeit | Hoch bei RAW/DERIVED/ASSESSMENT-Trennung | `INFERENCE` (Sheets + P2) |
| Erkenntnisgewinn | Hoch für Multipath-Sensing-Forschung/Instrument | `HYPOTHESIS` |
| Failure Modes | Kein Traffic → kein CSI; Chip-Mix; Presence-Overclaim; Traffic-Kontamination ohne E1–E4 | `FACT`/`REJECTED` Claims |

**Kill-Kriterien T1**

| Kill | Status |
|------|--------|
| Keine öffentliche CSI-API / kein Roh-I/Q | nicht eingetreten |
| Sensing ohne jegliche Frames | `REJECTED` Continuous Sounding |
| Motion-Assessment ohne Traffic-Kontrollen | `REJECTED` als Contract — **designfähig**, kein Technologie-Tod |
| Universelles CSI auf allen ESP32 | `REJECTED` Marketing; Chip pinnen |

**Verdict T1: `GO` (Experiment-/Instrument-Pfad)** — Messgröße und Rohdaten klar; Offline möglich; Hypothese durch HeliosSm **plausibel** gestützt unter Kontrollen; fundamentale Killerfrage „geht CSI technisch?“ verneint nicht.  
**Nicht:** Produkt-GO · Presence-GO · Entscheidung „wir bauen CSI-Projekt“.

---

### T2 — Promiscuous Capture

| Kriterium | Bewertung | Status / Beleg |
|-----------|-----------|----------------|
| Messgröße | Empfangene 802.11-Frame-Beobachtung (Header/Payload/Länge) | `FACT` IDF Sniffer (`P1-005`) |
| Rohdaten | `wifi_promiscuous_pkt_t` + Payload (MIMO oft nur Länge) | `FACT` |
| Metadaten | gleiches `rx_ctrl`-Bündel | `FACT` |
| Auflösung | Packet-Ereignisse; Drop unter Last | `FACT` Buffer-Limits (Sheet) |
| Passiv | Ja (RX-only Sniffer) | `FACT` |
| Externe Quelle | Fremd-Traffic in Luft | `FACT` |
| Eigener Traffic | Optional | — |
| Traffic vs Umwelt | Frame-Mix/Rate ≠ Multipath-Motion | `INFERENCE`; als Sensing **`REJECTED`** (`P1-005`, Sheet) |
| Repro / Offline | PCAP gut auditierbar | `FACT` Marauder-Pfad |
| Hardware | breit Wi-Fi-fähig; Throughput-Impact | `FACT` Docs |
| Sensing-Hypothese „Presence aus Sniff“ | nicht gestützt | **`REJECTED`** Contract |
| Aufwand | Mittel (Buffer/PCAP) | `INFERENCE` |
| Erkenntnisgewinn Sensing | niedrig als Motion-Sensor | `INFERENCE` |
| Failure Modes | Drops; ≠ CSI; ≠ Power-Meter; Policy (Capture≠Attack) | `FACT`/`REJECTED` |

**Verdict T2:**  
- **`NO-GO`** als RF-**Sensing**-Messvertrag (Motion/Presence/Multipath).  
- **`GO`** nur als **Capture-/Kontaminations-/Kontrast-Hilfswerkzeug** neben einem Sensing-Pfad (optional).

---

### T3 — RX-Metadaten (RSSI, noise_floor, …)

| Kriterium | Bewertung | Status / Beleg |
|-----------|-----------|----------------|
| Messgröße | Per-RX Radio-Meta (rssi, noise_floor, channel, ts, rate/MCS, …) | `FACT` (`P1-006`) |
| Rohdaten | Felder in `wifi_pkt_rx_ctrl_t` / HE-rxctrl | `FACT`; Layout chipabhängig |
| Auflösung | Pro Packet; kein kontinuierliches Spektrum | `FACT` |
| Passiv | Mit RX-Ereignissen (STA/Promisc/CSI-CB) | `FACT` |
| Traffic-Abhängigkeit | Braucht RX | `FACT` |
| Traffic vs Motion | RSSI allein: Walk-by möglich (Own-Link), aber ≠ CSI-Multipath | Field Own-Link `FACT`; Generalisierung **`UNKNOWN`** |
| Offline | Ja (Zeitreihen) | `FACT` |
| Sensing-Hypothese „Raum-Presence aus Meta allein“ | schwach / nicht belegt als Multipath | **`HYPOTHESIS`**/meist **`REJECTED`** wenn Presence |
| noise_floor = Occupancy | | **`REJECTED`** (`P1`) |
| Aufwand | niedrig als Beiwerk | `INFERENCE` |

**Verdict T3: `FURTHER AUDIT`** als **alleiniger** Sensing-Kern (zu grob / Hypothese dünn).  
**`GO` als Pflicht-Beiwerk** jedes CSI-/Promisc-Vertrags (Meta immer mitloggen).

---

### T4 — Own-Link high-rate RSSI

| Kriterium | Bewertung | Status / Beleg |
|-----------|-----------|----------------|
| Messgröße | RSSI des **eigenen** STA-Links über Zeit | `FACT` Method + rfmonitor Field |
| Rohdaten | RSSI-Samples (Ring) | `FACT` App/Method |
| Passiv bzgl. Sensing-TX | nutzt bestehenden Link; kein CSI | `FACT` |
| Traffic | Link-Traffic/Beacons der Association | `INFERENCE` |
| Motion-Hinweis | Walk-by reproduzierbar messbar (Küche) | `FACT` `EVID-RF-2026-10-26-001/002` |
| Presence / Person Count | | **`REJECTED`** (`003`, Method) |
| vs CSI | anderer Contract | `FACT` Sheet/Method |
| Offline | Session-Export | `FACT` |
| Hardware | STA-fähig; Mini/S3 getestet im rfmonitor-Kontext | Field |
| Erkenntnisgewinn | Char/Kontrast; nicht Multipath-Forschung | `INFERENCE` |

**Verdict T4: `GO`** für **engen** Charakterisierungs-/Kontrast-Pfad (Link-Motion-Sensitivity) — bereits Method + Field.  
**`NO-GO`** als Ersatz für CSI-Multipath-Sensing oder Presence-Produkt.

---

### T5 — Environment Scan / Score (`rf-environment-monitor`)

| Kriterium | Bewertung | Status |
|-----------|-----------|--------|
| Messgröße | Heuristik-Score über Scan-Listen | `FACT` Sheet — nicht Physik-Kalibrierung |
| Sensing Multipath/Motion | | **`REJECTED`** als CSI/Presence-Ersatz |
| CCA-Proxies | | **`REJECTED`** |
| Verdict | **`NO-GO`** für RF-Sensing-Messvertrag | Monitoring bleibt rfmonitor-Kontext |

---

## 6. Kill-Kriterien (kampagnenweit)

| # | Kill | Betrifft | Stand |
|---|------|----------|--------|
| K-A | Öffentliche CCA-Occupancy-API fehlt | T0 | **Kill bestätigt** → NO-GO |
| K-B | Promiscuous ≡ Sensing/Presence | T2 | **REJECTED** Claim |
| K-C | Motion-Assessment ohne Traffic-Kontrollen | T1 Assessment | **REJECTED** Contract; Technologie T1 nicht tot |
| K-D | CSI ohne RX-Frames | T1 | Continuous Sounding **REJECTED** |
| K-E | Own-Link ≡ Presence | T4 | **REJECTED** |
| K-F | Ein CSI-Binary für alle Chips | T1 | **REJECTED**; Chip pinnen |

Keine dieser Kills eliminiert T1 als **Experimentpfad**, sofern Assessment diszipliniert bleibt.

---

## 7. Offene UNKNOWNs

| UNKNOWN | Warum relevant |
|---------|----------------|
| CSI-Ausbeute/Stabilität auf **unserer** S3-Lab-Hardware | Transfer HeliosSm/ESPectre nicht automatisch |
| Passiv-Ambient-pps ohne Peer-TX | K5 Residual |
| HeliosSm Firmware/PHY-Repro | P2-009 |
| Cross-Room / Cross-Device CSI Transfer | field R0 |
| Ob RX-meta-alone für definierten Use-Case reicht | T3 |
| Ob Promiscuous-Drops unseren Capture-Vertrag sprengen | T2 Hilfspfad |
| A/B/C Projektklasse | bewusst offen — Matrix ≠ Entscheidung |

---

## 8. Ranking / Shortlist

| Rang | Kandidat | Wofür Shortlist? |
|------|----------|------------------|
| 1 | **T1 CSI** | Einziger Ansatz mit klarer Multipath-Rohgröße + plausibler Traffic×Motion-Evidenz |
| 2 | **T4 Own-Link RSSI** | Billiger, bereits field-belegter Kontrast-/Char-Pfad (anderer Claim) |
| 3 | **T3 RX-meta** | Pflicht-Beiwerk; allein nicht Shortlist-Kern |
| — | **T2 Promisc** | Tooling, nicht Sensing-Kern |
| — | **T5 / T0** | NO-GO Sensing |

---

## 9. GO / NO-GO / FURTHER AUDIT

| Kandidat | Verdict | Bedeutung |
|----------|---------|-----------|
| T1 CSI | **GO** | Darf als **möglicher nächster Experimentpfad** weiterverfolgt werden (nach explizitem Go) |
| T2 Promisc | **NO-GO** Sensing / **GO** Hilfs-Capture | Nicht als Sensing-Kern |
| T3 RX-meta | **FURTHER AUDIT** allein / **GO** Beiwerk | — |
| T4 Own-Link | **GO** enger Char-Pfad | Nicht CSI-Ersatz |
| T5 Env-Score | **NO-GO** Sensing | — |
| T0 CCA | **NO-GO** | geschlossen |

---

## 10. Abschließende Entscheidungsempfehlung

1. **Projektentscheidung: noch nicht möglich und nicht empfohlen** — Matrix ersetzt kein Lab und keine Scope-Wahl (Instrument vs Produkt vs Kontrast-only).  
2. **Technologie-Shortlist für „ob überhaupt weiter?“:**  
   - **Ja, ein Experimentpfad ist gerechtfertigt:** **T1 CSI** (RAW-Instrument + Traffic-Kontrollen; Assessment streng getrennt).  
   - **Parallel sinnvoll als Kontrast:** **T4 Own-Link** (bereits Method/Field; kein Presence).  
   - **Nicht** als Sensing-Kern: Promisc, Env-Score, CCA.  
3. Formulierung, falls gewünscht streng:  
   > **„Noch kein Kandidat ausreichend belastbar“** für ein **Produkt**/Presence-Projekt — korrekt.  
   > Für einen **auditierten CSI-Roh-/Characterization-Experimentpfad** ist T1 dagegen als **GO-Kandidat** belastbar genug, **ohne** damit CSI als gewähltes Produkt festzulegen.  
4. Nächster Schritt nach Review dieser Matrix: **explizite Entscheidung** (CSI-Experimentpfad / Own-Link-only / Pause / anderer Scope) — erst dann ggf. Lab. Uncommitted Instrument **nicht** stillschweigend als Entscheidung werten.

---

## Quellenverzeichnis (genutzt)

- PHASE0–2 · evidence `EVID-RFSENSE-P0/P1/P2-*`  
- ESP-IDF Wi-Fi CSI / Sniffer / types (via PHASE1 Pins)  
- Sheets: `wifi-csi-motion`, `esp-wifi-promiscuous-pcap`, `rf-environment-monitor`  
- Method: `own-link-motion-sensitivity`  
- Prior: espectre-2026-foreign, esp32-marauder-2026-foreign, rfmonitor motion-delta / v2  
- HeliosSm dataset + Desk-Repro P2-007  
- CSI-Tool / esp-csi console_test (P2)  

**Nicht gewertet als Tech-Evidenz:** uncommitted `instrument/*` A0-FAIL.
