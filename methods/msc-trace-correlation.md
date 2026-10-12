# Method: MSC Trace Correlation (Host vs Device Diag)

```yaml
slug: msc-trace-correlation
title: MSC Trace Correlation (Host vs Device Diag)
status: active
tags: [usb-device, tracing, field-verified]
```

## Zweck

HU-LBA-Traces (oder Lab-Host-Reads) mit Device-Diagnose (`bytesServed`, Seed/Live-Fenster, Play-Guess) zeitlich korrelieren — ohne Host-Timing ins `usb-msc`-Sheet zu ziehen.

## Voraussetzungen

- Instrumentierter MSC-Pfad (`msc-lba-timing-instrument` oder bestehende FW-Traces)
- Device-Diag-Log (PiDrive: `bytesServed`, map frozen, underruns)
- Gemeinsame Zeitbasis oder Event-Marker (Plug, GO, Track-Ende)

## Ablauf

1. Marker setzen (Cold-Plug, Play-Start, Auto-Next).
2. LBA-Fenster der Mediendatei(en) aus Geometrie ableiten.
3. Trace-Segmente den Markern zuordnen (Prefetch vs. Body vs. Re-Read).
4. `bytesServed` / Live-Bytes gegen erwartete Fensterlänge prüfen.
5. Claim nur mit Evidence-ID (C) formulieren — nicht als MSC-Spec.

## Artefakte

- Korrelationsnotiz + verlinkte Trace/Diag-Dateien
- Evidence-Zeilen im Host-Audit (`bmw-nbt-evo` / `pidrive-2026-bmw-hu`)

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Fenster × Bytes passen | ±Toleranz dokumentiert | Bytes ohne LBA-Erklärung |
| Lab≠Feld getrennt | getrennte IDs | Lab-PASS als Feld-Ohr |

## Fallstricke

- Warm-konfigurierte Traces ≠ „Sequenz tot“ (historisch `REJECTED` in PiDrive).
- Türöffnen/Re-Read kann zusätzliche Bursts erzeugen — Kausalität separat markieren.

## Beispiel-Einsätze

| Projekt / Audit | Hinweis |
|-----------------|---------|
| `pidrive-2026-bmw-hu` | bestehende EVID-USBMSC / BMWHU |
| `esp32-msc-gadget-refs` | Lab-PC Baseline vor HU |
