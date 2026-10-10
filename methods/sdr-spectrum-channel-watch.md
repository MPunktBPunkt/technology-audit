# Method Note: SDR Spectrum Channel Watch

```yaml
id: sdr-spectrum-channel-watch
related_tech: [sdr-spectrum-fft, pmr446, rtl-sdr]
status: active
```

## Zweck

Kanalisierte Aktivität (z. B. PMR446) über FFT/Energie erkennen, bevor oder während `rtl_fm` hört — mit klarer Trennung Peek vs. Activity-Trigger.

## Voraussetzungen

- Ein RTL-SDR, DVB-Module geblacklisted
- Exklusives Lock (kein paralleles welle-cli/fm)
- Numpy/IQ-Capture-Pfad verfügbar

## Schritte (kurz)

1. Lock als Owner `spectrum`/`scanner` nehmen.
2. Channelized watch über Band-Tabelle (Mittenfrequenzen + BW).
3. Mehrere FFT-Frames mitteln; Kanalenergie vs. Noise.
4. Peek < `trigger_on` nur markieren; Activity erst ab Schwelle; Hysterese `trigger_off`.
5. Optional Autotune → Demod; Hold-Zeit; danach Lock freigeben.
6. Spektrum-Snapshot parallel: Monitor preempten (Stick-Exklusivität).

## Artefakte

- Status-JSON + JSONL-Events (Peek/Activity/Tuned/Error)
- Letztes Spektrum (`/tmp/…spectrum.json` o. Ä.)

## Fallstricke

- welle-cli-Spektrum für UHF nutzen wollen
- Autotune ohne `begin_transition` / Source-State
- USB `Device busy` ohne sysfs-`authorized`-Recovery

## Bezug

PiDrive: `PMR-MONITOR.md`, `SCANNER-PMR.md`, `spectrum.py`.
