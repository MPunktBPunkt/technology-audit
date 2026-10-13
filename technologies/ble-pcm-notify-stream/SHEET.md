# Technology Sheet: BLE PCM Notify Stream

```yaml
slug: ble-pcm-notify-stream
title: BLE PCM Notify Stream (Custom GATT)
primary: C
tags: [streaming, fragile, lab-only]
type: pattern
status: active
seen_in: [esp32-i2s-ble]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/esp32-i2s-ble-2026-foreign
```

Nur Ebene **A**. Konkrete UUIDs, iOS-Apps, Mic-Boards → Application.  
**Kein** Bluetooth LE Audio (LC3) und **kein** Classic A2DP.

## Kurzfassung

Anwendungsspezifisches **GATT-Muster**: PCM-Samples (meist int16 LE) per **Notify** in Batches, oft mit Control-Characteristic (START/STOP), Sequence-Nummer und Ringbuffer zwischen Capture und Radio. Bandbreite begrenzt durch MTU und Notify-Interval.

## Abgrenzung

- **Ist:** Custom BLE Service für Roh-PCM oder ähnlich einfache Audio-Frames.
- **Ist nicht:** LE Audio / PBP / TMAP; A2DP (`bluetooth-a2dp`); AVRCP; BLE-HR/FTMS-Sheets.
- **Grenzt an:** I2S-Capture (`esp-i2s-audio`); allgemeine NimBLE Central/Peripheral Patterns.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Phone/App GATT Client | Subscribe + optional Write Control |
| unten | Capture-Quelle (I2S/ADC) + Ringbuffer | Rate-Mismatch abfangen |
| lateral | MTU-Negotiation | Packetgröße |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Custom Notify-PCM = LE Audio | `REJECTED` | anderes Profil / Codec / Binding |
| Custom Notify-PCM = A2DP | `REJECTED` | Classic vs. BLE; anderer Stack |
| Ohne Batching/Ringbuffer „einfach streamen“ | `REJECTED` / Gate | Peer droppt kleine/häufige Packets → Tempo-Artefakte |
| README-Sample-Rate = Wire-Rate ohne Check | `REJECTED` | Capture und Notify-Rate können differieren (Downsample) |
| Unbegrenzte Aufnahme ohne Overflow-Policy | `REJECTED` | Ring voll → Drop |

### Projektstart-Checkliste

- [ ] Explizit: Custom GATT ≠ LE Audio ≠ A2DP
- [ ] MTU, Samples/Notify, Interval, Ring-Kapazität
- [ ] Capture-Rate vs. Output-Rate dokumentieren
- [ ] Application + `seen_in`; Peer-OS-Verhalten = C

## Transfer

Nützlich für Speech-to-Text-Bridges und Lab-Mic-Streamer. Nicht als Bluetooth-Audio-Standard verkaufen.

## Referenzen

- Bluetooth Core GATT Notify
- Beispielmuster: I2S-Mic → NimBLE Notify (fremd)

## Offene Fragen

- Praktische Dauerlimits bei iOS ohne LE Audio?
- Opus-über-Notify vs. PCM Trade-offs?
