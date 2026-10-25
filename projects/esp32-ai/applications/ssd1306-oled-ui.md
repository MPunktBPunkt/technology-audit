# Project Application: ssd1306-oled-ui in esp32-ai

```yaml
project_id: esp32-ai
tech_slug: ssd1306-oled-ui
status: active
sheet: ../../../technologies/ssd1306-oled-ui/SHEET.md
audit: ../../../audits/esp32-ai-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

Optionales 128×64 I²C-OLED für Token-/Wort-Stream (LLM) und Spider-Escape-UI (Fly). Default-Controller **SH1106**; SSD1306 per Compile-Flag. Probe einmal am Boot — fehlendes Panel = Serial weiter, Draws no-op.

## Architektur / Datenfluss

```text
Inference / Escape world
  → display.h / escape_ui.h
  → Wire I²C SDA=GPIO18 SCL=GPIO46
  → SH1106G oder SSD1306 @ 0x3C (Fallback 0x3D bei Fly)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/esp32_barista/display.h` | Dual SH1106/SSD1306 + scroll grid |
| `firmware/esp32_tinystories/display.h` | analog |
| `firmware/esp32_fly/escape_ui.h` | Escape UI |

## Konfiguration und Parameter

| Parameter | Upstream | Status |
|-----------|----------|--------|
| Geometrie | 128×64 mono | `FACT` |
| Default controller | SH1106 (`OLED_CONTROLLER`) | `FACT` |
| Pins | SDA 18, SCL 46 | `FACT` |
| Absent panel | single probe, then no-op draws | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Optional OLED; Serial immer | `EVID-ESP32AI-2026-10-25-009` | `FACT` |
| SH1106 default; SSD1306 compile-time | `EVID-ESP32AI-2026-10-25-009` | `FACT` |
| Lab Panel-Varianten | — | `UNKNOWN` |

## Abweichungen vom Sheet-Titel

Sheet heißt SSD1306; dieses Projekt defaultet SH1106 — passt zur bestehenden Fallstrick-Zeile „Controller/Geometrie-Varianten“.

## Offene Fragen

- Adafruit SH110X vs. SSD1306 Init-Unterschiede auf N16R8 Devkits?
