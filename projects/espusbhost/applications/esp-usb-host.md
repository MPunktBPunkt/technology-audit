# Project Application: esp-usb-host in espusbhost

```yaml
project_id: espusbhost
tech_slug: esp-usb-host
status: active
sheet: ../../../technologies/esp-usb-host/SHEET.md
audit: ../../../audits/espusbhost-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Arduino-Library v2.x: Background FreeRTOS USB-Host-Task, Callback-API, Klassen HID/CDC/MSC/MIDI/Audio/Hub/NCM/CCID/Vendor. Primärziel S3; S2 RAM-enger; P4 + HS.

| Repo | Commit | Rolle |
|------|--------|-------|
| [tanakamasayuki/EspUsbHost](https://github.com/tanakamasayuki/EspUsbHost) | `6386f2a` | Library 2.10.0 |

## Architektur / Datenfluss

```text
USB Device(s)
  → OTG Host Controller (FS S2/S3; FS/HS P4)
  → IDF USB Host stack
  → EspUsbHost task + class APIs
  → Sketch callbacks / EspUsbHostCdcSerial / EspUsbHostMscFS
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `library.properties` / `src/espusbhost_version.h` | 2.10.0 |
| `src/EspUsbHost.h` | Core + MSC/CDC classes |
| `docs/usb-host-guide.md` / `advanced` | Limits power/speed/hubs |
| `docs/tested-devices.md` | Hardware matrix (C) |
| `examples/Storage/` | MSC Host + FatFs |

## Konfiguration (Desk)

| Parameter | Wert (Upstream) |
|-----------|-----------------|
| Min Arduino-ESP32 | S2/S3 ≥3.2.0; P4 ≥3.3.1 |
| Default max devices | 8 (S3), 3 (S2) |
| MSC | BOT/SCSI + `EspUsbHostMscFS` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Targets S2/S3/P4; version 2.10.0 | `EVID-USBH-2026-10-12-001` | `FACT` |
| Class matrix HID/CDC/MSC/… | `EVID-USBH-2026-10-12-002` | `FACT` |
| S2/S3 FS-only; HS-only devices fail | `EVID-USBH-2026-10-12-003` | `FACT` |
| DevKitC-1 OTG oft ohne VBUS 5 V | `EVID-USBH-2026-10-12-004` | `FACT` (tested-devices) |
| Control transfer max 256 B bricht große UVC | `EVID-USBH-2026-10-12-005` | `FACT` |
| Eigene Lab-Reproduktion | — | `UNKNOWN` |

## Offene Fragen

- MSC-Stick Performance für OTA-Images?
- Hub-Crash CH335F+DP100 — IDF vs. Library Boundary im eigenen Lab?
