# tools/

Assistenz für `technology-audit`: Strukturprüfung und Prompt-Vorbereitung.
**Schreibt keine** Dateien unter `technologies/`, `projects/`, `audits/`, `methods/`.

Vertrag: [`docs/PROMPT-CONTRACT.md`](../docs/PROMPT-CONTRACT.md)

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
python3 -m ta_assist check
```
(mit `PYTHONPATH=tools`)

Voraussetzung für Remote-Bootstrap: [`gh`](https://cli.github.com/) angemeldet (sonst lokale Clone-Pfade nutzen).

## Befehle

| Befehl | Zweck |
|--------|--------|
| `check` | Structure/Consistency → Exit 1 bei Errors |
| `scan` | Repo-Befund + Vorschlag nächster Prompt |
| `prepare next` | Prompt `next-step` nach `artifacts/prompts/` |
| `prepare bootstrap <url>` | Prompt `bootstrap-repo` |
| `prompt <type>` | expliziter Prompt-Typ |

Generierte Prompts: [`artifacts/prompts/`](../artifacts/prompts/).
