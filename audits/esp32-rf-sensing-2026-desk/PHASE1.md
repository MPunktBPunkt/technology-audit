# Phase 1 — ESP-IDF + esp-csi Primary-Source Gate

```yaml
campaign: esp32-rf-sensing-2026-desk
phase: 1
date: 2026-10-26
mode: primary-source-desk
idf_docs: "ESP-IDF Programming Guide stable v6.1 (chip-specific Wi-Fi Vendor Features / Modes)"
idf_headers_pin:
  repo: https://github.com/espressif/esp-idf
  ref: master@d35ea02   # 2026-10-23; headers cited below
esp_csi_pin:
  repo: https://github.com/espressif/esp-csi
  ref: master@8633d67   # 2026-04-22 README / examples (secondary to IDF API)
new_sheets: 0
```

**Exit P1:** K1–K4 geschlossen auf Desk-API-Ebene (siehe §4). CCA als Messgegenstand **nicht** weiterführen.

---

## 1. Capability-Matrix

Legende Zelle: `FACT` · `UNKNOWN` · `REJECTED` (als Mess-/API-Claim).  
„Gemessen“ hier = **API liefert dokumentierte Größe bei RX-Ereignis**, nicht Lab-VALIDATED.

### 1.1 Kernchips S3 / C6

| Capability | ESP32-S3 | ESP32-C6 | Primärquelle | Bemerkung |
|------------|----------|----------|--------------|-----------|
| Wi-Fi vorhanden | `FACT` | `FACT` | `SOC_WIFI_SUPPORTED` | `soc_caps.h` |
| CSI SoC-Cap | `FACT` | `FACT` | `SOC_WIFI_CSI_SUPPORT` | beide =1 |
| Wi-Fi 6 / HE SoC-Cap | `REJECTED` (kein HE-Cap) | `FACT` | `SOC_WIFI_HE_SUPPORT` nur C6 | treibt **unterschiedliche** CSI-Config-Typen |
| CSI Public API | `FACT` | `FACT` | `esp_wifi_set_csi*` / `wifi_csi_cb_t` | gleicher API-Name; Config-Struct chip-pfadabhängig |
| CSI Rohformat I/Q | `FACT` | `FACT` | Vendor Features CSI | pro Subcarrier 2×`int8`: **Imag dann Real** |
| CSI Amplitude/Phase als API-Felder | `REJECTED` | `REJECTED` | — | nur I/Q-Bytes; Amp/Phase = **Derived** |
| CSI braucht RX-Frames | `FACT` | `FACT` | Vendor Features | geschätzt bei Packet-RX; STA allein wenig CSI → Sniffer empfohlen |
| Promiscuous / Sniffer | `FACT` | `FACT` | Wi-Fi Modes · `esp_wifi_set_promiscuous*` | MGMT/DATA/CTRL/MIMO-len/CRC-err; Impact auf Throughput |
| `wifi_pkt_rx_ctrl_t` / RX-meta | `FACT` (classic Layout) | `FACT` (HE `esp_wifi_rxctrl_t`) | `esp_wifi_types_native.h` | **Layouts unterschiedlich** — nicht bytekompatibel annehmen |
| RSSI (per RX) | `FACT` | `FACT` | `rx_ctrl.rssi` | Metadatum, kein Occupancy |
| Noise floor (per RX) | `FACT` | `FACT` | `noise_floor` in rx_ctrl / HE rxctrl | Metadatum; ≠ CCA busy-time |
| Channel / BW / Timestamp | `FACT` | `FACT` | rx_ctrl Felder | S3: `channel`,`cwb`,`timestamp`; C6 HE: `channel`,`second`,`timestamp`,`cur_bb_format`,… |
| Öffentliche **CCA / Energy-Detect / Channel-busy-Zeit** API | `REJECTED` | `REJECTED` | kein Treffer in `esp_wifi.h` / Types / Vendor Features / Sniffer-Docs | siehe K3 |
| Packet-Count / Frame-Rate als „CCA“ | `REJECTED` | `REJECTED` | Ableitung | höchstens **Proxy**, nicht CCA nennen |
| Continuous RF power / spectrum | `REJECTED` | `REJECTED` | Sniffer+CSI Docs | Packet-Observation ≠ Power-Meter |

### 1.2 Weitere Familien (Kurz, SoC-Caps master@d35ea02)

| Chip | `SOC_WIFI_CSI_SUPPORT` | `SOC_WIFI_HE_SUPPORT` | Konsequenz |
|------|------------------------|------------------------|------------|
| ESP32 (classic) | `FACT` (1) | nein | Non-HE CSI-Config-Pfad |
| ESP32-S2 | `FACT` (1) | nein | Non-HE; rx_ctrl Layout-Variante |
| ESP32-C3 | `FACT` (1) | nein | Non-HE; ähnlich S3-Zweig noise_floor |
| ESP32-C2 | **kein** CSI-Cap in `soc_caps.h` | nein | CSI-API nicht als SoC-FACT annehmen |
| ESP32-C5 | `FACT` (1) | `FACT` (1) | HE-CSI-Pfad (wie C6-Familie) |
| ESP32-C61 | `FACT` (1) | `FACT` (1) | HE-CSI-Pfad |
| ESP32-H2 | kein Wi-Fi-Cap (leer/kein CSI) | — | out of Wi-Fi sensing |

**REJECTED:** esp-csi README-Claim „Full series support: All ESP32 series…“ als **universelle Hardware-Wahrheit** — widerspricht mindestens C2 ohne `SOC_WIFI_CSI_SUPPORT`. Status: **CLAIM** (esp-csi) vs. **SoC FACT** (IDF caps).

---

## 2. K1 — CSI (was die API liefert)

### API (beide Chips, sofern Cap)

| Schritt | API | Semantik |
|---------|-----|----------|
| Menuconfig | `CONFIG_ESP_WIFI_CSI_ENABLED` | hängt an `SOC_WIFI_CSI_SUPPORT`; RAM-Hinweis in Kconfig |
| Callback | `esp_wifi_set_csi_rx_cb(wifi_csi_cb_t, ctx)` | Aufruf aus Wi-Fi-Task; Buffer nach Return freigegeben → sofort kopieren |
| Config | `esp_wifi_set_csi_config` / `get` | Struct-Typ hängt an HE |
| Enable | `esp_wifi_set_csi(bool)` | Fehler u. a. wenn Wi-Fi nicht gestartet **oder** Promiscuous nicht enabled |

### Rohbeobachtung (`wifi_csi_info_t`)

| Feld | Klasse | Hinweis |
|------|--------|---------|
| `buf` / `len` | **RAW** | I/Q `int8` Paare; Länge abhängig von Packet/BW/LTF-Auswahl |
| `rx_ctrl` | **RX-meta** | siehe K2/K3 |
| `mac` / `dmac` / `rx_seq` | **RX-meta** | Frame-Bezug |
| `first_word_invalid` | **HW-Limit** | erste 4 Bytes können ungültig sein (S3/C6 Docs) |
| Amplitude, Phase, Variance, Motion | **Derived / Assessment** | nicht API |

### S3 Config (Non-HE) — `wifi_csi_config_t`

Flags: `lltf_en`, `htltf_en`, `stbc_htltf2_en`, `ltf_merge_en`, `channel_filter_en`, `manu_scale`/`shift`, `dump_ack_en`.  
LTF-Tabellen und Byte-Längen: IDF S3 Vendor Features (stable v6.1).

### C6 Config (HE) — `wifi_csi_acquire_config_t` (= `wifi_csi_config_t` wenn `SOC_WIFI_HE_SUPPORT`)

Flags u. a.: `acquire_csi_legacy`, `acquire_csi_force_lltf`, `acquire_csi_ht20/ht40`, `acquire_csi_su/mu/dcm/beamformed`, `acquire_csi_he_stbc_mode`.  
Zusätzlich HE: `rx_channel_estimate_info_vld` in `esp_wifi_rxctrl_t` als CSI-Validitätsbit.

### Erzeugung

| Modus | Status | Quelle |
|-------|--------|--------|
| CSI nur bei empfangenen Packets | `FACT` | Vendor Features |
| STA disconnected → kaum CSI | `FACT` | Configure-Text: enable promiscuous recommended |
| „Passiv ohne jeglichen TX in der Luft“ | `UNKNOWN` | Phase-1 API sagt nur: braucht RX; wer sendet → Phase 2 |
| Kontinuierliches Channel-Sounding ohne Frames | `REJECTED` | nicht in API |

---

## 3. K2 — Promiscuous / RX-Pfad

| Claim | Status | Quelle |
|-------|--------|--------|
| Enable via `esp_wifi_set_promiscuous` + RX-CB | `FACT` | `esp_wifi.h`, Modes Sniffer |
| Filter MGMT/CTRL/DATA/MISC (+ MPDU/AMPDU masks) | `FACT` | `wifi_promiscuous_filter_t` |
| Dump: MGMT, DATA (MPDU/AMPDU/AMSDU), CTRL, MIMO **nur Länge**, CRC-error frames | `FACT` | Sniffer Mode Docs S3 (gleicher Abschnitt chip-spezifisch) |
| Andere Error-Frames | nicht geliefert | Docs |
| Payload in `wifi_promiscuous_pkt_t` + `rx_ctrl` Header | `FACT` | native header |
| Sniffer in NULL/STA/AP/APSTA | `FACT` | Docs |
| Starker Einfluss auf STA/AP Throughput | `FACT` | Docs Warnung |
| Promiscuous = RF-Sensing / Presence | `REJECTED` | Contract-Ebene |
| Promiscuous = kontinuierliche RF-Leistung | `REJECTED` | Packet-Observation |

---

## 4. K3 — RX metadata / CCA

### Was belastbar als RX-meta gilt

| Größe | S3 | C6 | Klasse |
|-------|----|----|--------|
| RSSI | `FACT` | `FACT` | RX-meta |
| noise_floor | `FACT` | `FACT` | RX-meta |
| channel / secondary | `FACT` | `FACT` | RX-meta |
| timestamp (µs, Sleep-Caveat) | `FACT` | `FACT` | RX-meta |
| rate/MCS/sig_mode bzw. `cur_bb_format` | `FACT` | `FACT` | RX-meta (Layout anders) |
| sig_len / rx_state | `FACT` | `FACT` | RX-meta |
| ant (S3 classic) | `FACT` | `UNKNOWN`/anders in HE-struct | chip-spezifisch lesen |

### CCA / Channel Occupancy

| Claim | Status | Begründung |
|-------|--------|------------|
| Öffentliche IDF-API „CCA busy fraction / energy detect sample stream“ | **`REJECTED`** (als Messgegenstand) | In geprüften Primärquellen (`esp_wifi.h`, Types, Vendor Features, Sniffer, Kconfig CSI) **keine** API mit klarer CCA-/Occupancy-Semantik |
| Private/Closed-PHY Register CCA | `UNKNOWN` | nicht belegt; für Audit-Messvertrag irrelevant bis öffentlich |
| Packet-Count, CSI-Rate, RSSI-Histogramm als „CCA“ | **`REJECTED`** (Label) | höchstens **Proxy** — so kennzeichnen |
| `noise_floor` = Channel Occupancy | **`REJECTED`** | anderes Metadatum |

**Konsequenz:** CCA/Channel-Occupancy **nicht** als eigener Messvertrag / kein neues Sheet. Bleibt konsistent mit RF-Monitor `channel_*=Airtime` `REJECTED`.

---

## 5. K4 — Chip/PHY-Trennung (S3 vs C6)

| Aspekt | S3 | C6 |
|--------|----|----|
| CSI Config-Typ | Non-HE `wifi_csi_config_t` (lltf/htltf/…) | HE `wifi_csi_acquire_config_t` |
| RX-meta Typ | classic `wifi_pkt_rx_ctrl_t` | `typedef` → `esp_wifi_rxctrl_t` |
| PHY-Generation Docs | bis HT LTFs in CSI-Tabelle | HE-LTF / SU/MU/DCM Flags |
| Band | 2.4 GHz Wi-Fi (S3) | 2.4 GHz Wi-Fi 6 |
| Verallgemeinerung „ESP32 kann CSI so…“ | **`REJECTED`** | immer Chip+Config-Pfad nennen |

---

## 6. Evidence-IDs (Phase 1)

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-RFSENSE-P1-001` | S3+C6: `SOC_WIFI_CSI_SUPPORT=1` | `FACT` | `components/soc/esp32s3|c6/include/soc/soc_caps.h` @ `d35ea02` |
| `EVID-RFSENSE-P1-002` | Nur C6 (nicht S3): `SOC_WIFI_HE_SUPPORT=1` → anderer CSI-Config-/rxctrl-Pfad | `FACT` | soc_caps + `esp_wifi_types_native.h` / `esp_wifi_he_types.h` |
| `EVID-RFSENSE-P1-003` | CSI API: set_cb / set_config / set_csi; Callback-Buffer ephemer; braucht start oder promiscuous | `FACT` | `esp_wifi.h` + Vendor Features Configure |
| `EVID-RFSENSE-P1-004` | CSI RAW = Imag/Real int8 Subcarrier Responses bei Packet-RX; Amp/Phase nicht API | `FACT` / Derived-Trennung | S3 Vendor Features CSI; HE-Zweig RST |
| `EVID-RFSENSE-P1-005` | Promiscuous liefert Frame-Typen + Filter; Throughput-Impact; ≠ RF-Power | `FACT` / `REJECTED` Power-Claim | Wi-Fi Modes Sniffer |
| `EVID-RFSENSE-P1-006` | RX-meta: rssi, noise_floor, channel, timestamp, … in rx_ctrl (Layout S3≠C6) | `FACT` | native + HE headers |
| `EVID-RFSENSE-P1-007` | Keine öffentliche CCA/Occupancy-Mess-API in geprüften IDF-WiFi-Primärquellen | `REJECTED` (Messgegenstand) | negative Search §4 |
| `EVID-RFSENSE-P1-008` | C2 ohne `SOC_WIFI_CSI_SUPPORT`; esp-csi „full series“ nicht als SoC-FACT | `FACT` / CLAIM | soc_caps C2; esp-csi README @ `8633d67` |
| `EVID-RFSENSE-P1-009` | esp-csi: CSI aus Router-Ping / Device-Ping / Broadcast-TX Szenarien (Erzeugungs-Patterns) | `FACT` (Projekt-Doku) | esp-csi README — **Erzeugung**, nicht neue PHY-API |

---

## 7. Gate-Status K1–K4

| Gate | Status | Residual |
|------|--------|----------|
| **K1 CSI** | **geschlossen (Desk)** | Passive vs. managed TX → Phase 2; Lab-VALIDATED offen |
| **K2 Promiscuous** | **geschlossen (Desk)** | Drop/pps Lab offen; Contract klar |
| **K3 CCA** | **geschlossen → REJECTED als Messgegenstand** | Private PHY `UNKNOWN`, irrelevant für Vertrag |
| **K4 Chip-Matrix** | **geschlossen (Desk) für S3/C6 + Caps-Tabelle** | Feine HE-Tabellenwerte C6 nur über HE-Docs/RST; App muss Structs chip-spezifisch parsen |

---

## 8. Konsequenz für Phase 2

Phase 2 **nur** noch auf Kill-Fragen, die API nicht beantwortet:

| Gate | Fokus | Warum noch nötig |
|------|-------|------------------|
| **K5** | ESP32-CSI-Tool | Was ist **ohne** eigenen/managed TX praktisch capturebar? |
| **K6** | esp-wifi-radar-lab | Session/Export/Offline-Instrument-Muster? |
| **K7** | HeliosSm | Traffic vs Human Motion — **keine** Motion-Assessment ohne dieses Gate |

**Nicht** in Phase 2: CCA wiederbeleben; „ESP32 universell CSI“; Promiscuous-as-Sensing.

---

## 9. Rohbeobachtungen vs. verworfene Fähigkeiten (Antwort)

### Belastbar erfassbar (API-Desk) auf **S3 und C6**

1. **CSI RAW** — Subcarrier I/Q (`int8` Imag/Real) + Länge, gebunden an empfangene Packets; Config/LTF-Pfad **chip-abhängig** (Non-HE vs HE).  
2. **Promiscuous Frame Observation** — gefilterte 802.11 MGMT/DATA/CTRL/… + Payload (außer MIMO nur Länge).  
3. **Per-packet RX metadata** — mind. RSSI, noise_floor, channel, timestamp, Längen/State; **Struct-Layout S3≠C6**.

### Bereits auf API-Ebene verwerfen / nicht in Messvertrag

| Vermeintliche Fähigkeit | Status |
|-------------------------|--------|
| Öffentliche CCA / Channel-Occupancy-Zeitreihe | `REJECTED` |
| Packet-Count oder CSI-pps als „CCA“ | `REJECTED` (Label) |
| Amplitude/Phase/Motion/Presence als IDF-Rohgröße | `REJECTED` (sind Derived/Assessment) |
| Kontinuierliche RF-Leistung / Spektrum aus Promiscuous | `REJECTED` |
| Ein CSI-Binary-Format für alle ESP32 | `REJECTED` |
| CSI auf jedem „ESP32-series“ Chip (esp-csi Marketing) | `REJECTED` als Universalfact (Gegenbeispiel C2 Cap) |

### Noch offen (nicht Phase-1)

- Passive-only CSI ohne kontrollierten Traffic (K5)  
- Traffic↔Motion Trennbarkeit (K7)  
- Lab-VALIDATED Sampling/Drops  

---

## 10. Sheets

**Keine neuen Technology Sheets** in Phase 1 — Caps/API schärfen bestehende Kontraste (`wifi-csi-motion`, `esp-wifi-promiscuous-pcap`); CCA-Sheet entfällt.
