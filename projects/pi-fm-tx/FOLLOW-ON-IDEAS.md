# Follow-on ideas (aus pi-fm-tx)

```yaml
reuse_outcomes:
  - sheets: [rpi-gpio-fm-tx, fm-rds, rpitx]
    note: 0.6.6 Revalidation — Chip-Scope/Signalpfad/Gate, kein neues Sheet
  - process: "parity 0.6.3 → 0.6.6; DELTA in audits/pi-fm-tx-2026-foreign/"
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| E-0 Desk Pi5/RP1 Clock→Pad | `hw-path-gate`, Sheet-Abgrenzung | TRM/Docs: Source→…→Pad für UKW-nahen Träger; **kein** Sheet vor Evidence |
| E-1 Lab Pi5 Träger (ein Pin) | E-0 | 90/100/108 MHz Messgerät, keine Antenne; Go/No-Go |
| Geschirmter FM-Loopback-Lab | `rpi-gpio-fm-tx`, `fm-rds` | Pi→Kabel→RX; kein Antennenfeld |
| RDS vs. DAB-DLS Meta-Bridge | `fm-rds`, `dab-plus` | gleicher Zweck, anderes Protokoll |
| Spektrum-Watch auf Harmonische | `sdr-spectrum-fft` | nur Lab, mit Filter-Ethik |
| Nicht als PiDrive-Sendepfad | A2DP / Klinke | Produkt-Audio bleibt nicht-GPIO-TX |
| Ops-Player ohne RF | systemd + lokale Audio-Sink | pi-fm-player-Muster ohne GPIO-TX |
| rpitx Mode-Vertiefung | `rpitx` | nur bei konkretem Lab-Bedarf; Pi5 separat gaten |
| ESP32-S3 Clock-RF Gate (E-0/E-1) | `esp32-apll-fm-tx` (Classic belegt), Hub-Familie | Classic-APLL-FM als Sheet/Audit [`esp-fm-tx`](../esp-fm-tx/). S3-Pfad weiter **UNKNOWN**. Analog: Pi5/RP1-Gate oben. |

Rechtliche Grenze bleibt: Experiment ≠ Sendestation.
