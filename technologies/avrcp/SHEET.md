# Technology Sheet: AVRCP

```yaml
slug: avrcp
title: AVRCP
primary: C
tags: [bluetooth-classic, metadata]
type: protocol
status: active
seen_in: [pidrive, esp32-bt-gateway]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/pidrive-2026-radio-bt
```

Nur Ebene **A**. Konkretes HU-Tasten-/Browse-Verhalten → Host-Sheet / Application C.

## Kurzfassung

Audio/Video Remote Control Profile: Steuerung und Metadaten zwischen Controller und Target über AVCTP. Optional **Browsing**-Kanal für Listen/Ordner. Häufig gekoppelt mit A2DP, aber eigenständiges Profil.

## Abgrenzung

- **Ist:** Classic-BT Remote Control + Metadata (+ optional Browse).
- **Ist nicht:** A2DP-Audio; MPRIS (Linux-Abstraktion); Fahrzeug-eigene HMI-Tasten, die nie als AVRCP erscheinen.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | App / Infotainment-Logik | Events, Meta, Menübaum-Semantik |
| unten | AVCTP Control / Browsing PSMs | Pass-Through, Notifications, Folder Items |
| lateral | A2DP | oft gleiches Pairing |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Alle Medientasten der HU kommen als AVRCP | `REJECTED` | viele HUs behalten MENU/BACK/Dreh-Drück lokal |
| Metadata-Zeilen = vollständige Playlist | `REJECTED` | oft nur markierter Eintrag (Titel/Artist/Album) |
| BlueZ Target liefert immer Browsing | `REJECTED` | Browsing/Target-Lücken sind ein typischer Gateway-Treiber |
| Observe-first ist optional | `HYPOTHESIS` | empirisch oft nötig bevor Mapping |
| Lenkrad = immer AVRCP Pass-Through | `REJECTED` | Mapping oft App-seitig (D-Bus → Trigger) |
| Metadata-Pfad = MPRIS automatisch | `REJECTED` | getrennte Abstraktionen; explizit bridgen |

## Transfer

Nutzen wenn Steuerung/Meta vom Audio-Host entkoppelt oder BlueZ-Target unzureichend ist. Stufen denken (Pass-Through → Meta → Browse), nicht alles auf einmal.

### Projektstart-Checkliste

- [ ] Rollen Controller/Target klären (HU meist Controller)
- [ ] Welche Tasten wirklich als AVRCP ankommen (messen)
- [ ] Browsing-Ambition (S3) vs. Skip=Cursor-Workaround trennen
- [ ] Semantik des Menübaums im Client behalten — Transport generisch
- [ ] BlueZ Target vs. dediziertes Gateway (ESP) entscheiden
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Bluetooth AVRCP Spezifikation (SIG)
- Host-Notizen: PiDrive `avrcp_trigger.py`, `BMW-AVRCP-PROBE.md`
- Planung Gateway: `esp32.bt-gateway`

## Offene Fragen

- Welche Browse-Subset-Befehle NBT Evo zuverlässig nutzt?
