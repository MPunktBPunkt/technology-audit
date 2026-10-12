# Follow-on ideas (aus esp32sdr)

```yaml
reuse_outcomes:
  reused: [esp32-undoc-iq-rx, hw-path-gate]
  new: [esp32-wifi-tone-tx]
  not_helped: []
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | `esp32-undoc-iq-rx`, `hw-path-gate` |
| Neu | `esp32-wifi-tone-tx` |
| Nicht geholfen | — |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| S3 TX-Entscheidungsbaum Hub | `esp32-wifi-tone-tx`, `esp32-polar-phy-tx` | Tone vs polar vs rejected DAC |
| Remessung BER/Spurs | `esp32-wifi-tone-tx` | eigene Lab-IDs |
| Bridge + Tone Pair | `esp32-undoc-iq-rx`, esp-sdr-bridge | RX-host + keyed TX |
