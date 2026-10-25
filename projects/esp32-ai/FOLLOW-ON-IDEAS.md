# Follow-on ideas (aus esp32-ai)

Ideen, die aus diesem Fremd-Desk-Audit entstehen können — noch keine neuen Repos.

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [esp32-s3-silicon, ssd1306-oled-ui]
  new: [mcu-ple-inference, mcu-connectome-graph]
  not_helped: []
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | `esp32-s3-silicon`, `ssd1306-oled-ui` |
| Neu | `mcu-ple-inference`, `mcu-connectome-graph` |
| Nicht geholfen | — |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Bandbreiten-Remessung N16R8 | `esp32-s3-silicon`, `mcu-ple-inference` | Eigene Cycle-Counter-Zahlen vs. Upstream `RESULTS.md` |
| PLE-Port auf anderes Board | `mcu-ple-inference` | Flash-mmap + PSRAM-Head Budget prüfen |
| OLED-Controller-Gate im Lab | `ssd1306-oled-ui` | SH1106 vs SSD1306 Probe `0x3C`/`0x3D` |
| Method: host-gold before flash | `mcu-ple-inference` | Deploy-Gate-Muster als Method Note bei ≥2 Projekten |
| Asym. Vocab (Barista) zweites Upstream | `mcu-ple-inference` | A-Fallstrick erst bei Wiederbegegnung |
