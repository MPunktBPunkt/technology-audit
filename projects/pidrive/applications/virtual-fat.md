# Project Application: virtual-fat in PiDrive

```yaml
project_id: pidrive
tech_slug: virtual-fat
status: active
sheet: ../../../technologies/virtual-fat/SHEET.md
audit: ../../../audits/esp32-msc-gadget-refs-2026-foreign/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle

PiDrive nutzt eine **synthetische FAT12/16-Geometrie** (Slots = Medien) auf dem ESP32-MSC-Gadget. Directory/FAT bleiben indexierbar und möglichst statisch; File-Bodies können Prefill/Seed oder on-the-fly sein. Transport und Host-Timing bleiben in [`usb-msc.md`](usb-msc.md) / [`bmw-nbt-evo.md`](bmw-nbt-evo.md).

## Architektur (B)

```text
Statische Geometrie (BPB, FAT, Root, Slot-Namen)
        │
        ▼
Body-LBAs ← Prefill / Seed / Live-Stream (Application-Strategie)
        │
        ▼
USB-MSC onRead → BMW NBT Evo
```

## Evidenz / Kontrast

- Ops-MSC-Pilot: [`pidrive-2026-msc`](../../../audits/pidrive-2026-msc/)
- Callback-/Geometrie-Vorlagen Fremd: [`esp32-msc-gadget-refs`](../../esp32-msc-gadget-refs/)
- Next: LBA-Instrumentierung [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md)

## Ebene C

Host-Cache (Label/Serial), Prefetch, FAT32-Hypothese → nur [`bmw-nbt-evo.md`](bmw-nbt-evo.md).

## Verwandte

- Sheet: [`virtual-fat`](../../../technologies/virtual-fat/SHEET.md)
- MSC: [`usb-msc.md`](usb-msc.md) · FW: [`esp32-pidrive/.../virtual-fat`](../../esp32-pidrive/applications/virtual-fat.md)
