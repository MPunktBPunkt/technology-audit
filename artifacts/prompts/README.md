# Generierte Prompt-Artefakte

Hier legen Assistenz-Läufe (CLI, GitHub Action, manueller Prep) **ausgefüllte** Prompts ab.

- Vorlagen: [`templates/prompts/`](../../templates/prompts/)
- Vertrag: [`docs/PROMPT-CONTRACT.md`](../../docs/PROMPT-CONTRACT.md)

## Namensschema

```text
artifacts/prompts/<prompt-type>-<project-or-slug>-<YYYYMMDD>.md
```

Beispiele:

- `bootstrap-repo-esp32-ftmsprobe-20261005.md`
- `evidence-update-bmw-nbt-evo-20261005.md`
- `next-step-pidrive-20261005.md`

## Regeln

- Nur Prompt-Text und kurzer Scanner-Befund — **keine** automatischen Edits an Sheets/Applications/Audits.
- Artefakte dürfen committed werden, wenn ein Lauf reviewed werden soll; sonst lokal belassen.
- Veraltete Prompts können gelöscht oder mit Datum im Namen belassen werden (kein Single-Source-of-Truth für Wissen).
