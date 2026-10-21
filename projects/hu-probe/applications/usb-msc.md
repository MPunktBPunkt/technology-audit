# Project Application: usb-msc in hu-probe

```yaml
project_id: hu-probe
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/hu-probe-psram-board-free-2026-10-21/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R3
  reusability: W2
```

## Rolle im Projekt

hu-probe ist ein **USB-MSC Device** (ESP32-S3, TinyUSB/Arduino): Demo-/Virtual-FAT,
BOT-Instrumentierung (`capture_t_us`, `gap_us`, CBW/CSW, `read`-Events), TCP- oder
RAM/PSRAM-Offline-Capture (+ TripStore Drive-Home ab 0.3.x). Ziel = Host-Lesen messen.

## Architektur / Datenfluss

```text
HU USB Host ──BOT/SCSI──► TinyUSB MSC Device (hu-probe)
                              │
                              ├─ read/CBW Events (Ring; Slots in PSRAM)
                              ├─ tcp_live ──WiFi──► Collector
                              └─ ram_offline PSRAM ≤1 MiB (WIFI_OFF → Replay) ──► Collector
```

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `firmware/platformio.ini` | OTG Device, **PSRAM** `qio_qspi`, 8 MB Partitions |
| `firmware/src/capture/OfflineCapture.*` | PSRAM-Puffer-Stufen; compact Records |
| `firmware/src/net/EventBus.*` | Ring-Slots `preferPsram` |
| `docs/HARDWARE-YD-ESP32-S3.md` | Board; §2.3 PSRAM-Text driftet |
| `docs/OFFLINE-CAPTURE.md` | Capture-Vertrag |
| `sessions/*` | Rohdaten (nicht hierher kopieren) |

## Konfiguration und Parameter

| Parameter | Wert | Status |
|-----------|------|--------|
| BOT-Pfad | `bot_source=tinyusb` | `MEASURED` |
| MODE_SENSE6 Pad | ≥0.2.18 | `FACT` + Feld |
| PSRAM Build | `BOARD_HAS_PSRAM` + `qio_qspi` (N8R2) | `MEASURED` `EVID-HUPROBE-2026-10-21-001` |
| Offline capacity Feld | **1048576** B ab 0.2.37+ (vorher ~32 KiB) | `MEASURED` `002` |
| BMW Offline free | 3× PASS 0.2.40 | `MEASURED` `006` |
| Pace-Metrik | `gap_us` / `capture_t_us` (nicht UI-`t_us`) | `FACT` Instrument |
| Drive-Home 0.3.x | TripStore vorhanden; Footer oft unvollständig | `OBSERVED` `018` |

## Ebene C — Host- / Feld-Evidenz

Host-Verhalten (NBT) → [`bmw-nbt-evo.md`](bmw-nbt-evo.md). Hier **Device/Instrument**:

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| dropped=0 Kern-Sessions; Event-Chunk 4096 | `001`/`003`/`004` (15.10.) | `MEASURED` |
| MODE_SENSE6-Stalls vor Fix = Instrument | `006` (15.10.) | `REJECTED` als HU-Recovery |
| PSRAM 1 MiB Capture; overflow=0 free | `EVID-HUPROBE-2026-10-21-002` | `MEASURED` |
| HARDWARE §2.3 „PSRAM aus“ veraltet | `005` | `MEASURED` Doc-Drift |
| Lab Offline E2E; BMW Offline früher fail → free PASS | `007` (15.10.) → `006` (21.10.) | `MEASURED` |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| ≤0.2.30 | Offline-Puffer DRAM-eng (24–64 KiB) |
| 0.2.35+ | PSRAM Ring + Capture; Coex-Tod bleibt |
| 0.2.40 free | BMW Offline Integrity PASS mit 1 MiB |
| 0.3.x | 8 MB Partitionen, Drive-Mode; Audit Census offen |

## Abweichungen vom „Lehrbuch“

- TinyUSB Case-5 MODE_SENSE6 vs. BMW-CBW-Längen.
- Capture unter Coex: Offline-First; Live-Timeline fragmentiert.
- Doc kann hinter Build/Sessions zurückbleiben — Meta schlägt Narrativ.

## Offene Fragen

- Drive-Home Integrity-Census 0.3.1
- Upstream HARDWARE §2.3 + `hw.module` Ist-Wert
- t_us-Regression / Marker ohne WiFi

## Verwandte Applications / Methods

- [`bmw-nbt-evo.md`](bmw-nbt-evo.md) · [`esp32-s3-usb-wifi-coex.md`](esp32-s3-usb-wifi-coex.md)
- Method [`msc-host-read-semantics`](../../../methods/msc-host-read-semantics.md)
- Audit [`hu-probe-psram-board-free-2026-10-21`](../../../audits/hu-probe-psram-board-free-2026-10-21/)
