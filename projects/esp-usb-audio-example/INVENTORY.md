# Project Inventory: esp-usb-audio-example (Fremd)

```yaml
project_id: esp-usb-audio-example
updated: 2026-10-13
reviewed_commit: "662f2c0"
profile: lab-tool
pilot_order: [esp-usb-audio-uac, esp-i2s-audio]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| TinyUSB UAC Headset | `esp-usb-audio-uac` | reuse + App |
| I2S ↔ ES8311/ES7210 | `esp-i2s-audio` | reuse + App |
| USB Host | `esp-usb-host` | Abgrenzung |

Kampagne: [`esp-usb-audio-example-2026-foreign`](../../audits/esp-usb-audio-example-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp-usb-audio-uac` | USB UAC Device | C | applied | partial | [SHEET](../../technologies/esp-usb-audio-uac/SHEET.md) | [app](applications/esp-usb-audio-uac.md) |
| `esp-i2s-audio` | I2S Audio Path | B | applied | partial | [SHEET](../../technologies/esp-i2s-audio/SHEET.md) | [app](applications/esp-i2s-audio.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Host-OS Enumeration | Desk | Lab macOS/Win |
| espp Submodule API | nicht geklont | optional |
