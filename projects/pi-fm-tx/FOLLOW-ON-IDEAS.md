# Follow-on ideas (aus pi-fm-tx)

| Idee | Baut auf | Kurz |
|------|----------|------|
| Geschirmter FM-Loopback-Lab | `rpi-gpio-fm-tx`, `fm-rds` | Pi→Kabel→RX; kein Antennenfeld |
| RDS vs. DAB-DLS Meta-Bridge | `fm-rds`, `dab-plus` | gleicher Zweck, anderes Protokoll |
| Spektrum-Watch auf Harmonische | `sdr-spectrum-fft` | nur Lab, mit Filter-Ethik |
| Nicht als PiDrive-Sendepfad | A2DP / Klinke | Produkt-Audio bleibt nicht-GPIO-TX |
| Ops-Player ohne RF | systemd + lokale Audio-Sink | pi-fm-player-Muster ohne GPIO-TX |
| rpitx Mode-Vertiefung | `rpitx` | nur bei konkretem Lab-Bedarf |
| ESP32-S3 Clock-RF Gate (E-0/E-1) | `esp32-apll-fm-tx` (Classic belegt), Hub-Familie | Classic-APLL-FM jetzt als Sheet/Audit [`esp-fm-tx`](../esp-fm-tx/). S3-Pfad weiter **UNKNOWN**. Zuerst E-0 (Clock-Out → ein GPIO → Messgerät, 90/100/108 MHz). Kein S3-Sheet vor Lab-Evidence. Bei positivem Gate: Pi = Signalaufbereitung, ESP = network-controlled deterministic RF clock/modulation endpoint. |

Rechtliche Grenze bleibt: Experiment ≠ Sendestation.
