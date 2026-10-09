# Project Application: esp-lab-bus-tools in esp32.io-control

```yaml
project_id: esp32-io-control
tech_slug: esp-lab-bus-tools
status: active
sheet: ../../../technologies/esp-lab-bus-tools/SHEET.md
audit: ../../../audits/esp32-io-control-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

**Einzweck**-Lab: SVG-Pinout, GPIO-Tabelle, I2C/SPI/PWM/ADC/DAC/RGB, Scope/DMM-Endpoints. Geschwister zu toolnode-Modulen.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp32.io-control.ino` | Monolith |
| README API | `/api/pins`, i2c/spi, scope, dmm |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Pin-API + I2C/SPI/PWM | `EVID-IO-2026-10-09-001` | `FACT` |
| Restricted Pins mit force | `EVID-IO-2026-10-09-002` | `FACT` |
