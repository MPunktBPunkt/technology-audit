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
| [`callback-reentry-state-lifetime`](callback-reentry-state-lifetime.md) | State/Timer über Callback-Re-Entry (generischer Review Check) | active |
| [`msc-trace-correlation`](msc-trace-correlation.md) | HU-LBA-Traces vs. Diag/`bytesServed`/AV | active |
| [`nbt-medium-identity-resume`](nbt-medium-identity-resume.md) | Decoder-P, MSC-Offset, Cache und FAT-/USB-Identity isolieren | active |
| [`nbt-cache-eviction-play-intent`](nbt-cache-eviction-play-intent.md) | NBT Cache/Prefetch/Eviction, Play-Intent, ID3/APIC und Menüreads isolieren | active |
| [`field-av-offset-correlation`](field-av-offset-correlation.md) | Dateioffset, ausgelieferte Bytes und hör-/sichtbare AV-Marker korrelieren | active |
| [`hu-media-lifecycle`](hu-media-lifecycle.md) | HU-Medienzustand über Remount/Replug/Sleep/Fahrzeugzyklen isolieren | active |
| [`plug-power-reset-isolation`](plug-power-reset-isolation.md) | Brownout, VBUS, Resetreason und HU-Lifecycle trennen | active |
| [`usb-bot-command-observation`](usb-bot-command-observation.md) | CBW/CDB/CSW, BOT-Reset und Callbackgrenzen observe-only erfassen | active |
| [`pcm-clock-drift-jitter-buffer`](pcm-clock-drift-jitter-buffer.md) | Netzwerk-PCM, Clockdrift, Jitterbuffer, Reconnect und Fail-safe gaten | active |
| [`rf-loopback-rds-acceptance`](rf-loopback-rds-acceptance.md) | geschirmte FM-/RDS-/Spektrum-/Empfängerabnahme mit TX-OFF-Gates | active |
| [`usb-wifi-coex-discrimination`](usb-wifi-coex-discrimination.md) | S3 USB↔WiFi: Power / Starve / RF im Lab trennen | active |

## Gate-Coverage aus `next-audits.md`

Die Zuordnung konsolidiert die Todos in wenige Standard-0.7.1-Verfahren.
Alle noch nicht ausgeführten Gates sind präregistriert und `UNKNOWN`; die
Method Notes selbst erzeugen keine Evidence-IDs.

| Todos | Wiederverwendbare Methode / Gate |
|-------|----------------------------------|
| HU-A1, A3, A4, A6, A8 | [`nbt-cache-eviction-play-intent`](nbt-cache-eviction-play-intent.md) |
| HU-A2 | bestehend: [`nbt-medium-identity-resume`](nbt-medium-identity-resume.md) |
| HU-A5 | [`field-av-offset-correlation`](field-av-offset-correlation.md) |
| HU-A7 | bestehend: [`msc-busy-retry-semantics`](msc-busy-retry-semantics.md), bei Bedarf BOT-Beobachtung |
| HU-A9 | [`hu-media-lifecycle`](hu-media-lifecycle.md) |
| HU-A10 | [`usb-bot-command-observation`](usb-bot-command-observation.md) |
| HU-A11 | [`plug-power-reset-isolation`](plug-power-reset-isolation.md) |
| RF-B1, B3 | bestehend: [`hw-path-gate`](hw-path-gate.md), Chip-Scope vor E-0 |
| RF-B2, B6, B7, B9 | [`pcm-clock-drift-jitter-buffer`](pcm-clock-drift-jitter-buffer.md) |
| RF-B4, B5 | [`hw-path-gate`](hw-path-gate.md) für internen/externen Signalpfad; [`rf-loopback-rds-acceptance`](rf-loopback-rds-acceptance.md) für die Abnahme |
| RF-B8, B10 | [`rf-loopback-rds-acceptance`](rf-loopback-rds-acceptance.md) |

### Präregistrierte RF-Reihenfolge

1. **RF-B1** exakten Chip/Board-Scope erfassen; unklarer Scope → `KILL` für
   Pfadclaims.
2. **RF-B3/B5** internen beziehungsweise externen Pfad mit E-0/E-1 aus
   [`hw-path-gate`](hw-path-gate.md) gaten; E-1-`FAIL` stoppt diese Variante.
3. **RF-B4** MPX/RDS-Ort erst nach konkretem Pfad wählen; unvollständige Kette
   bleibt `UNKNOWN`.
4. **RF-B6/B7**, dann **RF-B2/B9** mit
   [`pcm-clock-drift-jitter-buffer`](pcm-clock-drift-jitter-buffer.md);
   Linkverlust ohne fristgerechtes Mute/TX-OFF ist `KILL`.
5. **RF-B8/B10** zuletzt geschirmt mit
   [`rf-loopback-rds-acceptance`](rf-loopback-rds-acceptance.md); Leakage,
   Spektrum oder Fail-safe außerhalb präregistrierter Grenzen ist `KILL`.

## Kandidaten (noch ohne Note)

| Slug | Thema |
|------|--------|
| `lab-prefill-oracle` | Lab-Prefill-/Seed-Validierung |

Anlegen bei erstem **konkreten** Einsatz, nicht spekulativ. Reviews: Methoden sind die transferierbarsten Assets — lieber wenige belastbare Notes als eine Kandidatenliste ohne Ablauf.

**Wann eine Note verdient ist:** derselbe Lab-/Feldablauf wird in ≥2 Projekten oder Kampagnen gebraucht, oder ein Pilot scheitert ohne reproduzierbares Verfahren.
