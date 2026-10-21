# Project Application: esp32-s3-silicon in hu-probe

```yaml
project_id: hu-probe
tech_slug: esp32-s3-silicon
status: active
sheet: ../../../technologies/esp32-s3-silicon/SHEET.md
audit: ../../../audits/hu-probe-psram-board-free-2026-10-21/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R1
  reusability: W2
```

## Rolle im Projekt

Board- und Speicher-Pin der Messsonde: **YD-ESP32-S3 N8R2** (8 MiB Flash +
2 MiB Quad-PSRAM), Dual-USB-C (OTG vs. CH343 COM). Silicon/Errata bleiben A;
hier nur **B** Build/Board und **C** Feld-Meta (Capture-Kapazität).

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `docs/HARDWARE-YD-ESP32-S3.md` | Foto/Pinout/Versorgung; §2.3 PSRAM-Text driftet |
| `firmware/platformio.ini` | `qio_qspi`, `-DBOARD_HAS_PSRAM`, 8 MB Partitions |
| `firmware/src/core/HwInfo.*` | eFuse/JEDEC → `hw.module` |
| `firmware/src/capture/OfflineCapture.*` | PSRAM-Puffer bis 1 MiB |
| `firmware/src/net/EventBus.*` | Ring-Slots in PSRAM |

## Konfiguration und Parameter

| Parameter | Wert | Status |
|-----------|------|--------|
| Modul-Ziel | N8R2 | `FACT` Build/Lab; eFuse-Ist FOLLOW-ON |
| PSRAM Build | `BOARD_HAS_PSRAM` + `qio_qspi` | `MEASURED` `EVID-HUPROBE-2026-10-21-001` |
| Offline capacity Feld | 1048576 B ab 0.2.37+ | `MEASURED` `002` |
| USB-OTG Brücke | offen lassen (kein VBUS-Kurz) | `FACT` Board-Regel |
| HARDWARE §2.3 „PSRAM aus“ | veraltet | `MEASURED` Doc-Drift `005` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Feld/Lab Offline `capacity_bytes=1MiB` nach PSRAM-Enable | `EVID-HUPROBE-2026-10-21-002` | `MEASURED` |
| PSRAM heilt USB↔WiFi-Coex | `015` | `REJECTED` |
| HU kann Sonde allein speisen | Board-Doc Betreiber | `MEASURED` (Betreiber) |

## Offene Fragen

- Upstream HARDWARE §2.3 + `hw.module` Ist-Wert am Feld-ESP
- USB-OTG-Lötbrücke am Exemplar visuell bestätigen
- Chip-Rev / Date Code für Errata-Spalten

## Verwandte Applications / Methods

- [`usb-msc.md`](usb-msc.md) · [`esp32-s3-usb-wifi-coex.md`](esp32-s3-usb-wifi-coex.md)
- Sheet [`esp32-s3-silicon`](../../../technologies/esp32-s3-silicon/SHEET.md)
- Audit [`hu-probe-psram-board-free-2026-10-21`](../../../audits/hu-probe-psram-board-free-2026-10-21/)
