# Audit Campaign: \<ID\>

```yaml
id: project-YYYY
project_id: example
started: YYYY-MM-DD
ended: null
status: planned   # planned | active | closed
profile: firmware   # firmware | lab-tool | planning | ops-field — siehe docs/AUDIT-PROFILES.md
standard_version: "0.7.1"   # = Inhalt von VERSION zum Audit-Zeitpunkt; Changelog: docs/STANDARD-CHANGELOG.md
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

Spalte **Wissenszeitpunkt** ist **optional** (ab 0.7.1-Klarstellung). Sie ersetzt keine Evidence-ID — sie ordnet nur ein, wann die Information für die Entscheidung galt. Erlaubte Labels: `KNOWN BEFORE TEST` · `DISCOVERED DURING TEST` · `DISCOVERED AFTER TEST` · `RETROFIT`. Ohne Spalte bleibt die 4-Spalten-Form gültig.

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| … | … | `EVID-…` | Ja / Nein / Lab nötig | … |

## Engineering Review Checks

Pflicht, wenn Evidence den Zielcode betrifft (Review **C11**). Aus entscheidungsrelevanter Evidence konkrete Pre-Test-Prüfungen ableiten — Desk-Wissen soll Fehler möglichst vor dem Lab finden.

Optionale Spalte **Wissenszeitpunkt** wie beim Decision Trace (keine Pflicht).

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-…` | z. B. kein State-Reset nur wegen `offset == 0`; Timer nur bei neuem Request; Re-Entry idempotent | … |

## Kill-Kriterien

Pflicht vor dem ersten Messlauf einer Hypothese (Review **C12**): prüfen, ob ein falsifizierbares Kill-Kriterium existiert — und es dann präregistrieren (nicht erst nach der Analyse).

**Hypothese:** …

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | … | offen |

Wenn nach Prüfung **kein** evidence-basiertes Falsifikationskriterium für den konkreten Entscheidungs-/Pfadkontext begründet werden kann:

```text
NO JUSTIFIED KILL CRITERION
Begründung: …
```

Das bedeutet **nur**: für diesen Kontext war kein Kill begründbar. Es bedeutet **nicht**: kein Test nötig · alles bewiesen · `UNKNOWN` automatisch akzeptiert · Pfad darf nie gestoppt werden. `UNKNOWN` allein ist kein automatisches STOP — kann aber weitere Untersuchung rechtfertigen oder zusammen mit anderer Evidence ein Gate/Kill auslösen.

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

## Retro-Impact (optional — Revalidation / Counterfactual)

**Nicht Pflicht** für normale Audits. Nutzen bei Revalidation oder retrospektiver Bewertung, wenn eine **spätere** Erkenntnis gegen früheren Wissensstand geprüft wird. Keine rückwirkende Umdeutung: nur behaupten „früher erkennbar“, wenn die relevante Evidence damals schon `KNOWN BEFORE` war.

| Spätere Erkenntnis | Früherer Review Check (hätte erfassen können?) | Betroffene Entscheidung | Potenziell vermeidbarer Umweg | Evidence-Basis | Counterfactual-Unsicherheit |
|--------------------|------------------------------------------------|-------------------------|-------------------------------|----------------|------------------------------|
| … | … / n/a | … | … | `EVID-…` | niedrig / mittel / hoch / UNKNOWN |

## Lessons → Transfer

Was in Technology Sheets oder Methods übernommen wurde:

- …

## Offene Punkte nach Abschluss

- …
