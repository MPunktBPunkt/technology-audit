# Follow-on ideas (aus esp32-msc-gadget-refs)

```yaml
reuse_outcomes:
  reused: [usb-msc, bmw-nbt-evo]
  new: [virtual-fat, msc-lba-timing-instrument, msc-trace-correlation]
  not_helped: []
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| LBA-Instrumentierung gegen NBT Evo | `msc-lba-timing-instrument` | Fake-MP3 + Delay-Stufen |
| On-the-fly Body statt PSRAM-Full-Image | `virtual-fat`, `usb-msc` | PiDrive Live-Stream |
| Volume-Label/Serial Cache-Tests | `bmw-nbt-evo` | Re-Index-Trigger empirisch |
| Multi-Sektor-Burst Budget | atomic14 Zahlen | Callback ≤ Host-Timeout |

## Checkliste: LBA-/Timing-Instrumentierung (nächster Lab-Schritt)

1. [ ] Statische Fake-MP3 + feste Geometrie (Label/Serial notieren)
2. [ ] `onRead` loggt `t_us,lba,offset,bufsize,dt_us` (CSV)
3. [ ] PC-Lab: `dd`/Copy → Burst-Histogramm + Max-Latenz ohne Abort
4. [ ] Delay-Stufen im Callback (0 / 100 µs / 1 ms / 5 ms …) bis Host-Error
5. [ ] NBT: Cold-Plug vs. Warm; Label unverändert außer Cache-Tests
6. [ ] Auswertung: Prefetch-Fenster, Seek-Sprünge, Idle-Lücken vs. Ton
7. [ ] Evidence-IDs + Korrelation mit PUMP (`msc-trace-correlation`)

Method: [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md).
