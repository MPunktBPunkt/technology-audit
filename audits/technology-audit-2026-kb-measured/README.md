# Audit Campaign: technology-audit-2026-kb-measured

```yaml
id: technology-audit-2026-kb-measured
project_id: technology-audit-kb
started: 2026-10-14
ended: 2026-10-14
status: closed
profile: ops-field
standard_version: "0.7.1"
reviewed_commit: "5fab7f5"
reuse_outcomes:
  reused: []
  new: []
  not_helped:
    - "Desk-FACT-Masse täuscht über knappen MEASURED-Kern hinweg."
    - "Sheet field_evidence=R0 ist meist korrekt — Navigation fehlt, nicht Maturity-Fehler."
  process: "Repo-Desk der eigenen Evidence-/Maturity-Lage; keine neuen Messungen."
  decisions_touched: [measured-is-real-but-concentrated, need-measured-index, close-stale-desk]
```

## Ziel

Feststellen, ob und wo die KB **messtechnisch bestimmte Fakten** (`MEASURED`)
trägt, wie sauber sie von Desk-`FACT` getrennt sind, und welche
Ops-Lücken (Auffindbarkeit, Kampagnenstatus, Quellenhärte) den Messkern
verdecken.

## Scope

- **Im Scope:** Zählung und Stichprobe Evidence-Status; MEASURED-Cluster;
  Application-/Sheet-Maturity; Kampagnenprofil active/closed; Epistemik-Regeln 0.7.1.
- **Nicht im Scope:** neue Lab-/Feldmessungen; Inhaltsaudit aller Fremdrepos;
  Massen-Close in diesem Lauf; neues Technology Sheet.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1, Meta-Kampagne dokumentiert | erfüllt |
| 2 | MEASURED-Corpus kartiert (IDs, Cluster, Quellen) | erfüllt |
| 3 | Epistemik-Hygiene bewertet (Desk≠Lab≠Field, A/B/C) | erfüllt |
| 4 | Navigations-/Ops-Lücken mit Follow-ons | erfüllt |
| 5 | Keine erfundenen MEASURED-IDs | erfüllt |
| 6 | C10–C13 | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|-----------------|
| Messkern existiert und ist konzentriert (PiDrive + Ergo/FTMS/HR) | Gibt es belastbare `MEASURED`-Blöcke? | `EVID-KBMEAS-2026-10-14-001`–`003` | Ja — ~28 unique MEASURED; nicht „leer“ | `DISCOVERED DURING TEST` |
| Zentralen MEASURED-Index anlegen (Follow-on) | Sind MEASURED leicht findbar? | `004`, `005` | Nein — unter ~383 FACT / 50 active begraben | `DISCOVERED DURING TEST` |
| Sheet-R0 nicht pauschal hochsetzen | Fehlt Feld-Reife in Sheets? | `006` | Nein — Feld gehört in Apps; 10 Apps ≥ R3 | `DISCOVERED DURING TEST` |
| Schwache MEASURED (README-only) nachziehen | Alle MEASURED gleich hart? | `007` | Nein — Härtegrade prüfen/downgraden | `DISCOVERED DURING TEST` |

## Engineering Review Checks

Ops-/Navigationsziel der KB (**C11**).

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|-----------------|
| `001`–`003` | Bei Architekturfragen zuerst MEASURED-Cluster (pidrive HU, ergo/ftms) zitieren, nicht nur jüngste Desk-Kampagne | `DISCOVERED DURING TEST` |
| `004`–`005` | Vor „wir haben viele Fakten“: Status trennen (Desk-FACT vs MEASURED) | `DISCOVERED DURING TEST` |
| `006` | Sheet `field_evidence` nicht als Proxy für App-Feldreife lesen | `DISCOVERED DURING TEST` |
| `007` | MEASURED ohne Artefakt-Link → PL2 / Downgrade | `DISCOVERED DURING TEST` |

## Kill-Kriterien

**Hypothese:** Die KB enthält einen nutzbaren Messkern; Desk-Volumen ersetzt ihn nicht.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Keine `MEASURED`-IDs mit Upstream-Artefakt-Link | widerlegt — Cluster vorhanden |
| 2 | Host-Messungen still als Sheet-A-FACT geführt | nicht beobachtet in Stichprobe HU/MSC |
| 3 | Meta-Audit erfindet neue Messwerte | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Meta-Lagebeschreibung ohne Messhypothese, die falsifiziert werden
müsste; Kill 1–3 sind Integritätschecks und bestanden bzw. nicht anwendbar.
```

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Structure/Epistemik (Review) | [`docs/REVIEW-CHECKS.md`](../../docs/REVIEW-CHECKS.md) E*/PL*/R* |
| Dokumentenstandard | [`docs/DOCUMENT-STANDARD.md`](../../docs/DOCUMENT-STANDARD.md) |

## Bezug Inventar

- Projekt: [`technology-audit-kb`](../../projects/technology-audit-kb/)
- Messkerne (fremd zu diesem Meta-Projekt, aber Evidenzträger):
  [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/),
  [`pidrive-2026-msc`](../pidrive-2026-msc/),
  [`esp32-ergo-2026-pilot`](../esp32-ergo-2026-pilot/),
  [`esp32-ftmsprobe-2026-pilot`](../esp32-ftmsprobe-2026-pilot/),
  [`esp32-heartrate-2026-pilot`](../esp32-heartrate-2026-pilot/)

## Ergebnisse

- [`evidence.md`](evidence.md) — `EVID-KBMEAS-2026-10-14-*`
- Bericht: [`docs/reports/2026-10-14-kb-measured-facts-audit.md`](../../docs/reports/2026-10-14-kb-measured-facts-audit.md)

## Knowledge Feedback

**C13:** n/a Lab/Field — Meta-Desk der KB.

| Ergebnis | Evidence-ID | Zurück in |
|----------|-------------|-----------|
| MEASURED-Karte + Ops-Lücken | `001`–`008` | Projekt FOLLOW-ON; optional later Ledger |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 Kill / NO JUSTIFIED | PASS (Integrität + n/a Messkill) |
| C13 Knowledge Feedback | n/a dokumentiert |

## Lessons → Transfer

- **Ja, es gibt viele messbestimmte Fakten** — aber konzentriert (~28 unique IDs), nicht gleichmäßig über 50 Sheets.
- Desk-Boom 2026-10-13/14 erhöht FACT/UNKNOWN, nicht MEASURED.
- Stärkste Messblöcke: BMW-NBT/MSC (Feld+Lab) und FTMS/Varon/HR (Lab/Geräteprofil).
- Nächster Hebel: MEASURED-Ledger + stale Desk closes — nicht mehr Fremd-Desk.

## Offene Punkte nach Abschluss

- Zentralen MEASURED-Index bauen
- Desk-complete Kampagnen schließen
- README-only MEASURED härten oder downgraden
