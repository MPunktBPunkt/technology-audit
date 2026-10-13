# Audit Campaign: esp-fm-rds-node-2026-foreign

```yaml
id: esp-fm-rds-node-2026-foreign
project_id: esp-fm-rds-node
started: 2026-10-13
ended: 2026-10-13
status: closed
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "PiratESP32@58e16970e3c05cb69d4ae8d51aba6101225f4505 ESP32-S3-STEREO-DSP@b9a4a4dd19133f05de890938a7042f423098b158 PixelRadio@22a3c3d9be38d090509765cfc1c4d0c015f5ebb0 fm-streamer@cabc20d2600a7c72ae3d6bafb1702176f96de124 Adafruit-Si4713@fa38460fb0303d7951ff6a20828d707d13225d30 DynamicRDS@638dce6f64ea403462df31a1dc9aae58ffda27b5 esp32_fmdevkit@f8416d27d4bd5e016d3618a8955cb30e093fbb6d ESP32C3_FM_TRANSMITTER@89e15ecc685345bd09ffc6144ae0cd63ae41983e"
reuse_outcomes:
  reused: [fm-rds, esp-i2s-audio]
  new: []
  not_created: [fm-stereo-rds-mpx, fm-rds-synthesizer-ic]
  not_helped: [esp32-apll-fm-tx]
  process: "A/B/C, immutable SHA, G17 chip-scope, preregistered gates"
  decisions_touched: [s3-mpx-external-modulator, qn8027-vs-si4713-contract]
```

## Ziel

Acht erreichbare Fremdrepos auf immutable Commits als Desk-Evidence erfassen,
die Architektur **ESP32-S3 → I2S-MPX → externer FM-Modulator** von externen
QN8027-/Si4713-Senderpfaden abgrenzen und bestehende `fm-rds`-/
`esp-i2s-audio`-Contracts wiederverwenden. Die angefragte ManojBhakarPCM-URL
ist 404/stale und wird als unavailable dokumentiert.

## Scope

- Im Scope: Code/README/Lizenzdateien der acht fixierten Snapshots,
  A/B/C-Trennung, Decision Trace, Review Checks, Kill-Kriterien, C10–C13,
  G17 und Reuse-Outcomes.
- Nicht im Scope: Build, Hardware, RF-/Audio-/RDS-Messungen, Antenne/Feld,
  Shared Indexes, Technology Sheets, Methods und `next-audits`.
- Gewissheit: Desk-`FACT` ≠ Lab-`MEASURED` ≠ Field-`MEASURED`.

Siehe [SCOPE](../../projects/esp-fm-rds-node/SCOPE.md).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1 und Profile `lab-tool` gesetzt | erfüllt |
| 2 | Acht erreichbare Repos auf vorgegebene volle SHA fixiert | erfüllt |
| 3 | ManojBhakarPCM als 404/stale/unavailable dokumentiert | erfüllt |
| 4 | S3 → I2S-MPX → externer Modulator klar; kein RF-Claim aus I2S | erfüllt |
| 5 | Classic ESP32, ESP32-S3 und ESP32-C3 strikt getrennt (G17) | erfüllt |
| 6 | QN8027 und Si4713 getrennt beschrieben | erfüllt |
| 7 | `fm-rds` und `esp-i2s-audio` über Applications wiederverwendet | erfüllt |
| 8 | Keine unbegründeten neuen Contracts/Sheets erstellt | erfüllt |
| 9 | Decision Trace, Engineering Review Checks und Kill-Kriterien vorhanden | erfüllt |
| 10 | Lab-/Field-Claims `UNKNOWN`; Gates vor Messung präregistriert | erfüllt |
| 11 | Lokale Links/Pfade geprüft | erfüllt (2026-10-13) |

Der Abschluss gilt für den **Desk-Lauf**. Offene Lab-/Field-Gates sind
Follow-on und kein fehlendes Pflicht-Exit dieser Kampagne.

## A/B/C-Trennung

| Ebene | Ergebnis |
|-------|----------|
| A — allgemein | vorhandene Sheets `fm-rds` und `esp-i2s-audio`; keine Änderung |
| B — Implementierung | Software-MPX, QN8027, Si4713 sowie S3-/Classic-/C3-Pfade in Applications |
| C — Lab/Field | ausschließlich `UNKNOWN`; keine Messung, kein Field-Claim |

## Decision Trace (C10)

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Ist PiratESP32 ein vollständiger FM-Sender? | Wo entsteht RF? | `EVID-FMRDS-2026-10-13-001`–`004` | **Nein**: I2S-DAC liefert MPX; externer FM-Modulator nötig | KNOWN BEFORE TEST |
| Darf Classic-APLL-FM für S3 wiederverwendet werden? | Gleicher Clock/RF-Contract? | `EVID-FMRDS-2026-10-13-004`, `006` | **Nein**: S3-Beleg ist I2S-Audio/MPX, nicht APLL-RF | KNOWN BEFORE TEST |
| Belegt C3 einen S3- oder Classic-Audiopfad? | Was implementiert C3 wirklich? | `EVID-FMRDS-2026-10-13-023`–`025` | **Nein**: C3 steuert QN8027; Analogaudio ist extern | KNOWN BEFORE TEST |
| Reuse `fm-rds`? | Sind PI/PTY/PS/RT/RDS-Kernsignale vorhanden? | `EVID-FMRDS-2026-10-13-003`, `009`, `015`, `017`, `018`, `021`, `024` | **Ja**, neue Project Application | KNOWN BEFORE TEST |
| Reuse `esp-i2s-audio`? | Sind konkrete ESP-I2S-Pfade belegt? | `EVID-FMRDS-2026-10-13-001`, `006`, `012`, `019` | **Ja**, neue Project Application | KNOWN BEFORE TEST |
| Gemeinsamer QN8027/Si4713-Contract jetzt? | Verdeckt er Chip-/Audio-/RDS-Unterschiede? | `EVID-FMRDS-2026-10-13-010`, `015`–`017`, `024` | **No-Go** bis G-IC-1; Kandidat, kein Sheet | KNOWN BEFORE TEST |
| MPX-Generator-Contract jetzt? | Ist der Übergang zum RF-Modulator belegt? | `EVID-FMRDS-2026-10-13-027` | **No-Go** bis G-MPX-0/2; kein Sheet | KNOWN BEFORE TEST |
| Field-/Antennentest? | Recht und kontrollierter Aufbau geklärt? | `EVID-FMRDS-2026-10-13-030` | **No-Go**; Desk-only, G-LEGAL-1 bleibt offen | KNOWN BEFORE TEST |

## Engineering Review Checks (C11)

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-FMRDS-2026-10-13-001`–`007` | Jeder S3-Pfad endet explizit bei I2S-DAC/MPX; RF-Modulator nicht implizieren | KNOWN BEFORE TEST |
| `EVID-FMRDS-2026-10-13-004`, `019`, `023` | Jeder Peripheral-/Clock-Claim nennt Classic, S3 oder C3; kein Sammelbegriff „ESP32“ (G17) | KNOWN BEFORE TEST |
| `EVID-FMRDS-2026-10-13-008`–`011`, `020`–`025` | QN8027-Audioeingang, RDS-Refresh und Controllerrolle separat prüfen | KNOWN BEFORE TEST |
| `EVID-FMRDS-2026-10-13-012`–`018` | Si4713 Analog-/Digitalinput und RDS-Property-/FIFO-Pfad nicht mit QN8027 gleichsetzen | KNOWN BEFORE TEST |
| `EVID-FMRDS-2026-10-13-005`, `007` | README-Performance-/„tested“-Aussagen nicht zu Kampagnen-`MEASURED` aufwerten | KNOWN BEFORE TEST |
| `EVID-FMRDS-2026-10-13-022` | Vendorte ManojBhakar-Kopien nur über den jeweiligen Host-Commit zitieren; kanonische URL unavailable lassen | KNOWN BEFORE TEST |
| `EVID-FMRDS-2026-10-13-026`–`030` | Kein Lab-/Field-PASS ohne Rohartefakt und neue Evidence-ID; C13-Rückkanal vorab benennen | KNOWN BEFORE TEST |

## Kill-Kriterien (C12)

Die folgenden Kriterien sind **vor** jedem späteren Messlauf präregistriert.
Diese Desk-Kampagne hat keinen Messlauf gestartet.

**Hypothese H1:** Der S3-I2S-DAC-MPX-Pfad kann einen ausgewählten externen
FM-Modulator speisen.

| # | Kill / Widerlegt wenn | Status |
|---|-----------------------|--------|
| K1 | G-MPX-0 findet keinen dokumentierten Composite-/MPX-Eingang mit passenden Bandbreiten-/Pegelgrenzen | offen |
| K2 | nach verifiziertem DAC-MPX kein stabiler Träger beziehungsweise kein Pilot im geschirmten Aufbau nach kontrollierter Wiederholung | offen |
| K3 | Pilot ist vorhanden, aber Stereo oder RDS bleibt mit Referenzvektor reproduzierbar nicht dekodierbar | offen |

**Hypothese H2:** Ein gemeinsamer QN8027/Si4713-Minimalcontract ist
technisch nützlich.

| # | Kill / Widerlegt wenn | Status |
|---|-----------------------|--------|
| K4 | die Schnittmenge reduziert sich auf generisches I2C/Tune und verdeckt Audioinput-, RDS- oder Statussemantik | offen |
| K5 | derselbe Control-Testvektor ist zwischen beiden Chips nicht semantisch vergleichbar | offen |

**Hypothese H3:** Ein späterer RF-Lauf ist verantwortbar.

| # | Kill / Widerlegt wenn | Status |
|---|-----------------------|--------|
| K6 | Rechtslage, Schirmung oder leitungsgebundener Aufbau ist ungeklärt | offen |
| K7 | der Test erfordert Antenne/Feldabstrahlung | offen |

`UNKNOWN` allein ist kein automatisches STOP. Die konkreten K1–K7 koppeln
fehlende Voraussetzungen an eine benannte Entscheidung.

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Hardware-Path Gate | [`hw-path-gate`](../../methods/hw-path-gate.md) |
| KB Cross-Check | [`kb-cross-check`](../../methods/kb-cross-check.md) |
| RF-/RDS-Abnahme | [`rf-loopback-rds-acceptance`](../../methods/rf-loopback-rds-acceptance.md) |

## Bezug Inventar

- [INVENTORY](../../projects/esp-fm-rds-node/INVENTORY.md)
- Priorität: `fm-rds`, `esp-i2s-audio`
- Gated candidates: `fm-stereo-rds-mpx`, `fm-rds-synthesizer-ic`

## Ergebnisse

- [Application `fm-rds`](../../projects/esp-fm-rds-node/applications/fm-rds.md)
- [Application `esp-i2s-audio`](../../projects/esp-fm-rds-node/applications/esp-i2s-audio.md)
- [Evidence-Register](evidence.md)
- [Follow-on-Gates](../../projects/esp-fm-rds-node/FOLLOW-ON-IDEAS.md)

## Knowledge Feedback (C13)

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| nicht durchgeführt | keine neue `MEASURED`-ID | n/a |
| künftiges G-I2S-1 | neue ID, nicht vorhandene Desk-ID umdeuten | `applications/esp-i2s-audio.md` |
| künftiges G-MPX-1/2 oder G-IC-2 | neue ID + Rohartefakt | `applications/fm-rds.md` und ggf. begründeter Sheet-Review |

Desk-Evidence wurde nicht als Lab-/Field-Fact zurückgespielt.

## Lessons → Transfer

- Der S3-Node ist zuerst ein **MPX-Basisbandgenerator**, nicht automatisch ein
  FM-Sender.
- QN8027 und Si4713 lösen RF/Stereo/RDS extern, besitzen aber keine
  automatisch identische Contract-Fläche.
- G17 verhindert drei Fehltransfers: Classic-APLL → S3, S3-I2S-MPX → C3 und
  C3-QN8027-Control → integriertes ESP-RF.
- Ein 404-Upstream darf über vendorte Kopien genealogisch sichtbar bleiben,
  aber nicht als verfügbarer Primärsnapshot erscheinen.

## Reuse Outcomes

| Ergebnis | Einordnung |
|----------|------------|
| `fm-rds` | reused; Software-MPX und Sender-IC als getrennte Ebene-B-Varianten |
| `esp-i2s-audio` | reused; S3- und Classic-Pfade, C3 als negative Abgrenzung |
| `fm-stereo-rds-mpx` | not created; RF-/Lab-Gates offen |
| `fm-rds-synthesizer-ic` | not created; QN8027/Si4713-Differenzen zuerst prüfen |
| `esp32-apll-fm-tx` | not helped / contrast; anderer RF-Contract |

## Offene Punkte nach Abschluss

- G-MPX-0, G-IC-1 und G-LIC-1 als nächste Desk-Gates.
- Lab/Field bleiben `UNKNOWN`.
- Keine Folgedatei oder Shared-Navigation wurde in dieser Kampagne geändert.
