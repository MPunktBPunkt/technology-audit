# Evidence — esp-iot-solution-2026-foreign

Desk 2026-10-13 · **standard_version 0.7.1** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/espressif/esp-iot-solution | `1d9a68a` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-IOTSOL-UAC-2026-10-13-001` | `usb_device_uac` Device UAC; Targets S2/S3/P4/S31/H4; TinyUSB | `FACT` | `components/usb/usb_device_uac/idf_component.yml`, README |
| `EVID-IOTSOL-UAC-2026-10-13-002` | Bis 8 SPK / 4 MIC Kanäle; Mute/Volume; Feedback-EP | `FACT` | `usb_device_uac/README.md` |
| `EVID-IOTSOL-UAC-2026-10-13-003` | Keine dynamische Sample-Rate; Win+Linux nicht gleichzeitig; macOS-Makro | `FACT` | `usb_device_uac/README.md` „Currently not supported“ |
| `EVID-IOTSOL-USBH-2026-10-13-001` | `usb_stream` Host UVC+UAC für S2/S3; ≤1 Cam + Mic + Spk | `FACT` | `components/usb/usb_stream/README.md`, idf_component.yml |
| `EVID-IOTSOL-MSC-2026-10-13-001` | Example Wireless Disk: MSC Device S2/S3 + WiFi File Server | `FACT` | `examples/usb/device/usb_msc_wireless_disk/README.md` |
| `EVID-IOTSOL-AUD-2026-10-13-001` | `pwm_audio` / `dac_audio` / `adc_mic` ohne I2S-Player-Contract | `FACT` | `components/audio/*/README.md` |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | Desk USB/Audio Fokus-Audit unter 0.7.1 |
