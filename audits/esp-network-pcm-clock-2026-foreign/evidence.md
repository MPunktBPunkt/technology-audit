# Evidence — esp-network-pcm-clock-2026-foreign

Desk 2026-10-13 · **standard_version 0.7.1** · Profile `lab-tool`.

## Immutable Snapshots

| Repository | Commit |
|------------|--------|
| `netham45/esp32-rtp` | `04562157e92cb8ee92f2c4623ec860e7e7e9ef78` |
| `shootao/esp_elastic_pcm_buffer` | `93fbda9f2e127f8bbc3f8d00b462f65aaa7788f4` |
| `lutyjj/esp32-streamline` | `c607c45b17da2e88f950aa826a5b8d53f5c5059b` |
| `NaturalDevCR/TCP-Streamer` | `94d5903d37917bb689e23ca6378d0026aef80cfe` |
| `badaix/snapcast` | `4fed179e177b251c67326e7b62a25c8d8fb2d1a9` |
| `pschatzmann/arduino-audio-tools` | `0ef1b1547f240aba146b0c100e0da610267aeffc` |

## Register

| ID | Claim (Kurz) | Status | Quelle / Review |
|----|--------------|--------|-----------------|
| `EVID-PCMNET-2026-10-13-001` | Sechs Desk-Quellen sind auf die oben genannten vollständigen SHAs fixiert; keine Laufzeitmessung | `FACT` | jeweilige GitHub-Commit-Trees; Review: Reproduzierbarkeit/SHA |
| `EVID-PCMNET-2026-10-13-002` | `esp32-rtp` beschreibt ESP32-S3, RTP über UDP und PCM S16/48 kHz/Stereo; A-Scope | `FACT` | [`README.md`](https://github.com/netham45/esp32-rtp/blob/04562157e92cb8ee92f2c4623ec860e7e7e9ef78/README.md); Review: RTP≠TCP, G17 |
| `EVID-PCMNET-2026-10-13-003` | Receiver-Code führt timestamped Ring-Slots; Underflow erhöht das Target bis Max, Overflow lehnt Push ab und setzt Füllstand auf Target | `FACT` | [`main/receiver/buffer.c`](https://github.com/netham45/esp32-rtp/blob/04562157e92cb8ee92f2c4623ec860e7e7e9ef78/main/receiver/buffer.c); Review: stale slots/Under-/Overflow |
| `EVID-PCMNET-2026-10-13-004` | Elastic Buffer implementiert Start/Low/Target/High, Prefill, Low/Normal/High/Underflow sowie Under-/Overflow-Zähler und Events | `FACT` | [`src/elastic_pcm_buffer.c`](https://github.com/shootao/esp_elastic_pcm_buffer/blob/93fbda9f2e127f8bbc3f8d00b462f65aaa7788f4/src/elastic_pcm_buffer.c); Review: Watermark-Ordnung/State |
| `EVID-PCMNET-2026-10-13-005` | Fill-Level unter/über Target empfiehlt niedrigere/höhere Speed; Sonic-Anwendung clamp-t im Code auf 0.85…1.15, ohne damit Audioqualität zu belegen | `FACT` | [`elastic_pcm_buffer.c`](https://github.com/shootao/esp_elastic_pcm_buffer/blob/93fbda9f2e127f8bbc3f8d00b462f65aaa7788f4/src/elastic_pcm_buffer.c), [`audio_speed_control.c`](https://github.com/shootao/esp_elastic_pcm_buffer/blob/93fbda9f2e127f8bbc3f8d00b462f65aaa7788f4/src/audio_speed_control.c); Review: Speed/Format |
| `EVID-PCMNET-2026-10-13-006` | StreamLine v2 nutzt eigenes `ELI1`-Framing: 24-Byte-LE-Header, sequence/sample-rate/frames/payload; 48 kHz S16LE stereo, 256 Frames; persistent TCP/TLS; ausdrücklich nicht RTP | `FACT` | [`docs/pcm-protocol.md`](https://github.com/lutyjj/esp32-streamline/blob/c607c45b17da2e88f950aa826a5b8d53f5c5059b/docs/pcm-protocol.md); Review: partielle TCP-Reads, Magic/Version/Länge, G17 Classic-ECO3 aus README |
| `EVID-PCMNET-2026-10-13-007` | StreamLine unterscheidet explizite Silence-Records, fehlende/late Sequenzen, Concealment und Rebuffering; Reconnect behält gelerntes Target, setzt Arrival-History zurück | `FACT` | [`docs/pcm-protocol.md`](https://github.com/lutyjj/esp32-streamline/blob/c607c45b17da2e88f950aa826a5b8d53f5c5059b/docs/pcm-protocol.md); Review: Zustände/Zähler |
| `EVID-PCMNET-2026-10-13-008` | TCP-Streamer trennt Ringkapazität vom adaptiven Standing-Latency-Target; Glitch erhöht Target, stabile Ticks senken es innerhalb Min/Max | `FACT` | [`buffer.rs`](https://github.com/NaturalDevCR/TCP-Streamer/blob/94d5903d37917bb689e23ca6378d0026aef80cfe/src-tauri/src/audio/engine/buffer.rs), [`latency.rs`](https://github.com/NaturalDevCR/TCP-Streamer/blob/94d5903d37917bb689e23ca6378d0026aef80cfe/src-tauri/src/audio/engine/latency.rs); Review: Capacity≠Target≠E2E |
| `EVID-PCMNET-2026-10-13-009` | TCP-Streamer hat getrennte TCP- und UDP-Transportmodule einschließlich UDP jitter/drift/packet; dies ist kein RTP-Beleg für den TCP-Pfad | `FACT` | [`src-tauri/src/audio/transport`](https://github.com/NaturalDevCR/TCP-Streamer/tree/94d5903d37917bb689e23ca6378d0026aef80cfe/src-tauri/src/audio/transport); Review: Transportzähler getrennt |
| `EVID-PCMNET-2026-10-13-010` | Snapcast versieht Chunks mit Serverzeit, puffert bis Playoutzeit und korrigiert Abweichungen per Hard-Sync bzw. Frame Drop/Duplicate; Desktop-/Multiroom-Kontrast, kein ESP-Beleg | `FACT` | [`README.md`](https://github.com/badaix/snapcast/blob/4fed179e177b251c67326e7b62a25c8d8fb2d1a9/README.md), [`client/stream.cpp`](https://github.com/badaix/snapcast/blob/4fed179e177b251c67326e7b62a25c8d8fb2d1a9/client/stream.cpp); Review: kein SoC-Transfer |
| `EVID-PCMNET-2026-10-13-011` | Arduino Audio Tools bietet Source/Sink-/Stream-Abstraktionen und `I2SStream`-Konfiguration; daraus folgt kein Zielboard-Clock- oder Reconnect-Nachweis | `FACT` | [`README.md`](https://github.com/pschatzmann/arduino-audio-tools/blob/0ef1b1547f240aba146b0c100e0da610267aeffc/README.md); Review: Format vor I2S |
| `EVID-PCMNET-2026-10-13-012` | Clockdrift, Under-/Overflow-Recovery, Rate-Control-Audioqualität und Classic↔S3-Transfer auf Zielhardware sind ungeprüft | `UNKNOWN` | [G-CLK/G-BUF/G-AUD/G17-SOC](README.md#präregistrierte-lab-gates); Review: Lab erforderlich |
| `EVID-PCMNET-2026-10-13-013` | Reconnect→Mute, Alt-PCM-Verwurf und Unmute erst nach validiertem Framing + Prefill sind auf Zielhardware ungeprüft | `UNKNOWN` | [G-REC](README.md#präregistrierte-lab-gates); Review: Session-State atomar zurücksetzen |
| `EVID-PCMNET-2026-10-13-014` | GitHub meldet für `esp32-rtp` AGPL-3.0, am gepinnten Commit ist jedoch keine Root-Lizenzdatei abrufbar; die Reuse-Lizenz bleibt deshalb `UNKNOWN` | `FACT` | GitHub-Repositorymetadaten plus 404 für `LICENSE` am Pin; keine Codeübernahme bis Klärung |

## Epistemische Grenze

- Alle `FACT`-Zeilen sind **Desk-Fakten** über Code/Dokumentation am SHA.
- Es gibt keine `MEASURED`- oder Field-Evidence.
- Zahlen in den Quellen beschreiben Quellcode-/Protokollparameter, nicht
  gemessene Leistung dieser Kampagne.
- Neue Labdaten erhalten neue Evidence-IDs; `-012`/`-013` werden nicht still
  zu `MEASURED` umetikettiert.

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | Desk-Audit 0.7.1; SHAs fixiert; A/B/C und Lab-Gates präregistriert |
