# Follow-on ideas (aus PiDrive)

Ideen, die aus PiDrive-Technologiewissen entstehen können — noch keine Projekte.

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [usb-msc, bmw-nbt-evo, dab-plus, rtl-sdr, bluetooth-a2dp, avrcp]
  new: [pmr446, airband-am, sdr-spectrum-fft]
  process: "0.6.6 revalidation radio-bt + bmw-hu; DELTAs in audits/"
  not_helped: []
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| ESP32 BT-Gateway | `bluetooth-a2dp`, `avrcp` | Classic-BT vom Pi auf ESP — Stack-Scope getrennt |
| Generische MSC-Gadgets | `usb-msc`, `scsi`, `fat` | USB-Storage ohne BMW-Kontext |
| Andere HU-Variante | `bmw-nbt-evo` | Gate/Evidence — Sheet nicht verbiegen |
| SDR-Empfangsbaustein | `dab-plus`, `rtl-sdr`, `sdr-spectrum-fft` | DAB+/Scanner/FFT als Modul |
| Freenet/LPD/CB Sheets | Scanner-Tabellen | eigene Slugs nur bei Transferbedarf (G19) |
| Trace-/Korrelations-Toolkit | `msc-lba-timing-instrument`, `msc-trace-correlation` | LBA-Bursts + Spektrum-Watch |
| Host-Behavior Sheet pflegen | `bmw-nbt-evo`, SIB/Forum | Cache/Label/FAT32-Gates |
| Generische MSC-Gadgets (Desk) | `esp32-msc-gadget-refs` | Callback/Perf ohne BMW |
| Metadaten-Bridge | `mpris2`, `avrcp` | Titel/Artist über Senken |
| DAB→BT Audio-Politik | `dab-plus`, `bluetooth-a2dp` | AUFTRAG-DAB-AUDIOWEG schließen |
| Feld-Ohr AV PASS | `bmw-nbt-evo` | Exit #6; dann Maturity/Method |
| Stuck-Capture Quiet vs Storm | `bmw-nbt-evo`, Abend-Audit | LBA/Klasse im Prefetch-Livelock; UART zuerst — [`pidrive-2026-10-17-prefetch-livelock`](../../audits/pidrive-2026-10-17-prefetch-livelock/) |
| FM-Meta-Kontrast RDS | `fm-rds` (Fremd `pi-fm-tx`) | nicht als PiDrive-TX; Protokoll-Vergleich zu DLS |

Radio/BT: [`pidrive-2026-radio-bt`](../../audits/pidrive-2026-radio-bt/) · HU: [`pidrive-2026-bmw-hu`](../../audits/pidrive-2026-bmw-hu/) · Method [`sdr-spectrum-channel-watch`](../../methods/sdr-spectrum-channel-watch.md).  
Fremd-TX: [`pi-fm-tx`](../pi-fm-tx/) · Fremd-RX: [`welle-io`](../welle-io/).
