# Project Inventory: esp32-i2s-ble (Fremd)

```yaml
project_id: esp32-i2s-ble
updated: 2026-10-13
reviewed_commit: "4d053c4"
profile: lab-tool
pilot_order: [ble-pcm-notify-stream, esp-i2s-audio]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Custom GATT PCM Notify + Ringbuffer | `ble-pcm-notify-stream` | **neu** |
| I2S MEMS Capture SPH0645 | `esp-i2s-audio` | reuse + App |
| A2DP / LE Audio | `bluetooth-a2dp` | **Abgrenzung** (kein Match) |
| BLE-HR GATT | `ble-hrm-gatt` | kein Match (anderes Service) |

Kampagne: [`esp32-i2s-ble-2026-foreign`](../../audits/esp32-i2s-ble-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `ble-pcm-notify-stream` | BLE PCM Notify | C | applied | partial | [SHEET](../../technologies/ble-pcm-notify-stream/SHEET.md) | [app](applications/ble-pcm-notify-stream.md) |
| `esp-i2s-audio` | I2S Audio Path | B | applied | partial | [SHEET](../../technologies/esp-i2s-audio/SHEET.md) | [app](applications/esp-i2s-audio.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| iOS Packet-Loss Lab | Desk | Method + Trace |
| Opus statt PCM | nicht im Repo | optional |
