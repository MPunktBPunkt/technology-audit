# Technology Sheet: ESP I2S Audio Path

```yaml
slug: esp-i2s-audio
title: ESP I2S Audio Path
primary: B
tags: [streaming, esp-idf, arduino, fragile]
type: implementation
status: active
seen_in: [esp32-audioi2s, esp-usb-audio-example, esp32-i2s-ble]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
pilot: audits/esp32-audioi2s-2026-foreign
```

Nur Ebene **A**. Konkrete DACs (MAX98357A, PCM5102, ES8311), Mic-Breakouts, Pinouts → Application.  
**Chip-Scope:** I2S-peripherie-fähig; **Decode-Player-Libraries** oft multi-core + PSRAM (S3/P4). Single-core / ohne PSRAM = Gate pro Library.

## Kurzfassung

ESP spricht **I2S** (STD/PDM/…) zu externem DAC, Codec oder MEMS-Mic: Decode→DOUT (Player) oder DIN→PCM (Capture). Sample-Rate, Bits, DMA und Resampling sind der Contract — nicht die Container-Formate allein.

## Abgrenzung

- **Ist:** On-chip I2S-Datenpfad + typische Codec-/Amp-Schnittstelle.
- **Ist nicht:** Browser-Webradio (`webradio-browser-host`); A2DP-Profil (`bluetooth-a2dp`); USB-UAC (`esp-usb-audio-uac`); PWM-/DAC-Audio ohne I2S (esp-iot-solution `pwm_audio`/`dac_audio` = angrenzend, eigener Pfad).
- **Grenzt an:** A2DP Source, der I2S-Samples frisst; BLE-PCM-Notify (`ble-pcm-notify-stream`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Decoder / Capture-Task / USB-UAC-Bridge | Soft-Pipeline |
| unten | I2S STD/PDM + GPIO BCLK/WS/DOUT|DIN | oft + MCLK |
| lateral | PSRAM / Dual-Core | Decode-Last |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Jede ESP32-Variante trägt schwere Decode-Player (MP3/FLAC/…) | `REJECTED` | z. B. ESP32-audioI2S: S2/C3 explizit ungeeignet; Classic nur eingeschränkt |
| PSRAM optional bei großen Decodern | `REJECTED` / Gate | Library-Claims oft „mit PSRAM“ |
| Feste 48 kHz I2S-Out = Quell-Sample-Rate | `REJECTED` | Resampler dazwischen (Upstream oft fest 48 kHz Out) |
| MEMS 32-bit I2S = direkt int16 ohne Scale | `REJECTED` | Shift/Clamp nötig (Capture-Pfad) |
| SEL/LR-Kanal am Mic ignorieren | `REJECTED` | Kanalwahl hardwareseitig |
| I2S-Player = Browser-Host-Webradio | `REJECTED` | anderer Audio-Ort |

### Projektstart-Checkliste

- [ ] Chip + PSRAM/Core-Anforderungen der Library geprüft
- [ ] Richtung: TX (Player) vs. RX (Mic) vs. Full-Duplex
- [ ] Sample-Rate-Contract: Capture vs. Output vs. Host
- [ ] Nicht mit A2DP/UAC/Browser-Sheets vermischen ohne Gate
- [ ] Application + `seen_in`

## Transfer

Basis für Webradio-on-device, USB-Headset-Bridges, BLE-Mic-Streamer. Codec-I2C-Steuerung bleibt Application.

## Referenzen

- ESP-IDF I2S driver (STD)
- schreibfaul1/ESP32-audioI2S
- Espressif codec / I2S examples

## Offene Fragen

- Einheitliche Resampler-Policy IDF vs. Arduino-Libs?
- Wann PWM-Audio statt I2S-DAC vertretbar ist?
