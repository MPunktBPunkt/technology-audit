# Audit Campaign: esp32-msc-gadget-refs-2026-foreign

```yaml
id: esp32-msc-gadget-refs-2026-foreign
project_id: esp32-msc-gadget-refs
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "multi-2026-10-12"
reuse_outcomes:
  reused: [usb-msc, bmw-nbt-evo, hw-path-gate]
  new: [virtual-fat, msc-lba-timing-instrument, msc-trace-correlation]
  not_helped: []
  process: "Deep foreign desk for PiDrive MSC niche; no HU field this campaign"
```

## Ziel

Öffentliche ESP32-MSC-Gadget-Referenzen tief in die KB: Callback-Contracts, Virtual FAT, USB-FS-Perf, Methods für LBA/Timing — als Bausteine für Fake-MP3/Live-Stream gegen NBT Evo.

## Scope

[SCOPE](../../projects/esp32-msc-gadget-refs/SCOPE.md) — Desk; BMW-Verhalten nur Querverweis.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 | erfüllt |
| 2 | Sheet `virtual-fat` + `usb-msc` Wachstum | erfüllt |
| 3 | Methods LBA-Timing + Trace-Correlation | erfüllt |
| 4 | Perf epistemisch getrennt (author→INFERRED) | erfüllt |
| 5 | Gap „kein fertiges Live-MP3-HU-Repo“ dokumentiert | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |
| 7 | Eigene HU LBA-Instrumentierung | offen (FOLLOW-ON) |

## Lessons → Transfer

- **Callback ist der Hebel**, Full-Image nur Demo.
- USB FS ~1 MB/s reicht für MP3-Bitrate; HU-Burst/Latenz ist das Risiko.
- Host-Cache (Label/Serial) gehört nach `bmw-nbt-evo`, nicht nach MSC-A.
- Kein öffentliches Repo macht bereits „Live-MP3 an Automotive-HU“ — PiDrive bleibt die Nische.

## Bezug

[INVENTORY](../../projects/esp32-msc-gadget-refs/INVENTORY.md) · [evidence](evidence.md) · [`pidrive-2026-msc`](../pidrive-2026-msc/) · [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/) · [`esp32-pidrive-2026-pilot`](../esp32-pidrive-2026-pilot/)
