# Audit Campaign: \<ID\>

```yaml
id: project-YYYY
project_id: example
started: YYYY-MM-DD
ended: null
status: planned   # planned | active | closed
profile: firmware   # firmware | lab-tool | planning | ops-field — siehe docs/AUDIT-PROFILES.md
standard_version: "0.7.0"   # = Inhalt von VERSION zum Audit-Zeitpunkt; Changelog: docs/STANDARD-CHANGELOG.md
# standard_gaps: []         # optional: was gegenüber neuerem Standard noch fehlt
# reuse_outcomes:           # am Ende ausfüllen (Transfer-Nachweis)
#   reused: []
#   new: []
#   not_helped: []
#   process: ""             # optional kurz
#   decisions_touched: []   # optional P2
#   cycles_avoided: []      # optional P2
```

## Ziel

Was dieser Lauf klären soll (1–3 Sätze).

## Scope

- Im Scope: …
- Nicht im Scope: …

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | … | offen |

## Decision Trace

Pflicht bei `lab-tool` / `ops-field` mit Go/No-Go-Entscheidung (Review **C10**). Sonst optional / „n/a“.

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz |
|--------------|-----------------|-------------|------------|
| … | … | `EVID-…` | Ja / Nein / Lab nötig |

## Engineering Review Checks

Pflicht, wenn Evidence den Zielcode betrifft (Review **C11**). Aus entscheidungsrelevanter Evidence konkrete Pre-Test-Prüfungen ableiten — Desk-Wissen soll Fehler möglichst vor dem Lab finden.

| Evidence-ID | Review Check |
|-------------|--------------|
| `EVID-…` | z. B. kein State-Reset nur wegen `offset == 0`; Timer nur bei neuem Request; Re-Entry idempotent |

## Kill-Kriterien

Pflicht vor dem ersten Messlauf einer Hypothese (Review **C12**). Präregistrieren — nicht erst nach der Analyse.

**Hypothese:** …

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | … | offen |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| … | [`methods/…`](../../methods/) |

## Bezug Inventar

Priorisierte Slugs / Coverage-Ziele:

- …

## Ergebnisse

Links zu Sheets, Applications, Berichten im Ursprungsrepo:

- …

## Knowledge Feedback

Pflicht bei Lab-/Field-Ergebnis (Review **C13**): neue Evidence-IDs + Rückkanal in Application/Sheet.

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| … | `EVID-…` | `projects/…/applications/….md` |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact.

## Lessons → Transfer

Was in Technology Sheets oder Methods übernommen wurde:

- …

## Offene Punkte nach Abschluss

- …
