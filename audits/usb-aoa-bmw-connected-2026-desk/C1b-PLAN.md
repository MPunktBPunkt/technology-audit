# C1b Messplan — AOA Reachability + BCL-on-Bulk (Desk 2026-10-29)

**Status:** Plan only · **kein** hu-probe-Code in diesem Audit  
**Bezug:** Kampagne [`usb-aoa-bmw-connected-2026-desk`](README.md) · Feld-Notizen hu-probe
`docs/feld/2026-10-29-c1b-p0-aoa-observe-feld.md` (Quellrepo, nicht hier editiert)  
**Epistemik:** **A** = Beobachtung/Evidence · **B** = Hypothese · **C** = nächste Messung

---

## Gap-Zusammenfassung (½ Seite)

BimmerGestalt belegt deskseitig: Connected Apps laufen über **BCL** (8-Byte-MUX) auf einem
Serial-Rohr — Doc nennt **USB Accessory / BT / ENET**; **BclCarLink** verdrahtet nur
**BT RFCOMM** und speist `BclClientTransport(InputStream, OutputStream)`. Phone-seitig
erkennt AAIdrive Accessory über `UsbAccessory.manufacturer` enthält `"BMW"` und zählt
File-Transfer oft als Vorbedingung. AOA selbst (51/52/53 → `0x18D1:0x2D0x` Bulk) ist
AOSP-`FACT`, aber **nicht** im BG-Code als Host-Handshake implementiert.

hu-probe C1b-P0 (`AoaObserveGadget` + `AoaControlTap`, FW 0.3.23, F20/NBT Evo): HU
**enumeriert** die Probe als Zubehör (`0x18D1:0x2D00`, UI „Zubehörmodus / AOA Observe“).
**A:** Vendor-Control 51/52/53-Zähler = 0; Bulk-RX = 0. Standard-/Class-Requests und
vollständiger AOA-Handshake sind instrumentierungsseitig noch unsichtbar; Bulk wird
nicht als BCL geframed. Damit: Accessory-**Erkennung** ja, Connected-**Rohr** nein —
B1 (Switch/Handshake-Pfad) und B2 (BCL-on-Bulk) bleiben die gezielten Messungen.

---

## Messungen (max. 3)

### 1 — B1: AOA-Reachability / Switch-Detection

| Tag | Inhalt |
|-----|--------|
| **B** | HU initiiert AOA nur, wenn das Device **noch nicht** als Google-Accessory
(`0x18D1:0x2D0x`) erscheint — Phone-like VID/PID → 51→52→53 → Re-Enum. Bereits-Accessory-Boot
kann Enum/UI auslösen, ohne Control/Bulk (Feld 2026-10-29). |
| **A (erwartetes Signal)** | (a) Vendor-Control `bRequest∈{51,52,53}` mit Zählern >0 **oder**
klar dokumentiertes Absent nach Phone-like Enum; (b) bei 53: Descriptor-Wechsel zu
`0x18D1:0x2D00`/`0x2D01` (wenn Post-53-Re-Enum beobachtbar); (c) optionale String-Capture
bei 52 (Manufacturer/Model — B3). Parallel: HU-UI-Zustand (Zubehör vs. Medien vs. Connected). |
| **Minimaler FW-/Log-Aufwand (nur Beobachtung)** | Boot-Profil „Phone-like“ (nicht-Google
VID/PID) **oder** externes Phone/Host als Referenz; `AoaControlTap`-Zähler 51/52/53 +
`ca_usb`; **alle** Control-SETUPs loggen soweit nur Vendor (Gap schließen); kein Soft-Cycle
unter Auto-OTG wenn WLAN-Messung nötig. Post-53 Descriptor-Override nur wenn Lab das
ohne MSC-Fingerprint-Bruch erlaubt — sonst externes Capture. |
| **Erfolgskriterium** | Mindestens eines: beobachteter 51→52→53-Pfad **oder** reproduzierbares
Negativ mit Phone-like Enum + vollständiger Control-Sichtbarkeit; Identity/PID nach Switch
dokumentiert. Kill K1 neu: „kein Bulk/Connected nach Accessory-Erkennung“ wenn Enum ja
aber Rohr nein (Desk-Kill „kein Switch zu 0x18D1“ greift nicht bei Already-Accessory). |
| **C danach** | Bei positivem Switch/Control → Messung **2 (B2)**. Bei dauerhaftem Absent
trotz sichtbarer Controls → paralleles Phone+Connected-Capture (Referenz) oder BT-SPP-Pfad
als Transport-Alternative priorisieren. |

### 2 — B2: BCL-Framing auf Bulk nach Switch

| Tag | Inhalt |
|-----|--------|
| **B** | Nach erfolgreichem Accessory-Rohr trägt Bulk dieselben BCL-8-Byte-BE-Header wie
auf BT RFCOMM (`cmd/src/dest/len`); dest `0x0FA4` = Etch-Kandidat; Handshake/SelectProto/Knock
folgen der BclCarLink-State-Machine. |
| **A (erwartetes Signal)** | Erste Bulk-RX-Bytes: 8-Byte-Header korrelierbar (command ∈
OPEN/DATA/CLOSE/HANDSHAKE/…; dest z. B. `0x0FA4` oder Watchdog `0x1389`); optional Init-
Bytes `12345678` (Phone-Client-Pfad) vs. HU-seitiger Handshake zuerst (**nicht belegt** für
USB — nur BT-Client-Code). Kein Auto-Feed in `BclFramer` bis Header-Muster stabil. |
| **Minimaler FW-/Log-Aufwand** | Raw Bulk-RX Hex/Counter in `ca_usb` (P0-E); optional
Offline-Dump der ersten N Bytes; **kein** Etch/SAS/RHMI; `BclFramer` erst nach manueller
Header-Bestätigung (C1b-P1 Gate). |
| **Erfolgskriterium** | Capture mit ≥1 korrelierbarem BCL-Frame **oder** klar negatives
Bulk ohne 8-Byte-Muster bei nachgewiesenem Rohr. |
| **C danach** | Positiv → C1b-P1/P2 (Framer quality) → P3 (dest-Semantik / Etch-Label).
Negativ bei offenem Rohr → Framing-Hypothese verwerfen oder anderen Transport (BT) messen. |

### 3 — (optional, nur wenn B1 unklar) Control-Sichtbarkeit / Mode-UI

| Tag | Inhalt |
|-----|--------|
| **B** | HU „USB-Modus aktivieren“ zielt auf MTP/MSC-File-Pfad, nicht Connected-Bulk;
fehlende Standard-/Class-Request-Logs maskieren Mode-Switches. |
| **A** | Vollständiges Control-Log (bmRequestType/bRequest) während UI-Aktion „USB-Modus“;
Vergleich mit Phone+Connected Referenzsession. |
| **Minimalaufwand** | Log-Erweiterung Observation-only; **kein** Soft-Composite MSC+AOA
im gleichen Boot (MSC-Fingerprint). |
| **Erfolg** | Aussage: welche Requests bei UI-Aktion ankommen / absent bleiben. |
| **C** | Informiert B1-Retry oder separates Mode-Experiment. |

---

## A/B-Gap-Tabelle (hu-probe vs. BG)

| # | A (Evidence) | B (Hypothese) |
|---|--------------|---------------|
| G1 | Feld: Enum `0x18D1:0x2D00`, UI Zubehör; 51/52/53=0; Bulk=0 | Already-Accessory-Boot reicht für UI, nicht für Connected-Rohr |
| G2 | Bis P0.5-A: Tap filterte auf Vendor-SETUPs. Ab hu-probe **0.3.24**: alle Callback-SETUPs + `setup_count`/`vendor_setup_count`/`drops`/`stage` — weiterhin **kein** voller EP0-Sniffer (nur was `USBVendor.onRequest` liefert) | Mode-/Class-Traffic kann den Callback nie erreichen; Lab-Instrument-Check nötig |
| G3 | BG Doc: USB Accessory = BCL-Weg; Code: nur BT | USB-BCL existiert am Wire, ist aber in BclCarLink nicht implementiert |
| G4 | AAIdrive: File Transfer vor Accessory; manufacturer `"BMW"` | HU sendet BMW-Strings bei 52; Phone-like Enum nötig für Switch |
| G5 | BclClientTransport stream-agnostisch; kein USB-Binder in BclCarLink | ITransport-Trennung korrekt; AOA und SPP austauschbar unter BclFramer |
| G6 | C1a `BclFramer` lab-PASS; Wire-Bulk nicht gefüttert | BCL-on-USB erst nach B2 messbar; kein Semantic-Claim vor P3 |

---

## Nicht tun (dieser Plan)

- AOA-/SAS-/Etch-/RHMI-Implementierung „weil Desk fertig“
- MSC-Gates / Soft-Composite ohne eigenen Gate-Schnitt
- Wire-FACTS aus AAIdrive-Issues ohne Capture
- A/B/C vermischen in Reports
