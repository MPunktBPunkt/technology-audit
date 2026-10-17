# Audit Campaign: pidrive-2026-10-17-prefetch-livelock

```yaml
id: pidrive-2026-10-17-prefetch-livelock
project_id: pidrive
started: 2026-10-17
ended: null
status: active
profile: ops-field
standard_version: "0.7.1"
tech_slug: bmw-nbt-evo
prior_audit: pidrive-2026-bmw-hu
related_audits:
  - pidrive-2026-bmw-hu
  - msc-host-read-semantics-s1s2s3-2026
  - hu-probe-bmw-s0s2-field-2026
upstream_pin:
  repo: https://github.com/MPunktBPunkt/pidrive
  commit: d50196e
  fw: "0.4.53-dev"
  stall: off
  uart: false
reuse_outcomes:
  reused:
    - bmw-nbt-evo
    - usb-msc
    - virtual-fat
    - nbt-cache-eviction-play-intent
    - msc-host-read-semantics
    - nbt-medium-identity-resume
  new: []
  not_helped:
    - "readCount/playRejectCount allein als Stuck-Marker (167/136 = Quiet-Plateau)"
    - "Stuck = USB tot / kein Guess möglich"
  process: "Tri-Review GPT/Grok/Mistral + Rohdaten-Nachrechnung Status+Polls; Patterns als C-Evidence, keine Sheet-A-Übernahme ohne Capture."
  decisions_touched:
    - quiet-vs-storm-morphology
    - reads-minus-rej-invariant
    - meta-bytes-session-constant
    - guess-during-storm
    - hostabs-overshoot-m27
```

## Ziel

Abend-Feld `feld-go-abend-01` (FW `0.4.53-dev`, Stall aus) auf **Messmuster**
reduzieren: Prefetch-Livelock vs. Post-Ton-Quiet, Quiet- vs. Storm-Stuck,
Meta-Sättigung, Head-/Mid-file-Dominanz, Guess-im-Storm, hostAbs-Overshoot.
Konsens + Nachrechnung: Upstream
[`TRI-REVIEW-ABEND-2026-10-17.md`](https://github.com/MPunktBPunkt/pidrive/blob/d50196e/docs/betrieb/artifacts-2026-10-17-feld/TRI-REVIEW-ABEND-2026-10-17.md)
(`pidrive@d50196e`).

## Scope

- **Im Scope:** Status-Snapshots + Status-Polls aus `feld-go-abend-01/`;
  Invarianten und Morphologie-Klassifikation; Epistemik FACT/INFERENCE/UNKNOWN;
  Verknüpfung zu Pilot-2 [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/);
  Auftrag für nächstes Feld (UART → Stuck-Capture → Reset-Isolation).
- **Nicht im Scope:** Panic-Root-Cause ohne UART; Stall-Leiter (M23) vor stabilem
  Guess; Sheet-A-Claims „NBT liest immer X“ ohne LBA-/MessCapture-Klasse;
  Rohdaten-Spiegelung in diese KB; Soft-Serial = Panic.

```text
kill:
  - (167 Reads, 136 Rejects) allein = Stuck / USB-tot
  - Prefetch-Livelock = kein Play-Guess möglich
  - Meta/FAT/DIR-Re-Enumeration als Ursache des Livelock-Traffics
  - Panic „gefixt“ (Abend: Panic beobachtet, UART fehlt)
  - M24 VID-alone = Ordner-/Cache-Beweis
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Kampagne + Evidence-Register (C) gegen `pidrive@d50196e` | erfüllt |
| 2 | Invariante `readCount − playRejectCount ∈ {31,32}` über Abend-Status | erfüllt — `EVID-BMWHU-2026-10-17-001` |
| 3 | Quiet-Plateau ≠ Stuck-Marker; Zwei Morphologien Q/S dokumentiert | erfüllt — `002`, `003` |
| 4 | Meta-Bytes session-konstant; Livelock = File-Body | erfüllt — `004` |
| 5 | Guess-im-Storm (Poll 17:58:21) als FACT | erfüllt — `005` |
| 6 | fromHead rar / midFile dominant; fav2 oft voll ohne Play | erfüllt — `006`, `007` |
| 7 | hostAbs-Overshoot nach Tonfenster (M27) | erfüllt — `008` |
| 8 | Application `bmw-nbt-evo` (pidrive) um Abend-Muster ergänzt | erfüllt |
| 9 | Nächstes Feld: UART + Stuck-Capture (Q vs S) mit LBA/Klasse | offen |
| 10 | C10–C13 für Abend-Kampagne | erfüllt (Desk-Nachrechnung; Kill präregistriert) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| 167/136 ist Quiet-Plateau, kein Stuck-Beweis | Gilt `reads−rej∈{31,32}` und `pref≈8` auch post-Ton / after-plug? | `001`, `002` | Stuck braucht Zusatzachsen (pref, midFile, stream, Ohr) | `DISCOVERED AFTER TEST` (Nachrechnung) |
| Zwei Stuck-Formen (Quiet vs Storm) | Trennen pref/midFile/bytesFile Storm von Quiet? | `003` | Stuck-Capture P0; Klasse P⊕C vs Index-only | `DISCOVERED AFTER TEST` |
| Livelock ≠ Guess unmöglich | Kommt `guess≥1` bei steigenden Rejects? | `005` | M22 weiter beobachten; Storm blockiert nicht absolut | `DISCOVERED DURING TEST` |
| Traffic = File-Body, nicht Meta-Rescan | Ändern sich bytesDir/Fat/Meta/Boot? | `004` | Fokus Play-Intent / Body-Reads | `DISCOVERED AFTER TEST` |
| hostAbs-Overshoot = Messfakt (M27) | hostAbs > expect/file end nach Fenster? | `008` | Cursor-Modell dokumentieren; kein Decoder-Claim | `DISCOVERED DURING TEST` |

## Engineering Review Checks

Zielcode/Telemetrie: `esp32.pidrive` Status/`slotMap` + Poll-Schema (**C11**).
Kein neuer Firmware-Fix in dieser Kampagne.

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001`/`002` | Dashboard/Alerts: nie nur `readCount`/`playRejectCount` als Stuck-Flag | `DISCOVERED AFTER TEST` |
| `003` | Stuck-Capture muss Morphologie (pref, fav0.midFile, bytesFile) mitschreiben | `DISCOVERED AFTER TEST` |
| `004` | Claims „erneute FAT-Enumeration“ nur mit steigenden Meta-Bytes | `DISCOVERED AFTER TEST` |
| `005` | Play-Guess-Logik: Storm darf Guess nicht als hard-impossible behandeln | `DISCOVERED DURING TEST` |
| `008` | hostAbs/expectOff: Overshoot ≠ Stream-Fehler ohne Ohr-/Ring-Kontext | `DISCOVERED DURING TEST` |

## Kill-Kriterien

**Hypothese H1:** Prefetch-Livelock ist ein **File-Body-/Play-Intent**-Problem
(HU liest weiter ohne Transition Prefetch→Guess), erkennbar an session-konstanten
Meta-Bytes und `reads−rej∈{31,32}`.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | In derselben Session steigen `bytesDir/Fat/Meta/Boot` proportional zum Reject-Sturm | offen (Abend: nicht beobachtet) |
| 2 | Alle Stuck-Zustände zeigen `readCount` stagnierend und USB/OTG down | offen — Abend widerspricht (Storm lebendig) |
| 3 | `guess` bleibt in Storm-Läufen mit n≥10 immer 0 | offen — ein Gegenbeispiel `005` |

**Hypothese H2:** `(167,136)` markiert Stuck.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Dieselbe Zählerlage bei Post-Ton / after-plug ohne Stuck-Symptom | **killed** — `002` |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| NBT Cache / Play-Intent | [`methods/nbt-cache-eviction-play-intent.md`](../../methods/nbt-cache-eviction-play-intent.md) |
| MSC Host-Read-Semantik | [`methods/msc-host-read-semantics.md`](../../methods/msc-host-read-semantics.md) |
| Medium Identity / Resume | [`methods/nbt-medium-identity-resume.md`](../../methods/nbt-medium-identity-resume.md) |
| MSC Trace-Korrelation | [`methods/msc-trace-correlation.md`](../../methods/msc-trace-correlation.md) |
| HU Media Lifecycle | [`methods/hu-media-lifecycle.md`](../../methods/hu-media-lifecycle.md) |

## Muster-Kurzkarte (Nachrechnung)

Klassifikation über 17 Status-Snapshots `feld-go-abend-01/status/`:

| Klasse | Kennzeichen | Beispiele |
|--------|-------------|-----------|
| Quiet-Plateau | `reads/rej≈167/136`, `pref≈8`, Meta konstant | `1752-after-plug`, `bayern-ton-*`, `bayern-notone`, `replug-180335` |
| Stuck-Q | Quiet-Zähler **ohne** neuen Guess/Ohr-Ton | `bayern-notone`, `replug-180335` |
| Stuck-S / Storm | `pref` 200–2200+, `fav0.midFile` 600–2000+, `bytesFile` → MiB | `tip-rock`, `rst-rock`, `all-files`, `stuck-1801` |
| Post-Ton Quiet | Quiet + oft `streamSlot=1`, hostAbs≥expect | `bayern-ton-175402` (+67 876), `bayern-ton2/3` (+859 417) |

**Zentrale offene Frage (übernommen):** Was liest der NBT im Prefetch-Livelock
(UID/LBA/Klasse), und warum wird daraus (meist) kein Play-Guess — auch über
ESP-RST hinweg?

## Ampel → nächstes Feld

| ID | Status | Hinweis |
|----|--------|---------|
| M20 | ☑ n≥3 Klasse A; Session-stabil ✗ | UART fehlt |
| M21 | ☑ ~6–7 s; Ring 8,2 s | |
| M22 | ☑/☐ labil; Storm-Guess möglich | `005` |
| M23 | ☐ | blockiert bis Guess stabiler |
| M24 | ☑ Gate; VID-allein geschwächt | |
| M25 | ☐ | Identity-Zeitpunkt |
| M27 | ☐ Doku | Overshoot FACT `008` |
| UART | ☐ P0 | |

**Reihenfolge:** UART → Stuck-Capture (Q vs S) → Reset-Isolation A–D →
Guess-Verteilung n≥10 → M25 → M23.

## Knowledge Feedback

| Ziel | Aktion | Status |
|------|--------|--------|
| [`projects/pidrive/applications/bmw-nbt-evo.md`](../../projects/pidrive/applications/bmw-nbt-evo.md) | Abend-Muster als C-Claims + Evidence-IDs | erfüllt (Exit #8) |
| [`technologies/bmw-nbt-evo/SHEET.md`](../../technologies/bmw-nbt-evo/SHEET.md) | **kein** A-Claim aus Abend ohne Capture | bewusst zurückgehalten |
| [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/) | Querverweis + Exit #6 Kontext | siehe Kampagnen-Notiz dort |

## Artefakte (Upstream, nicht gespiegelt)

Basis: `https://github.com/MPunktBPunkt/pidrive/blob/d50196e/docs/betrieb/artifacts-2026-10-17-feld/`

- [`TRI-REVIEW-ABEND-2026-10-17.md`](https://github.com/MPunktBPunkt/pidrive/blob/d50196e/docs/betrieb/artifacts-2026-10-17-feld/TRI-REVIEW-ABEND-2026-10-17.md)
- [`MASSNAHMEN-NACH-TRI-REVIEW-2026-10-17.md`](https://github.com/MPunktBPunkt/pidrive/blob/d50196e/docs/betrieb/artifacts-2026-10-17-feld/MASSNAHMEN-NACH-TRI-REVIEW-2026-10-17.md)
- [`UEBERGABE-NAECHSTE-KI-2026-10-17-FELD.md`](https://github.com/MPunktBPunkt/pidrive/blob/d50196e/docs/betrieb/artifacts-2026-10-17-feld/UEBERGABE-NAECHSTE-KI-2026-10-17-FELD.md)
- [`feld-go-abend-01/`](https://github.com/MPunktBPunkt/pidrive/tree/d50196e/docs/betrieb/artifacts-2026-10-17-feld/feld-go-abend-01)

Evidence: [`evidence.md`](evidence.md).
