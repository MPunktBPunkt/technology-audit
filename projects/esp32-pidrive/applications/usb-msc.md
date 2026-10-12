# Project Application: USB-MSC in esp32.pidrive

```yaml
project_id: esp32-pidrive
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/esp32-pidrive-2026-pilot/
maturity:
  technology: R4
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

Firmware-Implementierung des USB-MSC-Gadgets: TinyUSB Device, virtuelles FAT mit bis zu **4 Slots**, Prefill/Body-Seed, Play-Guess aus Host-Reads. Ops-/Feld-Sicht und Host-C: [`pidrive/applications/usb-msc.md`](../../pidrive/applications/usb-msc.md).

## Architektur / Datenfluss

```text
MenuStore (Namen/UIDs) ──▶ UsbMscGadget.applyMenuSlots
StreamBuffer (PUMP-Audio) ──▶ Overlay auf Slot-LBAs
USB Host READ(10) ──▶ virtuelle Sektoren / Demo-FAT / Live-Body
looksLikePlay ──▶ play_uid an PumpServer
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `src/msc/UsbMscGadget.*` | MSC-Gadget, Trace, Play-Detect |
| `src/msc/MscGeometry.h` | Legacy / L0 / L0-16M / L3 Profile |
| `src/msc/HostScsiProbe.*` | SCSI-Callback-Wrap / Fingerprint |
| `src/msc/LabBodySeed.h`, `Mp3Silence.h` | Seed / Stub-Audio |
| `platformio.ini` | `ARDUINO_USB_MODE=0`, Envs `pidrive-s3*` |
| `tools/msc_host_test.py`, `nbt_*.py` | Lab-Host / Replay |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| Chip / USB | ESP32-S3 OTG, TinyUSB, `ARDUINO_USB_MODE=0` | `FACT` |
| Slot-Anzahl | `kSlots = 4` | `FACT` |
| Legacy-Geometrie | FAT12, 2 MiB, 512 KiB-Slots (`0.4.36` Feld-Baseline) | `FACT` |
| Lab L0 | FAT12-klassifiziert, 4 MiB / 1 MiB-Slots (`PIDRIVE_GEO_L0`) | `FACT` |
| Lab L0-16M / L3 | FAT16 16 MiB; L3 ungleiche Slots | `FACT` |
| Play-Detect | plugWindow / minSeqBytes / cooldown aus Config | `FACT` (B) |

## Ebene C — Host- / Feld-Evidenz

Primärregister: [`pidrive-2026-bmw-hu/evidence`](../../../audits/pidrive-2026-bmw-hu/evidence.md) · Application [`bmw-nbt-evo`](../../pidrive/applications/bmw-nbt-evo.md).

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Firmware exportiert MSC unter TinyUSB MODE=0 | `EVID-MSC-2026-10-09-001` | `FACT` |
| Geometrie-Profile per Build-Flag wählbar | `EVID-MSC-2026-10-09-002` | `FACT` |

## Abweichungen vom „Lehrbuch“

- Medien virtuell/on-the-fly; nicht Stick-Inhalt auf Flash.
- Soft-Paging der Menüs liegt in PUMP/Bridge (4 sichtbare Slots), nicht in MSC-Spec.

## Verwandte

- Sheet: [`usb-msc`](../../../technologies/usb-msc/SHEET.md) · [`virtual-fat`](../../../technologies/virtual-fat/SHEET.md)
- Ops-Application: [`pidrive` usb-msc](../../pidrive/applications/usb-msc.md)
- PUMP: [`pump-control-link`](pump-control-link.md)
- Callback/Perf-Referenzen: [`esp32-msc-gadget-refs`](../../esp32-msc-gadget-refs/)
- Next Lab: [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md) am `UsbMscGadget`-Read-Pfad
