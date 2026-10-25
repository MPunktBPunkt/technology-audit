# Follow-on ideas (aus esp32-marauder)

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [rf-environment-monitor, lan-device-inventory]
  new: [esp-wifi-promiscuous-pcap]
  not_helped: []
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | Kontrast `rf-environment-monitor`, `lan-device-inventory` |
| Neu | `esp-wifi-promiscuous-pcap` |
| Nicht geholfen | — |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Authorized Lab: Drop-Rate vs. BUF_SIZE | `esp-wifi-promiscuous-pcap` | Double-Buffer unter Last |
| Kontrast-App rfmonitor vs Marauder | `rf-environment-monitor` | Scan-Score ≠ Promiscuous |
| C5 Dual-Band Gate | Sheet Chip-Scope | 2.4 vs 5 GHz Channel-Walk |
| Method: promiscuous→PCAP pipeline | Sheet | bei ≥2 Projekten |
