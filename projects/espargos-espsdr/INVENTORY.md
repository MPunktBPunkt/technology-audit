# Project Inventory: espargos-espsdr (Fremd)

```yaml
project_id: espargos-espsdr
updated: 2026-10-11
reviewed_commit: "esp-sdr@e74f2a4 SoapyESPSDR@6f2cc72 CardputerADV-SDR@aa4737d"
profile: lab-tool
pilot_order: [esp32-undoc-iq-rx]
```

**Reuse / Match:**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Undoc I/Q dump multi-chip | `esp32-undoc-iq-rx` | **neu** (Pilot) |
| S3 IQS continuous | `esp32-undoc-iq-rx` | Matrix-Zelle |
| S31 USB/Eth stream + Soapy | `esp32-undoc-iq-rx` | Matrix + G7 |
| Cardputer on-device UI/audio | `esp32-undoc-iq-rx` | Port Application-Tiefe |
| C5 5 GHz band in table | `esp32-undoc-iq-rx` | Matrix; Detail → `c5vrx` |
| Polar / APLL TX | `esp32-polar-phy-tx` / `esp32-apll-fm-tx` | **Abgrenzung** |

Kampagne: [`espargos-espsdr-2026-foreign`](../../audits/espargos-espsdr-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp32-undoc-iq-rx` | Undoc I/Q RX Dump | A | applied | partial | [SHEET](../../technologies/esp32-undoc-iq-rx/SHEET.md) | [app](applications/esp32-undoc-iq-rx.md) |
| `esp32-polar-phy-tx` | S3 Polar PHY TX | D | documented | none | [SHEET](../../technologies/esp32-polar-phy-tx/SHEET.md) | — |
| `rtl-sdr` | RTL-SDR Host-Ökosystem | A | documented | none | [SHEET](../../technologies/rtl-sdr/SHEET.md) | — (Kontrast Dongle) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| S31 Signalqualität / DC-Peak | Upstream experimental | Lab oder Upstream-Track |
| Phase-kohärentes Array | Site/Array-Produkt | FOLLOW-ON |
| TX withheld | kein Public-Code | nicht spekulieren |

## Signale ohne Eintrag

- esp-web-sdr Browser-UI — Host-Schicht, kein eigener Slug
- H21/H4 preview — Matrix `UNKNOWN`
