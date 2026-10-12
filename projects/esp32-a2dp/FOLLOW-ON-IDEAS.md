# Follow-on ideas (aus esp32-a2dp)

```yaml
reuse_outcomes:
  reused: [bluetooth-a2dp, avrcp]
  new: []
  not_helped: []
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | `bluetooth-a2dp`, `avrcp` (ESP-Bluedroid-Zelle) |
| Neu | — |
| Nicht geholfen | — |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Gateway Source gegen NBT Evo | `bluetooth-a2dp`, `avrcp`, `bmw-nbt-evo` | pschatzmann Source + Pass-Through als Lab-Baseline |
| Sink-Speaker vs. Gateway-Source Dual | `bluetooth-a2dp` | Rollen-Exklusivität empirisch bestätigen |
| AAC SEP auf IDF ≥6.1 | `bluetooth-a2dp` | nur wenn Codec-Pfad nötig |
| Katalog-Geschwister | `avrcp` | EspBle CT/TG, IDF CoverArt/AbsVol, HFP-Client — siehe FAMILIES Lab/BT |
