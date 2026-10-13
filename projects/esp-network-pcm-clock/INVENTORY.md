# Project Inventory: esp-network-pcm-clock (Fremdvergleich)

```yaml
project_id: esp-network-pcm-clock
updated: 2026-10-13
profile: lab-tool
pilot_order: [pdap, esp-i2s-audio]
```

**Reuse / Match:** Es werden ausschließlich die bestehenden Sheets `pdap` und
`esp-i2s-audio` wiederverwendet. Kein neues Technology Sheet und kein
Sheet-Delta in dieser Kampagne.

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| PCM + Framing + Sequenz/Control über WLAN | `pdap` | reuse + Application |
| I2S-/Audio-Sink-Contract | `esp-i2s-audio` | reuse + Application |
| RTP/UDP vs. proprietäres TCP-Framing | `pdap` | in Application strikt kontrastieren |
| Watermark-/Clock-Regelung | `pdap` | Implementierungsvariante, kein neuer Slug |

Kampagne:
[`esp-network-pcm-clock-2026-foreign`](../../audits/esp-network-pcm-clock-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `pdap` | PCM + Control over WiFi | J | `streaming` | applied | partial | [SHEET](../../technologies/pdap/SHEET.md) | [app](applications/pdap.md) |
| `esp-i2s-audio` | ESP I2S Audio Path | B | `streaming, esp-idf, arduino, fragile` | applied | partial | [SHEET](../../technologies/esp-i2s-audio/SHEET.md) | [app](applications/esp-i2s-audio.md) |

## Varianten-Coverage

| Variante | Desk-Abdeckung | Lab-Status |
|----------|----------------|------------|
| RTP/UDP | Framing/Sequenz, ESP32-S3-Receiverpuffer | `UNKNOWN` |
| TCP | `ELI1`-Records, Host-Puffer-/Sync-Kontraste | `UNKNOWN` |
| Elastic Buffer | vier Watermarks, Fill-Level→Speed, Events | `UNKNOWN` |

## Coverage-Lücken

| Bereich | Warum offen | Präregistrierter nächster Schritt |
|---------|-------------|-----------------------------------|
| End-to-end Clockdrift | Desk-only, verschiedene Clockdomänen | G-CLK |
| Under-/Overflow unter Störung | keine Messung | G-BUF |
| Reconnect → Mute → Prefill | keine Messung | G-REC |
| Audioqualität bei Rate-Control | keine Hör-/Signalmessung | G-AUD |
| SoC-/I2S-Transfer | S3 und Classic-Belege nicht austauschbar | G17-SOC |

## Signale ohne eigenen Eintrag

- Snapcast bleibt Zeit-/Multiroom-Kontrast, kein ESP-Projektnachweis.
- TCP-Streamer bleibt Host-Kontrast; dessen getrennte UDP-Module machen den
  TCP-Pfad nicht zu RTP.
- `esp_elastic_pcm_buffer` ist kein Transportprotokoll.
