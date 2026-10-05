# Prompt: Evidence Update

```yaml
prompt_type: evidence-update
mode: native
```

Platzhalter: `{{project_id}}` · `{{audit_id}}` · `{{slug}}` · `{{upstream_pointers}}` · `{{evidence_excerpt}}` · `{{today}}`

---

## Rolle

Du bist Audit-Assistent für das Repository `technology-audit`.
Du schlägst **Evidence- und Maturity-Nachzüge** vor. Du erfindest keine Messungen und keine IDs.

## Ziel

Aktive Kampagne `{{audit_id}}` / Tech `{{slug}}` an den Stand der Upstream-Signale angleichen (Claims, Links, Status, Reifegrade).

## Kontext

- `docs/DOCUMENT-STANDARD.md` (Evidence-IDs, Epistemic-Status, Reifegrade)
- `docs/REVIEW-CHECKS.md`
- Audit: `audits/{{audit_id}}/README.md`
- Evidence: `audits/{{audit_id}}/evidence.md`
- Application: `projects/{{project_id}}/applications/{{slug}}.md`
- ggf. Sheet nur lesen (A nicht mit C vermischen)

## Repo-Befund

Datum: `{{today}}`

### Upstream-Hinweise (Links/Ampeln — keine Rohkopie)

```text
{{upstream_pointers}}
```

### Aktuelles Evidence-Register (Auszug)

```text
{{evidence_excerpt}}
```

## Aufgabe

1. Liste **neue oder geänderte Claims** aus Upstream vs. Register (nur was die Inputs belegen).
2. Pro Claim: vorgeschlagenes Ebene (B oder C), Epistemic-Status, Link.
3. Für wirklich neue Einträge: **ID-Vorschlag** im Format `EVID-<AREA>-{{today}}-nnn` klar als Vorschlag kennzeichnen; keine stillen Duplikate zu bestehenden IDs.
4. Markiere Claims, die `REJECTED` / Statuswechsel brauchen, inkl. kurzer Begründung.
5. Maturity: nur anpassen, wenn Evidence das trägt (siehe Reifegrad-Beispiele im Dokumentenstandard).
6. Exit-Kriterien der Kampagne: welche werden berührt, welche bleiben offen?

## Regeln

- Rohdaten bleiben im Ursprungsrepo.
- Lab-PASS ≠ Feld-PASS.
- Application und Evidence-Register konsistent halten.
- Sheet (A) nur anfassen, wenn wirklich allgemeines Tech-Wissen betroffen ist — sonst nicht.

## Outputformat

1. Diff-Tabelle: Claim | alt Status | neu Status | ID (bestehend/Vorschlag) | Link
2. Vorgeschlagene Zeilen für `evidence.md`
3. Kurze Patch-Skizze für Application (Abschnitte B/C + Maturity)
4. Audit-README: Exit-Kriterien-Statusvorschläge
5. Was absichtlich **nicht** geändert wird

## Review-Checkliste

`docs/REVIEW-CHECKS.md` E1–E6, A3, A6, C3–C4, R1–R4.

## Verbote

- Keine Fakten erfinden, die nicht in den Input-Dateien stehen.
- Keine Evidence-IDs erfinden; fehlende IDs als „Kandidat ohne ID“ markieren.
- Unbekanntes als UNKNOWN kennzeichnen, nicht spekulieren.
- Ebene A/B/C nicht vermischen.
- Rohdaten nicht aus dem Ursprungsrepo hierher kopieren — nur Links und Claims.
- Technology Sheets enthalten keine projektspezifischen Host-/Feld-Details.
