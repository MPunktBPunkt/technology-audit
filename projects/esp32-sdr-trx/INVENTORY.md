# Project Inventory: esp32-sdr-trx (Fremd)

```yaml
project_id: esp32-sdr-trx
updated: 2026-10-11
reviewed_commit: "esp32-sdr-trx@e1aebbf eSpDR@f279bf8"
profile: lab-tool
pilot_order: [esp32-polar-phy-tx, esp32-undoc-iq-rx]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| S3 polar PHY test-tone FM/SSB/RTTY | `esp32-polar-phy-tx` | **neu** |
| S3 undoc dump → CIC/FIR → rtl_tcp | `esp32-undoc-iq-rx` | **reuse** (Matrix-Zelle S3 narrowband) |
| FPGA 80 Msps (h0m3us3r) | `esp32-undoc-iq-rx` | Provenance / High-rate-Zelle |
| Classic APLL UKW | `esp32-apll-fm-tx` | **Abgrenzung** |
| Raw I/Q TX research | — | observed (`esp32-raw-iq-tx`) — kein Sheet (G19) |

Kampagne: [`esp32-sdr-trx-2026-foreign`](../../audits/esp32-sdr-trx-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp32-polar-phy-tx` | S3 Polar PHY TX | D | applied | partial | [SHEET](../../technologies/esp32-polar-phy-tx/SHEET.md) | [app](applications/esp32-polar-phy-tx.md) |
| `esp32-undoc-iq-rx` | Undoc I/Q RX Dump | A | applied | partial | [SHEET](../../technologies/esp32-undoc-iq-rx/SHEET.md) | [app](applications/esp32-undoc-iq-rx.md) |
| `esp32-apll-fm-tx` | Classic APLL FM | D | documented | none | [SHEET](../../technologies/esp32-apll-fm-tx/SHEET.md) | — (Kontrast) |
| `esp32-raw-iq-tx` | Raw I/Q SRAM TX | D | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Eigene Spurs/Power-Messung | Desk only | Lab + Evidence-IDs |
| Thermal-Modell fremdes Board | author 2 boards | revalidate |
| C5/S31 polar-TX | unbelegt | Gate / nicht still übertragen |

## Signale ohne Eintrag

- M17 feature-branch — Protokoll-Nebenpfad, nicht inventarisiert
- Claude-as-coding-assistant — Prozessrisiko, kein Tech-Slug
