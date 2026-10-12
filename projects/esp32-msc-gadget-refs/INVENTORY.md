# Project Inventory: esp32-msc-gadget-refs (Fremd)

```yaml
project_id: esp32-msc-gadget-refs
updated: 2026-10-12
reviewed_commit: "multi @ 2026-10-12"
profile: lab-tool
pilot_order: [usb-msc, virtual-fat]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| MSC BOT Device + READ(10) callbacks | `usb-msc` | **reuse** (Gadget-Callback-Zelle) |
| Synthetic FAT12/16 in RAM/PSRAM | `virtual-fat` | **neu** |
| USB FS throughput limits | `usb-msc` | Fallstricke / Transfer |
| BMW cache / re-index | `bmw-nbt-evo` | **nicht hier** — Host-C |

Kampagne: [`esp32-msc-gadget-refs-2026-foreign`](../../audits/esp32-msc-gadget-refs-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `usb-msc` | USB Mass Storage Class | C | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |
| `virtual-fat` | Virtual FAT Disk | E | applied | partial | [SHEET](../../technologies/virtual-fat/SHEET.md) | [app](applications/virtual-fat.md) |
| `bmw-nbt-evo` | BMW NBT Evo | I | documented | none | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | — (Kontrast Host) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Eigene LBA-Trace vs NBT | Desk foreign | Method + pidrive Lab |
| On-the-fly MP3 framing | kein öffentliches Repo | PiDrive FOLLOW-ON |
| FAT32 Minimalgeometrie HU | Community/SIB | Host-C Evidence |

## Signale ohne Eintrag

- Wear-leveling SPI-Flash LUN (IDF) — Persistenz-Backend, nicht Virtual-FAT
- Lazy-write ohne Error-Handling (atomic14) — Perf-Trick, riskant
