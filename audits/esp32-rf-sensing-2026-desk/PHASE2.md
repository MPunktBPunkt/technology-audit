# Phase 2 — Kill-Gates K5 / K6 / K7 (gezielt, kein Voll-Audit)

```yaml
campaign: esp32-rf-sensing-2026-desk
phase: 2
date: 2026-10-26
mode: foreign-kill-desk
pins:
  csi_tool: "StevenMHernandez/ESP32-CSI-Tool@cce5b1a"
  esp_csi_radar: "espressif/esp-csi@8633d67 examples/esp-radar/console_test"
  helios: "HeliosSm/wifi-sensing-csi-network-traffic@3f374b5"
new_sheets: 0
full_audits: false
```

**Exit P2:** K5–K7 auf Desk-Ebene beantwortet; Residuals für Phase 3 benannt; **keine** A/B/C-Entscheidung; **keine** Experimentplanung.

Hinweis K6: Eigenständiges Repo `esp-wifi-radar-lab` nicht auffindbar → Gate auf **esp-csi `esp-radar/console_test`** gemappt (Instrument-/Session-Muster aus PHASE0 G5).

---

## 1. K5 — ESP32-CSI-Tool (Passiv)

### Fragen → Status

| Frage | Status | Kurzantwort |
|-------|--------|-------------|
| CSI ohne eigenen TX-Stack / kontrollierte Sendesequenz nutzbar? | **`FACT`** (API-Design) | Ja im Subprojekt `./passive`: `WIFI_MODE_NULL` + Promiscuous + CSI-CB — **kein** eigenes TX |
| Was bedeutet „passiv“ konkret? | **`FACT`** | RX-only auf festem Kanal; CSI nur bei empfangenen Frames Dritter |
| Welche Frames/Traffic-Quelle liefern Samples? | **`FACT`** / Residual | Filter `WIFI_PROMIS_FILTER_MASK_DATA`; Maintainer: CSI-fähige **OFDM DATA** auf Kanal nötig — sonst leer (`UNKNOWN` Rate/Qualität ohne Lab) |
| Rohmessung vs Processing/Assessment? | **`FACT`** | Firmware-Default: CSV `CSI_DATA` + RX-meta + **I/Q RAW**; Amp/Phase nur Compile-Flags / Host-Plot = **Derived**; keine Motion-Assessment im Tool |

### Belege

- `passive/main/main.cc`: `esp_wifi_set_mode(WIFI_MODE_NULL)`, Promiscuous DATA, Channel pin, `csi_init("PASSIVE")`.
- `_components/csi_component.h`: `CSI_RAW 1`; Amp/Phase `#if` aus; Serial-Zeile = meta + `buf`.
- `active_sta`: eigener TX via `socket_transmitter_sta_loop` — Kontrast zu Passiv.
- Issue #22 (Maintainer): ohne nahe CSI-fähige OFDM-Frames → keine CSI; Kanal/Band müssen passen.

### Gate-Status K5

| | |
|--|--|
| **Geschlossen** | Passiv = RX ohne eigenen TX-Stack ist **implementiert und definiert**; Roh = I/Q+meta |
| **Offen** | Praktische Ausbeute (pps, Drop, Stabilität) ohne Lab; ob „nur Ambient“ für Messvertrag reicht |
| **Konsequenz** | Passiv-Pfad darf in Phase 3 als Option stehen, muss aber **Traffic-Quelle Dritter** spezifizieren — nicht „TX-frei im Raum“ |

---

## 2. K6 — Radar-Lab / Instrument-Muster (`esp-radar/console_test`)

### Fragen → Status

| Frage | Status | Kurzantwort |
|-------|--------|-------------|
| Minimale belastbare Instrument-/Session-/Offline-Struktur? | **`FACT`** (Muster) | Host-Tool schreibt Session-Logs: `log/csi_data.csv`, `log/radar_data.csv`, `log/device_info.csv`, `log/log_data.txt`; Action-Capture unter `tools/data/<label>/` |
| Messinfrastruktur vs Demo-/Experimentcode? | **`FACT`** Trennung | **Infrastruktur:** Serial-Protokoll, CSI-CSV, Label-Capture, optional TX (`csi_send` / Null-Data / Ping). **Demo/Produkt:** „Radar model“ Presence/Move, Kalibrier-UI, Bewegungsstatistik |
| Brauchbarer Raw→Derived→Assessment-Pfad? | **`INFERENCE`** / begrenzt | UI trennt Raw vs Radar; Assessment (someone/move) ist **Algorithmus-Demo**, kein auditfester Messvertrag; Derived oft implizit (Filter, Eigenwerte) |

### Belege

- README console_test: Display / Acquisition / Analysis; Kalibrierung leerer Raum; Action collection → Dateien.
- `esp_csi_tool.py`: legt `log/*` an; sammelt gelabelte CSI unter `data/`.
- `app_main.c`: managed Traffic (`WIFI_CSI_SEND_NULL_DATA` oder Ping) für CSI-Rate — **kein** Passiv-Instrument.

### Gate-Status K6

| | |
|--|--|
| **Geschlossen** | Wiederverwendbares Muster: **Session-CSV + Labels + getrennte Raw-Ansicht**; braucht kontrollierten TX oder Router-Antworten |
| **Offen** | Drop/Timestamp-Contract, Chip-Layout-Parser, Offline-Replay-Schema als **eigene Spec** (nicht im Demo fertig) |
| **Konsequenz** | Phase-3 Instrument = Spec ableiten, **nicht** console_test/Radar-UI klonen; Presence/Move-Demo **nicht** als Assessment-Contract übernehmen |

---

## 3. K7 — HeliosSm (Traffic vs Motion) — Belastungstest Messvertrag

Repo: `wifi-sensing-csi-network-traffic` — **kein** weiteres „interessantes CSI-Produkt“, sondern Kontrollgruppen-Design.

### Design (Desk-FACT)

| Element | Status | Inhalt |
|---------|--------|--------|
| Vergleichsgruppen | **`FACT`** | E1 Baseline · E2 Human Motion (LOS Walk) · E3 UDP-Traffic (2/5/10 Mbps, static) · E4 Coexistenz Motion+random Traffic |
| Capture | **`FACT`** (Doku) | 100× 60 s, ~50 Hz CSI, ESP32-C6 Paar; CSV `CSI_DATA` + I/Q; E4 parallel `tasas_*.csv` |
| Pipeline-Schichten | **`FACT`** | RAW I/Q → Amp → Median+Butterworth → PCA → PSD/Var/`d95` (**Derived**); Threshold/Presence = **Assessment** |
| Firmware | **`UNKNOWN`/Gap** | `firmware/` nur README — Quellcode **nicht** publiziert (TX `esp_wifi_80211_tx` 50 Hz behauptet) |

### Reproduktion (dieser Desk-Lauf, 2026-10-26)

Upstream-Skript `Escenario 4/analisis_validacion_e4.py` auf mitgelieferten CSVs:

| Szenario | n | VarMov_max (Ø) | Comp95 (Ø) |
|----------|---|----------------|------------|
| E1 Baseline | 15 | 4.46 | 47.2 |
| E2 Motion | 20 | 309.37 | 4.05 |
| E3 Traffic | 45 | 7.05 | 46.4 |
| E4 Mov+Traffic | 20 | 422.18 | 2.10 |

- ANOVA Var.movil: F≈132, p≈6e-34  
- E4 Mbps vs Var.movil: **Pearson r ≈ 0.02** (n≈55k) — Rate moduliert kinematische Varianz kaum  
- Silhouette (4 Klassen, Feature-Set): **0.182** — Klassenüberlapp nicht vernachlässigbar  
- „Presence“ tau>30 in E4: 100 % der Iterationen im **ihrem** Assessment — für unseren Vertrag nur **Upstream-CLAIM/INFERENCE**, nicht VALIDATED Transfer

### Fragen → Status

| Frage | Status | Kurzantwort |
|-------|--------|-------------|
| Motion vs Traffic-Variation getrennt? | **`FACT`** (dieses Design) | E2/E4 ≫ E1/E3 auf kinematischen Metriken; E3 ≈ Baseline; r(Mbps,var)≈0 |
| Kontrollierte Bedingungen / Vergleichsgruppen? | **`FACT`** | E1–E4 + Traffic-Log in E4 |
| Baseline / Traffic / Motion / Umwelt getrennt? | **`FACT`** Design; Umwelt **`UNKNOWN`** | Umweltvariation (andere Räume/Geräte) nicht systematisch |
| Welche Motion-/Presence-Claims evidenzgetragen? | **`INFERENCE`** lokal | „In diesem Setup trennt kinematische Varianz Motion von UDP-Last“ belastbar als Desk-Repro; **Presence-Produkt** / Generalisierung **nicht** |
| Wo bricht Übertragbarkeit? | **`UNKNOWN`** / Risiken | Ein Raum, ein Subjekt, LOS, festes C6-Paar, unveröffentlichtes FW, schwache 4-Klassen-Silhouette, andere Traffic-Arten (TCP/BU/Video) ungetestet |

### Gate-Status K7

| | |
|--|--|
| **Geschlossen (Kill)** | Motion-/Presence-**Assessment ohne** Traffic-Kontrollgruppen → **`REJECTED`** für Messvertrag |
| **Geschlossen (Positiv)** | Kontrollmuster E1–E4 + Schichttrennung RAW/Derived/Assessment ist **Vorbild** für Phase-3 Spec |
| **Offen** | Eigenes Lab; Cross-Room/Device; Firmware-Repro; andere Traffic-Klassen |

---

## 4. Evidence-IDs (Phase 2)

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-RFSENSE-P2-001` | CSI-Tool `passive`: NULL-Mode + Promisc DATA + CSI, kein eigener TX | `FACT` | `passive/main/main.cc` @ `cce5b1a` |
| `EVID-RFSENSE-P2-002` | Passiv braucht fremde OFDM-DATA auf Kanal; sonst leer | `FACT` (Maintainer) / Rate `UNKNOWN` | Issue #22 + Code-Filter |
| `EVID-RFSENSE-P2-003` | CSI-Tool Default-Ausgabe = RAW I/Q + RX-meta CSV; Amp/Phase Derived | `FACT` | `csi_component.h`; Host-Plot Derived |
| `EVID-RFSENSE-P2-004` | console_test Session-Muster: `log/csi_data.csv` (+ radar/device/log) und gelabelte `data/` | `FACT` | `esp_csi_tool.py` @ `8633d67` |
| `EVID-RFSENSE-P2-005` | console_test Radar Presence/Move = Demo-Assessment, nicht Messvertrag; CSI-Rate via Null/Ping/csi_send | `FACT` / `REJECTED` als Contract | README + `app_main.c` |
| `EVID-RFSENSE-P2-006` | HeliosSm E1–E4 Kontrollgruppen + Traffic-Log E4 | `FACT` | README + Capture-Skripte @ `3f374b5` |
| `EVID-RFSENSE-P2-007` | Repro: Motion-Metriken ≫ Traffic-only; Pearson r(Mbps,var)≈0.02 | `FACT` (Desk-Repro Upstream-Pipeline) | `analisis_validacion_e4.py` auf Repo-CSVs, 2026-10-26 |
| `EVID-RFSENSE-P2-008` | Motion/Presence ohne Traffic-Kontrollen als Messvertrags-Assessment | **`REJECTED`** | Konsequenz aus P2-006/007 + SCOPE |
| `EVID-RFSENSE-P2-009` | HeliosSm Firmware-Quellcode nicht im Repo → Capture-PHY nicht voll repro | `UNKNOWN` (Gap) | `firmware/README.md` |
| `EVID-RFSENSE-P2-010` | Kein neues Technology Sheet aus Phase 2 | `FACT` (Prozess) | dieser Text §6 |

---

## 5. Kill-Fragen: geschlossen vs offen

| Gate | Geschlossen | Bleibt offen |
|------|-------------|--------------|
| **K5** | Passiv-Definition; RAW vs Derived; kein eigener TX möglich | Lab-Ausbeute Ambient; Messvertrags-Tauglichkeit Passiv-only |
| **K6** | Session/Label-Muster; Demo ≠ Instrument-Contract | Offline-Replay-Spec; Drop/Clock; Chip-Parser |
| **K7** | Traffic-Kontrollen **Pflicht** vor Motion-Assessment; E1–E4 Vorbild; lokal Traffic≪Motion auf Metriken | Transfer; FW-Repro; Traffic-Klassen; eigenes Lab |

---

## 6. Sheets / Apps

| Kandidat | Phase 2 Entscheidung |
|----------|----------------------|
| Neues Technology Sheet (Passiv-CSI / Traffic-Kontamination / Radar-Lab) | **Nein** — kein neuer Hardware-/API-Contract; bestehendes `wifi-csi-motion` + IDF-FACTS reichen |
| Neue Application unter `esp32-rf-sensing` | **Nein** — Planung, kein Messvertrag |
| Method-Note „CSI traffic-vs-motion controls“ | **Kandidat Phase 3** (≥1 eigener Einsatz + Spec) — nicht jetzt anlegen |

---

## 7. Konsequenz für Phase 3 (ohne A/B/C-Entscheidung)

Phase 3 darf synthetisieren:

1. **Rohbeobachtungen** (aus P1): CSI I/Q, Promiscuous, RX-meta — CCA bleibt `REJECTED`.
2. **Erzeugung:** managed TX **oder** dokumentierte Fremd-Traffic-Quelle (K5); Passiv nicht als „sensor ohne RF-Ereignisse“ verkaufen.
3. **Instrument-Minimum (K6):** Session mit RAW-CSV, Timestamps/Drops spezifiziert, Labels — **ohne** eingebettetes Presence-Produkt.
4. **Assessment-Gate (K7):** Jeder Motion-/Presence-Claim braucht Vergleichsgruppen mindestens analog E1–E4 (Baseline / Motion / Traffic / Coexistenz); sonst Claim `REJECTED`.
5. **Keine** A/B/C- und keine Experimentplanung in diesem Lauf — nur obige Constraints als Input.

---

## 8. Phase-2 Exit → Stop

| Check | Ergebnis |
|-------|----------|
| K5/K6/K7 beantwortet | ja |
| Evidence-IDs | P2-001…010 |
| Neue Sheets | 0 |
| A/B/C Decision | **nicht** |
| Experimentplanung | **nicht** |
| Nächster Schritt | **Phase 3 Synthese** (separater Lauf) |
