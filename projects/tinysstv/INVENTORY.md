# Project Inventory: tinysstv (Fremd)

```yaml
project_id: tinysstv
updated: 2026-10-25
reviewed_commit: "b9977a62d45dbd459d6bbec6e971383e721ddcf4"
profile: lab-tool
pilot_order: [sstv-martin-m1, esp32-apll-fm-tx, rpi-gpio-fm-tx]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Martin M1 SSTV tone sequence, DDS 40 kHz, PDM GPIO | `sstv-martin-m1` | **neu** + App |
| Classic ESP32 APLL UKW-Träger | `esp32-apll-fm-tx` | **Kontrast** — RF ≠ AF |
| Pi GPIO/Clock FM | `rpi-gpio-fm-tx` | **Kontrast** |
| Captive portal / open AP | — | observed |
| microSD BMP stream | — | observed (App) |
| PTT drive | — | gap (not implemented) |

Kampagne: [`tinysstv-2026-foreign`](../../audits/tinysstv-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `sstv-martin-m1` | Martin M1 SSTV TX (AF) | A | applied | partial | [SHEET](../../technologies/sstv-martin-m1/SHEET.md) | [app](applications/sstv-martin-m1.md) |
| `esp32-apll-fm-tx` | ESP32 APLL FM TX | D | observed | none | [SHEET](../../technologies/esp32-apll-fm-tx/SHEET.md) | — (Kontrast) |
| `rpi-gpio-fm-tx` | Pi GPIO FM TX | D | observed | none | [SHEET](../../technologies/rpi-gpio-fm-tx/SHEET.md) | — (Kontrast) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| PTT-Automatiк | Upstream reserved | FOLLOW-ON |
| Andere SSTV-Modes | nur Martin M1 | defer |
| Cardputer-Variante | anderes Repo | optional Bootstrap |

## Signale ohne Eintrag

- Open AP ohne Passwort — Ops/Security Hinweis in App, kein Slug
