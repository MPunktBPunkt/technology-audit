# Technology Sheet: ESP USB Audio (UAC Device)

```yaml
slug: esp-usb-audio-uac
title: ESP USB Audio (UAC Device)
primary: C
tags: [usb-device, streaming, esp-idf, fragile]
type: protocol
status: active
seen_in: [esp-iot-solution, esp-usb-audio-example]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
pilot: audits/esp-iot-solution-2026-foreign
```

Nur Ebene **A**. Board-Codecs (ES8311/ES7210), Box-Pinouts → Application B/C.  
**Chip-Scope:** USB Device/OTG auf **ESP32-S2 / ESP32-S3 / ESP32-P4** (Upstream-Targets). Classic ESP32 ohne Device-OTG = außerhalb.

## Kurzfassung

ESP als **USB-Audio-Gerät** (USB Audio Class, typisch UAC1/UAC2 über TinyUSB): Host sieht Headset/Speaker/Mic; Isochronous Streaming + Feature-Unit (Mute/Volume). Audio pflegt die Firmware oft parallel über I2S zu einem Codec.

## Abgrenzung

- **Ist:** USB **Device**-Rolle, Audio-Klasse (UAC) gegenüber einem Host-PC/Phone.
- **Ist nicht:** USB **Host**-Audio (`usb_stream` / `esp-usb-host`); USB-MSC-Gadget (`usb-msc`); Bluetooth A2DP/LE Audio; reiner I2S-Player ohne USB.
- **Grenzt an:** TinyUSB Device-Stack; I2S-Codec-Pfad (`esp-i2s-audio`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Host OS Audio (ALSA/CoreAudio/WASAPI) | Enum als Audio-Gerät |
| unten | TinyUSB UAC + USB Device Controller | Isochronous EP IN/OUT |
| lateral | I2S ↔ Codec / PWM / DAC | oft paralleler Pfad |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Classic ESP32 = UAC Device ohne Gate | `REJECTED` | Device-OTG nur S2/S3/P4-Familie (Upstream-Targets) |
| `esp-usb-host` Sheet deckt Device-Headset ab | `REJECTED` | Host ≠ Device; anderer Slug |
| UAC ≡ MSC-Gadget | `REJECTED` | andere USB-Klasse / andere Host-Erwartung |
| Ein Descriptor für Windows und Linux „immer“ | `REJECTED` / Gate | Espressif: nicht gleichzeitig kompatibel; macOS braucht Extra-Makro |
| Dynamische Sample-Rate-Umschaltung „einfach“ | `REJECTED` (Stand Espressif Component) | Upstream: noch nicht supported |
| LE Audio / A2DP = gleicher Contract | `REJECTED` | getrennte Transport-/Profil-Sheets |

### Projektstart-Checkliste

- [ ] Chip S2/S3/P4? Classic = Gate
- [ ] Device- vs. Host-Rolle explizit
- [ ] Mic/Spk-Kanäle + Sample-Rate (Kconfig / TinyUSB CFG)
- [ ] Codec/I2S-Pfad getrennt dokumentieren (`esp-i2s-audio`)
- [ ] Application + `seen_in`; Host-OS-Quirks = C

## Transfer

Relevant für Headset-/Mic-Gadgets, USB-Speaker-Bridges, Lab-Audio ohne Bluetooth. Nicht still auf Host-UAC oder MSC übertragen.

## Referenzen

- Espressif `usb_device_uac` (esp-iot-solution)
- USB Audio Class Spec (UAC1/UAC2)
- TinyUSB Audio device examples

## Offene Fragen

- Welche Host-OS-Kombinationen mit Feedback-EP stabil sind?
- P4 HS vs. FS Bandbreiten-Budget für Stereo 48 kHz?
