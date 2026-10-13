# Project Application: esp-usb-host in esp-iot-solution

```yaml
project_id: esp-iot-solution
tech_slug: esp-usb-host
status: active
sheet: ../../../technologies/esp-usb-host/SHEET.md
audit: ../../../audits/esp-iot-solution-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Offizielle Host-Stream-Component `usb_stream`: gleichzeitig UVC (Video) + UAC Mic + UAC Speaker von USB-Peripherie am ESP-Host (S2/S3).

| Repo | Commit | Rolle |
|------|--------|-------|
| [espressif/esp-iot-solution](https://github.com/espressif/esp-iot-solution) | `1d9a68a` | `usb_stream` 1.5.2 |

## Architektur / Datenfluss

```text
USB Camera / Headset (Device)
  → ESP OTG Host (FS S2/S3)
  → usb_stream (UVC + UAC)
  → App: Display / WiFi / Player Examples
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `components/usb/usb_stream/` | Host UVC+UAC Driver |
| `components/usb/usb_stream/idf_component.yml` | Targets S2/S3; IDF 4.4.1–5.5 |
| `examples/usb/host/usb_camera_mic_spk/` | Combined Example |
| `examples/usb/host/usb_audio_player/` | UAC Host Player |

## Konfiguration (Desk)

| Parameter | Wert (Upstream) |
|-----------|-----------------|
| Targets | esp32s2, esp32s3 |
| UVC modes | isochronous + bulk |
| Parallel streams | ≤1 UVC + 1 Mic + 1 Spk (README) |
| IDF ≥5.3.3 + UVC | Bias IN FIFO Hinweis |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| usb_stream = Host UVC+UAC für S2/S3 | `EVID-IOTSOL-USBH-2026-10-13-001` | `FACT` |
| Device-UAC Sheet deckt Host-Stream ab | — | `REJECTED` (Rollen) |
| Eigene Camera/Headset Labmatrix | — | `UNKNOWN` |

## Offene Fragen

- FIFO-Bias Defaults vs. EspUsbHost Arduino-Limits?
