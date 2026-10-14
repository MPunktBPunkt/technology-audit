# Project Scope: technology-audit KB (Meta)

```yaml
project_id: technology-audit-kb
title: technology-audit — Wissensbasis-Qualität (Meta)
updated: 2026-10-14
profile_hint: ops-field
status: active
repos:
  - https://github.com/MPunktBPunkt/technology-audit
reviewed_commit: "5fab7f5"
```

## Zweck

Meta-Audit der eigenen KB: Wie stark sind **messtechnisch** bestimmte Claims
(`MEASURED`) vertreten, auffindbar und epistemisch sauber von Desk-`FACT`
getrennt — angesichts vieler Lab-/Feldmessungen in den Ursprungsrepos.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| Evidence-Register unter `audits/*/evidence.md` | Statuszählung, ID-Cluster | ja |
| Technology Sheets / Applications Maturity | `field_evidence`, A/B/C | ja |
| Kampagnenstatus active/closed | Auffindbarkeit vs. Desk-Last | ja |
| Epistemic-Standard 0.7.1 | Desk ≠ Lab ≠ Field | ja |
| Neue Messungen / Lab-Läufe | — | **nein** |
| Inhaltsaudit jedes Fremdrepos | — | **nein** (nur KB-Spiegel) |

## Nicht-Ziele

- keine neuen `MEASURED`-IDs aus diesem Meta-Lauf erfinden
- keine Feld-/Lab-Wiederholung
- kein Massen-Close aller open Desk-Kampagnen in diesem Commit (nur Empfehlung)
- kein neues Technology Sheet „KB-Qualität“

## Prioritäten

1. MEASURED-Corpus kartieren (wo, wie viele, wie stark verlinkt)
2. Epistemik-Hygiene: FACT vs MEASURED vs UNKNOWN vs REJECTED
3. Navigations-/Maturity-Lücken benennen
4. Nächste Schritte für Mess-Sichtbarkeit (Index, Closes)
