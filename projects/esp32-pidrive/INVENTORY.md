# Project Inventory: esp32.pidrive

```yaml
project_id: esp32-pidrive
updated: 2026-10-09
reviewed_commit: b00e453
profile: firmware
pilot_order: [usb-msc, pump-control-link, esp-hub-telemetry]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.3](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| TinyUSB MSC Device + virtuelle Geometrie/Slots | `usb-msc` | wachsen + FW-Application (Ops-App bleibt unter `pidrive`) |
| Line-JSON + Binärframes UART/TCP Pi↔ESP | `pump-control-link` | **neu** |
| HubClient `fwType=pidrive`, `chipModel=esp32s3` | `esp-hub-telemetry` | wachsen |
| SoftAP/STA HTML+REST (kein SSE) | — | observed (`embedded-web-ui`) — Sheet `esp-embedded-web-sse` erst bei SSE |
| WiFiManager / SoftAP | `wifi-manager-captive` | observed |
| SCSI wrap / Host-Probe | `scsi` | observed (Sheet geplant) |
| FAT12/16 Geometrie-Profile | `fat` | observed (Sheet geplant) |
| BMW NBT Prefetch/Decode | `bmw-nbt-evo` | C bleibt bei [`pidrive`](../pidrive/) |

Ursprung: [esp32.pidrive](https://github.com/MPunktBPunkt/esp32.pidrive).  
Kampagne: [esp32-pidrive-2026-pilot](../../audits/esp32-pidrive-2026-pilot/).  
Ops-Inventar: [`pidrive/INVENTORY`](../pidrive/INVENTORY.md).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `usb-msc` | USB Mass Storage Class | C | `usb-device`, `automotive` | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |
| `pump-control-link` | PUMP Control Link | C | `uart`, `streaming` | applied | partial | [SHEET](../../technologies/pump-control-link/SHEET.md) | [app](applications/pump-control-link.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `iobroker` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `wifi-manager-captive` | WiFiManager / SoftAP | F | — | observed | none | — | — |
| `scsi` | SCSI (über MSC) | C | `usb-device` | observed | none | — | — |
| `fat` | FAT / LBA-Geometrie | E | — | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Host-C / Feld-AV | absichtlich bei `pidrive` | Pilot 2 `bmw-nbt-evo` |
| `scsi` / `fat` Sheets | nur Signale | bei Geometrie-Vertiefung anlegen |
| Web ohne SSE | REST+Polling | SSE nachziehen oder observed belassen |

## Signale ohne Eintrag

- mDNS (`pidrive-<mac>.local`)
- Lab-Endpoints `/api/lab/*`, NBT-Replay-Tools (`tools/nbt_*.py`)
- Doc-Drift: `HUB-INTEGRATION.md` erwähnt ESP-IDF — Ist-Build ist Arduino/PlatformIO
