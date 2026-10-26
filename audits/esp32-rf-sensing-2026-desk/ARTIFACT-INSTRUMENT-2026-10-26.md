# Artefakt-Notiz — vorzeitiger Instrument-/A0-Pfad (2026-10-26)

```yaml
campaign: esp32-rf-sensing-2026-desk
artifact_class: instrumentation-accident
project_decision_csi: false
lab_path_status: suspended
commit: none
push: none
rfmonitor_changed: false
```

**Kernaussage:** Es wurde **kein** Technologie-/Projektentscheid für CSI getroffen.  
`instrument/s3-csi-raw`, `instrument/d1-traffic-n` und `host/capture_session.py` sind **nur** Artefakte eines versehentlich begonnenen A0-Pfads nach freigegebenem PHASE3-v3-Plan — **nicht** Beweis oder Auswahl eines Sensing-Produkts.

Pfad **gestoppt:** kein D1-Flash, kein weiterer A0, kein C1/C2, keine weitere FW/Host-Entwicklung.

---

## 1. Was wurde tatsächlich gebaut?

| Komponente | Inhalt | Build | Flash |
|------------|--------|-------|-------|
| S3 CSI-RAW Instrument | PlatformIO Arduino FW: STA→`RFSENSE_N`, CSI-CB, Serial `CSI_RAW,...` | SUCCESS | **ja** auf Desk-S3 (`/dev/ttyACM0`) — ersetzt dort vorübergehend rfmonitor-Image im Flash |
| D1 Traffic Profil N | PlatformIO Arduino FW: SoftAP + UDP Δt=20 ms, `TX_COUNT` | SUCCESS | **nein** (Gerät nicht am Host) |
| Host Capture | `capture_session.py` → `session.yaml` + `csi_raw.csv` + `session_stats.json` | Skript lauffähig | n/a |

**Nicht gebaut:** Motion/Presence/ML/Feature-Pipeline · Promiscuous-PCAP-Produkt · rfmonitor-Features · C1/C2-Auswertung.

---

## 2. Dateien / Änderungen (Working Tree — uncommitted)

### Neu (Instrument)

```
projects/esp32-rf-sensing/instrument/
  README.md
  .gitignore
  s3-csi-raw/platformio.ini
  s3-csi-raw/src/main.cpp
  d1-traffic-n/platformio.ini
  d1-traffic-n/src/main.cpp
  host/capture_session.py
  sessions/.gitkeep
  sessions/a0_smoke_20261026/   # lokal; gitignored Inhalt
```

### Neu / geändert (Audit-Doku, ebenfalls uncommitted bzw. Working Tree)

| Pfad | Rolle |
|------|--------|
| `audits/.../PHASE3.md` | Plan v3 Messvertrag + C1–C3 Spec (**Desk**, nicht ausgeführt) |
| `audits/.../LAB-A0.md` | A0 Smoke FAIL (2 Läufe) |
| `audits/.../LAB-INSTRUMENT.md` | Instrumentierungsbericht |
| `audits/.../ARTIFACT-INSTRUMENT-2026-10-26.md` | diese Notiz |
| Kampagnen-README / evidence / SCOPE / INVENTORY / FOLLOW-ON | Working-Tree-Anpassungen zu P3-Plan |

**Committed bisher (unverändert durch diesen Stopp):** nur P0–P2 (`7344699`, `c863f9d`, `86a8e47`).  
**Kein Commit/Push** der Instrumentierung oder P3-Lab-Doku in diesem Schritt.

### Hardware-Nebenwirkung (Desk)

- ESP32-S3 Flash enthält derzeit `s3-csi-raw`, nicht mehr `esp32.rfmonitor` 1.10.2.  
- **rfmonitor-Repo/Source unverändert.** Wiederherstellung = rfmonitor erneut flashen (Operator), falls gewünscht — hier nicht ausgeführt.

---

## 3. Herkunft esp-csi / ESP-IDF

| Element | Herkunft | Nachweis |
|---------|----------|----------|
| CSI API `esp_wifi_set_csi*` / `wifi_csi_config_t` / `wifi_csi_info_t` | ESP-IDF Wi-Fi (über Arduino-ESP32 SDK S3, CSI in sdkconfig enabled) | Headers / PHASE1 Pins |
| Init-Muster: Promiscuous **vor** `set_csi`, Non-HE CSI-Config, RX-CB | angelehnt an `espressif/esp-csi` `examples/get-started/csi_recv` (`wifi_csi_init`) | LAB-INSTRUMENT / Codekommentar in `s3-csi-raw` |
| Serial-Linienformat `CSI_RAW,...` + Host-Bundle | **eigen**, für `MV-ESP32-CSI-RAW-v0` Draft | nicht Upstream |
| SoftAP+UDP Profil N auf D1 | **eigen** (nicht esp-csi ESP-NOW `csi_send`) | — |

---

## 4. Annahmen der Instrumentierung (nicht Projektentscheid)

1. PHASE3-v3-Pfad (S3 RX + D1 Traffic N) sei als Nächstes zu **implementieren** — das war eine **Lab-Annahme**, keine Matrix-/Portfolio-Entscheidung.  
2. SoftAP `RFSENSE_N` + UDP 50 pkts/s erzeuge am S3 nutzbare CSI-Samples.  
3. Promiscuous am S3 nur als **API-Voraussetzung** für CSI (esp-csi-Muster), nicht als Capture-Contract.  
4. Ein Host-Serial-Capture reiche für A0-Dateien.  
5. D1 sei verfügbar — **falsifiziert** am Desk (nur ein USB-Serial).

---

## 5. A0 — was beobachtet wurde?

| Lauf | Beobachtung |
|------|-------------|
| Vor Instrument | S3 = rfmonitor 1.10.2; kein CSI; kein Session-Bundle; D1 unsichtbar |
| Nach Instrument | S3 bootet `INSTR s3-csi-raw`; Join-Timeout `RFSENSE_N`; `csi_ok=0`; Host schreibt leere CSV + Stats `n_samples=0` |

Session-Artefakt (lokal): `instrument/sessions/a0_smoke_20261026/`.

---

## 6. Warum A0 FAIL?

**Instrumentierungs-/Setup-Blocker**, nicht Widerlegung einer Sensing-Hypothese:

1. D1 Mini nicht am Host → kein AP / kein Profil-N-Traffic.  
2. S3 daher kein Wi-Fi-Join → CSI nie enabled/READY.  
3. Keine RAW-Samples → Zeit/seq/Gaps nicht prüfbar.

---

## 7. Was ist Artefakt ≠ Projektentscheidung?

| Artefakt | Bedeutet **nicht** |
|----------|-------------------|
| Existenz von `s3-csi-raw` | „CSI ist das gewählte Projekt“ |
| PHASE3 `MV-ESP32-CSI-RAW-v0` Draft | verbindlicher Messvertrag ohne Matrix/Entscheidung |
| Flash von s3-csi-raw auf Lab-S3 | Produkt-/Upstream-Wechsel |
| A0-FAIL | CSI-Technologie ist untauglich |

**Gültig bleiben (committed Desk):** PHASE0–2 Facts/Rejects (Capability, CCA REJECTED, K5–K7 Gates, Sheet-Reuse).  
**Offen / zurückgestellt:** jegliches Lab, Projektklasse A/B/C, Instrument-Weiterbau.

---

## 8. Nächster Audit-Schritt (vereinbart)

Zurück in den **Desk-Audit-Modus**:

> Kandidaten-/Technologiematrix: CSI · Promiscuous Capture · RX-Metadaten · weitere relevante Ansätze — gleiche Kriterien.  
> Erst nach Matrix + **expliziter Entscheidung** ggf. Experiment/Projekt.

Kein A0/C1 bis dahin.
