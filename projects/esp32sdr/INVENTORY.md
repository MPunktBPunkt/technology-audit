# Project Inventory: esp32sdr (Fremd)

```yaml
project_id: esp32sdr
updated: 2026-10-12
reviewed_commit: "dbff7bb"
profile: lab-tool
pilot_order: [esp32-wifi-tone-tx, esp32-undoc-iq-rx]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Burst capture / SRAM I/Q | `esp32-undoc-iq-rx` | **reuse** (S3 burst-Zelle) |
| Wi-Fi tone OOK/FSK TX | `esp32-wifi-tone-tx` | **neu** |
| DAC replay / raw I/Q TX | — | observed/`REJECTED` on S3 — kein Sheet |
| Polar PHY TX | `esp32-polar-phy-tx` | **Abgrenzung** |

Kampagne: [`esp32sdr-2026-foreign`](../../audits/esp32sdr-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp32-wifi-tone-tx` | Wi-Fi Tone Keying TX | D | applied | partial | [SHEET](../../technologies/esp32-wifi-tone-tx/SHEET.md) | [app](applications/esp32-wifi-tone-tx.md) |
| `esp32-undoc-iq-rx` | Undoc I/Q RX Dump | A | applied | partial | [SHEET](../../technologies/esp32-undoc-iq-rx/SHEET.md) | [app](applications/esp32-undoc-iq-rx.md) |
| `esp32-polar-phy-tx` | Polar PHY TX | D | documented | none | [SHEET](../../technologies/esp32-polar-phy-tx/SHEET.md) | — (Kontrast) |
| `esp32-raw-iq-tx` | Raw I/Q DAC TX | D | observed | none | — | — (`REJECTED` S3) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Eigene BER/Spurs | Desk | Lab + Evidence |
| Tone auf Nicht-S3 | unbelegt | Gate |

## Signale ohne Eintrag

- ST7735 on-device display — UI, kein RF-Slug
- Host Flask GUI — Application-Nebenpfad
