# Project Inventory: esp32-doom (Fremd)

```yaml
project_id: esp32-doom
updated: 2026-10-25
reviewed_commit: "085f21b630f11adb69a3894db5a1efa39a7aa31a"
profile: lab-tool
pilot_order: [esp-psram-heavy-port, esp32-s3-silicon, ssd1306-oled-ui]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| PrBoom Port; SPIRAM malloc; 240 MHz; SPI LCD FB | `esp-psram-heavy-port` | **neu** + App |
| Classic ESP32 + 4 MiB PSRAM (Wrover) | `esp-psram-heavy-port` | Chip-Scope im Sheet |
| S3 Errata / Octal-PSRAM | `esp32-s3-silicon` | **Kontrast** — anderes Silicon |
| Tiny OLED Status-UI | `ssd1306-oled-ui` | **Kontrast** — ≠ Game-FB |
| WAD flash partition + mmap | `esp-psram-heavy-port` | Asset-Partition-Muster |
| Sound / Music | — | unsupported (README) |
| Dual-Core Game Loop | — | Task pinned Core 0; observed |

Kampagne: [`esp32-doom-2026-foreign`](../../audits/esp32-doom-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp-psram-heavy-port` | ESP PSRAM Heavy Port | D | applied | partial | [SHEET](../../technologies/esp-psram-heavy-port/SHEET.md) | [app](applications/esp-psram-heavy-port.md) |
| `esp32-s3-silicon` | ESP32-S3 Silicon | D | observed | none | [SHEET](../../technologies/esp32-s3-silicon/SHEET.md) | — (Kontrast) |
| `ssd1306-oled-ui` | SSD1306 OLED UI | G | observed | none | [SHEET](../../technologies/ssd1306-oled-ui/SHEET.md) | — (Kontrast) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| FPS / Heap-Profil gemessen | Desk PoC 2017 | Lab auf Wrover (optional) |
| S3-Remount des Ports | nicht Upstream | Gate / anderes Repo |
| Audio | unsupported | defer |

## Signale ohne Eintrag

- PSX Controller Bitbang — Input-HAL, kein Slug
- Menü-Crash (fehlende PrBoom-Data) — PoC-Bug, kein Sheet
