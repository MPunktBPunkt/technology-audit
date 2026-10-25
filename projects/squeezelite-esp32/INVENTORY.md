# Project Inventory: squeezelite-esp32 (Fremd)

```yaml
project_id: squeezelite-esp32
updated: 2026-10-25
reviewed_commit: "ee1720c7556ffec5f43329aadd47c20546bdbb79"
profile: lab-tool
pilot_order: [lms-squeezelite, esp-i2s-audio, esp-psram-heavy-port, bluetooth-a2dp, webradio-browser-host]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| LMS/Squeezelite player, multi-room sync | `lms-squeezelite` | **neu** + App |
| I2S DAC / SPDIF (I2S-reuse) | `esp-i2s-audio` | **reuse** + App |
| 4 MB PSRAM Pflicht, 240 MHz heavy decode | `esp-psram-heavy-port` | **reuse** + App |
| BT from phone / to speaker | `bluetooth-a2dp` | **reuse** + App (Rollen) |
| Browser plays audio on phone | `webradio-browser-host` | **Kontrast** |
| AirPlay 1 / Spotify Connect | — | observed |
| Displays SSD1306/… | `ssd1306-oled-ui` | partial / observed |

Kampagne: [`squeezelite-esp32-2026-foreign`](../../audits/squeezelite-esp32-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `lms-squeezelite` | LMS / Squeezelite Player | F | applied | partial | [SHEET](../../technologies/lms-squeezelite/SHEET.md) | [app](applications/lms-squeezelite.md) |
| `esp-i2s-audio` | ESP I2S Audio Path | B | applied | partial | [SHEET](../../technologies/esp-i2s-audio/SHEET.md) | [app](applications/esp-i2s-audio.md) |
| `esp-psram-heavy-port` | ESP PSRAM Heavy Port | D | applied | partial | [SHEET](../../technologies/esp-psram-heavy-port/SHEET.md) | [app](applications/esp-psram-heavy-port.md) |
| `bluetooth-a2dp` | Bluetooth A2DP | C | applied | partial | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | [app](applications/bluetooth-a2dp.md) |
| `webradio-browser-host` | Web-Radio Browser Host | G | observed | none | [SHEET](../../technologies/webradio-browser-host/SHEET.md) | — (Kontrast) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Multi-room Sync Lab | Desk | FOLLOW-ON |
| AirPlay/Spotify Sheets | Add-ons | observed bis Bedarf |
| S3 official release lag | README | Chip-Gate |

## Signale ohne Eintrag

- Ethernet RMII/SPI — Hardware-Option
- LED VU strip — UI sugar
