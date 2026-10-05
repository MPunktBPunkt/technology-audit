# tools/

Assistenz für `technology-audit`: Strukturprüfung und Prompt-Vorbereitung.
**Schreibt keine** Dateien unter `technologies/`, `projects/`, `audits/`, `methods/`.

Vertrag: [`docs/PROMPT-CONTRACT.md`](../docs/PROMPT-CONTRACT.md) · Prüfliste: [`docs/REVIEW-CHECKS.md`](../docs/REVIEW-CHECKS.md)

## Versionierung

| Was | Wo | Bedeutung |
|-----|-----|-----------|
| **Framework** | [`VERSION`](../VERSION) | Dokumentenstandard, Methodik, Repo-Reife (z. B. 0.5.x) |
| **CLI** | `tools/ta_assist/__init__.py` → `__version__` | Assistenz-Tool semver (unabhängig, z. B. 0.1.x) |

Die Versionen müssen nicht identisch sein. Bei Breaking-Änderungen am Checker/Prompt-Format: CLI semver erhöhen und kurz in diesem README notieren.

## Schnellstart

```bash
# von Repo-Root
python3 tools/ta-assist check
python3 tools/ta-assist prepare next
python3 tools/ta-assist prepare bootstrap https://github.com/MPunktBPunkt/esp32.ftmsprobe
python3 tools/ta-assist scan
python3 tools/ta-assist prompt evidence-update --project pidrive --audit pidrive-2026-bmw-hu --slug bmw-nbt-evo
```

Oder:

```bash
PYTHONPATH=tools python3 -m ta_assist check
```

Remote-Bootstrap: [`gh`](https://cli.github.com/) angemeldet, sonst lokaler Clone-Pfad.

## Befehle

| Befehl | Zweck |
|--------|--------|
| `check` | Structure/Consistency → Exit 1 bei Errors |
| `scan` | Repo-Befund + Vorschlag nächster Prompt |
| `prepare next` | Prompt `next-step` nach `artifacts/prompts/` |
| `prepare bootstrap <url>` | Prompt `bootstrap-repo` |
| `prompt <type>` | expliziter Prompt-Typ |

Generierte Prompts: [`artifacts/prompts/`](../artifacts/prompts/).

## `suggest_next` (Heuristik)

`scan` und `prepare next` leiten den nächsten Prompt-Typ ab (`promptgen.suggest_next`):

1. **Aktive Audit-Kampagne** → `evidence-update` (project + audit + slug aus YAML, sonst ID-Heuristik `bmw`/`msc`).
2. Sonst **`avrcp`** im Inventar ohne Sheet → `pilot-prep`.
3. Sonst erstes **`observed`/`candidate`** ohne Sheet → `new-tech-sheet`.
4. Sonst → `quality-review`.

Das ist eine **Arbeitsvorschlag-Heuristik**, keine fachliche Priorität. Bei Bedarf `prompt <type>` manuell wählen.

## Bootstrap-Scan (Heuristik)

Im Modus `bootstrap` liest `scanner.py` README/Top-Level und markiert **Signale** (z. B. `esp32`, `ftms`, `gatt`, `bluetooth`, `platformio`, `avrcp`, `usb-msc` als Phrase).

- Ausgabe = Kandidaten für Scope/Inventar-Prompt, **kein** verifiziertes Inventar.
- Token-Treffer können falsch positiv sein (z. B. Substrings in Projektnamen) — menschlich/KI prüfen.

## Checker ↔ REVIEW-CHECKS

`checker.py` bildet einen **Teil** der Regeln aus [`docs/REVIEW-CHECKS.md`](../docs/REVIEW-CHECKS.md) ab (Struktur, Inventar, Frontmatter, Evidence-ID-Format, Audit-Exit-Hinweise).

- Neue Check-ID im Standard → prüfen, ob `checker.py` nachgezogen werden soll.
- Oder in REVIEW-CHECKS als „nur manuell / KI“ kennzeichnen.
- Semantische Warnungen (z. B. S4 Projekt-Tokens im Sheet) bleiben **warning**, nie Autofix.

## GitHub Actions

- `audit-structure-check` — `python3 tools/ta-assist check`
- `audit-prompt-pack` — manuell `workflow_dispatch`
