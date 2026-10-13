# Project Application: esp-usb-audio-uac in esp-iot-solution

```yaml
project_id: esp-iot-solution
tech_slug: esp-usb-audio-uac
status: active
sheet: ../../../technologies/esp-usb-audio-uac/SHEET.md
audit: ../../../audits/esp-iot-solution-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Offizielle Component `usb_device_uac` + Example `examples/usb/device/usb_uac`: ESP als UAC-Gerät (Mic + Speaker, Mute/Volume) gegenüber Host-PC.

| Repo | Commit | Rolle |
|------|--------|-------|
| [espressif/esp-iot-solution](https://github.com/espressif/esp-iot-solution) | `1d9a68a` | Component 1.3.2 + Example |

## Architektur / Datenfluss

```text
Host OS Audio
  ↔ USB Device (TinyUSB UAC)
  ↔ uac_device_* callbacks (input/output/mute/volume)
  ↔ Board Codec / I2S (Example: LCD-EV-Board / P4 EV)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `components/usb/usb_device_uac/` | Driver + `uac_device_init` |
| `components/usb/usb_device_uac/idf_component.yml` | Targets S2/S3/P4/S31/H4; tinyusb ^0.19 |
| `components/usb/usb_device_uac/README.md` | Features / Nicht-Features |
| `examples/usb/device/usb_uac/` | Demo Mic+Spk |

## Konfiguration (Desk)

| Parameter | Wert (Upstream) |
|-----------|-----------------|
| Targets | esp32s2, s3, p4, s31, h4 |
| IDF | ≥ 5.0 |
| Channels | Kconfig SPK/MIC (Example: bis 2 Mic) |
| Sample rate | Kconfig; **keine** dynamische Umschaltung |
| macOS | Extra-Makro `UAC_SUPPORT_MACOS` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Component beschreibt UAC Device S2/S3/P4 | `EVID-IOTSOL-UAC-2026-10-13-001` | `FACT` |
| Max 8 SPK / 4 MIC Kanäle (Component README) | `EVID-IOTSOL-UAC-2026-10-13-002` | `FACT` |
| Keine dynamische Sample-Rate; Win+Linux nicht gleichzeitig | `EVID-IOTSOL-UAC-2026-10-13-003` | `FACT` |
| Eigene Host-OS Lab-Reproduktion | — | `UNKNOWN` |

## Offene Fragen

- Feedback-EP Stabilität unter Dauerlast?
- Kontrast zu finger563 Box-Headset-Example?
