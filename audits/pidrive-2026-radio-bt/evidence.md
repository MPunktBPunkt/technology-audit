# Evidence — pidrive-2026-radio-bt

Desk-/Ops-Audit 2026-10-09 @ `b61df4d` · Original **0.6.3** · Revalidation 2026-10-11 · **0.6.6**.

Basis: `https://github.com/MPunktBPunkt/pidrive/blob/b61df4d/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-DAB-2026-10-09-001` | welle-cli Gain-Index ≠ rtl_fm dB | `FACT` | `WELLE-CLI.md`, AUFTRAG-DAB DA-P* |
| `EVID-DAB-2026-10-09-002` | welle `/spectrum` nur DAB-Kanäle | `FACT` | AUFTRAG-SPEKTRUM SA1 |
| `EVID-DAB-2026-10-09-003` | DAB-Audio-Route kann BT umgehen | `FACT` | AUFTRAG-DAB-AUDIOWEG DA* |
| `EVID-RTL-2026-10-09-001` | flock Lock + Owner | `FACT` | `rtlsdr.py` |
| `EVID-RTL-2026-10-09-002` | USB Reset sysfs authorized | `FACT` | PMR-MONITOR Recovery |
| `EVID-PMR-2026-10-09-001` | 16× 12.5 kHz ab 446.00625 | `FACT` | `scanner.py` PMR446_CHANNELS |
| `EVID-PMR-2026-10-09-002` | Monitor Hysterese + hold | `FACT` | PMR-MONITOR.md |
| `EVID-AIR-2026-10-09-001` | AM + airband_stations.json | `FACT` | scanner + config |
| `EVID-AIR-2026-10-09-002` | spectrum 118–137 ≠ AM-Demod | `FACT` | SPECTRUM-CLI.md |
| `EVID-FFT-2026-10-09-001` | capture_spectrum peaks API | `FACT` | spectrum.py / Auftrag SA2 |
| `EVID-FFT-2026-10-09-002` | welle nicht Allzweck-SA | `FACT` | AUFTRAG-SPEKTRUM SA1 |
| `EVID-A2DP-2026-10-09-001` | PipeWire/pactl A2DP routing | `FACT` | `bt_audio.py` |
| `EVID-AVRCP-2026-10-09-001` | D-Bus → pidrive_cmd Bridge | `FACT` | `avrcp_trigger.py` |
| `EVID-AVRCP-2026-10-09-002` | nicht alle HU-Tasten = AVRCP | `FACT` | Sheet + BMW-AVRCP-PROBE |
| `EVID-SCOPE-2026-10-11-001` | RX-Sheets ≠ Pi/ESP GPIO-Clock-TX; getrennte Slugs | `FACT` | Sheet-Abgrenzungen + `pi-fm-tx` / `esp-fm-tx`; Revalidation |
| `EVID-SCOPE-2026-10-11-002` | A2DP/AVRCP Pi BlueZ/PW ≠ ESP Classic-Gateway-Stack | `FACT` | Apps + `esp32-bt-gateway`; Revalidation |
| `EVID-MATCH-2026-10-11-001` | welle-io Fremd-Audit wächst `dab-plus`/`rtl-sdr`; Freenet/LPD/CB ohne Sheet | `FACT` | Inventar + G19; Revalidation |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Antennenvergleich 2026-09-22 vollständig in Maturity | `UNKNOWN` | JSON-Artefakte verlinken bei Bedarf |
| DAB→BT hörbar im Fahrzeug | `UNKNOWN` | Audio-Politik nachziehen |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Radio/FFT/BT-Vertiefung; 5 neue Sheets; A2DP/AVRCP Apps |
| 2026-10-11 | Revalidation **0.6.6**: RX≠TX, Stack-Scope, [DELTA](DELTA.md) |
