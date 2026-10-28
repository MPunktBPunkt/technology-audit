# Phase 3 — Messvertrag + minimale Characterization (**PLAN / Review v3**)

```yaml
campaign: esp32-rf-sensing-2026-desk
phase: 3
date: 2026-10-26
mode: synthesis-plan
status: draft-for-review-v3   # kein Lab; kein Commit
new_sheets: 0
new_methods_published: 0
ml_radar_presence: false
promiscuous_v0: false
lab_chip: esp32-s3
traffic_peer: d1-mini
lab_exclude: [esp32-c6]
```

**Ziel:** kleinster physikalisch sinnvoller, reproduzierbarer **Rohmessvertrag** + **2–3 Characterization-Methoden** — **kein** Sensing-Produkt, kein ML, kein Radar, kein Presence-Sheet.

**Stop (aktualisiert 2026-10-26):** v3 Desk freigegeben, danach vorzeitiger A0-Instrument-Pfad → **suspendiert**.  
Lab/C1 **nicht** fortführen. Instrument = Artefakt ohne Projektentscheid — siehe [ARTIFACT-INSTRUMENT-2026-10-26](ARTIFACT-INSTRUMENT-2026-10-26.md).  
Nächster Kampagnenschritt = **Technologiematrix**, nicht A0.

---

## 0. Entschiedene Pins (Review-Input)

| Thema | Entscheidung |
|-------|--------------|
| Lab-Vergleich S3↔C6 | **Nein** — C6 Capability bereits Phase 1 Desk; **außerhalb** dieses Experiments |
| CSI-Messknoten | **ESP32-S3** |
| Traffic-Gegenstelle | **D1 Mini** (kontrollierter Wi-Fi-Traffic), sofern technisch geeignet |
| Messpfad v0 | **D1 Mini → kontrollierter Wi-Fi-Traffic → S3 CSI RX** |
| Promiscuous v0 | **Nein** — später optional |
| C1 Akzeptanz-% / pps | **Nicht vorab** — erst charakterisieren, dann empirische Bänder |
| C3 | **Nur nach C1/C2-Entscheidung** — nicht erzwingen |
| Traffic N/H · Motion · Dauer · Capture | **§8** (v3) |

---

## 1. Ebenen — RAW → DERIVED → ASSESSMENT

```text
RAW          CSI-I/Q-Ereignis + RX-meta + Zeit/ID/Gaps   ← Messknoten-Contract
  ↓ (Formel, versioniert)
DERIVED      Amplitude, Phase, Raten, Streuungsmaße      ← Diagnose / Characterization
  ↓ (Interpretation + Kontrollen)
ASSESSMENT   Motion / Presence / …                       ← bewusst getrennt; keine Grundfähigkeit
```

| Ebene | Ist | Ist nicht |
|-------|-----|-----------|
| **RAW** | Beobachtung des Radios am S3 bei RX (I/Q + Meta) | Motion, Presence, „jemand da“ |
| **DERIVED** | Rechenbare Größen aus RAW derselben Session | Assessment-Label |
| **ASSESSMENT** | Anspruch über Weltzustand (Motion/Presence) | Teil des Raw-Contracts oder der Messknoten-Grundfunktion |

**CSI = Rohbeobachtung.** Amp/Phase/Statistiken = **DERIVED**. Motion/Presence = **ASSESSMENT** und **keine** Grundfähigkeit des S3-Messknotens.

---

## 2. Minimaler Messvertrag `MV-ESP32-CSI-RAW-v0` (Draft)

### 2.1 Identität / Topologie

| Feld | Wert |
|------|------|
| Contract-ID | `MV-ESP32-CSI-RAW-v0` |
| RX-Knoten | ESP32-S3 (Non-HE CSI-Config-Pfad; Parser S3-classic) |
| TX / Traffic | D1 Mini — Profile **N** / **H** (§8.1); Eignung vor C1 smoke-testen (A0) |
| Pfad | D1 Mini → kontrollierter Wi-Fi-Traffic → S3 CSI RX |
| Band / Kanal | 2.4 GHz; Kanal in `session.yaml` fest |
| Außerhalb | ESP32-C6; Promiscuous-Capture; CCA |
| Session | Host-Bundle; **keine** on-device Motion-/Presence-Semantik |

Wenn D1 Mini als kontrollierte Gegenstelle **technisch ungeeignet** ist → Instrumentierungs-Gate vor C1 (anderer Peer oder TX-Modus); Contract-Topologie dann nachziehen — **kein** stilles Ausweichen auf unkontrollierten Ambient-Traffic als Default.

### 2.2 RAW — Pflicht pro Sample

| Gruppe | Pflicht | Inhalt |
|--------|---------|--------|
| **CSI I/Q** | ja | `buf` Imag/Real `int8` + `len` (IDF S3-Semantik) |
| **RX-Metadata** | ja | mind. `rssi`, `noise_floor`, `channel` (+ secondary/BW wo Struct), rate/MCS/`sig_mode`, `sig_len`/`rx_state` wo vorhanden |
| **Zeitbasis** | ja | Device-`timestamp` (rx_ctrl) **und** Host-Empfangszeit; Drift notieren |
| **Channel / PHY-Kontext** | ja | `esp32-s3`, CSI-Config-Flags, Kanal, Wi-Fi-Mode am RX |
| **Sample-/Frame-ID** | ja | monotoner `seq`; Quell-MAC wenn API liefert; optional `rx_seq` |
| **Drops / Gaps** | ja, soweit belastbar | Session-Zähler und/oder `seq`-Sprünge; Unsicherheit als `UNKNOWN` markieren — nicht erfinden |
| Promiscuous-Frames | **nein (v0)** | später optional |
| CCA / Occupancy | **nein** | `REJECTED` (P1-007) |
| Motion / Presence Felder | **nein** | ASSESSMENT |

**Session-Header:** Contract-ID, Tool/FW-Pins, S3 + D1-Rolle, Kanal, Traffic-Profil-ID, Start-Hostzeit, Lage/Stimulus-Notiz.

**Bundle:** `session.yaml` · `csi_raw.csv`|`.ndjson` · `session_stats.json` (counts, duration, observed_rate, gap_summary).

### 2.3 DERIVED — außerhalb RAW-Wahrheit

Nur versionierte Formeln aus RAW:

| Derived | Rolle in Characterization | Nicht nennen als |
|---------|---------------------------|------------------|
| Amplitude / Phase pro Subcarrier | C1 Streuung; C2 Effektmaße | Motion / Presence |
| Sample-/Frame-Rate, Gap-Rate | C1 Repro | CCA / „busy“ |
| Streuungsmaße (σ, Δ) über Zeit/Sessions | C1/C2 Diagnose | Assessment |
| Weitere Filter/PCA/… | nur in Method-Pipeline, versioniert | Raw-Contract |

### 2.4 ASSESSMENT — getrennt

| Claim | Im Messknoten-Contract? | Wann |
|-------|-------------------------|------|
| Motion | **nein** | frühestens nach C2; nur mit Zellen A–D |
| Presence / empty-room | **nein** — keine Grundfähigkeit | außerhalb Phase-3-Exit |
| Person Count / Identity | `REJECTED` | SCOPE |

Phase-3-Exit = **Vertrag + Methoden**, nicht Produkt.

---

## 3. Characterization

### C1 — Baseline / Reproduzierbarkeit (**charakterisieren, nicht vorab passen**)

| | |
|--|--|
| **Frage** | Wie stabil und reproduzierbar ist der Rohdatenstrom unter identischer Situation? |
| **Setup** | S3 + D1; Traffic-Profil **N** (§8.1); Lage fix (§8.2); **kein** Motion-Stimulus; Capture laut §8.4 |
| **Ablauf** | ≥3 Sessions à **T_session** (§8.3); gleiches Header-Profil; Abweichungen dokumentieren |
| **Messen / berichten** | (1) Sample-/Frame-Rate · (2) Gaps/Drops · (3) Zeitstabilität (Device vs Host) · (4) I/Q- bzw. Amp-Streuung bei identischer Situation · (5) RSSI/RX-Metadata-Stabilität · (6) Session-zu-Session-Streuung |
| **Akzeptanzgrenzen** | **keine** festen Gap-%/pps-Schwellen vorab; **nach** C1 empirische Bänder für spätere Sessions ableiten |
| **Abbruch** | Instrument liefert Pflicht-RAW nicht, D1-Pfad unbrauchbar, oder Streuung so hoch dass kein sinnvoller Vertrag formulierbar → zurück Instrumentierung; Klasse **A** nur als Fallback-Diskussion, nicht automatischer Produktpfad |

### C2 — Motion × Traffic (2×2)

| | **normaler Traffic** (Profil N) | **hoher/variierter Traffic** (Profil H) |
|--|--------------------------------|----------------------------------------|
| **kein Motion** | **A** Baseline | **B** Traffic-Effekt |
| **Motion** | **C** Motion-Effekt | **D** Motion×Traffic |

| | |
|--|--|
| **Traffic** | Nur **N** und **H** (§8.1) |
| **Motion** | Ein Protokoll (§8.2); in C und D identisch wiederholen |
| **Zieltrennung** | Baseline (A) · Traffic-Effekt (B vs A) · Motion-Effekt (C vs A) · Interaktion (D vs C und D vs B) |
| **Metrik** | Wenige vorher benannte **DERIVED**-Diagnosen (nicht ML); gleiche Pipeline für A–D |
| **Pass / Fail** | Empirisch nach C1-Bändern wo sinnvoll; klar dokumentieren ob Trennung gelingt. Scheitert Trennung → Motion-**ASSESSMENT** bleibt `REJECTED`; Rohvertrag kann bestehen |
| **Nicht** | Presence, Person Count, ML, Radar |

### C3 — Transfer (**bedingt**)

| | |
|--|--|
| **Entscheidung** | Erst **nach** Auswertung C1/C2 |
| **Erzwingen** | **Nein**, wenn Rohmessung oder Kontrollbedingungen (A–D) nicht ausreichend stabil |
| **Falls ja** | Zuerst neuer Zeitpunkt / neue Session bei gleicher Lage; erst dann optional Lage **oder** Person |
| **Sonst** | Contract bleibt lab-lokal; Phase-3-Exit ohne C3 möglich |

---

## 4. Erwartete Ausgaben

| Artefakt | Inhalt |
|----------|--------|
| Freigegebener Messvertrag | §2 RAW/DERIVED/ASSESSMENT + Topologie |
| C1-Report | Repro-Charakteristik + **abgeleitete** empirische Bänder |
| C2-Report | A–D Trennung Baseline / Traffic / Motion / Interaktion |
| C3-Report | nur wenn freigegeben |
| Method-Notes | nach erstem Einsatz (Kandidaten §6) |
| **Nicht** | fertiges Sensing-Produkt / Presence-Sheet |

---

## 5. Akzeptanz- / Abbruch (Kampagne)

| Stufe | Kriterium | Folge |
|-------|-----------|--------|
| **A0** | D1→S3-Pfad liefert RAW-Pflicht | Fail → Instrument; kein C1 |
| **A1** | C1 Charakterisierung abgeschlossen; empirische Bänder formulierbar **oder** Abbruch begründet | Fail/Abbruch → kein C2 Motion-Pfad; Vertrag ggf. verwerfen |
| **A2** | C2 A–D ausgewertet; Trennung oder „nicht trennbar“ explizit | nicht trennbar → Assessment `REJECTED`; RAW ok möglich |
| **A3** | C3 nur nach bewusster Go-Entscheidung | Skip erlaubt |
| **Hard stop** | CCA / Presence als Grundfähigkeit / ML-Radar-Sheet | Prozess-`REJECTED` |

---

## 6. Decision Trace — Projektklasse A / B / C

| Klasse | Bedeutung | Bezug dieses Plans |
|--------|-----------|-------------------|
| **A** | Observation ohne CSI-Pflicht (z. B. später Promisc/RX-meta) | Fallback-Diskussion wenn CSI-Rohstrom scheitert — **nicht** v0-Ziel |
| **B** | **CSI RAW Lab Instrument** (S3 + kontrollierter Peer-Traffic, Session/Offline) | **angestrebt** nach erfolgreichem C1 |
| **C** | Sensing-Produkt (on-device Motion/Presence) | **nicht** Phase-3-Exit; erst nach C2+expliziter Entscheidung |

| Entscheidung | Evidence / Pin | Konsequenz |
|--------------|----------------|------------|
| Lab-Hardware | Review v2 | S3 RX + D1 Traffic; C6 out |
| Erzeugung | Review v2 | kontrollierter Peer-Traffic, nicht Passiv-Default |
| Promisc v0 | Review v2 | **Nein** |
| Presence Grundfähigkeit | P2-008 | **Nein** |
| CCA | P1-007 | **Nein** |
| C1 Schwellen vorab | Review v2 | **Nein** — empirisch nach C1 |
| Default-Klasse | Desk | **B** anstreben; Final nach Lab |
| Neues Sheet | — | **Nein** |

---

## 7. Method-Kandidaten (noch nicht anlegen)

| Draft-Slug | Versuch | Anlegen wenn |
|------------|---------|--------------|
| `csi-raw-session-reproducibility` | C1 | nach Review + erstem C1 |
| `csi-motion-traffic-controls` | C2 | nach Review + erstem C2 |
| `csi-raw-transfer-check` | C3 | nur bei Go + Ausführung |

Kontrast: `own-link-motion-sensitivity` ≠ CSI.

---

## 8. Konkretisierung Lab-Parameter (minimal)

Zweck: C1/C2 ausführbar machen — **kein** Scope-Zuwachs, kein Feature-Projekt.

### 8.1 Traffic-Profile N / H (D1 Mini)

Genau **zwei** Profile. Erzeugung = periodischer, vom D1 gesteuerter Frame-/Paketausstoß Richtung S3-Link (oder gemeinsamer AP-Pfad, der am S3 CSI auslöst). Kein Ambient-Default.

| ID | Name | Mechanismus (reproduzierbar) | Soll-Parameter | Dokumentation pro Session |
|----|------|------------------------------|----------------|---------------------------|
| **N** | Normal / konstant | fester Inter-Paket-Abstand `Δt_N` über die ganze Session | **`Δt_N = 20 ms`** → Soll-Rate **50 pkts/s** konstant | `profile_id=N`, `delta_t_ms`, `tx_count`, `t_arm`/`t_disarm`, Soft-/FW-Pin D1 |
| **H** | High / variiert | bewusst **höher** und **zeitlich variiert**: Blockmuster | Zyklus **10 s:** **5 s** bei **`Δt_H = 4 ms`** (250 pkts/s) + **5 s** bei **`Δt_N = 20 ms`** (50 pkts/s); über Session wiederholen | wie N, plus `block_hi_s=5`, `block_lo_s=5`, `delta_t_hi_ms`, `delta_t_lo_ms` |

| Regel | |
|-------|--|
| Zweck | Einfluss von Traffic auf CSI charakterisieren — **kein** Throughput-Benchmark |
| Messbarkeit | Soll-Rate aus `Δt`; Ist = `tx_count / duration` (D1-Log oder Host-Zähler); Abweichung notieren |
| Verbot | qualitative Labels („viel Traffic“) ohne `Δt`/`tx_count` |
| A0-Anpassung | Wenn D1 **50/250 pkts/s** nicht stabil hält: **ein** Paar `(Δt_N, Δt_H)` mit `Δt_H < Δt_N` und klarer Trennung wählen, in `session.yaml` festschreiben — Profil-**IDs N/H** und Blocklogik von H bleiben |

C1 nutzt nur **N**. C2: A/C → N · B/D → H.

### 8.2 Motion-Protokoll

Kein Presence-/Personen-Claim — nur wiederholbarer physischer Stimulus.

| Element | Festlegung |
|---------|------------|
| Geräte | S3 und D1 **fix** (Markierung auf Tisch/Boden); Abstand und Orientierung in `session.yaml` (cm / Skizze) |
| Bahn | Eine Gerade **durch die LOS** zwischen D1 und S3 (oder klar markierte Parallele ≤0,5 m versetzt, falls Raum eng) |
| Start / Ende | Bodenmarken **S** und **E**; eine Passage = S→E in eine Richtung |
| Bewegung | Gehende, möglichst **konstante** Geschwindigkeit; **eine** Passage pro Motion-Fenster |
| Timing | Motion-Fenster = mittlere **T_motion** der Session (Default: Sekunden **20–40** bei `T_session=60 s`); außerhalb still |
| Wiederholung | Identische Bahn, Richtung, Fensterlage in allen C- und D-Sessions |
| Operator | dieselbe Person für alle C2-Zellen eines Laufs; kein „natürliches Herumlaufen“ |

Zellen A/B: gesamte Session still (kein Passage).

### 8.3 Session-Dauer

| Parameter | Wert | Status |
|-----------|------|--------|
| **`T_session`** | **60 s** | **experimenteller Startwert** — ausreichend für Baseline + eine Motion-Passage; C1 (≥3×) und C2 (4 Zellen, ggf. je ≥2) noch laborpraktisch |
| C1 Wiederholungen | ≥3 Sessions mit Profil N | fest |
| C2 Wiederholungen | ≥1 vollständige A–D-Matrix; ideal ≥2 | fest als Minimum 1 |
| Anpassung | Wenn A0/erste Captures zu wenige CSI-Samples oder Capture überlastet → `T_session` **einmal** anpassen (z. B. 45–90 s) und in Header pinnen; **kein** Feintuning-Katalog |

`T_session` ist **kein** vorab „bewiesener“ Optimum-Wert, sondern Startparameter.

### 8.4 S3-Capture-Tooling (Instrument A0 — vor C1)

Nur Instrumentierung für `MV-ESP32-CSI-RAW-v0`. Kein Sensing-Feature, keine UI-Produktarbeit.

| Frage | Minimale Antwort für v0 |
|-------|-------------------------|
| Verlustarme CSI-RAW-Erfassung? | S3: CSI-CB → sofort kopieren/serialisieren; Host: hoher Baud; Capture-Prozess schreibt durchgehend in Datei (kein blockierendes Pretty-Print) |
| Device- + Host-Zeit? | Pro Sample: `rx_ctrl.timestamp` (Device) **und** Host-Zeit beim Empfang der Zeile (monotonic bevorzugt; UTC zusätzlich ok) |
| Eindeutige Sample-Nummer? | Host-`seq` 0…N−1 in Empfangsreihenfolge (Device-`rx_seq` zusätzlich speichern falls vorhanden) |
| Drops/Gaps erkennbar? | (a) Sprünge in `seq`/`rx_seq` · (b) `session_stats`: `n_samples`, `duration`, `observed_pps` vs Soll aus Profil · (c) fehlende Pflichtfelder → Record verwerfen + Zähler |
| Session Start/Ende? | Feste Reihenfolge: Header schreiben → D1-Profil arm → Capture arm → `T_session` → Capture disarm → D1 disarm → `session_stats` flush; Zeiten in Header |
| Offline-RAW-Format? | Bundle: `session.yaml` + **`csi_raw.csv`** (eine Zeile/Sample: `seq,host_t,device_t,rssi,…,len,iq…`) + `session_stats.json` |

A0-Smoke: eine Kurzsession mit Profil N muss Pflicht-RAW + Stats liefern, bevor C1 zählt.

---

## 9. Plan-Exit (dieser Stop)

| Deliverable | Status |
|-------------|--------|
| 1. Minimaler Messvertrag (S3 + D1-Pfad, ohne Promisc) | §2 |
| 2. C1–C2 Spec (+ C3 bedingt) | §3 |
| 3. RAW / DERIVED / ASSESSMENT klar | §1–2 |
| 4. Akzeptanz/Abbruch (C1 ohne Vorab-% ) | §5 |
| 5. A/B/C Trace | §6 |
| 6. N/H · Motion · Dauer · Capture | **§8 konkret (v3)** |
| Lab | **nein** |
| Commit | **nein** |
