# Project Inventory: PiDrive

```yaml
project_id: pidrive
updated: 2026-10-09
reviewed_commit: b61df4d
pilot_order: [usb-msc, bmw-nbt-evo, dab-plus, sdr-spectrum-fft, pmr446, airband-am, bluetooth-a2dp, avrcp]
```

Pilot 1 (`usb-msc`) **closed**. Pilot 2 (`bmw-nbt-evo`) **active**.  
**Radio/BT-Vertiefung 2026-10-09:** Kampagne [`pidrive-2026-radio-bt`](../../audits/pidrive-2026-radio-bt/) — DAB+/RTL-SDR/PMR/Airband/FFT + A2DP/AVRCP Applications. Transfer-BT: [`esp32-bt-gateway`](../esp32-bt-gateway/).

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.3](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| welle-cli DAB+ Ensemble/DLS | `dab-plus` | **neu** + App |
| RTL2832 Stick Lock/Reset/PPM | `rtl-sdr` | **neu** + App |
| PMR446 16ch + Spektrum-Monitor | `pmr446` | **neu** + App |
| VHF Airband AM + Presets | `airband-am` | **neu** + App |
| IQ-FFT Peaks / channelized watch | `sdr-spectrum-fft` | **neu** + App + Method |
| BlueZ A2DP + PipeWire | `bluetooth-a2dp` | wachsen + App (Kontrast ESP-Gateway) |
| AVRCP Controller → Trigger | `avrcp` | wachsen + App (Kontrast ESP-Gateway) |
| Freenet/LPD/CB Raster | — | observed in Scanner (kein eigenes Sheet) |
| UKW WBFM | — | observed (teilweise unter rtl-sdr/fm) |

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `dab-plus` | DAB+ | A | `sdr`, `streaming` | applied | partial | [SHEET](../../technologies/dab-plus/SHEET.md) | [app](applications/dab-plus.md) |
| `rtl-sdr` | RTL-SDR Host | A | `sdr`, `usb-host` | applied | partial | [SHEET](../../technologies/rtl-sdr/SHEET.md) | [app](applications/rtl-sdr.md) |
| `pmr446` | PMR446 | A | `sdr`, `radio` | applied | partial | [SHEET](../../technologies/pmr446/SHEET.md) | [app](applications/pmr446.md) |
| `airband-am` | Airband AM | A | `sdr`, `radio` | applied | partial | [SHEET](../../technologies/airband-am/SHEET.md) | [app](applications/airband-am.md) |
| `sdr-spectrum-fft` | SDR Spectrum FFT | H | `sdr`, `lab-only` | applied | partial | [SHEET](../../technologies/sdr-spectrum-fft/SHEET.md) | [app](applications/sdr-spectrum-fft.md) |
| `webradio` | Webradio | A | `streaming` | observed | none | — | — |
| `pipewire` | PipeWire | B | `linux-userspace` | observed | none | — | — |
| `usb-msc` | USB Mass Storage | C | `usb-device`, `automotive` | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |
| `scsi` | SCSI (MSC/BOT) | C | `usb-device` | observed | none | — | — |
| `bluetooth-a2dp` | Bluetooth A2DP | C | `bluetooth-classic` | applied | partial | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | [app](applications/bluetooth-a2dp.md) |
| `avrcp` | AVRCP | C | `bluetooth-classic` | applied | partial | [SHEET](../../technologies/avrcp/SHEET.md) | [app](applications/avrcp.md) |
| `esp32` | ESP32 | D | `esp-idf` | observed | none | — | — |
| `fat` | FAT / LBA | E | — | observed | none | — | — |
| `systemd` | systemd | F | `linux-userspace` | observed | none | — | — |
| `mpris2` | MPRIS2 | G | `metadata` | observed | none | — | — |
| `bmw-nbt-evo` | BMW NBT Evo Host | I | `automotive` | applied | partial | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | [app](applications/bmw-nbt-evo.md) |

## Nach Kategorie

### A — Empfang

`dab-plus`, `rtl-sdr`, `pmr446`, `airband-am`, `webradio` (+ observed: UKW-FM, Freenet/LPD/CB)

### B — Audio

`pipewire`

### C — Protokolle

`usb-msc`, `scsi`, `bluetooth-a2dp`, `avrcp`

### H — Test / Analyse

`sdr-spectrum-fft` · Method [`sdr-spectrum-channel-watch`](../../methods/sdr-spectrum-channel-watch.md)

### I — Fahrzeug

`bmw-nbt-evo`

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| DAB→BT hörbar | Audio-Politik historisch | AUFTRAG-DAB nachziehen |
| Antennenvergleich JSON | Artefakte roh | Evidence verdichten |
| Freenet/LPD/CB Sheets | nur Scanner-Tabellen | bei Bedarf eigene Slugs |
| MPRIS2 Sheet | observed | nach Meta-Pilot |

## Signale ohne Eintrag

- Spotify / raspotify
- Trigger-Dispatcher / Lenkrad-Mapping (teilweise in AVRCP-App)
- SoftAP Diagnose auf ESP (→ `esp32-pidrive`)
