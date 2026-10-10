# Follow-on ideas (aus pi-fm-tx)

| Idee | Baut auf | Kurz |
|------|----------|------|
| Geschirmter FM-Loopback-Lab | `rpi-gpio-fm-tx`, `fm-rds` | Pi→Kabel→RX; kein Antennenfeld |
| RDS vs. DAB-DLS Meta-Bridge | `fm-rds`, `dab-plus` | gleicher Zweck, anderes Protokoll |
| Spektrum-Watch auf Harmonische | `sdr-spectrum-fft` | nur Lab, mit Filter-Ethik |
| Nicht als PiDrive-Sendepfad | A2DP / Klinke | Produkt-Audio bleibt nicht-GPIO-TX |
| Ops-Player ohne RF | systemd + lokale Audio-Sink | pi-fm-player-Muster ohne GPIO-TX |
| rpitx Mode-Vertiefung | `rpitx` | nur bei konkretem Lab-Bedarf |

Rechtliche Grenze bleibt: Experiment ≠ Sendestation.
