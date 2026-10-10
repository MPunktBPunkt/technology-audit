# Follow-on ideas (aus PiDrive)

Ideen, die aus PiDrive-Technologiewissen entstehen können — noch keine Projekte.

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [usb-msc, bmw-nbt-evo, dab-plus, rtl-sdr, bluetooth-a2dp, avrcp]
  new: [pmr446, airband-am, sdr-spectrum-fft]
  not_helped: []  # bisher keine Folgeprojekte gegen diese Kampagne gemessen
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| ESP32 BT-Gateway | `bluetooth-a2dp`, `avrcp` | Classic-BT vom Pi auf ESP (`esp32.bt-gateway`) — Apps kontrastiert |
| Generische MSC-Gadgets | `usb-msc`, `scsi`, `fat` | USB-Storage ohne BMW-Kontext |
| SDR-Empfangsbaustein | `dab-plus`, `rtl-sdr`, `sdr-spectrum-fft` | DAB+/Scanner/FFT als Modul |
| Freenet/LPD/CB Sheets | Scanner-Tabellen | eigene Slugs nur bei Transferbedarf |
| Trace-/Korrelations-Toolkit | Methods | MSC + Spektrum-Watch |
| Metadaten-Bridge | `mpris2`, `avrcp` | Titel/Artist über Senken |
| DAB→BT Audio-Politik | `dab-plus`, `bluetooth-a2dp` | AUFTRAG-DAB-AUDIOWEG schließen |
| FM-Meta-Kontrast RDS | `fm-rds` (Fremd `pi-fm-tx`) | nicht als PiDrive-TX; nur Protokoll-Vergleich zu DLS |

Radio/BT-Kampagne: [`pidrive-2026-radio-bt`](../../audits/pidrive-2026-radio-bt/) · Method [`sdr-spectrum-channel-watch`](../../methods/sdr-spectrum-channel-watch.md).  
Fremd-TX-Kontrast: [`pi-fm-tx`](../pi-fm-tx/).
