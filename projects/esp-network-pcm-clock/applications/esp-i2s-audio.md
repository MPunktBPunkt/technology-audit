# Project Application: esp-i2s-audio in esp-network-pcm-clock

```yaml
project_id: esp-network-pcm-clock
tech_slug: esp-i2s-audio
status: active
sheet: ../../../technologies/esp-i2s-audio/SHEET.md
audit: ../../../audits/esp-network-pcm-clock-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W1
```

## Rolle im Projekt — Ebene B

I2S ist der lokale Sink-/Source-Clock-Contract hinter dem Netz- und
Pufferpfad. Die Application dokumentiert nur die Kopplung; sie behauptet keine
gemessene Clockstabilität.

```text
network record
  → transport-specific validation/reassembly
  → PCM frame queue / elastic policy
  → format gate
  → I2S TX clock domain
  → codec/DAC
```

## Quellrollen und relevante Pfade

| Repository @ SHA | Pfad | Rolle |
|------------------|------|-------|
| `pschatzmann/arduino-audio-tools@0ef1b154…` | `src/AudioTools.h`, I2S- und Stream-Klassen unter `src/` | Source/Sink-/`I2SStream`-Abstraktion |
| `shootao/esp_elastic_pcm_buffer@93fbda9f…` | `src/elastic_pcm_buffer.c`, `src/audio_speed_control.c` | PCM vor dem Sink puffern/anpassen |
| `netham45/esp32-rtp@04562157…` | `main/receiver/audio_out.c`; USB/S/PDIF-Sinks als Kontrast | Empfänger-Ausgabe, kein I2S-Labbeleg |

## Implementierungsclaims

| Claim | Status | Evidence |
|-------|--------|----------|
| Arduino Audio Tools modelliert Audio als Sources/Sinks und zeigt `I2SStream` mit Sample-Rate, Kanälen und Bits | `FACT` (Desk) | `EVID-PCMNET-2026-10-13-011` |
| Die Bibliotheksabstraktion beweist keine Drift-, Underflow- oder Reconnect-Eigenschaft des Zielboards | `FACT` (Scope-Folge) | `EVID-PCMNET-2026-10-13-011` |
| Der I2S-Sink darf erst nach Framing-/Formatprüfung und Prefill freigegeben werden | `HYPOTHESIS` / Design-Gate | `EVID-PCMNET-2026-10-13-013` |

## G17 — Chip-/SoC-Scope

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `esp32-rtp` nennt ESP32-S3 als Hardwareanforderung | `EVID-PCMNET-2026-10-13-002` | `FACT` |
| StreamLine nennt den offiziellen Ai-Thinker ESP32 Audio Kit v2.2 und ESP32 ECO3 | `EVID-PCMNET-2026-10-13-006` | `FACT` |
| Gleiches I2S-/Clockverhalten auf ESP32 classic und ESP32-S3 | `EVID-PCMNET-2026-10-13-012` | `UNKNOWN` |
| Zielboard-Pinout, DMA-Tiefe, APLL/Clockquelle und Codecverhalten | `EVID-PCMNET-2026-10-13-012` | `UNKNOWN` |

## Ebene C — Host-/Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| I2S-Ausgabe bleibt nach Netz-Reconnect bis zum vollständigen Prefill digital stumm | `EVID-PCMNET-2026-10-13-013` | `UNKNOWN` |
| Unter konstanter Quelle bleibt Pufferfüllung trotz unabhängiger Netz-/I2S-Clocks begrenzt | `EVID-PCMNET-2026-10-13-012` | `UNKNOWN` |
| Rate-Control erzeugt auf Zielcodec keine unzulässigen Artefakte | `EVID-PCMNET-2026-10-13-012` | `UNKNOWN` |

## Präregistrierte Review Checks

- Sample-Rate, Bits, Kanäle und Endianness vor I2S-Start gegen den
  Transport-Header prüfen.
- Parser-/Queue-/Sonic-Zustand bei Sessionwechsel nicht über Reconnect retten.
- Under-/Overflow und Mute als explizite Zustände, nicht nur Logzeilen.
- SoC, Board, I2S-Peripheral, Clockquelle und Codec im Labartefakt nennen.

## Offene Fragen

- Welcher SoC und welches Board sind Ziel der ersten G17-SOC-Ausführung?
- Wird Clockkorrektur im PCM (Time-Scale/Drop-Duplicate) oder in der
  Peripheral-Clock vorgenommen?
- Wie wird digitaler Mute am konkreten Codec verifiziert?
