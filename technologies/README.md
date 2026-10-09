# technologies/

Wiederverwendbare Technology Sheets. Ein Ordner pro Slug: `technologies/<slug>/SHEET.md`.

Vorlage: [`templates/technology-sheet.md`](../templates/technology-sheet.md)  
Regeln: [`docs/DOCUMENT-STANDARD.md`](../docs/DOCUMENT-STANDARD.md) · Taxonomie: [`docs/TAXONOMY.md`](../docs/TAXONOMY.md)  
**Wiederbegegnung:** [Wissenswachstum](../docs/DOCUMENT-STANDARD.md#wissenswachstum-wiederbegegnung-mit-bekannter-tech) — bestehende Slugs erweitern, nicht forken.

## Index (extrahiert)

| Slug | Primary | Reuse | Gesehen in |
|------|---------|-------|------------|
| [`usb-msc`](usb-msc/SHEET.md) | C | W2 | [pidrive](../projects/pidrive/) |
| [`bmw-nbt-evo`](bmw-nbt-evo/SHEET.md) | I | — | [pidrive](../projects/pidrive/) |
| [`ble-hrm-gatt`](ble-hrm-gatt/SHEET.md) | C | W3 | heartrate · ergo |
| [`ble-hr-relay`](ble-hr-relay/SHEET.md) | C | W3 | heartrate · ergo |
| [`esp-embedded-web-sse`](esp-embedded-web-sse/SHEET.md) | G | W3 | heartrate · ergo |
| [`esp-hub-telemetry`](esp-hub-telemetry/SHEET.md) | F | W3 | heartrate · ergo |
| [`bluetooth-ftms`](bluetooth-ftms/SHEET.md) | C | W2 | [esp32-ergo](../projects/esp32-ergo/) |
| [`hammer-varon-xtr`](hammer-varon-xtr/SHEET.md) | I | W1 | [esp32-ergo](../projects/esp32-ergo/) |

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

PiDrive-Pilot-Reihenfolge: `usb-msc` → `bmw-nbt-evo` → `avrcp`.  
ESP-Node-Bootstrap: [`esp32-heartrate`](../projects/esp32-heartrate/) → [`esp32-ergo`](../projects/esp32-ergo/).
