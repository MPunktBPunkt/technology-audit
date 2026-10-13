# Project Scope: esp-iot-solution (Fremd)

```yaml
project_id: esp-iot-solution
title: Espressif IoT Solution — USB/Audio Fokus (Fremd)
updated: 2026-10-13
profile_hint: lab-tool
reviewed_commit: "1d9a68a"
repos:
  - https://github.com/espressif/esp-iot-solution
status: active
```

## Zweck

Offizielle Espressif-Komponentenbibliothek in die KB: **USB Device UAC**, **USB Host Stream (UVC+UAC)**, Abgrenzung zu Device-MSC und zu Community-Beispielen. Kein Vollinventar aller Sensor-/Display-Treiber.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `components/usb/usb_device_uac` | UAC Device | ja (Desk) |
| `components/usb/usb_stream` | Host UVC+UAC | ja (Desk) |
| `examples/usb/device/usb_uac` | UAC Demo | ja |
| `examples/usb/device/usb_msc_wireless_disk` | MSC Device | angrenzend (Kontrast) |
| `components/audio/*` | pwm/dac/adc_mic | observed / Kontrast zu I2S |
| Sensoren, Display, Motor, … | Katalogrest | **nein** (dieses Audit) |
| Lab-Messung Host-OS | — | FOLLOW-ON |

## Nicht-Ziele

- Jede Component als eigenes Sheet
- Claims für Classic-ESP32-USB-Device ohne Gate
- Feldversuche Headset/Camera

## Prioritäten

1. Sheet `esp-usb-audio-uac` + Application  
2. Sheet `esp-usb-host` wachsen (Host-Stream)  
3. Kontrast MSC / I2S / Community-UAC-Beispiel
