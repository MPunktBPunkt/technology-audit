# Evidence — esp-usb-audio-example-2026-foreign

Desk 2026-10-13 · **standard_version 0.7.1** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/finger563/esp-usb-audio-example | `662f2c0` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBAUD-EX-2026-10-13-001` | S3-BOX/BOX-3 als USB audio headset | `FACT` | README |
| `EVID-USBAUD-EX-2026-10-13-002` | Target esp32s3; TinyUSB Device only S2/S3 Kommentar | `FACT` | sdkconfig.defaults |
| `EVID-USBAUD-EX-2026-10-13-003` | UAC TinyUSB CFG; default 48 kHz; Mic/Spk buffers | `FACT` | tusb_config.h, usb_audio.cpp |
| `EVID-USBAUD-EX-2026-10-13-004` | I2S STD + ES8311/ES7210 Codec-Pfad | `FACT` | i2s_audio.cpp, components/codec |
| `EVID-USBAUD-EX-2026-10-13-005` | IDF ≥5.3; tinyusb ^0.15 dependency | `FACT` | main/idf_component.yml |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | Desk Community-UAC Audit 0.7.1 |
