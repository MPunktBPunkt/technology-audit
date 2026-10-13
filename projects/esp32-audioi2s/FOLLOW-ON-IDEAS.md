# Follow-on ideas (aus esp32-audioi2s)

```yaml
reuse_outcomes:
  reused: [bluetooth-a2dp, webradio-browser-host]
  new: [esp-i2s-audio]
  not_helped: []
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | A2DP/Browser als Kontrast |
| Neu | `esp-i2s-audio` |
| Nicht geholfen | — |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| On-device Webradio vs. Browser-Host | `esp-i2s-audio`, `webradio-browser-host` | Produktentscheidung |
| I2S→A2DP Source Pipeline | `esp-i2s-audio`, `bluetooth-a2dp` | Example vertiefen |
| PSRAM/Core Labgate | `esp-i2s-audio` | S3 vs Classic Matrix |
