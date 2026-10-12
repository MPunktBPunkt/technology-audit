# Project Inventory: espusbhost (Fremd)

```yaml
project_id: espusbhost
updated: 2026-10-12
reviewed_commit: "6386f2a"
profile: lab-tool
pilot_order: [esp-usb-host]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| USB Host OTG S2/S3/P4 | `esp-usb-host` | **neu** |
| MSC BOT/SCSI als Host | `esp-usb-host` (+ lateral `usb-msc` Abgrenzung) | reuse Klasse / neue Rolle |
| USB Device Gadget | `usb-msc` | **Abgrenzung** |

Kampagne: [`espusbhost-2026-foreign`](../../audits/espusbhost-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp-usb-host` | ESP32 USB Host | C | applied | partial | [SHEET](../../technologies/esp-usb-host/SHEET.md) | [app](applications/esp-usb-host.md) |
| `usb-msc` | USB MSC (Device) | C | documented | none | [SHEET](../../technologies/usb-msc/SHEET.md) | — (Kontrast) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Eigene Stick-/HID-Lab | Desk | peer tests nachziehen |
| EspUsbDevice | nicht inventarisiert | optional Folgeaudit |

## Signale ohne Eintrag

- DisplayLink / USBTMC / ESC-POS Examples — vendor sketches, observed
- UVC Core-Limit 256 B — im Sheet als Fallstrick, kein Video-Slug
