# Audit Campaign: msc-host-read-semantics-s1s2s3-2026

```yaml
id: msc-host-read-semantics-s1s2s3-2026
project_id: hu-probe
started: 2026-10-15
ended: 2026-10-15
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: usb-msc
reuse_outcomes:
  reused:
    - usb-msc
    - bmw-nbt-evo
    - virtual-fat
    - msc-lba-timing-instrument
    - msc-trace-correlation
    - nbt-cache-eviction-play-intent
    - field-av-offset-correlation
  new:
    - msc-host-read-semantics
  not_helped:
    - "Linux usb-storage / MSG Read-Ahead = Lab-Kontrast nur; nie NBT-Prefetch."
    - "esp-usb Host-MSC beschreibt Normal-Host-Kommandos, nicht NBT-Timing."
    - "Throughput-Benchmarks (dd) messen Bus/Sonde, nicht Eager/Cache."
  process: "Enges Desk: PiDrive-Claims inventarisieren → LBA-Auswertelogik → Medium/Slots → Messplan S1–S3. Keine NBT-Zahlen, kein WiFi, kein Mazda."
  decisions_touched:
    - pidrive-claims-hypothesis-not-huprobe-fact
    - medium-gt-512kib-for-s1
    - linux-readahead-not-nbt
```

## Ziel

Messplan und Auswerteskript-Spezifikation für hu-probe-Szenarien **S1 Eager-EOF**,
**S2 Prefetch/Auto-Next**, **S3 Cache-Hit/Replay** — PiDrive-/Profil-Claims schärfen,
**nicht** als hu-probe-`FACT` übernehmen. Ergebnis: Marker-Protokoll, LBA-Regeln,
Medium-Empfehlung, Claim→Status-Tabelle. **Keine** neuen NBT-Zahlen.

## Scope

- **Im Scope:** `hu-probe` `profiles/bmw_nbt_evo.json` + `docs/` Szenarien/Schema;
  `technology-audit` `pidrive-2026-msc` / `pidrive-2026-bmw-hu` + Methods;
  PiDrive-Feldartefakte / HU-Facts R15–R21 (Claims-Herkunft);
  TinyUSB/IDF `tud_msc_read10_cb`, ein Virtual-FAT-Muster (`esp32usbmsc`);
  bestehende `esp32-msc-gadget-refs`; Linux/`esp-usb` Host nur als Lab-Fußnote.
- **Nicht im Scope:** Root-Cause WiFi/Coex; Mazda-Übertrag; Wire-Capture;
  HU-Firmware-Leaks; generische Audio-Decoder; `dd`-Throughput als Eager-Proxy;
  Feldmessung in diesem Desk; neue Evidence-IDs mit NBT-Timing-Zahlen.

```text
kill:
  - fremde Host-Muster = NBT-FACT
  - PiDrive-Zahlen als hu-probe-FACT
  - Wire-Claims
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1, Kampagnenartefakte + Report | erfüllt |
| 2 | Primärquellen auf immutable SHA / Evidence-Pfad | erfüllt |
| 3 | Marker-Protokoll S2/S3 (play_start … stop) | erfüllt |
| 4 | Auswerte-Regeln: LBA-Monotonie, Bytes-bis-EOF, Reads-vor-hörbarem-Wechsel, Replay-ohne-Replug | erfüllt |
| 5 | Medium-Empfehlung S1 (Slot vs. 512 KiB) | erfüllt |
| 6 | Tabelle PiDrive-Claim → hypothesis / superseded / needs_field | erfüllt |
| 7 | Keine NBT-Zahlen / kein Mazda / kein WiFi-Root-Cause | erfüllt |
| 8 | C10–C13 Desk; Method `msc-host-read-semantics` | erfüllt |

## Decision Trace

Desk mit Go/No-Go für den **nächsten** S1–S3-Feld-/Lab-Lauf (**C10**).

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| hu-probe-Profil-Werte nur als Hypothesen-Anker | Sind `eager_eof` / `prefetch_lead_s≈15` / `cache_hit` hu-probe-`FACT`? | `EVID-MSCRHS-2026-10-15-001`–`004` | Nein — Herkunft PiDrive; Status `needs_field` / `hypothesis` | `DISCOVERED DURING TEST` |
| S1-Medium ≫ 512 KiB (+ 512 KiB-Kontrollslot) | Kann 512 KiB Eager vs. Batch trennen? | `005`, ANALYSE B1/B5 | Nein — Bus-Read ≈0,6 s; größere Slots Pflicht | `KNOWN BEFORE TEST` (PiDrive); Desk bestätigt |
| Auswerte-Skript an `tud_msc_read10_cb` (lba, offset, bufsize) | Reicht App-Callback für LBA-Folgen? | `006`–`008` | Ja für Datei-vs-Prefetch-Klassifikation; CBW-Tag optional (Reuse BOT) | `DISCOVERED DURING TEST` |
| Linux-Read-Ahead nur Lab-Fußnote | Darf VFS/MSG-Muster NBT-Prefetch belegen? | `009` | Nein — Kill-Regel | `KNOWN BEFORE TEST` |

## Engineering Review Checks

Ziel: hu-probe Capture/Auswertung vor S1–S3 (**C11**).

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001`–`004` | Profil `class: FACT` nicht in Session-Diff als hu-probe-PASS werten | `DISCOVERED DURING TEST` |
| `005` | Geometrie: mind. ein Slot ≥ mehrerer MiB; 512 KiB nur Kontrollzelle | `DISCOVERED DURING TEST` |
| `006`–`008` | Logger: `t_us`, `lba`, `offset`, `bufsize`; LBA→Datei-Map vor Lauf | `DISCOVERED DURING TEST` |
| `003`, Method | Marker `play_start`/`audible_change`/`track_next` Pflicht vor Prefetch-Claim | `KNOWN BEFORE TEST` |
| `009` | Lab-`dd`/VFS-Traces nie mit `scenario=s2_prefetch` mergen | `KNOWN BEFORE TEST` |

## Kill-Kriterien

Präregistriert für künftigen S1–S3-Lauf (**C12**); hier kein Messlauf.

**Hypothese:** Mit Marker-Protokoll + LBA-Regeln lassen sich Eager-EOF, Prefetch und
Cache-Hit am NBT **reproduzierbar klassifizieren** — Zahlen kommen erst aus dem Lauf.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | PiDrive-/Sim-Zahlen als hu-probe-`FACT` ohne neue Session-IDs | Integritäts-Kill |
| 2 | Linux-Host- oder esp-usb-Host-Muster als NBT-Prefetch/`FACT` | Integritäts-Kill |
| 3 | Wire-/Paketebene behauptet | Integritäts-Kill |
| 4 | S1 nur mit 512 KiB-Slots und Claim „Eager bewiesen“ | präregistriert — Lauf ungültig für Batch-vs-Eager |
| 5 | S2/S3 ohne Marker `play_start`/`audible_change`/`replay` | präregistriert — Prefetch/Cache nicht auswertbar |
| 6 | Mazda-/andere-HU-Übertrag stiller Defaults | Integritäts-Kill |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| **MSC Host-Read-Semantik S1–S3** | [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md) |
| LBA/Timing-Instrument | [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) |
| Trace-Korrelation | [`msc-trace-correlation`](../../methods/msc-trace-correlation.md) |
| Cache/Prefetch/Intent | [`nbt-cache-eviction-play-intent`](../../methods/nbt-cache-eviction-play-intent.md) |
| AV-Offset/Marker | [`field-av-offset-correlation`](../../methods/field-av-offset-correlation.md) |

## Bezug Inventar

- Projekt: [`hu-probe`](../../projects/hu-probe/)
- Sheet-Reuse: [`usb-msc`](../../technologies/usb-msc/SHEET.md), [`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md), [`virtual-fat`](../../technologies/virtual-fat/SHEET.md)
- Prior-Audits: [`pidrive-2026-msc`](../pidrive-2026-msc/), [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/), [`esp32-msc-gadget-refs-2026-foreign`](../esp32-msc-gadget-refs-2026-foreign/)
- hu-probe-Szenarien: `s1_eager_eof` · `s2_prefetch` · `s3_cache_hit` ([SZENARIEN](https://github.com/MPunktBPunkt/hu-probe/blob/main/docs/SZENARIEN.md))
- Open gates (Profil): `HU-PROBE-GATE-01`, `HU-A1`, `HU-A2`, … — Instrument vor Zahlen

## Ergebnisse (festgelegt)

| # | Artefakt | Ort |
|---|----------|-----|
| 1 | Marker-Protokoll S2/S3 | Method + [`evidence`](evidence.md) § Marker |
| 2 | Auswerte-Regeln | Method § Auswerte-Skript-Spez |
| 3 | Medium-Empfehlung S1 | Method + Evidence `005` |
| 4 | PiDrive-Claim → Status | Evidence § Claim-Tabelle |
| — | Evidence-Register | [`evidence.md`](evidence.md) |
| — | Kurzbericht | [`docs/reports/2026-10-15-msc-host-read-semantics-s1s2s3.md`](../../docs/reports/2026-10-15-msc-host-read-semantics-s1s2s3.md) |

## Knowledge Feedback

**C13:** n/a Lab/Field — Desk-only. Rückkanal = Method + hu-probe FOLLOW-ON.

| Ergebnis | Evidence-ID | Zurück in |
|----------|-------------|-----------|
| Claim-Trennung / Messplan | `EVID-MSCRHS-2026-10-15-*` | Method · [`hu-probe` FOLLOW-ON](../../projects/hu-probe/FOLLOW-ON-IDEAS.md) |
| LBA-Callback-Contract | `006`–`008` | Reuse `usb-msc` / gadget-refs (kein neues Sheet) |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 präregistrierte Kill-Kriterien | PASS; Status offen (kein Messlauf) |
| C13 Knowledge Feedback | n/a dokumentiert |

## Lessons → Transfer

- hu-probe `bmw_nbt_evo.json` aggregiert **PiDrive-Feldmodell**; epistemisch für die Sonde = Hypothesen-Anker, nicht Golden-FACT.
- `prefetch_lead_s≈15` stammt aus HU-Fact **R21** ([S], s1-morgen) + Lab-Anker G4N — nicht aus einem hu-probe-Lauf.
- 512 KiB-Slots sind für S1 **zu klein** für Batch-vs-Eager; größerer Medium-Körper ist Messvoraussetzung.
- `tud_msc_read10_cb(lba, offset, bufsize)` reicht für LBA-Folgen→Datei/Prefetch; CBW-Hooks sind optional (Reuse).

## Offene Punkte nach Abschluss

- Feld/Lab S1–S3 nach GATE-01-Freigabe; neue Evidence-IDs nur aus Sessions
- hu-probe-Profil: `class: FACT` → Anker/`hypothesis` umetikettieren (Upstream)
- HU-A1 Startgate bleibt Voraussetzung für kausale Prefetch/Cache-Claims
