# Technology Sheet: LMS / Squeezelite Player

```yaml
slug: lms-squeezelite
title: LMS / Squeezelite Multi-Room Player
primary: F
tags: [streaming, esp-idf, fragile, lab-only]
type: pattern
status: active
seen_in: [squeezelite-esp32]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/squeezelite-esp32-2026-foreign
```

Nur Ebene **A**. NVS-Keys, Board-Named-Configs, Plugin-UI → Application.  
**Chip-Scope:** ESP32(+S3) mit **PSRAM**; WROOM ohne PSRAM = Gate.

## Kurzfassung

**Squeezelite**-Client an **Logitech Media Server (LMS)**: Netzwerk-Stream, Decode, optional Resample/EQ, Multi-Room-Sync; Ausgabe typisch I2S/SPDIF/BT. Auf ESP ist der Contract „LMS-first“ — AirPlay/BT/Spotify sind oft Add-ons am gleichen Player-Core, nicht der Kernvertrag.

## Abgrenzung

- **Ist:** LMS/Squeezelite player protocol + sync + on-device decode pipeline.
- **Ist nicht:** Browser-Webradio (`webradio-browser-host`); Spotify Web-API Remote ohne Decode (`spotify-web-api-remote`); reiner I2S-Pfad ohne LMS (`esp-i2s-audio` allein); A2DP-Profil allein (`bluetooth-a2dp`); Doom-style Legacy-Port ohne Audio-Stack (`esp-psram-heavy-port` nur Memory-Last).
- **Grenzt an:** I2S/SPDIF sinks; BT Classic (nicht auf S3); LMS plugins; Spotify Connect Add-ons ≠ Web-API-PKCE-Remote.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | LMS (LAN) | discovery + stream |
| Mitte | Decode / sync / buffers | PSRAM + 240 MHz typisch |
| unten | I2S DAC / SPDIF / BT speaker | mutually exclusive paths oft |
| lateral | AirPlay / Spotify / BT sink | Add-ons; shortcomings |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| WROOM ohne PSRAM reicht | `REJECTED` | Upstream: PSRAM required |
| BT/AirPlay/Spotify = gleicher Reifegrad wie LMS | `REJECTED` | Add-ons; LMS-first Design |
| 192 kHz immer stabil | `REJECTED` / Gate | Upstream empfiehlt oft ≤96 kHz report |
| Display-Last gratis | `REJECTED` | niedrigste Prio; kann High-Rate stören |
| S3 hat Classic BT Audio wie ESP32 | `REJECTED` | S3 ohne Classic BT |
| Browser-Host-Webradio ≡ Squeezelite | `REJECTED` | Audio-Ort anders |

### Projektstart-Checkliste

- [ ] PSRAM + Flash ≥4 MB; Chip Classic vs S3
- [ ] Primärpfad: LMS vs BT-only Use-Case ehrlich wählen
- [ ] Output: I2S / SPDIF / BT — Exklusivität
- [ ] Sample-Rate-Report (-Z) und Stats-Optionen
- [ ] Application + `seen_in`; Add-ons nicht als A-Kern verkaufen

## Transfer

Für Multi-Room ESP-Player und schwere Decode-Workloads. I2S-/PSRAM-Details in Nachbar-Sheets vertiefen.

## Referenzen

- Logitech Media Server / Squeezelite ecosystem
- Pilot: [sle118/squeezelite-esp32](https://github.com/sle118/squeezelite-esp32)

## Offene Fragen

- Welche Sync-Toleranzen im eigenen Lab messbar sind?
- Slimproto vs. SqueezeNet Details als eigenes Protokoll-Sheet?
