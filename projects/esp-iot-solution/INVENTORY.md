# Project Inventory: esp-iot-solution (Fremd)

```yaml
project_id: esp-iot-solution
updated: 2026-10-13
reviewed_commit: "1d9a68a"
profile: lab-tool
pilot_order: [esp-usb-audio-uac, esp-usb-host]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| USB Device UAC TinyUSB | `esp-usb-audio-uac` | **neu** |
| USB Host UVC+UAC (`usb_stream`) | `esp-usb-host` | **wachsen** |
| USB MSC Wireless Disk | `usb-msc` | Abgrenzung / observed |
| pwm_audio / dac_audio / adc_mic | — | observed (kein I2S-Player-Slug) |
| BLE profiles in tree | bestehende BLE-Sheets | **nicht** vertieft |

Kampagne: [`esp-iot-solution-2026-foreign`](../../audits/esp-iot-solution-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp-usb-audio-uac` | USB UAC Device | C | applied | partial | [SHEET](../../technologies/esp-usb-audio-uac/SHEET.md) | [app](applications/esp-usb-audio-uac.md) |
| `esp-usb-host` | USB Host OTG | C | applied | partial | [SHEET](../../technologies/esp-usb-host/SHEET.md) | [app](applications/esp-usb-host.md) |
| `usb-msc` | USB MSC Device | C | documented | none | [SHEET](../../technologies/usb-msc/SHEET.md) | — (Kontrast) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Host-OS UAC Matrix | Desk only | Lab Windows/macOS/Linux |
| usb_stream Camera+Audio | Example gesehen | eigene Application bei Bedarf |
| Vollkatalog Sensors | out of scope | Folgeaudit |

## Signale ohne Eintrag

- `esp_tinyuf2`, RNDIS/ECM/CDC Host-Modem — observed
- `bluetooth/ble_*` — vorhanden, nicht inventarisiert in diesem Lauf
