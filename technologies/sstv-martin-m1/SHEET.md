# Technology Sheet: Martin M1 SSTV (AF TX)

```yaml
slug: sstv-martin-m1
title: Martin M1 SSTV Tone Transmit (AF)
primary: A
tags: [ham-radio, lab-only, fragile, esp-idf]
type: protocol
status: active
seen_in: [tinysstv]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/tinysstv-2026-foreign
```

Nur Ebene **A**. Pinouts, Filter-RC, Callsign-Praxis → Application.  
**Recht:** Funkbetrieb unterliegt lokalen Amateurfunkregeln; Sheet ≠ Sendelizenz.  
**Chip-Scope (Pilot):** ESP32-C3 + Sigma-Delta/PDM-GPIO; andere SoCs = Gate.

## Kurzfassung

**Martin M1** Slow-Scan Television: Bildzeilen werden als zeitlich definierte **AF-Töne** (Frequenz ↔ Helligkeit/Farbe) gesendet. MCU erzeugt die Tone-Sequenz (oft DDS + LUT) und gibt sie als **Basisband** aus (z. B. PDM/Sigma-Delta → LPF → Mikrofon-/AF-Eingang eines Transceivers) — **nicht** als direkter UKW-RF-Träger.

## Abgrenzung

- **Ist:** Martin-M1-Timing/VIS, Tone-Queue, AF-Ausgabe zum Radio.
- **Ist nicht:** Classic-ESP32 APLL→UKW-GPIO (`esp32-apll-fm-tx`); Pi-GPIO-FM (`rpi-gpio-fm-tx`); FM-RDS (`fm-rds`); Webcam/JPEG-on-device Decoder.
- **Grenzt an:** Externes LPF/DC-Block; PTT-Schaltung; Captive-Upload-UI (App).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Bildquelle (Browser crop / BMP) | oft 320×240 + black bars → 320×256 |
| Mitte | Martin M1 Encoder + Tone Queue | ~115 s typisch |
| unten | DDS/Sample-ISR → PDM/DAC GPIO | PDM ≠ Line-Pegel |
| lateral | Radio AF in + optional PTT | galvanische Trennung / Pegel |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| SSTV-PDM-GPIO = direkter UKW-Sender | `REJECTED` | AF-Pfad; RF macht das Funkgerät |
| PDM-Pin ohne LPF an Mic/Line | `REJECTED` | 1 MHz Carrier; Filter Pflicht |
| Martin M1 ≡ APLL-FM-Sheet | `REJECTED` | anderer Contract |
| PTT-GPIO immer im Firmware-Scope | `REJECTED` / Gap | kann reserved/unimplemented sein |
| VIS/Farben egal | `REJECTED` | VIS 44; Scan G→B→R |
| Ohne Amateurfunklizenz „Labor = On-Air ok“ | `REJECTED` | Recht lokal prüfen |

### Projektstart-Checkliste

- [ ] Nur Martin M1 oder weitere Modes?
- [ ] AF-Filter/Pegel vor Radio gemessen
- [ ] PTT: manuell vs. Firmware vs. Gap
- [ ] Chip + Audio-Pfad (PDM/DAC/I2S)
- [ ] Application + `seen_in`; Kontrast APLL-FM

## Transfer

Für Ham-SSTV-Nodes und Lab-Decoder-Validierung. Nicht still auf RF-GPIO-FM oder Webradio übertragen.

## Referenzen

- Martin M1 timing / VIS (Amateur-Radio Praxis)
- Pilot: [JO3ALT/TinySSTV](https://github.com/JO3ALT/TinySSTV)

## Offene Fragen

- Welche Mindest-LPF-Ordnungen für saubere Demod-Sync?
- Scottie/PD-Modes als eigene Slugs oder Mode-Tabelle im Sheet?
