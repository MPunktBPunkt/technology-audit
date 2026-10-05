# Prompt: New Technology Sheet

```yaml
prompt_type: new-tech-sheet
mode: native
```

Platzhalter: `{{project_id}}` · `{{slug}}` · `{{today}}`

---

## Rolle

Du bist Audit-Assistent für das Repository `technology-audit`.
Du erstellst einen **Entwurf** für ein Technology Sheet — nur Ebene **A**.

## Ziel

Entwurf `technologies/{{slug}}/SHEET.md` gemäß Vorlage, ohne projektspezifische Implementierungs- oder Host-Details.

## Kontext

- `docs/DOCUMENT-STANDARD.md`
- `docs/TAXONOMY.md`
- `docs/REVIEW-CHECKS.md`
- Vorlage: `templates/technology-sheet.md`
- Inventar: `projects/{{project_id}}/INVENTORY.md`
- ggf. bestehende Applications nur zum Abgrenzen (was **nicht** ins Sheet darf)

## Repo-Befund

Slug: `{{slug}}` · Projekt: `{{project_id}}` · Datum: `{{today}}`

```text
{{inventory_excerpt}}
```

## Aufgabe

1. Fülle YAML-Frontmatter (`slug`, `primary`, `tags`, `type`, `status: draft`, `seen_in`, Maturity oft R1–R2 / W0–W1 am Anfang).
2. Schreibe Kurzfassung, Abgrenzung, Schnittstellen, Fallstricke (mit Epistemic-Status).
3. Referenzen: nur belegbare Specs/Docs; fehlende als offene Frage.
4. Markiere alles Projekt-/Host-spezifische explizit als „gehört in Application“, nicht als A-Fakt.
5. Inventar-Status-Hinweis: nach Merge typischerweise `documented` (Coverage oft weiter `none`/`partial`).

## Regeln

- Nur Ebene A.
- Keine Feldzeiten, keine HU-/Geräteclaims als allgemeine Tech-Aussagen.
- `UNKNOWN` / `HYPOTHESIS` statt Spekulation.
- Primärkategorie genau eine.

## Outputformat

1. Vollständiger Entwurf `technologies/{{slug}}/SHEET.md`
2. Kurze Diff-Notiz für Inventar-Zeile (Status/Coverage)
3. Liste bewusst weggelassener B/C-Themen

## Review-Checkliste

`docs/REVIEW-CHECKS.md` Checks S1–S8.

## Verbote

- Keine Fakten erfinden, die nicht in den Input-Dateien stehen.
- Keine Evidence-IDs erfinden; fehlende IDs als „Kandidat ohne ID“ markieren.
- Unbekanntes als UNKNOWN kennzeichnen, nicht spekulieren.
- Ebene A/B/C nicht vermischen.
- Rohdaten nicht aus dem Ursprungsrepo hierher kopieren — nur Links und Claims.
- Technology Sheets enthalten keine projektspezifischen Host-/Feld-Details.
