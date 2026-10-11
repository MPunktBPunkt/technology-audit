# Prompt-Contract

Verbindlicher Vertrag für **Audit-Assistenz**: wie standardisierte Arbeitsaufträge (Prompts) aus dem Repository-Zustand gebaut werden.

Ziel: KI und Mensch bekommen denselben, nachvollziehbaren Auftrag.  
Nicht-Ziel: automatisches Schreiben oder Bewerten von Fachinhalten.

Verwandt: [DOCUMENT-STANDARD.md](DOCUMENT-STANDARD.md) · [METHODOLOGY.md](METHODOLOGY.md) · [REVIEW-CHECKS.md](REVIEW-CHECKS.md) · Vorlagen unter [`templates/prompts/`](../templates/prompts/).

## Rolle des Tools

Ein Assistenz-Tool / eine GitHub Action / ein manueller Prep-Lauf darf:

| Erlaubt | Verboten |
|---------|----------|
| Repo scannen und Befund listen | Inhalte in `technologies/`, `projects/`, `audits/`, `methods/` schreiben |
| Prompt aus Template + Befund erzeugen | Fakten, Evidence-IDs oder Reifegrade erfinden |
| Struktur-/Konsistenzfehler melden | Fachliche Wahrheit setzen oder „PASS“ behaupten |
| Artefakte unter `artifacts/prompts/` ablegen | Autocommit / Automerge von Wissensdateien |

Ausgabeorte für generierte Prompts:

- `artifacts/prompts/<kurzname>-<YYYYMMDD>.md` (bevorzugt)
- GitHub Action Summary / PR-Kommentar / Issue-Body (gleicher Inhalt)

## Betriebsarten

| Modus | Wann | Ergebnis |
|-------|------|----------|
| `native` | Repo folgt diesem Standard (`docs/DOCUMENT-STANDARD.md` vorhanden) | präzise Prompts für nächsten Audit-Schritt |
| `bootstrap` | Fremd-/Quellenrepo ohne Audit-Struktur | Startprompt: Scope + Inventar-Kandidaten, keine strengen Checks |

## Prompt-Typen (v1)

| Typ | Zweck | Vorlage |
|-----|-------|---------|
| `bootstrap-repo` | Fremdrepo → erster Audit-Einstieg | [`bootstrap-repo.md`](../templates/prompts/bootstrap-repo.md) |
| `next-step` | aus aktuellem Stand den nächsten sinnvollen Schritt wählen | [`next-step.md`](../templates/prompts/next-step.md) |
| `new-tech-sheet` | Sheet-Entwurf (nur Ebene A) vorbereiten | [`new-tech-sheet.md`](../templates/prompts/new-tech-sheet.md) |
| `new-application` | Project Application vorbereiten | [`new-application.md`](../templates/prompts/new-application.md) |
| `evidence-update` | Evidence/Maturity anhand Upstream-Signale nachziehen | [`evidence-update.md`](../templates/prompts/evidence-update.md) |
| `pilot-prep` | neue Audit-Kampagne vorbereiten | [`pilot-prep.md`](../templates/prompts/pilot-prep.md) |
| `quality-review` | Dokumentqualität gegen Review-Checks prüfen | [`quality-review.md`](../templates/prompts/quality-review.md) |
| `kb-cross-check` | Sheets als Reasoning-Bausteine prüfen (inkl. Blindtest) | [`kb-cross-check.md`](../templates/prompts/kb-cross-check.md) |

Weitere Typen (später): `maturity-review`, `method-candidate`, `close-audit-review`.

## Pflichtbausteine jedes Prompts

Jeder erzeugte Prompt enthält in dieser Reihenfolge:

1. **Rolle** — Audit-Assistent für `technology-audit`, kein Autor fachlicher Wahrheit  
2. **Ziel** — ein Satz, was dieser Lauf liefern soll  
3. **Kontext** — Pfade zu Standard, Methodik, Taxonomie und relevanten Artefakten  
4. **Repo-Befund** — was der Scanner gesehen hat (Fakten über Dateien/Status, keine Domänenbehauptungen)  
5. **Aufgabe** — nummerierte Schritte  
6. **Regeln** — A/B/C, Epistemic-Status, Evidence-IDs, Reifegrade  
7. **Outputformat** — welche Dateien/Abschnitte erwartet werden  
8. **Review-Checkliste** — Verweis auf [REVIEW-CHECKS.md](REVIEW-CHECKS.md) oder Auszug  
9. **Verbote** — siehe unten  

Platzhalter in Templates: `{{variable}}` (Jinja-kompatibel). Unbekannte Werte als `UNKNOWN` belassen, nicht raten.

## Verbote (immer einfügen)

```text
- Keine Fakten erfinden, die nicht in den Input-Dateien stehen.
- Keine Evidence-IDs erfinden; fehlende IDs als „Kandidat ohne ID“ markieren.
- Unbekanntes als UNKNOWN kennzeichnen, nicht spekulieren.
- Ebene A/B/C nicht vermischen.
- Rohdaten nicht aus dem Ursprungsrepo hierher kopieren — nur Links und Claims.
- Technology Sheets enthalten keine projektspezifischen Host-/Feld-Details.
```

## Einfache Bedienung (Ziel-UX)

Fachliche Einstiege statt Optionsflut:

| Einstieg | Typisch erzeugter Prompt |
|----------|---------------------------|
| Audit starten | `bootstrap-repo` oder `pilot-prep` |
| Nächsten Schritt vorbereiten | `next-step` |
| Dokumentqualität prüfen | `quality-review` |
| Evidence nachziehen | `evidence-update` |
| Technologieanalyse vorbereiten | `new-tech-sheet` |

### CLI (Schicht 1)

```bash
python3 tools/ta-assist check
python3 tools/ta-assist prepare next
python3 tools/ta-assist prepare bootstrap <repo-url>
python3 tools/ta-assist prompt evidence-update --project pidrive --audit pidrive-2026-bmw-hu --slug bmw-nbt-evo
```

Siehe [`tools/README.md`](../tools/README.md). GitHub Actions: `audit-structure-check`, `audit-prompt-pack` (manuell).

Expertenmodus: `--project`, `--slug`, `--audit`, `--repo`.

## Mindest-Inputs

| Typ | Pflicht | Optional |
|-----|---------|----------|
| `bootstrap-repo` | Quellen-Repo-URL oder Pfad | gewünschte `project_id` |
| `next-step` | Pfad zu diesem Repo | `project_id` |
| `new-tech-sheet` | `project_id`, `slug` | — |
| `new-application` | `project_id`, `slug` | `audit_id` |
| `evidence-update` | `project_id`, `audit_id` oder `slug` | Upstream-URL/Pfad |
| `pilot-prep` | `project_id`, `slug` | vorgeschlagene Kampagnen-ID |
| `quality-review` | Pfad oder Dateiliste | Dokumenttyp-Filter |

## Qualitätsregel für den erzeugten Prompt

Ein Prompt gilt als vertragskonform, wenn:

1. alle neun Pflichtbausteine vorhanden sind,
2. mindestens eine konkrete Input-Datei genannt ist,
3. die Verbote wörtlich oder sinngleich enthalten sind,
4. das Outputformat auf Vorlagen unter `templates/` oder bestehende Dateien verweist,
5. bei `native` A/B/C explizit genannt wird.

## Abweichungen

Dauerhafte Änderungen an diesem Vertrag gehören hierher, nicht in einzelne Prompt-Artefakte.
