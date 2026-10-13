# Project Scope: esp-network-pcm-clock (Fremdvergleich)

```yaml
project_id: esp-network-pcm-clock
title: ESP Network PCM Clock — Framing und elastische Puffer
updated: 2026-10-13
profile_hint: lab-tool
audit: esp-network-pcm-clock-2026-foreign
status: active
```

## Zweck

Desk-only Vergleich wiederverwendbarer Bausteine für PCM über WLAN:
Framing, Sequenzierung, adaptive/elastische Puffer, Watermarks, Clockdrift,
Under-/Overflow und sicheres Verhalten bei Reconnect. Ziel ist eine
präregistrierte Variantenentscheidung, kein Leistungsnachweis.

## Quell-Snapshots

| Repository | Immutable SHA | Rolle |
|------------|---------------|-------|
| [netham45/esp32-rtp](https://github.com/netham45/esp32-rtp/tree/04562157e92cb8ee92f2c4623ec860e7e7e9ef78) | `04562157e92cb8ee92f2c4623ec860e7e7e9ef78` | UDP/RTP Sender/Receiver |
| [shootao/esp_elastic_pcm_buffer](https://github.com/shootao/esp_elastic_pcm_buffer/tree/93fbda9f2e127f8bbc3f8d00b462f65aaa7788f4) | `93fbda9f2e127f8bbc3f8d00b462f65aaa7788f4` | Elastic Buffer, Watermarks/Rate-Control |
| [lutyjj/esp32-streamline](https://github.com/lutyjj/esp32-streamline/tree/c607c45b17da2e88f950aa826a5b8d53f5c5059b) | `c607c45b17da2e88f950aa826a5b8d53f5c5059b` | eigenes TCP-PCM-Framing |
| [NaturalDevCR/TCP-Streamer](https://github.com/NaturalDevCR/TCP-Streamer/tree/94d5903d37917bb689e23ca6378d0026aef80cfe) | `94d5903d37917bb689e23ca6378d0026aef80cfe` | TCP-Kontrast: Host-Puffer/Drift |
| [badaix/snapcast](https://github.com/badaix/snapcast/tree/4fed179e177b251c67326e7b62a25c8d8fb2d1a9) | `4fed179e177b251c67326e7b62a25c8d8fb2d1a9` | Zeit-/Playout-Sync-Kontrast |
| [pschatzmann/arduino-audio-tools](https://github.com/pschatzmann/arduino-audio-tools/tree/0ef1b1547f240aba146b0c100e0da610267aeffc) | `0ef1b1547f240aba146b0c100e0da610267aeffc` | I2S-/Pipeline-Kontrast |

## Systeme und Grenzen

| System | Im Scope | Grenze |
|--------|----------|--------|
| ESP-Empfang/Senden und Host-Referenzen | ja, Desk | nur Code/Dokumentation der SHAs |
| UDP/RTP | ja | Paket-, Sequenz- und Zeitstempelsemantik bleibt RTP |
| TCP | ja | eigener Record-Contract nötig; kein „RTP über TCP“-Claim |
| Elastischer PCM-Puffer | ja | kein eigener Netzwerktransport |
| I2S-Ausgabe | ja, Contract/Gate | reale Peripheral-Clock und Boardverhalten `UNKNOWN` |
| Lab/Feld | nein | präregistriert, nicht ausgeführt |

## Nicht-Ziele

- Keine erfundenen Jitter-, Latenz-, Drift- oder Audioqualitätswerte.
- Keine Gleichsetzung von TCP-Zustellung mit RTP-Paketverlust.
- Kein allgemeiner ESP32-Claim aus einem ESP32-S3- oder Classic-ESP32-Beleg.
- Keine Auswahl eines Produktionsprotokolls ohne Variantenvergleich im Lab.
- Keine Änderungen an Shared Indexes, Technology Sheets, Methods oder
  `next-audits`.

## G17 — Chip-/SoC-Scope

- `esp32-rtp`: README-Hardware-Scope **ESP32-S3**.
- `esp32-streamline`: offizieller Preset-Scope **ESP32 classic ECO3** mit
  ES8388; nicht auf S3 übertragen.
- `esp_elastic_pcm_buffer` und Arduino Audio Tools: der konkrete Ziel-SoC und
  dessen I2S-/Clockverhalten sind für dieses Projekt `UNKNOWN`; eigenes Gate
  erforderlich.
