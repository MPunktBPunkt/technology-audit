# methods/

Analyseverfahren, die in Audits und Project Applications wiederverwendet werden.

Vorlage: [`templates/method-note.md`](../templates/method-note.md)

## Index

| Slug | Thema | Status |
|------|--------|--------|
| [`ftms-capability-probe`](ftms-capability-probe.md) | FTMS Caps/Wirkung vor Coach-Firmware | active |
| [`sdr-spectrum-channel-watch`](sdr-spectrum-channel-watch.md) | RTL-SDR FFT + Kanal-Watch (PMR/Airband) | active |
| [`hw-path-gate`](hw-path-gate.md) | RF/Clock E-0…E-3 Gates vor Varianten-Sheet | active |
| [`kb-cross-check`](kb-cross-check.md) | KB als Reasoning-Bausteine prüfen (Blindtest) | active |
| [`msc-lba-timing-instrument`](msc-lba-timing-instrument.md) | MSC Read-Callback LBA/Burst/Latenz (Lab→HU) | active |
| [`msc-busy-retry-semantics`](msc-busy-retry-semantics.md) | TinyUSB Busy/`return 0` vs. Block vs. ASYNC testen | active |
| [`msc-trace-correlation`](msc-trace-correlation.md) | HU-LBA-Traces vs. Diag/`bytesServed`/AV | active |

## Kandidaten (noch ohne Note)

| Slug | Thema |
|------|--------|
| `field-av-correlation` | Audio/Video-Fenster vs. Dateioffset |
| `lab-prefill-oracle` | Lab-Prefill-/Seed-Validierung |

Anlegen bei erstem **konkreten** Einsatz, nicht spekulativ. Reviews: Methoden sind die transferierbarsten Assets — lieber wenige belastbare Notes als eine Kandidatenliste ohne Ablauf.

**Wann eine Note verdient ist:** derselbe Lab-/Feldablauf wird in ≥2 Projekten oder Kampagnen gebraucht, oder ein Pilot scheitert ohne reproduzierbares Verfahren.
