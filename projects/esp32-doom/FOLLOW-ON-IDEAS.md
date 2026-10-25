# Follow-on ideas (aus esp32-doom)

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [esp32-s3-silicon, ssd1306-oled-ui]
  new: [esp-psram-heavy-port]
  not_helped: []
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | Kontrast S3-Silicon / OLED |
| Neu | `esp-psram-heavy-port` |
| Nicht geholfen | — |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Wrover Lab: FPS + heap caps | `esp-psram-heavy-port` | Internal FB vs PSRAM heap messen |
| S3 Port-Gate Checkliste | Sheet + `esp32-s3-silicon` | nicht still flashen |
| SPI-LCD Framebuffer Sheet | Heavy-port | bei 2. Upstream |
| Kontrast esp32-ai PSRAM-Nutzung | `mcu-ple-inference` | Head/Table vs Game-Heap |
