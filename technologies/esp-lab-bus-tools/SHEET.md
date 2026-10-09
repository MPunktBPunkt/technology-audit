# Technology Sheet: ESP Lab Bus / GPIO Tools

```yaml
slug: esp-lab-bus-tools
title: ESP Lab Bus / GPIO Tools
primary: H
tags: [lab-only, esp-idf]
type: pattern
status: active
seen_in: [esp32-io-control, esp32-toolnode]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W3
```

## Kurzfassung

Werkstatt-Muster: GPIO (Input/Output/PWM/ADC/DAC), I²C-Scan/R-W, SPI-Transfer, optional Signal/OW — per Web-UI und/oder Hub-IO. Geschwister: **Einzweck** (`io-control`) vs. **Module** in Modular-Firmware (`toolnode`).

## Abgrenzung

- **Ist:** interaktive Bus-/Pin-Werkzeuge am ESP.
- **Ist nicht:** fertiges Sensor-Produkt; Produktions-HMI; RF-/LAN-Scanner.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| BOOT/USB/UART-Pins jederzeit schreiben | `REJECTED` | Pin-Schutz / Confirm |
| ADC2 während WiFi nutzbar | `HYPOTHESIS` | ESP32-Klassik: ADC2 ↔ WiFi Konflikt |
| Einzweck und Modul brauchen getrennte Slugs | `REJECTED` | Geschwister → gleicher Slug |

### Projektstart-Checkliste

- [ ] Einzweck vs. Modul (Application kontrastieren)
- [ ] Pin-Guard / restricted Pins
- [ ] Board-Defaults (I2C/SPI)
- [ ] Hub `ios` Mapping
- [ ] Application + `seen_in`

## Referenzen

- esp32.io-control · esp32.toolnode Lab-Module

## Offene Fragen

- Scope/DMM-Capture als eigenes Method-Note?
