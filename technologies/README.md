# technologies/

Wiederverwendbare Technology Sheets. Ein Ordner pro Slug: `technologies/<slug>/SHEET.md`.

Vorlage: [`templates/technology-sheet.md`](../templates/technology-sheet.md)  
**Reuse:** [`docs/REUSE.md`](../docs/REUSE.md) · **Profile:** [`docs/AUDIT-PROFILES.md`](../docs/AUDIT-PROFILES.md) · Taxonomie: [`docs/TAXONOMY.md`](../docs/TAXONOMY.md)

Bei neuem Projekt: Index → Match → Sheet wachsen oder begründet neu — keine Forks. Jedes Sheet: Projektstart-Checkliste.

## Index (extrahiert)

| Slug | Primary | Reuse | Gesehen in |
|------|---------|-------|------------|
| [`avrcp`](avrcp/SHEET.md) | C | W2 | pidrive, esp32-bt-gateway |
| [`ble-hr-relay`](ble-hr-relay/SHEET.md) | C | W3 | esp32-heartrate, esp32-ergo |
| [`ble-hrm-gatt`](ble-hrm-gatt/SHEET.md) | C | W3 | esp32-heartrate, esp32-ergo, esp32-ftmsprobe |
| [`ble-http-gatt-probe`](ble-http-gatt-probe/SHEET.md) | H | W2 | esp32-ftmsprobe |
| [`bluetooth-a2dp`](bluetooth-a2dp/SHEET.md) | C | W2 | pidrive, esp32-bt-gateway |
| [`bluetooth-ftms`](bluetooth-ftms/SHEET.md) | C | W3 | esp32-ftmsprobe, esp32-ergo |
| [`bmw-nbt-evo`](bmw-nbt-evo/SHEET.md) | I | W1 | pidrive, esp32-bt-gateway |
| [`esp-embedded-web-sse`](esp-embedded-web-sse/SHEET.md) | G | W3 | esp32-heartrate, esp32-ergo, esp32-ftmsprobe |
| [`esp-hub-telemetry`](esp-hub-telemetry/SHEET.md) | F | W3 | esp32-heartrate, esp32-ergo, esp32-ftmsprobe, esp32-bt-gateway |
| [`hammer-varon-xtr`](hammer-varon-xtr/SHEET.md) | I | W2 | esp32-ftmsprobe, esp32-ergo |
| [`pdap`](pdap/SHEET.md) | J | W1 | esp32-bt-gateway |
| [`usb-msc`](usb-msc/SHEET.md) | C | W2 | pidrive |

## Geplant (noch ohne Sheet)

| Slug | Primary |
|------|---------|
| `dab-plus` | A |
| `rtl-sdr` | A |
| `webradio` | A |
| `pipewire` | B |
| `scsi` | C |
| `esp32` | D |
| `fat` | E |
| `systemd` | F |
| `mpris2` | G |

PiDrive-Pilot: `usb-msc` → `bmw-nbt-evo` → **`avrcp`** (Sheet jetzt vorhanden).  
ESP: heartrate → ergo → ftmsprobe → **bt-gateway (planning)**.
