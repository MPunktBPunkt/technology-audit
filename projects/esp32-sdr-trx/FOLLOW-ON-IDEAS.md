# Follow-on ideas (aus esp32-sdr-trx)

```yaml
reuse_outcomes:
  reused: [esp32-undoc-iq-rx, hw-path-gate, esp32-apll-fm-tx]
  new: [esp32-polar-phy-tx]
  not_helped: []
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Lab-Remessung polar FM/SSB (fremde SA/SDR) | Sheet + `hw-path-gate` | Author-Hz → eigene `MEASURED`-IDs |
| Spurs/ACLR / uncalibrated power | transmitter.md Claims | Filterpflicht? |
| Raw-I/Q-TX Research-Zweig Desk | `research/iq-tx` | nur observed; Sheet erst nach Stabilität |
| Chip-Gate C5/S31 polar | Matrix | vermutlich Fail — dokumentieren |
| Hub: S3 als 13 cm Experimental-Node | Hub-Familie | erst nach Legal+Lab; getrennt von UKW-APLL |

Recht: Amateurlizenz / Lab-Last. Kein Antennen-Sendepfad in der KB.
