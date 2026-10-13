# Technology Sheet: PDAP (PCM + Control over WiFi)

```yaml
slug: pdap
title: PDAP (PCM + Control over WiFi)
primary: J
tags: [streaming]
type: protocol
status: active
seen_in: [esp32-bt-gateway, esp-network-pcm-clock]
maturity:
  technology: R1
  implementation: R0
  field_evidence: R0
  reusability: W1
```

Nur Ebene **A** (Muster). Konkrete Framing/Ports → Application B.

## Kurzfassung

Muster eines schmalen Client→Gateway-Vertrags: **PCM-Audio** plus **Metadaten/Kommandos** (optional Menübaum) über WLAN, damit die Gateway-Hardware nur Funk-/Profil-Arbeit macht und keine Infotainment-Geschäftslogik kennt.

## Abgrenzung

- **Ist:** logischer Transport-Contract Client ↔ BT-/Media-Gateway.
- **Ist nicht:** A2DP/AVRCP selbst; Hub-Telemetrie; allgemeines MQTT/Home-Automation.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Client | PCM festes Format + Events | z. B. 44.1/S16/Stereo erzwingen |
| Gateway | Encode/BT + Event-Weiterleitung | keine Quell-Semantik |
| lateral | Hub/OTA | getrennt vom Media-Pfad |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Gateway darf Sender-/App-Semantik kennen | `REJECTED` | Semantik bleibt Client; Baum nur generisch |
| Beliebiges PCM „was die Quelle liefert“ | `REJECTED` | Contract auf dem Client erzwingen |
| Ein WiFi-Modus reicht immer (STA+BT) | `HYPOTHESIS` | SoftAP/STA/Coexistence als Betriebsmodi planen |

## Transfer

Wiederverwendbar für jedes „Gehirn WLAN, Funk-Hardware separat“-Setup (nicht nur BMW). Spez früh einfrieren: Sampleformat, Event-Namen, Menübaum-Paging.

### Projektstart-Checkliste

- [ ] PCM-Contract (Rate/Format/Kanäle) schriftlich
- [ ] Event-Namen stabil halten (`next`/`previous`/…)
- [ ] Menübaum-Größe/Paging bedenken
- [ ] WiFi-Betriebsmodi vs. Classic-BT dokumentieren
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Planung: `esp32.bt-gateway` Konzept / Pflichtenheft (Vertragsname PDAP)

## Offene Fragen

- Framing (Roh-TCP vs. Chunks vs. RTP-ähnlich) — Entscheidung vor Phase 0
