# hu-probe — Heimfahrt / Remount / Scheduler / Prefetch — 2026-10-22

**Delta-Audit seit Media-Leiter 2026-10-22**

| Feld | Wert |
|------|------|
| Repo | `MPunktBPunkt/hu-probe` @ **`4fdf519`** (Grok-Übergabe; Gesamtbericht `28249de`) |
| FW Pin | Capture **0.3.17** · Probe `.89` · `ram_offline` / `drive_home` · one-shot ab **0.3.19** |
| Audit | [`audits/hu-probe-heimfahrt-2026-10-22/`](../../audits/hu-probe-heimfahrt-2026-10-22/) |
| Prior | [`2026-10-22-hu-probe-media-ladder`](2026-10-22-hu-probe-media-ladder.md) |

---

## 1. Kurzfazit

Die Heimfahrt ist der stärkste Modell-Schritt nach der Media-Leiter:

1. **Remount ≠ Cold Start** — `#22` zweite Mount-Signatur mit **395xxx**-Probe; `#23` normale Signatur, aber Resume in **ROCK/R04**-Kontext.
2. **Drei Read-Modi** — Head (`0/240+240/240+480/32`), Eager Body (~93–99 % Coverage), Neighbor/Partial mit **LBA-Interleave**.
3. **Prefetch-Lead kontextabhängig** — MIX ~7 s situativ; ROCK/CLASSIC **140–240 s**. „8 s“ als Konstante **REJECTED**.
4. **Eager ≠ Play Intent** — C0x fast vollständig hintereinander, Atom-Lücken teils **~4 ms**, ohne Audible.
5. **TUR 2,2388 s** / 4‑KiB p50 **3,896 ms** / Bulk **240** / BUSY **1,623 s** abandoned ohne Reset — Lieferseite stabil.

Nächster Sprung: **Audible GATE + Play-Intent**, nicht weitere Ladder-Varianten.

---

## 2. Datenbasis

| Trip | Session | Ende | Events | Remounts | Kern |
|------|---------|------|-------:|---------:|------|
| `#22` | `12777_bmw_drive_home` | `power_loss` | 50 187 | 2 | MIX lang + 395xxx-Remount |
| `#23` | `20261022-171751_bmw_drive_home` | `max_duration` | 24 456 | 2 | R04-Schleife + Scheduler/Eager |
| `#24` | `20261022-173030_bmw_drive_home` | `power_loss` | 2 924 | 1 | nur C01, kurz |

Alle: `integrity_pass`, `upload_status=delivered`, Medium `drive_mix`.

---

## 3. Modellkorrektur

### 3.1 Remount

```text
USB Remount
  ├── normale Init-Signatur          (#23 @448,5 s)
  └── oder 395xxx-Positionsprobe     (#22 @595,7 s)  ← Semantik UNKNOWN
        ▼
  Kontextaufnahme (nicht Datei 1 des Mediums)
        ▼
  Head → Eager / Neighbor Prefetch
```

### 3.2 Read-Modi & Scheduler

| Modus | Muster | Epistemik |
|-------|--------|-----------|
| Head/Selection | `0/240`, `240/240`, `480/32` | FACT |
| Eager Body | ~90–99 % File-Coverage | FACT |
| Neighbor + Interleave | Folgetracks / R04-Regionen verzahnt | FACT / STRONG |
| Globaler Elevator | — | **SUPERSEDED** |
| Lokales `tail_then_head` | Media-Leiter `cache_place` | bleibt erklärbar |

### 3.3 Prefetch-Lead

| Kontext | Lead | Status |
|---------|------|--------|
| MIX `#22` M01/M02 | ~7,2–7,7 s | situationsgebunden FACT |
| ROCK/CLASSIC `#23` | 140–237 s | FACT |
| „8 s HU-Parameter“ | — | **REJECTED** |

---

## 4. PiDrive-Vertrag (geschärft)

| Ebene | Stand nach Heimfahrt |
|-------|----------------------|
| Struktur / FAT / Head ~80 KiB | Pflicht (unverändert) |
| 240-Block / ~1 MiB/s / Multi-Track | beherrschbar |
| Neighbor Eager / Partial Refill | erwarten; ≠ Play |
| BUSY / Backpressure | HU setzt fort ohne Reset |
| Remount | Zustand/Kontext möglich — kein Flush annehmen |
| Audible / Intent / Cache-Key / 395xxx | **offen** (P0/P1) |

---

## 5. Ampel

| Bereich | Status |
|---------|--------|
| Offline Trip Upload `#22`–`#24` | **grün** |
| Remount ≠ Cold Start | **grün** STRONG |
| Eager + Neighbor Prefetch | **grün** |
| LBA-Scheduler / Interleave | **grün** STRONG |
| TUR / 4‑KiB / 240 | **grün** |
| Prefetch-Lead Konstante | **rot** verworfen |
| Play Intent / Audible | **rot/gelb** offen |
| Cache-Key / 395xxx | **gelb** offen |

---

## 6. Auftrag Next

1. **P0** hörbarer Marker → GATE-01 + Korrelation Read↔Play.  
2. **P0** Play-Intent (Eager/Neighbor ≠ Decode).  
3. **P1** Cache-Key / `seq_ident`.  
4. **P1** 395xxx-Remount-Semantik.  

**Nicht tun:** Media-Ladder nur für Prefetch-Zahlen; Lead=8 s; Remount=Cold Start; großer Read=Play.

---

## 7. Verweise

- Audit: [`audits/hu-probe-heimfahrt-2026-10-22/`](../../audits/hu-probe-heimfahrt-2026-10-22/)
- Upstream: `docs/feld/2026-10-22-gesamtbericht-heimfahrt.md`,  
  `docs/feld/2026-10-22-uebergabe-heimfahrt-grok.md` @ `4fdf519`
- Prior: [`2026-10-22-hu-probe-media-ladder`](2026-10-22-hu-probe-media-ladder.md)
