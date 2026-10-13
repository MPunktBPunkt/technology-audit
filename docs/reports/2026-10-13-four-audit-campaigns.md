# Abschluss — Vier Auditkampagnen · 2026-10-13

**Standard:** 0.7.1  
**Umfang:** Desk-Audits, Knowledge Feedback und Präregistrierung. Keine
Firmware, kein Flash, keine Hardwaremessung und keine RF-Aussendung.

## Ergebnis

| Kampagne | Status | Kernergebnis |
|----------|--------|--------------|
| [`esp-fm-rds-node-2026-foreign`](../../audits/esp-fm-rds-node-2026-foreign/) | closed | S3 ist als I2S-MPX-Generator belegt, nicht als RF-Sender; QN8027 und Si4713 bleiben getrennte externe Pfade. |
| [`esp-network-pcm-clock-2026-foreign`](../../audits/esp-network-pcm-clock-2026-foreign/) | active | RTP/UDP, TCP und Elastic Buffer getrennt; Clockdrift, Reconnect und Fail-safe sind präregistrierte Lab-Gates. |
| [`bmw-nbt-media-index-2026-foreign`](../../audits/bmw-nbt-media-index-2026-foreign/) | closed | Repositories liefern Offline-Medien-/Backup-/Forensikkontext, aber keinen Beleg für Live-USB-Cache, Resume oder HU-Identity. |
| [`usb-bot-observation-2026-foreign`](../../audits/usb-bot-observation-2026-foreign/) | closed | Device-Instrumentierung ist der erste Kandidat; Inline-Transparenz und reale NBT-CDB-/Timingwerte bleiben `UNKNOWN`. |

Alle erreichbaren Quellen sind auf immutable SHAs gesetzt. Unklare Lizenzen
bleiben `UNKNOWN`; der direkte ManojBhakar-QN8027-Link war nicht erreichbar.
Details:
[`Source Snapshots`](2026-10-13-next-audits-source-snapshots.md).

## Transfer

- Keine parallelen NBT-, USB-MSC-, RDS-, I2S- oder PCM-Sheets erzeugt.
- Reuse: `fm-rds`, `esp-i2s-audio`, `pdap`, `bmw-nbt-evo`, `usb-msc`.
- `seen_in`, Project Applications und generierte Kataloginhalte wurden
  bidirektional nachgezogen.
- HU-A1…A11 und RF-B1…B10 sind im
  [`Methodenindex`](../../methods/README.md) auf sieben neue beziehungsweise
  bestehende Verfahren abgebildet.
- Die aktive HU-Kampagne ist auf Standard 0.7.1 nachgezogen; neue Gates stehen
  ausdrücklich auf `UNKNOWN` und erzeugen noch keine Evidence-ID.

## Qualitätsprüfung

- Pflichtartefakte: vier Scopes, vier Inventare, sechs Applications, vier
  Kampagnen-READMEs und vier Evidence-Register vorhanden.
- Manuelle Indexparität: **52/52 Projekte**, **50/50 Technology Sheets**.
- Application↔Sheet-`seen_in` für alle neuen Projekte geprüft.
- Evidence-IDs, epistemische Status, A/B/C-Trennung, G17 sowie C10–C13
  manuell gegen `docs/REVIEW-CHECKS.md` geprüft.
- Zweiter unabhängiger Strukturreview: keine verbleibenden Findings nach
  Korrektur der Variantenlabels und zusammengesetzten Statusfelder.
- Später eingetroffene, tiefe Quellenreviews wurden nachgeführt:
  `esp32_fmdevkit` ist GPL-3.0 (nicht Apache-2.0), die `esp32-rtp`-Lizenz
  bleibt mangels Lizenzdatei am Pin `UNKNOWN`, und der fm-streamer-
  README-/Code-Widerspruch beim Analog-/Digitalinput ist jetzt explizit.
  Zusätzlich sind persistente NBT-SQLite-Felder dokumentiert, ohne sie zum
  Live-Cache-Key aufzuwerten.
- `python3 tools/ta-assist index/check` konnte nicht ausgeführt werden:
  Python ist auf diesem Windows-System nicht installiert. Die vier
  Katalogdateien wurden äquivalent nach den Source-of-Truth-Dateien
  aktualisiert und ihre Parität mit PowerShell geprüft.

## Weiterhin offen

1. HU-A1 als erstes Lab-Startgate: kein/Mid/Head-Read plus ausgelieferter
   Inhalt; erst danach Identity-, Eviction- und Play-Intent-Leiter.
2. Zielchip/Board für den HF-Knoten festlegen; Classic, S3 und C3 nicht
   übertragen.
3. S3-MPX nur mit dokumentiertem externem Modulator weiterführen oder
   QN8027/Si4713 als externe RF-Architektur wählen.
4. Netzwerk-PCM-Gates für Clockdrift, Buffer, Reconnect→Mute/TX-OFF ausführen.
5. RF-Abnahme ausschließlich geschirmt, gedämpft, ohne Antenne und mit
   getrennten Audio-/Stereo-/RDS-/Spektrum-/Fail-safe-PASSes.
