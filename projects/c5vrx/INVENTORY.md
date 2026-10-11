# Project Inventory: c5vrx (Fremd)

```yaml
project_id: c5vrx
updated: 2026-10-11
reviewed_commit: "C5VRX@6887fb3"
profile: lab-tool
pilot_order: [esp32-undoc-iq-rx]
```

**Reuse / Match:**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| C5 MODEM_DIAG I/Q continuous | `esp32-undoc-iq-rx` | **reuse** + Application |
| BitScrambler WBFM + R-DAC CVBS | `esp32-undoc-iq-rx` | Application-Tiefe (nicht neuer Slug) |
| ESPARGOS C5 burst/5 GHz | `esp32-undoc-iq-rx` | Geschwister-Kontrast |
| Classic APLL / polar TX | — | **Abgrenzung** |

Kampagne: [`c5vrx-2026-foreign`](../../audits/c5vrx-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp32-undoc-iq-rx` | Undoc I/Q RX Dump | A | applied | partial | [SHEET](../../technologies/esp32-undoc-iq-rx/SHEET.md) | [app](applications/esp32-undoc-iq-rx.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Range-edge / long session | Author offen | optional Lab |
| Andere C5-Boards als XIAO | unbelegt | Port-Check |

## Signale ohne Eintrag

- Discord/Web-Flasher — Ops, kein Tech-Slug
