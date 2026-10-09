# technologies/

Wiederverwendbare Technology Sheets. Ein Ordner pro Slug: `technologies/<slug>/SHEET.md`.

Vorlage: [`templates/technology-sheet.md`](../templates/technology-sheet.md)  
Regeln: [`docs/DOCUMENT-STANDARD.md`](../docs/DOCUMENT-STANDARD.md) · **Reuse:** [`docs/REUSE.md`](../docs/REUSE.md) · Taxonomie: [`docs/TAXONOMY.md`](../docs/TAXONOMY.md)

Bei neuem Projekt: Index lesen → Signal matchen → Sheet wachsen oder begründet neu — keine Forks.

## Index (extrahiert)

| Slug | Primary | Reuse | Gesehen in |
|------|---------|-------|------------|
| [`usb-msc`](usb-msc/SHEET.md) | C | W2 | pidrive |
| [`bmw-nbt-evo`](bmw-nbt-evo/SHEET.md) | I | — | pidrive |
| [`ble-hrm-gatt`](ble-hrm-gatt/SHEET.md) | C | W3 | heartrate · ergo · ftmsprobe |
| [`ble-hr-relay`](ble-hr-relay/SHEET.md) | C | W3 | heartrate · ergo |
| [`esp-embedded-web-sse`](esp-embedded-web-sse/SHEET.md) | G | W3 | heartrate · ergo · ftmsprobe |
| [`esp-hub-telemetry`](esp-hub-telemetry/SHEET.md) | F | W3 | heartrate · ergo · ftmsprobe |
| [`bluetooth-ftms`](bluetooth-ftms/SHEET.md) | C | W3 | ftmsprobe · ergo |
| [`hammer-varon-xtr`](hammer-varon-xtr/SHEET.md) | I | W2 | ftmsprobe · ergo |
| [`ble-http-gatt-probe`](ble-http-gatt-probe/SHEET.md) | H | W2 | ftmsprobe |

## Geplant (noch ohne Sheet)

| Slug | Primary |
|------|---------|
| `dab-plus` | A |
| `rtl-sdr` | A |
| `webradio` | A |
| `pipewire` | B |
| `scsi` | C |
| `bluetooth-a2dp` | C |
| `avrcp` | C |
| `esp32` | D |
| `fat` | E |
| `systemd` | F |
| `mpris2` | G |

PiDrive-Pilot: `usb-msc` → `bmw-nbt-evo` → `avrcp`.  
ESP-Familie: heartrate → ergo → **ftmsprobe** (Lab/Method).
