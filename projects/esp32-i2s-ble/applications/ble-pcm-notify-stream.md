# Project Application: ble-pcm-notify-stream in esp32-i2s-ble

```yaml
project_id: esp32-i2s-ble
tech_slug: ble-pcm-notify-stream
status: active
sheet: ../../../technologies/ble-pcm-notify-stream/SHEET.md
audit: ../../../audits/esp32-i2s-ble-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle

Custom NimBLE Service streamt downsampled PCM16 an iPhone; Control Char START/STOP; Ringbuffer entkoppelt Capture von Notify-Rate.

| Repo | Commit | Rolle |
|------|--------|-------|
| [iancarscadden/esp32-i2s-BLE](https://github.com/iancarscadden/esp32-i2s-BLE) | `4d053c4` | Firmware |

## Architektur / Datenfluss

```text
I2S Capture 16 kHz
  → convert 32→16 bit + downsample 2:1 → 8 kHz PCM
  → Ring (~6 s @ 8 kHz)
  → BLE Notify batches (120 samples / ~15 ms)
  → iPhone GATT Client
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/main.cpp` | UUIDs, Ring, Notify, MTU 247 |
| `platformio.ini` | NimBLE-Arduino, Feather S3 |
| `README.md` | Protokollbeschreibung (teils 16 kHz Wire — siehe Gate) |

## Konfiguration (Desk)

| Parameter | Wert (Code `4d053c4`) |
|-----------|------------------------|
| Capture | 16 000 Hz I2S |
| Wire/Output | **8 000 Hz** (Downsample) |
| Notify | 120 samples, ~15 ms |
| MTU | 247 |
| Device name | `ESP32S3-Audio` |
| Service UUID | `3c3b0001-8c5a-4b78-9c3a-1d5a6db3a001` |

Packet: seq u16 LE · count u16 LE · int16 samples LE.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Custom GATT PCM Notify + START/STOP | `EVID-I2SBLE-2026-10-13-001` | `FACT` |
| Capture 16 kHz → Wire 8 kHz Downsample | `EVID-I2SBLE-2026-10-13-002` | `FACT` |
| Ringbatching gegen iPhone Drops (Upstream-Claim) | `EVID-I2SBLE-2026-10-13-003` | `FACT` (Dokumentation; Lab `UNKNOWN`) |
| ≡ LE Audio oder A2DP | — | `REJECTED` |
| Eigene iOS Packet-Loss Messung | — | `UNKNOWN` |

## Abweichungen README vs. Code

README-Abschnitte sprechen teils von „16 kHz PCM over BLE“; Code/`4d053c4` Message: Capture 16 kHz, **Output 8 kHz**. Wire-Rate = Code.

## Offene Fragen

- Max. sinnvolle Dauer ohne Overflow bei typischem iOS Scheduling?
