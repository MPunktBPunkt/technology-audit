# Technology Sheet: ESP32 USB Host (OTG)

```yaml
slug: esp-usb-host
title: ESP32 USB Host (OTG)
primary: C
tags: [usb-host, esp-idf, fragile]
type: implementation
status: active
seen_in: [espusbhost, esp-iot-solution, esp32-usb-analyzer]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/espusbhost-2026-foreign
```

Nur Ebene **A**. Konkrete Geräte-VIDs, Board-VBUS-Quirks → Application C.  
**Chip-Scope:** USB Host/OTG auf **ESP32-S2 / ESP32-S3** (Full-Speed) und **ESP32-P4** (FS + HS). Classic ESP32 ohne OTG-Host = außerhalb.

## Kurzfassung

ESP als **USB-Host**: enumeriert Peripherie (HID, CDC/VCP, MSC BOT/SCSI, MIDI, Audio, Hub, CDC-NCM/ECM, CCID, Vendor-Bulk) über den On-Chip-USB-OTG-Controller. Events typisch in einer Background-Task; Sketches registrieren Callbacks statt zu pollen.

## Abgrenzung

- **Ist:** USB **Host**-Rolle (ESP steuert Bus, speist/enumerated Devices).
- **Ist nicht:** USB **Device**/Gadget (`usb-msc` als Stick gegenüber HU); TinyUSB Device-Pfade; PC-Host-Treiber.
- **Grenzt an:** MSC BOT/SCSI (Klasse gleich, Rolle umgekehrt); USB-Serial-Bridges als Host-Clients; Android Open Accessory Host-Handshake [`usb-aoa`](../usb-aoa/SHEET.md) (Vendor-Control 51/52/53 auf dem Host-Stack).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Klassen-APIs / Sketch-Callbacks | HID, CDC Stream, MSC fs::FS, … |
| unten | USB OTG Host Controller + IDF host stack | FS vs. HS (P4) |
| lateral | VBUS 5 V Versorgung | Board-abhängig — oft Gate |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| USB-MSC Sheet = Host kann Sticks lesen | `REJECTED` still | gleicher BOT/SCSI-Contract, **andere Rolle** → dieses Sheet + Application |
| S2/S3 hosten HS-only Devices | `REJECTED` | Host FS-only; braucht FS-Config am Device oder P4-HS |
| Jedes DevKit speist VBUS | `REJECTED` | z. B. Espressif S3-DevKitC-1 OTG oft ohne 5 V |
| Hub auf P4-HS „einfach“ | `REJECTED` / Gate | Upstream: HS-Port-Hubs praktisch unbrauchbar |
| Config-Descriptor &gt; Control-Transfer-Max | `FACT` Fallstrick | Arduino-prebuilt oft 256 B → große UVC scheitern |
| Library-API 1.x ≡ 2.x | `REJECTED` | Breaking redesign (Callbacks) |
| Host-`usb_stream` (UVC+UAC) = Device-UAC-Headset | `REJECTED` | Host-Stream ≠ Device-UAC (`esp-usb-audio-uac`) |

### Projektstart-Checkliste

- [ ] Chip S2/S3/P4? Classic ESP = Gate
- [ ] Host vs. Device-Rolle explizit (nicht `usb-msc` missbrauchen)
- [ ] VBUS-Versorgung der Board-Buchse geprüft
- [ ] Speed: FS vs. HS-only Device
- [ ] Application + `seen_in`; Geräte-Evidence = C

## Transfer

Relevant für Hub-Flash-Sticks, Lab-HID, USB-Ethernet, Instrumente — alles wo der ESP **Host** ist. PiDrive/`esp32-pidrive` MSC-Gadget bleibt Device-Seite.

## Referenzen

- [tanakamasayuki/EspUsbHost](https://github.com/tanakamasayuki/EspUsbHost) v2.x
- Espressif USB Host API / Arduino-ESP32 USB Host

## Offene Fragen

- Welche MSC-Sticks unter Hub-OTA-Last stabil sind?
- P4 HS FIFO-Split Defaults für Audio/UVC?
