# Project Inventory: esp32-audioi2s (Fremd)

```yaml
project_id: esp32-audioi2s
updated: 2026-10-13
reviewed_commit: "45db753"
profile: lab-tool
pilot_order: [esp-i2s-audio]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Decode → I2S DAC | `esp-i2s-audio` | **neu** |
| Browser-Webradio | `webradio-browser-host` | Abgrenzung |
| A2DP Source Example | `bluetooth-a2dp` | Kontrast / reuse Sheet |
| USB UAC | `esp-usb-audio-uac` | nicht in diesem Repo |

Kampagne: [`esp32-audioi2s-2026-foreign`](../../audits/esp32-audioi2s-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp-i2s-audio` | ESP I2S Audio Path | B | applied | partial | [SHEET](../../technologies/esp-i2s-audio/SHEET.md) | [app](applications/esp-i2s-audio.md) |
| `bluetooth-a2dp` | A2DP (Example Bridge) | C | observed | none | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | — (Kontrast Example) |
| `webradio-browser-host` | Browser-Radio | G | documented | none | [SHEET](../../technologies/webradio-browser-host/SHEET.md) | — (Abgrenzung) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| DAC-Hardware-Matrix | Desk | Lab MAX98357A/PCM5102 |
| Opus/FLAC Edge Cases | Library intern | bei Bedarf |
