# Follow-on ideas (aus espectre)

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [esp-wifi-promiscuous-pcap, rf-environment-monitor, mqtt-node-telemetry, esp-embedded-web-sse]
  new: [wifi-csi-motion]
  not_helped: []
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | Kontrast Sniff/RF-Score; MQTT/SSE observed |
| Neu | `wifi-csi-motion` |
| Nicht geholfen | — |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Authorized room Lab vs Upstream holdout | `wifi-csi-motion` | False-positive in eigenem Raum |
| Marauder CSI-Kontrast-App | `wifi-csi-motion` | Toolkit-CSI vs Sensing-Produkt |
| Airtime-Budget multi-sensor | Sheet Traffic-Abschnitt | pps × Geräte |
| Method: temporal CSI admission replay | Sheet | bei ≥2 Projekten |
