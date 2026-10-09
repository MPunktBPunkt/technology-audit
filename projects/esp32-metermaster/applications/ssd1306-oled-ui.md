# Project Application: ssd1306-oled-ui in esp32.MeterMaster

```yaml
project_id: esp32-metermaster
tech_slug: ssd1306-oled-ui
status: active
sheet: ../../../technologies/ssd1306-oled-ui/SHEET.md
audit: ../../../audits/esp32-metermaster-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

64×48 SSD1306 (EastRising-Konstruktor), 4 Stile, Carousel bis 5 Zähler, Alarm-Darstellung; Config über Web/Adapter.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp32.MeterMaster.ino` | U8g2, `oledValue`, styles |
| `docs/hardware/*.jpg` | Referenzaufbau |
| `docs/CODING-RULES.md` | Zeichenbudget |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| EastRising 64×48 Konstruktor | `EVID-OLED-2026-10-09-001` | `FACT` |
| 4 OLED-Stile + Carousel | `EVID-OLED-2026-10-09-002` | `FACT` |
