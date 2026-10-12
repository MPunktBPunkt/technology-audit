# Project Application: virtual-fat in esp32-pidrive

```yaml
project_id: esp32-pidrive
tech_slug: virtual-fat
status: active
sheet: ../../../technologies/virtual-fat/SHEET.md
audit: ../../../audits/esp32-msc-gadget-refs-2026-foreign/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R0
  reusability: W3
```

## Rolle

Firmware baut die virtuelle Disk-Geometrie (FAT12/16-Profile, Slot-Directory) und bedient Body-Sektoren im TinyUSB-Read-Pfad. Ops-/Host-Claims bleiben bei [`pidrive`](../../pidrive/).

## Architektur (B)

Siehe [`usb-msc.md`](usb-msc.md). Geometrie vs. Transport: Sheet-Trennung `virtual-fat` / `usb-msc`.

## Relevante Signale

| Signal | Hinweis |
|--------|---------|
| FAT12/16 Profile | Inventar früher `fat` observed → jetzt dieses Sheet |
| Volume Label / Serial | Cache-Tests nur mit Host-App abstimmen |
| Full-Disk PSRAM | optional; Live-Body braucht kein Full-Image (Gadget-Refs) |

## Next Lab

Instrumentierung am Read-Callback: [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md). Vorlagen: [`esp32-msc-gadget-refs`](../../esp32-msc-gadget-refs/).

## Verwandte

- Sheet: [`virtual-fat`](../../../technologies/virtual-fat/SHEET.md)
- Ops: [`pidrive/.../virtual-fat`](../../pidrive/applications/virtual-fat.md)
- MSC FW: [`usb-msc.md`](usb-msc.md)
