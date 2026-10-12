# Project Scope: espusbhost (Fremd)

```yaml
project_id: espusbhost
title: EspUsbHost — ESP32 USB Host Library (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "6386f2a"
repos:
  - https://github.com/tanakamasayuki/EspUsbHost
status: active
```

## Zweck

USB-**Host**-Contract für S2/S3/P4 in die KB: Klassenmatrix, Speed/VBUS/Hub-Gates, klare Abgrenzung zu Device-MSC (`usb-msc`).

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| EspUsbHost v2.10.0 | Arduino USB Host library | ja (Desk) |
| EspUsbDevice sibling | Device-Seite / Loopback | angrenzend (nicht vertieft) |
| Classic ESP32 Host | — | **nein** |
| Eigene Geräte-Labmatrix | — | FOLLOW-ON |

## Nicht-Ziele

- Device-Gadget-Claims in dieses Sheet mischen
- Jede getestete VID als A-FACT ohne Application

## Prioritäten

1. Neues Sheet `esp-usb-host`  
2. Kontrast `usb-msc` (Device)  
3. Chip/Speed/VBUS-Fallstricke
