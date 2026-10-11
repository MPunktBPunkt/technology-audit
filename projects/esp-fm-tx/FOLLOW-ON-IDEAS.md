# Follow-on ideas (aus esp-fm-tx)

```yaml
reuse_outcomes:
  - sheet: esp32-apll-fm-tx
    note: Classic APLL-FM als eigener Slug neben rpi-gpio-fm-tx
  - process: "0.6.6 Transfer-Gates + kb-cross-check"
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| E-0 Desk S3 Clock-Out | `hw-path-gate`, Sheet-Abgrenzung | TRM/IDF: Source→Divider→MCLK/CLK_OUT→Pad; max. Frequenz pro Pin |
| E-1 Lab S3 Träger 90/100/108 MHz | E-0 | ein Pin, Messgerät, keine Modulation; Go/No-Go |
| E-2/E-3 Raster + FM | E-1 positiv | erst dann Hub-MVP / ggf. Sheet `esp32-clock-rf-tx` |
| Network clock endpoint | Hub-Familie | Pi berechnet Teilerwerte; ESP = deterministischer Ausgabeknoten — **nach** E-1 |
| Harmonic Lab beider Upstreams | `esp32-apll-fm-tx` | Spektrum bis ≥5. Harmonische; Filterpflicht |
| polar_mod als eigene DSP-Note | hiperiondev | nur wenn SSB/AM-Modes später relevant |
| S3 LCD-PCLK @32 MHz Desk | Forum + IDF | E-0 Kandidat neben LEDC-`INFERENCE` |
| PixelRadio als Hub-RDS-Steuer-Vorbild | `fm-rds` | MQTT/HTTP — RF = QN8027, nicht APLL |
| Kontrast S3 polar 13 cm | `esp32-polar-phy-tx` | anderer Contract/Band |

Rechtliche Grenze bleibt: Experiment ≠ Sendestation. Kein Sheet für S3-UKW vor Lab-Evidence.
