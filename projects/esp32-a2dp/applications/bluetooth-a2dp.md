# Project Application: bluetooth-a2dp in esp32-a2dp

```yaml
project_id: esp32-a2dp
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/esp32-a2dp-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

Arduino/IDF-Library: **A2DP Sink** (PCM aus SBC → I2S/AudioTools/Callback) und **A2DP Source** (PCM/Callback → SBC → Peer-Sink). Stack = Espressif **Bluedroid** Classic.

| Repo | Commit | Rolle |
|------|--------|-------|
| [pschatzmann/ESP32-A2DP](https://github.com/pschatzmann/ESP32-A2DP) | `a9e946a` | Library + Examples |

## Architektur / Datenfluss

```text
Sink:  Phone/Source ──A2DP/SBC──▶ ESP Bluedroid ──PCM──▶ I2S / AudioTools / stream_reader
Source: PCM callback/Stream ──SBC──▶ ESP Bluedroid ──A2DP──▶ Speaker/HU Sink
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/config.h` | Chip-Gate `IS_VALID_PLATFORM` (ESP32, ESP32-S31); Legacy-I2S; Managed Codec Gates |
| `src/BluetoothA2DPSink.h` / `.cpp` | Sink + Decode-Pfad |
| `src/BluetoothA2DPSource.h` / `.cpp` | Source + Encode-Pfad |
| `src/BluetoothA2DPSinkQueued.*` | Ringbuffer/I2S-Task gegen Jitter |
| `examples/bt_music_receiver*` | Sink-Varianten |
| `examples/bt_music_sender*` | Source-Varianten |

## Konfiguration (Desk)

| Parameter | Wert (Upstream) |
|-----------|-----------------|
| Chip-Scope Compile | `CONFIG_IDF_TARGET_ESP32` oder `ESP32S31`; sonst `#error` / stub |
| Default PCM Source | 44.1 kHz, S16, Stereo (SBC) |
| Output | AudioTools empfohlen ab Arduino-ESP32 v3 / IDF v5; Legacy I2S nur IDF &lt; 5 |
| Managed AAC/SBC SEP | IDF ≥5.5 (+ AAC runtime oft ≥6.1) |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Compile-Gate nur Classic ESP32 (+ S31 Flag) | `EVID-A2DP-LIB-2026-10-12-001` | `FACT` |
| Sink und Source als getrennte Klassen | `EVID-A2DP-LIB-2026-10-12-002` | `FACT` |
| HFP/HSP nicht supported | `EVID-A2DP-LIB-2026-10-12-003` | `FACT` (README) |
| NBT-Evo hörbar stabil | — | `UNKNOWN` |

## Abweichungen

- PiDrive Evidence bleibt BlueZ/PipeWire — hier Bluedroid; gleicher Slug, getrennte Applications.
- Gateway plant **Source**; die meisten Library-Beispiele sind **Sink**-lastig.

## Offene Fragen

- Dual-Role Sink+Source auf einem Classic-ESP unter Gateway-Last?
- S31-Flag: echte Classic-Controller-Caps vs. Compile-Vorbereitung?
