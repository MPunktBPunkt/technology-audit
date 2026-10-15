# Method: MSC Host-Read-Semantik (S1–S3)

```yaml
slug: msc-host-read-semantics
title: MSC Host-Read-Semantik (Eager-EOF / Prefetch / Cache-Hit)
status: active
tags: [usb-msc, lab-tool, field, preregistered]
```

## Zweck

Am USB-MSC-Device (hu-probe) Host-Lesen so instrumentieren und auswerten, dass
**Eager-EOF (S1)**, **Prefetch/Auto-Next (S2)** und **Cache-Hit/Replay (S3)**
trennbar werden — ohne PiDrive-Zahlen oder Lab-Linux-Muster als NBT-`FACT` zu
übernehmen.

Desk-Basis: [`msc-host-read-semantics-s1s2s3-2026`](../audits/msc-host-read-semantics-s1s2s3-2026/).

## Voraussetzungen

- GATE-01 Messintegrität soweit für den Lauf freigegeben (sonst nur Lab-Trockenlauf)
- LBA→Datei-Map + bekannte Slot-Größen (Virtual FAT)
- Event-Stream mit `t_us`, READ10 (`lba`/`offset`/`bufsize` oder äquivalent)
- Operator-Marker-Kanal (`markers.jsonl`)
- PiDrive-/Profil-Anker nur als Hypothesenliste, nicht als Pass-Schwellen

Reuse: [`msc-lba-timing-instrument`](msc-lba-timing-instrument.md),
[`msc-trace-correlation`](msc-trace-correlation.md),
[`nbt-cache-eviction-play-intent`](nbt-cache-eviction-play-intent.md),
[`field-av-offset-correlation`](field-av-offset-correlation.md).

## Marker-Protokoll (S2/S3)

| Marker-ID | Bedeutung | Wann |
|-----------|-----------|------|
| `play_start` | Wiedergabe dieses Tracks beginnt (UI und/oder Ohr) | vor Prefetch-/Cache-Claims |
| `track_next` | Wechselabsicht (Auto-Next oder manuell) | S2 |
| `audible_change` | hörbarer Inhalt gewechselt | S2; AV-Korrelation |
| `replay` | derselbe Track erneut **ohne** Replug/Identity-Flip | S3 |
| `stop` | Stop/Pause/Abwahl | Session-Ende / Abbruch |

Regeln:

- Jeder Marker: Session-ID, monotoner Zeitanker (`t_us` bevorzugt), Kurznotiz.
- Ohne `play_start` + (`audible_change` \| `track_next`) → S2 = `UNKNOWN`.
- Ohne `replay` → S3 = `UNKNOWN`.
- Replug/Serial-Change ist **nicht** S3 — das ist Remount/Identity (S4/A2).

## Ablauf

### S1 — Eager-EOF

1. Medium: mind. ein **großer** Slot (≥ 4 MiB) + optional 512 KiB-Kontrolle.
2. Cold oder dokumentierter Warm-State; Identity festhalten.
3. Track wählen; keine Busy-Politik ändern (außer dokumentiert).
4. Trace bis EOF der Datei-LBA-Range oder `stop`/Abwahl.
5. Auswerten: LBA-Monotonie, Bytes-bis-EOF vs. `file_size`.

### S2 — Prefetch / Auto-Next

1. Zwei Slots mit unterscheidbaren Markern (Audio/Stille).
2. `play_start` auf Slot A; warten; `track_next` / Auto-Next beobachten.
3. `audible_change` setzen, sobald B hörbar ist.
4. Auswerten: Reads auf B **vor** `audible_change`; Lead-Zeit nur berichten, nicht aus Profil hardcoden.

### S3 — Cache-Hit / Replay

1. Slot einmal vollständig eager lesen lassen (oder aus S1 übernehmen).
2. `stop`, dann `replay` **ohne** Replug.
3. Auswerten: Body-Reads in Datei-Range nach `replay` (Zielhypothese: keine/kaum).

## Auswerte-Skript-Spez

**Eingabe**

- `events.jsonl` — READ10/BOT-Events mit `t_us`, `lba`, Länge
- `markers.jsonl` — Marker oben
- `geometry.json` — pro Datei: `lba0`, `n_sectors`, `size_bytes`, `uid`

**Ausgabe** `derived/s1s2s3_eval.json` (Beispielschema):

```json
{
  "schema": 1,
  "session_id": "...",
  "scenario": "s2_prefetch",
  "rules": {
    "lba_monotonic": {"result": "PASS|FAIL|UNKNOWN", "detail": {}},
    "bytes_to_eof": {"result": "PASS|FAIL|UNKNOWN", "bytes": null, "file_size": null},
    "reads_before_audible_change": {"result": "PASS|FAIL|UNKNOWN", "next_uid": null},
    "reads_on_replay_no_replug": {"result": "PASS|FAIL|UNKNOWN", "body_reads": null}
  },
  "kill_flags": [],
  "notes": "no golden numeric thresholds from pidrive profile"
}
```

**Regeln (boolean)**

| Key | Pass-Idee | Fail-Idee |
|-----|-----------|-----------|
| `lba_monotonic` | sequenziell in Datei-Range (dok. Toleranz) | große Rücksprünge ohne Marker |
| `bytes_to_eof` | gelieferte Bytes erreichen `file_size` vor Abwahl | klarer Stop weit vor EOF ohne `stop` |
| `reads_before_audible_change` | Next-Slot-Reads mit `t < audible_change` | Next-Reads erst danach / gar nicht bei behauptetem Prefetch |
| `reads_on_replay_no_replug` | nach `replay` keine Body-Reads | Body-Reads trotz Replay ohne Identity-Change |

**Verboten im Skript:** hardcodierte `15`, `65`, Profil-`FACT` als Assert.

## Medium-Empfehlung (S1)

| | 512 KiB | ≥ 4 MiB (empfohlen) |
|--|---------|---------------------|
| Bus-Vollread | ~0,5–0,7 s | mehrere Sekunden |
| Eager vs. Batch-then-Play | **nicht trennbar** | trennbar mit Markern |
| Rolle | Kontrollzelle / PiDrive-L3-Vergleich | **Messzelle S1** |

Nachbarslot für S2: gleiche Größenklasse, anderer Inhalt-Marker. Virtual-FAT-Muster:
feste Dateien in RAM (vgl. `esp32usbmsc` / gadget-refs) — nicht Throughput-Bench.

## Lab-Fußnote (nie NBT)

- Linux `usb-storage` + VFS Read-Ahead / Mass-Storage-Gadget: Burst-Muster eines
  **PC-Hosts** — Kill: nicht als NBT-Prefetch zitieren.
- esp-usb Host-MSC: normale BOT/SCSI-Kommandofolge eines ESP-Hosts — Instrument-
  Kontrast, kein Fahrzeug-Claim.

## Pass / Fail (Kampagnen-Ebene)

| Kriterium | Pass | Fail / Kill |
|-----------|------|-------------|
| Marker vollständig für Szenario | ja | S2/S3 `UNKNOWN` oder Lauf verwerfen |
| Medium S1 ≥ Mess-Slot | ja | nur 512 KiB + Eager-`FACT`-Claim → Kill |
| Epistemik | PiDrive = Hypothese | PiDrive-Zahl als hu-probe-`FACT` |
| Host-Kontrast | getrennt gelabelt | Linux = NBT |

## Fallstricke

- Warm-Cache / Identity-Drift → S3 falsch positiv/negativ (A2 zuerst bei Zweifel).
- Busy-Pacing ändert Read-Tempo — S1–S3 nicht mit Stall-Leiter vermischen.
- WiFi/OTG-Death bricht Timelines — nicht als Host-Semantik deuten.
- `onRead` ohne LBA-Map = keine Datei-Zuordnung.

## Beispiel-Einsatz

| Projekt / Audit | Hinweis |
|-----------------|---------|
| `hu-probe` | Szenarien `s1_eager_eof` / `s2_prefetch` / `s3_cache_hit` |
| `msc-host-read-semantics-s1s2s3-2026` | Desk-Messplan |
| `hu-probe-bmw-s0s2-field-2026` | S0/S2 **Transport** `MEASURED`; Prefetch/Eager/Cache weiter `INFERRED` bis LBA+Marker-Formal |
| `pidrive-2026-bmw-hu` | HU-A1 Startgate vor kausalen Prefetch-Claims |
