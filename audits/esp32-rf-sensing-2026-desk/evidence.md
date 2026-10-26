# Evidence — esp32-rf-sensing-2026-desk

**Phase 0 (2026-10-26)** · Profile `planning` · **standard_version 0.7.1** · KB-only (keine neuen Upstream-Desk-Claims).

## Phase-0 Meta-Evidence

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-RFSENSE-P0-001` | CSI-Motion-Contract bereits als Sheet+App+Evidence (ESPectre) vorhanden — Reuse, kein Bootstrap | `FACT` | [`wifi-csi-motion`](../../technologies/wifi-csi-motion/SHEET.md) · [`espectre-2026-foreign/evidence`](../espectre-2026-foreign/evidence.md) |
| `EVID-RFSENSE-P0-002` | Promiscuous-PCAP-Contract bereits vorhanden; Capture ≠ CSI ≠ CCA | `FACT` | [`esp-wifi-promiscuous-pcap`](../../technologies/esp-wifi-promiscuous-pcap/SHEET.md) · [`esp32-marauder-2026-foreign/evidence`](../esp32-marauder-2026-foreign/evidence.md) |
| `EVID-RFSENSE-P0-003` | Own-Link Motion Sensitivity ist separate Method; ≠ CSI Presence | `FACT` | [`own-link-motion-sensitivity`](../../methods/own-link-motion-sensitivity.md) · `EVID-RF-2026-10-26-001`…`003` |
| `EVID-RFSENSE-P0-004` | `channel_*`/density/pressure als Airtime/CCA im RF-Monitor-Kontext `REJECTED`; kein CCA-API-FACT in KB | `FACT` (REJECTED-Claim) / Gap | [`rf-environment-monitor`](../../technologies/rf-environment-monitor/SHEET.md) · `EVID-RF-2026-10-25-005` |
| `EVID-RFSENSE-P0-005` | Phase 0 rechtfertigt **kein** neues Technology Sheet | `FACT` (Prozess) | [PHASE0](PHASE0.md) §5 |
| `EVID-RFSENSE-P0-006` | Messvertrag blockiert durch IDF Capability/CCA-Gate (G1/G2) und Traffic-vs-Motion (G4/K7) | `FACT` (Gap-Inventar) | [PHASE0](PHASE0.md) §3–4 |

## Reuse-Index (Prior-IDs, nicht neu vergeben)

| Prior-ID | Kurz | Für RF-Sensing |
|----------|------|----------------|
| `EVID-ESPECTRE-2026-10-25-001` | CSI motion sensor on-device; privacy | F1/F7 |
| `EVID-ESPECTRE-2026-10-25-002` | Temporal admission / pps | F4 |
| `EVID-ESPECTRE-2026-10-25-003` | Lightweight vs MLP | F5 |
| `EVID-ESPECTRE-2026-10-25-004` | Traffic modes + chip matrix (Upstream) | F3/F6 |
| `EVID-ESPECTRE-2026-10-25-008` | No people-count / empty-room proof | F7 |
| `EVID-MARAUDER-2026-10-25-002` | Promiscuous sniff / packet rate | F8 |
| `EVID-MARAUDER-2026-10-25-003` | PCAP double-buffer | F9 |
| `EVID-RF-2026-10-25-005` | Proxies ≠ Airtime | F11 |
| `EVID-RF-2026-10-26-001`/`002`/`003` | Own-Link ≠ CSI Presence | F12/F13 |

## Phase-1 Primary-Source Evidence

IDF Docs: stable **v6.1** · Headers: `espressif/esp-idf` `master@d35ea02` · esp-csi: `master@8633d67`. Details: [PHASE1](PHASE1.md).

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-RFSENSE-P1-001` | S3+C6: `SOC_WIFI_CSI_SUPPORT=1` | `FACT` | `soc_caps.h` S3/C6 |
| `EVID-RFSENSE-P1-002` | C6 HE vs S3 Non-HE → andere CSI-Config + rx_ctrl Layouts | `FACT` | soc_caps · `esp_wifi_types_native.h` · `esp_wifi_he_types.h` |
| `EVID-RFSENSE-P1-003` | CSI API set_cb/config/enable; Buffer ephemer; start oder promiscuous nötig | `FACT` | `esp_wifi.h` · Vendor Features Configure |
| `EVID-RFSENSE-P1-004` | CSI RAW = Imag/Real int8 bei Packet-RX; Amp/Phase nicht API | `FACT` | S3/C6 Vendor Features CSI |
| `EVID-RFSENSE-P1-005` | Promiscuous Frame-Typen + Filter; ≠ RF-Power/Sensing | `FACT` / `REJECTED` Power | Wi-Fi Modes Sniffer |
| `EVID-RFSENSE-P1-006` | RX-meta rssi/noise_floor/channel/timestamp/… (Layout S3≠C6) | `FACT` | native + HE rxctrl |
| `EVID-RFSENSE-P1-007` | Keine öffentliche CCA/Occupancy-Mess-API in geprüften IDF-WiFi-Quellen | `REJECTED` (Messgegenstand) | negative Search PHASE1 §4 |
| `EVID-RFSENSE-P1-008` | C2 ohne CSI-Cap; esp-csi „full series“ ≠ SoC-Universalfact | `FACT` / CLAIM | soc_caps C2 · esp-csi README |
| `EVID-RFSENSE-P1-009` | esp-csi Erzeugungsmuster Router-Ping / Device / Broadcast-TX | `FACT` (Projekt-Doku) | esp-csi README |

## Phase-2 Kill-Gate Evidence

Pins: CSI-Tool `cce5b1a` · esp-csi console_test `8633d67` · HeliosSm `3f374b5`. Details: [PHASE2](PHASE2.md).

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-RFSENSE-P2-001` | CSI-Tool Passiv: NULL + Promisc DATA + CSI, kein eigener TX | `FACT` | `passive/main/main.cc` |
| `EVID-RFSENSE-P2-002` | Passiv braucht fremde OFDM-DATA auf Kanal | `FACT` / Rate `UNKNOWN` | Issue #22 + Filter |
| `EVID-RFSENSE-P2-003` | CSI-Tool Default = RAW I/Q + meta; Amp/Phase Derived | `FACT` | `csi_component.h` |
| `EVID-RFSENSE-P2-004` | console_test: `log/csi_data.csv` (+ radar/device/log) + `data/` Labels | `FACT` | `esp_csi_tool.py` |
| `EVID-RFSENSE-P2-005` | Radar Presence/Move = Demo; CSI-Rate via Null/Ping/csi_send | `FACT` / `REJECTED` Contract | README + `app_main.c` |
| `EVID-RFSENSE-P2-006` | HeliosSm E1–E4 + Traffic-Log E4 | `FACT` | README + Capture-Skripte |
| `EVID-RFSENSE-P2-007` | Repro: Motion ≫ Traffic-only; r(Mbps,var)≈0.02 | `FACT` (Desk-Repro) | `analisis_validacion_e4.py` 2026-10-26 |
| `EVID-RFSENSE-P2-008` | Motion/Presence-Assessment ohne Traffic-Kontrollen | **`REJECTED`** | Konsequenz P2-006/007 |
| `EVID-RFSENSE-P2-009` | HeliosSm Firmware-Quellcode fehlt | `UNKNOWN` (Gap) | `firmware/README.md` |
| `EVID-RFSENSE-P2-010` | Kein neues Technology Sheet Phase 2 | `FACT` (Prozess) | [PHASE2](PHASE2.md) §6 |

## Offene Claims (nach Phase 2)

| Claim | Status | Nächste Phase |
|-------|--------|---------------|
| CCA als eigenständiger Messgegenstand | **`REJECTED`** | — |
| Chip × CSI × Promiscuous × RX-meta (S3/C6 Desk) | `FACT` | Lab optional |
| Passiv ohne eigenen TX (Definition) | `FACT` | Lab-Ausbeute optional |
| Instrument Session/Label-Muster | `FACT` (Muster) | Phase 3 Spec (Drops/Clock) |
| Motion-Assessment ohne Traffic-Kontrollen | **`REJECTED`** | — |
| Traffic vs Motion in HeliosSm-Design | `FACT` (lokal) | Transfer `UNKNOWN` → eigenes Lab |
| Kleinste Plattform = Klasse A vs B | `HYPOTHESIS` | nach Matrix-Entscheidung + ggf. Lab |
| Method „CSI traffic-vs-motion controls“ | Kandidat | nur nach Go + Einsatz |
| CSI Experimentpfad shortlistbar? | Matrix T1 **GO-Kandidat** | [TECHNOLOGY-MATRIX](TECHNOLOGY-MATRIX.md) — **keine** Projektentscheidung |
| Vorzeitiger Instrument-/A0-Pfad | Artefakt (nicht Tech-Evidenz) | [ARTIFACT-INSTRUMENT-2026-10-26](ARTIFACT-INSTRUMENT-2026-10-26.md) |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-25 | ESPectre + Marauder Foreign Desk; Sheets CSI / Promiscuous |
| 2026-10-25/26 | rfmonitor v2 + motion-delta; CCA-proxy + CSI-Abgrenzung |
| 2026-10-26 | Kampagne Phase 0 Exit |
| 2026-10-26 | Phase 1 IDF/esp-csi Gate — CCA Messgegenstand `REJECTED` |
| 2026-10-26 | Phase 2 K5–K7 Kill-Gates — Traffic-Kontrollen Pflicht vor Motion-Assessment |
| 2026-10-26 | Technologiematrix Desk; Instrument-Pfad als Artefakt eingefroren |
