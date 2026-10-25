# Technology Sheet: SSD1306 OLED UI (small)

```yaml
slug: ssd1306-oled-ui
title: SSD1306 OLED UI (small)
primary: G
tags: []
type: pattern
status: active
seen_in: [esp32-metermaster, esp32-ai]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Kurzfassung

Kleines I²C-OLED (häufig SSD1306, z. B. 64×48) als lokale Anzeige: wenige Zeilen/Stile, Alarm/Carousel, gesteuert aus App-Logik — ergänzend zur Web-UI, nicht als Ersatz für komplexe Dashboards.

## Abgrenzung

- **Ist:** Embedded-Pixel-Display-UI für Status/Werte.
- **Ist nicht:** Web-UI; HDMI; Touch-HMI; SPI-LCD-Game-Framebuffer (`esp-psram-heavy-port`).

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Alle 0.66″ OLEDs gleichen Konstruktor | `REJECTED` | Controller/Geometrie-Varianten (z. B. EastRising; SH1106 vs SSD1306) |
| Textgröße skaliert wie Desktop | `REJECTED` | Zeichenbudget eng (z. B. 10×6) |
| Display ersetzt Remote-Config | `REJECTED` | Config weiter Web/Adapter |
| Fehlendes Panel = Boot-Fail | `REJECTED` | Probe-once + no-op draws möglich (esp32-ai Desk) |

### Projektstart-Checkliste

- [ ] Controller + Auflösung + I²C-Adresse
- [ ] Library/Konstruktor verifizieren
- [ ] Zeichen-/Stilbudget
- [ ] Application + `seen_in`

## Referenzen

- SSD1306 / U8g2
- Beispiel: MeterMaster Hardware-Docs

## Offene Fragen

- Welche Mindest-Font-Strategien für Alarm+Wert auf 64×48?
