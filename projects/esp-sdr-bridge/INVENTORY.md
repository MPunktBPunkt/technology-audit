# Project Inventory: esp-sdr-bridge (Fremd)

```yaml
project_id: esp-sdr-bridge
updated: 2026-10-12
reviewed_commit: "7da8aea"
profile: lab-tool
pilot_order: [esp32-undoc-iq-rx]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| S3 IQS FIR DDC → Host SDR | `esp32-undoc-iq-rx` | **reuse** (S3 continuous/IQS Zelle) |
| SpyServer / rtl_tcp servers | `esp32-undoc-iq-rx` | lateral Host-Backend (G7) |
| rtl-sdr USB dongle | `rtl-sdr` | **Abgrenzung** (anders Hardware) |

Kampagne: [`esp-sdr-bridge-2026-foreign`](../../audits/esp-sdr-bridge-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp32-undoc-iq-rx` | Undoc I/Q RX Dump | A | applied | partial | [SHEET](../../technologies/esp32-undoc-iq-rx/SHEET.md) | [app](applications/esp32-undoc-iq-rx.md) |
| `rtl-sdr` | RTL-SDR Host | A | documented | none | [SHEET](../../technologies/rtl-sdr/SHEET.md) | — (Kontrast Backend-API) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Eigene Soak/SNR | Desk | Lab gegen VSG |
| Firmware-Pin an Upstream esp-sdr | angrenzend | Commit der IQS-Firmware notieren |

## Signale ohne Eintrag

- `--fake` tone mode — Test-Hilfe
- PDF measurement report — Evidence-Quelle, kein Slug
