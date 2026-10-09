# Project Application: esp-lab-bus-tools in esp32.toolnode

```yaml
project_id: esp32-toolnode
tech_slug: esp-lab-bus-tools
status: active
sheet: ../../../technologies/esp-lab-bus-tools/SHEET.md
audit: ../../../audits/esp32-toolnode-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

**Geschwister** zu io-control: Lab als **Module** (`I2cLab`, `UartTool`, `OneWire`, `Signal`, optional SPI) hinter `esp-module-host`, nicht Einzweck-Pinout-UI.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/modules/I2cLabModule.*` | I²C |
| `src/modules/UartToolModule.*` | UART |
| `src/modules/OneWireModule.*` | OneWire |
| `src/modules/SignalToolModule.*` | PWM/Pulse |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Lab-Module unter ENABLE_* Flags | `EVID-MOD-2026-10-09-002` | `FACT` |
