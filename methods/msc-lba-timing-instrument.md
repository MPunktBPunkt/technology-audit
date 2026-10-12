# Method: MSC LBA / Timing Instrumentation

```yaml
slug: msc-lba-timing-instrument
title: MSC LBA / Timing Instrumentation
status: active
tags: [usb-device, tracing, lab-only]
```

## Zweck

Im USB-MSC **Read-Callback** das genaue Leseverhalten eines Hosts erfassen (LBA, Länge, Intervall, Callback-Latenz), bevor on-the-fly-Inhalte (Fake-MP3 / Live-Body) stabil gegen eine Automotive-HU gefahren werden.

## Voraussetzungen

- ESP32-S2/S3/P4 (oder gleichwertig) mit Device-USB OTG + TinyUSB/USBMSC
- Bekannte statische Fake-MP3 (oder Seed-Body) auf virtuellem FAT
- Host unter Test (PC Lab zuerst, dann Ziel-HU)
- Uhr mit µs-Auflösung (`esp_timer_get_time` o. ä.)

## Ablauf

1. **Baseline-Geometrie** — festes FAT12/16, eine Datei bekannter Länge/CRC; Volume Label + Serial notieren.
2. **Instrument onRead** — pro Aufruf loggen: `t_us`, `lba`, `offset`, `bufsize`, `dt_since_prev_us`, optional running CRC der gelieferten Bytes.
3. **PC-Lab** — sequentielles `dd`/Kopieren der Datei; Burst-Größen und Max-Callback-Latenz ohne Abort messen.
4. **Stress-Latenz** — künstliche Delay-Stufen im Callback (0 / 100 µs / 1 ms / 5 ms …) bis Host Abort / I/O-Error.
5. **Ziel-HU** — gleiche Instrumentierung; Cold-Plug vs. Warm; Label/Serial unverändert lassen außer in gezielten Cache-Tests.
6. **Auswertung** — Histogramm `bufsize` (Sektor vs. Multi-Sektor), Seek-Sprünge, Idle-Lücken, Prefetch-Fenster vor Decode.

## Artefakte

| Artefakt | Inhalt |
|----------|--------|
| `lba-trace-YYYYMMDD-HHMM.csv` | t_us,lba,offset,bufsize,dt_us |
| `geometry.md` | FAT-Typ, Sektoren, Datei-LBA-Range, Label, Serial |
| Evidence-IDs | `EVID-MSC-LBA-…` in Audit |

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Trace deckt volle Datei-LBA-Range | ja, Lücken dokumentiert | stille Lücken ohne Erklärung |
| Callback-Budget bekannt | max `dt` ohne Host-Abort | Abort ohne Schwellenwert |
| HU vs PC getrennt | zwei Trace-Sätze | vermischte Claims |

## Fallstricke

- Logging selbst darf USB Full-Speed nicht sättigen (Ringbuffer → später flush).
- `bufsize` kann &gt; 512 sein — Multi-Sektor als ein Callback behandeln.
- Warm-Caches der HU verfälschen Cold-Prefetch — Serial/Label-Change nur bewusst.
- Throughput-Zahlen aus SD-Backends (atomic14) ≠ on-the-fly-CPU-Budget.

## Beispiel-Einsätze

| Projekt / Audit | Hinweis |
|-----------------|---------|
| `esp32-msc-gadget-refs` | Callback-APIs + Perf-Baseline |
| `pidrive` / `esp32-pidrive` | gegen bestehende Traces / `msc-trace-correlation` |
| `pidrive-2026-bmw-hu` | Host-C Evidence ergänzen |
