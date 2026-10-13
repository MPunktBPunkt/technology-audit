# Method: Callback Re-Entry State Lifetime

```yaml
slug: callback-reentry-state-lifetime
title: Callback Re-Entry State Lifetime
status: active
tags: [firmware, lab-only, review-check]
canonical_example: stallCmdT0_ / TinyUSB MSC Busy-Retry (PiDrive 0.4.47→0.4.48)
```

## Zweck

Generischer **Engineering Review Check** für Host-/IO-Callbacks, die vom Stack **erneut mit denselben Parametern** aufgerufen werden (Busy/Retry/NAK/Partial), bevor der Transfer fortschreitet.

Verhindert, dass zeitkritischer oder kommandogebundener Zustand unbeabsichtigt bei jedem Re-Entry zurückgesetzt wird — typisch Timerstart, „neuer Request“-Zähler, Producer-Arming, Idempotenz-Flags.

**Nicht** projektspezifisch: gilt für USB MSC, andere BOT/SCSI-Callbacks, und analoge „not ready yet → same call again“-Muster.

## Wann anwenden

- Evidence zeigt: Callback bei „busy“ / „try again“ / Partial **mit gleichen Parametern** erneut (Desk `FACT` oder Spec).
- Zielcode startet Timer, Zähler oder State-Maschinen-Übergänge im Callback.
- Vor Lab-Flash einer Stall-/Retry-/Pacing-Firmware (**C11**).

## Voraussetzungen

- Bekannter Re-Entry-Vertrag des Stacks (z. B. TinyUSB `return 0` → Fake-Xfer-Complete → gleicher `(LBA, offset)`).
- Identifizierte State-Variablen: Timer-Anker, cmd-counter, armed-flags, ring/cursor.

## Ablauf (Review Checklist)

1. **Re-Entry-Semantik benennen** — Wann ruft der Stack denselben Callback erneut auf? Mit welchen Parametern?
2. **State klassifizieren**
   - *Request-lifetime:* gilt für einen logischen Host-Request / CBW / Transfer.
   - *Callback-lifetime:* darf bei jedem Entry neu sein.
   - *Session-lifetime:* überlebt Remount/Replug nicht ohne Reset-Pfad.
3. **Gefährliche Trigger suchen** — Reset nur wegen:
   - `offset == 0` / „Anfang des Puffers“
   - „erster Aufruf dieses Transfers“ ohne stabile Request-ID
   - Partial-Länge / Chunk-Grenze
   - Fehlerpfad, der Busy mit Neu-Start verwechselt
4. **Key für „neuer Request“** — explizit: z. B. `(LBA, offset)`-Wechsel, neue CBW-Tag, Rising-Edge „command start“ — **nicht** bloßer Wiedereintritt.
5. **Idempotenz** — Re-Entry mit gleichem Key: Timer nicht neu; Zähler nicht doppelt; Producer-State stabil.
6. **Lab-Gate** — Telemetrie: `maxMs`/Timeouts greifen; retries steigen ohne Zähler-Explosion; Host-Abort getrennt dokumentieren.

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Re-Entry-Vertrag belegt | Evidence-ID oder Spec-Zitat | Annahme „jeder Call = neuer Request“ |
| Timer/Zähler an Request gebunden | Start nur bei keyChanged / neuem CBW | Reset bei jedem `offset==0`-Re-Entry |
| Telemetrie plausibel | `maxMs` wirkt; cmds ≈ Host-Kommandos | cmds/retries explodieren, Timeout greift nie |
| Desk ≠ Host | Host-Abort = Lab/Field-ID | Abort-ms als Sheet-A-FACT |

## Kanonisches Beispiel (PiDrive — nicht generalisieren als Host-FACT)

| Stufe | Inhalt |
|-------|--------|
| Evidence | TinyUSB Busy: Callback erneut mit gleichen Params — `EVID-TINYUSB-MSC-2026-10-12-001`/`002` (**KNOWN BEFORE** Lab) |
| Review Check | Timer `stallCmdT0_` nicht bei jedem Re-Entry mit `offset==0` zurücksetzen |
| Bug | In **0.4.47**: `if (offset == 0) stallCmdT0_ = now` → `stallMaxMs` wirkungslos |
| Fix | **0.4.48**: Timer/`cmds++` nur bei keyChanged — [lab ERGEBNIS-048](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-12-lab/lab-e7-stall-flash/ERGEBNIS-048.md) |
| Impact | Vermeidbarer Lab-Umweg (**Retro-Impact A**); Feld S6 lief auf gefixtem Build |

Counterfactual: Mit diesem Check **vor** Lab wäre der Fehler mit hoher Wahrscheinlichkeit im Code-Review aufgefallen — siehe [Revalidation 2026-10-13](../docs/reports/2026-10-13-v0.7.0-pidrive-revalidation.md).

## Fallstricke

- `offset == 0` heißt im Busy-Pfad oft „Anfang *dieses* Chunks / derselben offenen Transferstufe“, nicht „neuer Host-Request“.
- Partial-Read ≠ Busy-Re-Entry — getrennt prüfen.
- Host-Timeouts gehören nicht ins Technology Sheet (A); nur Lab/Field (C).
- Nachträgliche Review Checks als „damals gewusst“ kennzeichnen (`RETROFIT`), wenn erst nach dem Bug formuliert.

## Verwandte

- Method Busy-Semantik: [`msc-busy-retry-semantics`](msc-busy-retry-semantics.md)
- Desk-Audit: [`tinyusb-msc-busy-retry-2026`](../audits/tinyusb-msc-busy-retry-2026/)
- Host-C: [`pidrive-2026-bmw-hu`](../audits/pidrive-2026-bmw-hu/)
- Review **C11** / Evidence **E7**: [`docs/REVIEW-CHECKS.md`](../docs/REVIEW-CHECKS.md)
