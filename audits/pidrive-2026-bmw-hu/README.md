# Audit Campaign: pidrive-2026-bmw-hu

```yaml
id: pidrive-2026-bmw-hu
project_id: pidrive
started: 2026-10-05
ended: null
profile: ops-field
standard_version: "0.7.0"
revalidated_from: "0.6.6"
revalidated: 2026-10-13
status: active
pilot: 2
prior_audit: pidrive-2026-msc
next_pilots: [avrcp]
tech_slug: bmw-nbt-evo
reuse_outcomes:
  - new: [bmw-nbt-evo]
  - layer: "C-host claims stay in Application; usb-msc stays protocol"
  - sharpened: "0.7.0 Decision Trace / Review Checks / Kill / Feedback; host-variant scope NBT Evo"
  - process: "0.6.6 parity 2026-10-11; 0.7.0 ops parity 2026-10-13 (no new field session)"
  - not_transferred: "HU timing → usb-msc sheet; NBT → other BMW HU"
  - decisions_touched: [E7-go, field-go-S6, ring-limit-rejected, psram-not-default]
```

## Ziel

**BMW NBT Evo** als zweiten Pilot durch das Framework: Technology Sheet (A) + Application (C) + Evidence — Host-Verhalten getrennt von USB-MSC-Spec und PiDrive-Device-Impl (**B** in `usb-msc`).

**Revalidation 2026-10-11:** Prozess-Parität **0.5.1 → 0.6.6**. Historie: [DELTA](DELTA.md).

**Field Feedback 2026-10-12:** E7/S6 Busy-Pacing am NBT (~65 s vs. ~6 s Stall-off) → `EVID-BMWHU-2026-10-12-*`. Exit #6 (Sender/Menü-Gate) bleibt **offen**.

**0.7.0-Nachzug 2026-10-13:** Decision Trace, Engineering Review Checks, Kill-Kriterien, Upstream-Links — kein neuer Feldlauf; Wissenszeitpunkte nicht rückdatiert ([Revalidation-Bericht](../../docs/reports/2026-10-13-v0.7.0-pidrive-revalidation.md)).

## Scope

- Im Scope: Sheet `technologies/bmw-nbt-evo/`; Application; Evidence für C-Claims; Reifegrade; Verknüpfung zu MSC-Application; 0.7.0 C10–C13.
- Nicht im Scope: vollständiges HU-Reverse-Engineering; AVRCP als USB-C-Duplikat (→ radio-bt / Gateway); neue Feldmessungen in diesem Nachzug.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Sheet `technologies/bmw-nbt-evo/SHEET.md` (nur A) | erfüllt |
| 2 | Application mit C-Claims (aus MSC übernommen) | erfüllt |
| 3 | Evidence-Register (C-Layer) | erfüllt |
| 4 | MSC-Application: C gekürzt, Verweis hierher | erfüllt |
| 5 | Inventar / Indexe aktualisiert | erfüllt |
| 6 | Feld-AV PASS (Ohr) — Sender-Slots / Meta-Menü-Gate | offen — getrennt vom Busy-Pacing-Tonfenster 2026-10-12 (`EVID-BMWHU-2026-10-12-002`). C′ Feld PASS 2026-10-05 · [MSC-AKTUELL](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) |
| 7 | Revalidation 0.6.6: Gaps geschlossen + Host-Scope + DELTA | erfüllt (2026-10-11) |
| 8 | Knowledge Feedback Busy-Pacing E7/S6 → Evidence + Applications + Upstream-Links | erfüllt (2026-10-13) |
| 9 | 0.7.0 C10–C13 (Decision Trace / Review Checks / Kill / Feedback) | erfüllt (2026-10-13; Kill für E7/S6 teils retro gekennzeichnet) |

## Decision Trace

Ops-field mit Go/No-Go (**C10**). Spalte „Wissenszeitpunkt“: Stand *zum Entscheid*, nicht heutiges Wissen.

| Entscheidung | Phase | Benötigte Frage | Evidence-ID | Wissenszeitpunkt | Konsequenz |
|--------------|-------|-----------------|-------------|------------------|------------|
| Ring ≈ Tonfenster (48 KiB ~8 s) | Feld S3 08.10. | Warum nur ~5–6 s Ton? | Upstream S3-Analyse (keine BMWHU-ID) | DURING S3 | Stall oder großer Puffer als Dauerstrom-Pfad |
| Ring = harte Dauerstrom-Grenze? | bis vor S6 | Dauerstrom ohne größeren Ring? | `EVID-BMWHU-2026-10-12-005` | Annahme vor S6; **AFTER S6 → REJECTED** | PSRAM/Ring nicht Default |
| MSC Prefetch/Burst | 04.–05.10. | Liest HU blockweise? | `EVID-USBMSC-2026-10-04-001` | DURING Pilot | Device muss Burst aushalten |
| Seed / Cold-Body / C′ | 04.–05.10. | Geht Seed an HU? | `EVID-USBMSC-2026-10-04-004`/`005`, `EVID-BMWHU-2026-10-05-001` | DURING | Seed-/Menü-Gates |
| Busy/Stall als Hebel | S3-Analyse + Desk 12.10. | Device bremst READ auf Producer-Takt? | `EVID-TINYUSB-MSC-2026-10-12-001`/`002` | Desk BEFORE Feld; Host C damals UNKNOWN | E7 priorisieren |
| Lab E7 PC Go | Lab 12.10. | PC akzeptiert Busy ≥~700 ms/4 KiB? | Lab [`ERGEBNIS`](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-12-lab/lab-e7-ladder/ERGEBNIS.md) | DURING Lab | Feld-Go freigeben |
| Field-Go Stall OTA | S6 Prep | Q11 Klasse A + Lab L1? | Ops `E7-FELD.md` / `GO.md` | BEFORE Stall-OTA | OTA `0.4.48` nur mit Go |
| E7 Busy-Pacing NBT | S6 12.10. | NBT akzeptiert BUSY über Ringfenster hinaus? | `EVID-BMWHU-2026-10-12-001`–`004` | DURING/AFTER S6 | Busy = Produktkern |
| PSRAM gegen Burst | nach S6 | Primärlösung? | `EVID-BMWHU-2026-10-12-005` | AFTER S6 | nein — Fixed Huge File + BUSY |
| Menü-Latenz unter Stall | S6 / S7-Plan | Warum ~20 s? | `EVID-BMWHU-2026-10-12-006` | DURING S6 (Phänomen); Mechanismus INFERRED | S7 Startup-Usability |
| Rock 8 MiB oft stumm | S6 | Alle Stationen gleich? | `EVID-BMWHU-2026-10-12-007` | DURING S6 | Resume-P / Identity; nicht „alle gleich“ |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact. TinyUSB-Desk: [`tinyusb-msc-busy-retry-2026`](../tinyusb-msc-busy-retry-2026/).

## Engineering Review Checks

Zielcode: `esp32.pidrive` Stall/`onRead` (**C11**). Generisches Muster: [`callback-reentry-state-lifetime`](../../methods/callback-reentry-state-lifetime.md).

| Evidence-ID | Review Check | Wann prüfen | Wissenszeitpunkt |
|-------------|--------------|-------------|------------------|
| `EVID-TINYUSB-MSC-2026-10-12-001`/`002` | Kein State-Reset nur wegen `offset == 0` (Re-Entry ≠ neuer Request) | **vor Lab** | Desk FACT BEFORE Lab; Bug `stallCmdT0_` DURING Lab 0.4.47 → Fix 0.4.48 |
| `EVID-TINYUSB-MSC-2026-10-12-001`/`002` | Timer/`cmds++` nur bei neuem `(LBA, offset)` / keyChanged | **vor Lab** | RETROFIT 0.7.0 DERIVED aus Desk-FACT |
| `EVID-TINYUSB-MSC-2026-10-12-001`/`010` | Busy-Pfad: Producer-/Live-State idempotent | **vor Lab** | Desk + B-Vertrag |
| `EVID-TINYUSB-MSC-2026-10-12-003` | Hybrid Yield (`vTaskDelay`) vs. reines Busy | **vor Lab** | Desk #2035 |
| Lab ERGEBNIS-048 | `stallMaxMs` Telemetrie unter Re-Entry plausibel | **vor Feld** | DISCOVERED DURING Lab |
| Code `onRead` / UEBERGABE-S6 | Kein Claim „BUSY bremst FAT/DIR“ ohne Code-Check | **vor Sheet-Update** | AFTER S6 Code-Check |
| `EVID-BMWHU-2026-10-12-005` | Ring-MEASURED ≠ „Dauerstrom unmöglich“ | Architektur-Review | AFTER S6 (Absolute war Überinterpretation) |
| `EVID-BMWHU-2026-10-12-006`/`007` | Stall-Scope / Resume-P vor Größenleiter im Feld | **vor nächstem Feld** | AFTER S6 |

**Counterfactual (konserviert):** Mit Review Check „State lifetime across callback re-entry“ wäre `stallCmdT0_`-Reset in 0.4.47 mit hoher Wahrscheinlichkeit vor dem Lab-Lauf aufgefallen — siehe Method + [Revalidation §3.9](../../docs/reports/2026-10-13-v0.7.0-pidrive-revalidation.md).

## Kill-Kriterien

### E7/S6 Busy-Pacing (Referenz — Inhalt aus Ops + TinyUSB-Retro)

**Hypothese:** Busy-Pacing ermöglicht dem NBT Ton über das bisherige ~6–8 s-Ringfenster hinaus.

| # | Kill / Widerlegt wenn | Status (nach Feld) | Präregistrierung |
|---|----------------------|--------------------|------------------|
| 1 | NBT beendet READ10 trotz korrektem BUSY-Pacing | nicht eingetreten | Ops Fail-Gate `E7-FELD.md` BEFORE; Audit-Tabelle RETRO 0.7.0 |
| 2 | Kein wiederholter Callback bei BUSY | nicht eingetreten | Desk TinyUSB BEFORE |
| 3 | Host-Timeout / Medium weg vor nutzbarem Tonfenster | nicht eingetreten (Stall-Defaults) | Ops BEFORE |
| 4 | Ton trotz kontinuierlicher Reads ≤ bisheriges Ringfenster | widerlegt durch ~65 s (`002`) | Ops Pass-Hint BEFORE; formalisiert RETRO |

### Frühere Experimente (S3–S5)

Formale Audit-Kill-Tabellen damals **nicht** vorhanden → `STANDARD_GAP_PRE_0.7.0`. Ops-Hypothesen lebten in Feldberichten; hier nicht nachträglich als präregistriert dargestellt.

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Sheet | [`technologies/bmw-nbt-evo/SHEET.md`](../../technologies/bmw-nbt-evo/SHEET.md) |
| Application | [`projects/pidrive/applications/bmw-nbt-evo.md`](../../projects/pidrive/applications/bmw-nbt-evo.md) |
| Evidence | [`evidence.md`](evidence.md) |
| DELTA | [`DELTA.md`](DELTA.md) |
| Revalidation 0.7.0 | [`docs/reports/2026-10-13-v0.7.0-pidrive-revalidation.md`](../../docs/reports/2026-10-13-v0.7.0-pidrive-revalidation.md) |
| Method Re-Entry | [`methods/callback-reentry-state-lifetime.md`](../../methods/callback-reentry-state-lifetime.md) |

## Vorgänger

Pilot 1: [`pidrive-2026-msc/`](../pidrive-2026-msc/) — Schema-Validation MSC; C-Claims formal hierher verlagert.

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| E7/S6 Busy-Pacing NBT | `EVID-BMWHU-2026-10-12-001`–`007` | [`bmw-nbt-evo` Application](../../projects/pidrive/applications/bmw-nbt-evo.md) · [`esp32-pidrive` usb-msc](../../projects/esp32-pidrive/applications/usb-msc.md) |
| Desk-Basis | `EVID-TINYUSB-MSC-2026-10-12-*` | [`tinyusb-msc-busy-retry-2026`](../tinyusb-msc-busy-retry-2026/) |
| Lab Timer-Fix 0.4.48 | Lab ERGEBNIS-048 (B) | Method [`callback-reentry-state-lifetime`](../../methods/callback-reentry-state-lifetime.md) |

Upstream: [`ERGEBNIS-S6.md`](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-12-feld/feld-s6-prep/ERGEBNIS-S6.md) · [`UEBERGABE-S6`](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-12-feld/UEBERGABE-S6-NAECHSTE-KI-2026-10-12.md) · Lab [`lab-e7-ladder/ERGEBNIS.md`](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-12-lab/lab-e7-ladder/ERGEBNIS.md).

## Lessons Learned

1. Gleiche Evidence-IDs (`EVID-USBMSC-*`) vermeiden Doppelpflege beim Migrationsschritt; neue HU-Claims → `EVID-BMWHU-*`.
2. Feld-AV Exit #6 bleibt getrennt vom Busy-Pacing-Tonfenster — kein stilles globales Ohr-PASS.
3. Revalidation mischt Framework-Sprung und historische Evidence — DELTA trennt beides.
4. **2026-10-12:** Desk TinyUSB-BUSY → gezieltes E7 → Feld S6 widerlegt „kleiner Ring = Grenze“.
5. **2026-10-13:** 0.7.0-Parität; Counterfactual `stallCmdT0_` als generischer Re-Entry-Check konserviert — Engineering-Nutzen, nicht nur Doku.

## Offene Punkte

- Exit #6 Feld-Ohr PASS upstream (Menü/Sender-Gate) — nicht durch Busy-Pacing-Session erfüllt
- Mechanismus Menü-~20 s unter Stall: Phänomen `MEASURED` (`006`); Ursache weiter `INFERRED`/`UNKNOWN`
- Rock 8 MiB oft stumm: Session-`MEASURED` (`007`); Ursache offen (Resume/Play-Detect)
- Nach Exit #6 PASS: Maturity (field_evidence R4+) + ggf. Method Note `field-av-correlation`
- Pilot 3 `avrcp` — BT-Host-Profil in [`pidrive-2026-radio-bt`](../pidrive-2026-radio-bt/) / Gateway, nicht USB-C duplizieren
