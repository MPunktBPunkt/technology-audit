# Phase 0 — KB Reuse / Gap Check

```yaml
campaign: esp32-rf-sensing-2026-desk
phase: 0
date: 2026-10-26
mode: kb-only
new_sheets: 0
re_audit_espectre: false
re_audit_marauder: false
```

**Exit P0:** erfüllt. Stop vor Phase 1.

---

## 1. Wiederverwendbare Assets

### Sheets

| Slug | Maturity (A) | Rolle für RF-Sensing | Aktion |
|------|--------------|----------------------|--------|
| `wifi-csi-motion` | R1 / W1 / field R0 | CSI Amplitude → Admission → Detector → Motion/Score | **reuse** |
| `esp-wifi-promiscuous-pcap` | R1 / W1 / field R0 | Promiscuous RX → Buffer → PCAP | **reuse** + Abgrenzung |
| `rf-environment-monitor` | R3 / W3 / field R1 | Environment Scan / Score / Own-Link / Location | **Kontrast**; CSI/Promiscuous/CCA-airtime `REJECTED` |

### Applications (Prior-Projekte)

| App | Projekt | Nutzen |
|-----|---------|--------|
| `applications/wifi-csi-motion.md` | `espectre` | Messkette managed traffic → CSI → detector; Chip-Liste Upstream-Desk |
| `applications/esp-wifi-promiscuous-pcap.md` | `esp32-marauder` | Capture-Contract; Buffer/PCAP; Filter MGMT\|DATA |
| RF / Hub / Web Apps | `esp32-rfmonitor` | Grenze: was **nicht** Sensing-CSI ist (Own-Link Method ≠ CSI) |

### Methods

| Method | Nutzen |
|--------|--------|
| `own-link-motion-sensitivity` | Kontrast: Walk-by über Own-Link-RSSI, explizit **ohne** CSI/Presence |
| *(keine CSI-Char-Method)* | Gap → erst ab Phase 3 / ≥2 Einsätze anlegen |

### Prior Kampagnen / Evidence-Pools

| Kampagne | IDs (Reuse) |
|----------|-------------|
| `espectre-2026-foreign` | `EVID-ESPECTRE-2026-10-25-001` … `008` |
| `esp32-marauder-2026-foreign` | `EVID-MARAUDER-2026-10-25-001` … `008` |
| `esp32-rfmonitor-2026-v2-validation` | u. a. `EVID-RF-2026-10-25-005` (Proxies≠Airtime) |
| `esp32-rfmonitor-2026-motion-delta` | `EVID-RF-2026-10-26-001`…`003` (Own-Link ≠ Presence/CSI) |

---

## 2. FACT-Liste (aus KB — gilt für das neue Thema)

Nur Aussagen, die bereits Evidence-IDs oder Sheet-Fallstricke tragen. Keine neuen Upstream-Claims.

| # | Aussage | Status | Beleg |
|---|---------|--------|-------|
| F1 | CSI-Motion und Promiscuous-PCAP sind **verschiedene Contracts** | `FACT` / `REJECTED` Vermischung | Sheets + `EVID-ESPECTRE-…-001` Kontext; Marauder Capture-Pipeline |
| F2 | CSI-Motion ≠ RF-Environment-Score / Own-Link-Monitor | `FACT` / `REJECTED` Vermischung | `rf-environment-monitor` Fallstricke; `EVID-RF-2026-10-26-003` |
| F3 | ESPectre: managed Traffic (ping/dns/wifi_raw/external) steuert nutzbare CSI-Rate | `FACT` | `EVID-ESPECTRE-2026-10-25-004` |
| F4 | ESPectre: Temporal Admission (`csi_target_pps`, ≤1 pkt/slot) ist Teil des Produktionsvertrags | `FACT` | `EVID-ESPECTRE-2026-10-25-002` |
| F5 | ESPectre: Lightweight vs High-Accuracy (MLP) on-device; AGC on | `FACT` | `EVID-ESPECTRE-2026-10-25-003` |
| F6 | ESPectre beansprucht Chip-Matrix C6/C5/C3/S3/S2/Classic (Upstream-Desk) | `FACT` (Upstream-Doku) | `EVID-ESPECTRE-2026-10-25-004` — **nicht** IDF-Primärgate |
| F7 | ESPectre: kein People-Count / empty-room-Beweis / Safety-Ersatz | `FACT` | `EVID-ESPECTRE-2026-10-25-008` |
| F8 | Marauder: Promiscuous + Sniff-Callbacks + Packet-Rate-Mode | `FACT` | `EVID-MARAUDER-2026-10-25-002` |
| F9 | Marauder: Double-Buffer → PCAP; Budget `BUF_SIZE`/`SNAP_LEN` | `FACT` | `EVID-MARAUDER-2026-10-25-003` |
| F10 | Unbegrenzte Capture-Rate ohne Drop ist nicht haltbar | `REJECTED` | Sheet Promiscuous Fallstrick |
| F11 | Packet-/AP-Count-Proxies (`channel_*`) ≠ Airtime/CCA | `REJECTED` | Sheet RF-Monitor; `EVID-RF-2026-10-25-005` |
| F12 | Own-Link high-rate RSSI kann Walk-by messen ohne CSI | `FACT` (Field, Küche) | `EVID-RF-2026-10-26-001`/`002` |
| F13 | Own-Link Motion ≠ Presence / Personenzählung | `REJECTED` (Claim) | `EVID-RF-2026-10-26-003` |
| F14 | Eigene Raum-Lab-Zahlen für ESPectre CSI-Motion | `UNKNOWN` | espectre App / Exit #7 |
| F15 | Hub-/Adapter-End-to-End für RF-Monitor `rf.alert` | `UNKNOWN` | rfmonitor Exit #6 — **außerhalb** Sensing-Messvertrag |

**Schicht-Disziplin (bereits in KB verankert):**

```text
RAW (CSI amp / frames / RSSI)
  → DERIVED (features / proxies)
  → DETECTOR
  → ASSESSMENT (motion / score / claim)
```

Vermischung dieser Ebenen ist Anti-Pattern (ESPectre App trennt Pipeline; RF-Monitor Observation Model analog).

---

## 3. Gaps für den neuen Messvertrag

| Gap-ID | Gap | Warum blockierend | Phase |
|--------|-----|-------------------|-------|
| G1 | **IDF/esp-csi Primär-Capability** Chip × CSI × Promiscuous × `wifi_pkt_rx_ctrl_t`/RX-meta × CCA | ESPectre-Chip-Liste ist Upstream-Desk, kein IDF-SoT | **1 Kill/Gate** |
| G2 | **CCA / Energy-Detect Messsemantik** (API, Auflösung, busy-Bedeutung) | Ohne API kein Messgegenstand; RF-Monitor-Proxy bereits `REJECTED` | **1 Gate** |
| G3 | **Passive CSI** ohne kontrollierten/managed TX | ESPectre-Kern = managed traffic; Passiv-Pfad unklar für Minimalvertrag | **2** (CSI-Tool) |
| G4 | **Traffic vs. Human Motion** Kontamination / Kontrollbedingungen A–D | Upstream holdout ≠ Traffic-Gate; Motion-Claims sonst CLAIM | **2 Kill** (HeliosSm) |
| G5 | Capture-Session + Offline-Replay als **Instrument-Contract** (roh, timestamps, drops) | ESPectre = Produkt-Detektor; Marauder = Frame-PCAP; Minimal-Lab dazwischen fehlt | **2** (radar-lab / CSI-Tool) |
| G6 | Eigene Characterization-Method (CSI) | Method erst bei ≥2 Einsätzen / nach Messvertrag | **3** optional |
| G7 | Cross-Room / Cross-Device Transfer CSI | field_evidence R0 | nach Messvertrag Lab |
| G8 | Multi-Link / Presence-Demos / SenseFi | nicht messvertragsminimal | P2 nur bei Kill-Bedarf — **jetzt skip** |

---

## 4. Kill- / Gate-Fragen für Phase 1 / 2

### Phase 1 — ESP-IDF + esp-csi (Pflicht-Gate)

| Gate | Frage | Fail → |
|------|-------|--------|
| **K1** | Welche Chips (mind. S3, C6; ggf. Classic/C3/C5/S2) haben dokumentierte **CSI-API**? | CSI aus Minimalvertrag streichen oder Chip-Pin zwingend |
| **K2** | Welche Chips haben **Promiscuous** + welche RX-Metadata-Felder (`wifi_pkt_rx_ctrl_t` o. Ä.) sind öffentlich? | Metadata-Contract schrumpfen |
| **K3** | Existiert eine **öffentliche CCA / Energy-Detect / channel busy**-Mess-API mit klarer Semantik? | CCA als Messgegenstand `UNKNOWN`/`REJECTED` — **kein Sheet** |
| **K4** | STA + CSI und/oder STA + Promiscuous: dokumentierte Coexistence / Limits? | Messvertrag muss Duty/Mode spezifizieren |

**Pflichtartefakt Phase 1:** Matrixzeilen mit `FACT`/`UNKNOWN`/`REJECTED` + Primärquellenpfad (Header/Doc/Kconfig), nicht Community-README allein.

### Phase 2 — nur offene Kills (nach Phase 1)

| Gate | Repo-Fokus | Frage | Fail → |
|------|------------|-------|--------|
| **K5** | ESP32-CSI-Tool | Was ist **passiv** erfassbar ohne dedizierten CSI-Sender? | Passive nicht in Projekt A |
| **K6** | esp-wifi-radar-lab (+ ggf. rf-sensing) | Gibt es Session/Export/Offline-Analyse als Instrument-Muster? | Pattern nur CLAIM |
| **K7** | **HeliosSm** (Traffic vs Motion) | Unterscheidet Design Traffic-Effekt von Human Motion (Kontrollen, Features, GT)? | Keine Motion-/Presence-Assessment in Messvertrag |

Regel: Keine Motion-/Presence-Aussage akzeptieren, ohne K7 zu adressieren.

---

## 5. Explizit nicht neu aufrollen

| Entscheidung | Status | Hinweis |
|--------------|--------|---------|
| `channel_*` / density / pressure = Airtime/CCA (RF-Monitor) | `REJECTED` | bleibt |
| CSI / Promiscuous in rfmonitor nachziehen | out of scope | SCOPE |
| ESPectre/Marauder Voll-Reaudit | nicht nötig | Reuse |
| Sheet „CCA“ / „Channel Occupancy“ / „WiFi Sensing“ / „CSI Presence“ in Phase 0 | **nicht angelegt** | Evidence fehlt |

---

## 6. Zwischenfazit (noch keine Projektentscheidung)

Aus KB allein:

- **Getrennt haltbare Messklassen:** (1) Environment/Own-Link (`rf-environment-monitor` + Own-Link-Method), (2) Frame-Capture (`esp-wifi-promiscuous-pcap`), (3) CSI→Detector (`wifi-csi-motion`).
- **Kleinste auditierbare Neuplattform** ist **noch nicht entscheidbar**: blockiert durch **G1/G2** (IDF) und **G4/G7** (Traffic-Kontamination / Transfer).
- Hypothese für spätere Synthese (nicht FACT): Projektklasse **B (CSI Lab Instrument)** näher am Gap G5 als Produkt-Klon ESPectre; Klasse **A** könnte RX-metadata/Promiscuous-Instrument ohne CSI sein — **nur nach Phase-1-Matrix**.

---

## 7. Phase-0 Exit → Stop

| Check | Ergebnis |
|-------|----------|
| Reuse inventarisiert | ja |
| FACT-Liste | F1–F15 |
| Gaps | G1–G8 |
| Kill/Gates Phase 1/2 | K1–K7 |
| Neue Sheets | 0 |
| Nächster Schritt | **Phase 1 Gate** (siehe Kampagnen-README) — **nicht in diesem Lauf** |
