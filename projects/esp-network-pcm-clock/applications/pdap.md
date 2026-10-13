# Project Application: pdap in esp-network-pcm-clock

```yaml
project_id: esp-network-pcm-clock
tech_slug: pdap
status: active
sheet: ../../../technologies/pdap/SHEET.md
audit: ../../../audits/esp-network-pcm-clock-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle im Projekt — Ebene B

`pdap` ist der gemeinsame logische PCM-Contract. Der Wire-Contract bleibt je
Variante getrennt:

```text
RTP/UDP: PCM → RTP Header/sequence/timestamp → UDP → receiver → packet buffer
TCP: PCM → ELI1 record/sequence → TCP/TLS byte stream → bridge playout buffer
Elastic Buffer: validierte PCM frames → elastic buffer → I2S sink
```

Der Elastic Buffer ist eine Pufferschicht, kein drittes Netzprotokoll.

## Quellrollen und relevante Pfade

| Repository @ SHA | Pfad | Rolle |
|------------------|------|-------|
| `netham45/esp32-rtp@04562157…` | `main/receiver/network_in.c`, `main/receiver/buffer.c`, `main/sender/network_out.c` | RTP/UDP, timestamped packet ring |
| `shootao/esp_elastic_pcm_buffer@93fbda9f…` | `include/elastic_pcm_buffer.h`, `src/elastic_pcm_buffer.c`, `src/audio_speed_control.c` | Elastic Buffer: Watermarks, Prefill, Fill→Speed, Events |
| `lutyjj/esp32-streamline@c607c45b…` | `docs/pcm-protocol.md`, `firmware/streamline/src/protocol.rs`, `bridge/src/streamline_bridge/protocol.py` | TCP: `ELI1` v2 Framing |
| `NaturalDevCR/TCP-Streamer@94d5903d…` | `src-tauri/src/audio/engine/{buffer,latency}.rs`, `src-tauri/src/audio/transport/{tcp_client,tcp_server}.rs` | TCP-Kontrast: adaptive Host-Latenz |
| `badaix/snapcast@4fed179e…` | `client/stream.cpp` | Zeit-/Playout-Kontrast |

## Framing und Pufferpolitik

| Claim | Status | Evidence |
|-------|--------|----------|
| RTP-Pfad nutzt UDP; README nennt PCM S16, 48 kHz, Stereo | `FACT` (Desk, S3-Repo) | `EVID-PCMNET-2026-10-13-002` |
| RTP-Pfad erhöht nach Underflow die Zielpuffergröße schrittweise bis zum konfigurierten Maximum; Overflow verwirft den Push und kürzt den Füllstand | `FACT` (Code) | `EVID-PCMNET-2026-10-13-003` |
| TCP/StreamLine nutzt eigenes 24-Byte-`ELI1`-v2-Recordformat mit Sequenz, Format, Frames und Payload-Länge über persistentem TCP/TLS | `FACT` (Code/Doc) | `EVID-PCMNET-2026-10-13-006` |
| `ELI1` ist ausdrücklich kein RTP | `FACT` (Doc) | `EVID-PCMNET-2026-10-13-006` |
| StreamLine trennt explizite Silence-Records von fehlenden Sequenzpositionen und concealment | `FACT` (Doc) | `EVID-PCMNET-2026-10-13-007` |
| Elastic Buffer klassifiziert Prefill/Normal/Low/High/Underflow über Start-, Low-, Target- und High-Watermarks | `FACT` (Code) | `EVID-PCMNET-2026-10-13-004` |
| Elastic Buffer empfiehlt unter Target langsamere und über Target schnellere Wiedergabe; Sonic begrenzt den angewendeten Faktor im Code | `FACT` (Code), Audioqualität unbekannt | `EVID-PCMNET-2026-10-13-005` |

## Ebene C — Host-/Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| RTP/UDP hält auf Zielhardware Clockdrift ohne nachhaltigen Fill-Level-Marsch aus | `EVID-PCMNET-2026-10-13-012` | `UNKNOWN` |
| TCP bleibt bei demselben Störprofil ohne Under-/Overflow und mit begrenztem Backlog | `EVID-PCMNET-2026-10-13-012` | `UNKNOWN` |
| Elastic Buffer konvergiert nach Störung ohne hörbares Pumpen oder falsche Sample-Rate | `EVID-PCMNET-2026-10-13-012` | `UNKNOWN` |
| Reconnect erzwingt Mute, verwirft Alt-PCM und gibt erst nach validiertem Framing + Prefill frei | `EVID-PCMNET-2026-10-13-013` | `UNKNOWN` |

## Engineering-Grenzen

- TCP garantiert geordnete Bytes, aber keine Recordgrenzen; der TCP-Pfad muss Header und
  Payload vollständig reassemblieren.
- RTP-Sequenz-/Zeitstempellücken sind RTP-spezifisch. Sie dürfen nicht als
  TCP-Paketverlustzähler wiederverwendet werden.
- Buffer-**Kapazität**, Ziel-Füllstand und End-to-end-Latenz sind verschiedene
  Größen.
- Reconnect setzt Parser-/Sessionzustand zurück und hält den Sink stumm.

## Offene Fragen

- Welche Variante besteht G-CLK, G-BUF und G-REC auf dem konkret benannten SoC?
- Ist Fill-Level-Speed-Control oder Silence-only-Anpassung für den Zielpfad
  akustisch vertretbar?
- Welche Control-Nachrichten gehören später zusätzlich zum PCM-Contract?
