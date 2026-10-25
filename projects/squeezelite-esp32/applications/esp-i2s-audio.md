# Project Application: esp-i2s-audio in squeezelite-esp32

```yaml
project_id: squeezelite-esp32
tech_slug: esp-i2s-audio
status: active
sheet: ../../../technologies/esp-i2s-audio/SHEET.md
audit: ../../../audits/squeezelite-esp32-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Primärer Lokal-Ausgang: I2S zu DAC/Codec (PCM5102, TAS57xx, AC101, ES8388, …); SPDIF über I2S-Controller-Reuse (BCK/WS/DO).

## Datenfluss

```text
Decode → I2S (bck/ws/do[/mck]) → DAC
       → or SPDIF (same I2S block, DO pin)
```

## Pfade / Config

| Item | Upstream |
|------|----------|
| NVS `dac_config` | model/bck/ws/do/mck/i2c… |
| NVS `spdif_config` | bck/ws/do; exclusive vs I2S DAC often |
| Built-in DAC models | TAS57xx, TAS5713, AC101, … |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| I2S DAC + SPDIF via I2S non-standard reuse | `EVID-SQZ-2026-10-25-004` | `FACT` |
| MCLK/GPIO0 vs Ethernet RMII conflict | `EVID-SQZ-2026-10-25-004` | `FACT` |
