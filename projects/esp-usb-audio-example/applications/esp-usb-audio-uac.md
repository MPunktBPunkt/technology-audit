# Project Application: esp-usb-audio-uac in esp-usb-audio-example

```yaml
project_id: esp-usb-audio-example
tech_slug: esp-usb-audio-uac
status: active
sheet: ../../../technologies/esp-usb-audio-uac/SHEET.md
audit: ../../../audits/esp-usb-audio-example-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

ESP32-S3-BOX / BOX-3 erscheint dem Host als USB-Audio-Headset (Mic+Speaker) via TinyUSB Audio Class; Soft-Buffers koppeln an I2S-Codecs.

| Repo | Commit | Rolle |
|------|--------|-------|
| [finger563/esp-usb-audio-example](https://github.com/finger563/esp-usb-audio-example) | `662f2c0` | Example Firmware |

## Architektur / Datenfluss

```text
Host PC
  ↔ TinyUSB UAC (CFG_TUD_AUDIO, Isochronous)
  ↔ usb_audio.cpp callbacks / buffers
  ↔ i2s_audio (ES8311 TX / ES7210 RX)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `main/usb_audio.cpp` | UAC callbacks, 48 kHz default |
| `main/tusb_config.h` | Headset Stereo Desc, Formats 16/8 bit |
| `main/sdkconfig.defaults` | `CONFIG_IDF_TARGET="esp32s3"` |
| `main/idf_component.yml` | tinyusb ^0.15; IDF ≥5.3 |

## Konfiguration (Desk)

| Parameter | Wert (Upstream) |
|-----------|-----------------|
| Target | ESP32-S3 only (defaults) |
| Sample rate | 48000 (`AUDIO_SAMPLE_RATE`) |
| Channels | TX Mic 1 / RX Spk 1 (CFG) |
| FreeRTOS tick | 1000 Hz |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| README: S3-BOX/BOX-3 USB audio headset | `EVID-USBAUD-EX-2026-10-13-001` | `FACT` |
| sdkconfig erzwingt esp32s3 (TinyUSB Device) | `EVID-USBAUD-EX-2026-10-13-002` | `FACT` |
| TinyUSB Audio CFG + 48 kHz | `EVID-USBAUD-EX-2026-10-13-003` | `FACT` |
| Host-OS Lab | — | `UNKNOWN` |

## Offene Fragen

- Descriptor vs. Espressif `usb_device_uac` — welche Hosts bevorzugen welchen Pfad?
