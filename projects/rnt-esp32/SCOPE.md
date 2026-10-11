# Project Scope: Random Nerd Tutorials — ESP32 Catalog (Fremd)

```yaml
project_id: rnt-esp32
title: Random Nerd Tutorials — ESP32 Projects Catalog (Fremd)
updated: 2026-10-11
profile_hint: lab-tool
source_kind: secondary-web-catalog
reviewed_snapshot: "2026-10-11"
reviewed_snapshot_note: Desk-Scan der Index-Seite; kein Code-Commit; Inhalte können sich ändern
repos: []
sources:
  - https://randomnerdtutorials.com/projects-esp32/
status: active
```

## Zweck

Sekundäre Desk-Quelle: den öffentlichen **ESP32-Tutorial-Katalog** von Random Nerd Tutorials gegen den bestehenden Sheet-Katalog matchen — Signale, Lücken, Chip-Scope-Fallen. **Kein** Produkt, kein Code-Import, **keine** Tutorial-Texte in die KB.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| Index `projects-esp32/` | Themen-/Tutorial-Katalog | ja (Desk) |
| Einzelne Tutorial-Artikel | Claim-Quellen bei Vertiefung | nur gezielt, verlinkt |
| RNT-Code-Snippets | — | **nein** (nicht spiegeln) |
| Espressif TRM / IDF / eigene Repos | normative / projektinterne SoT | angrenzend (stärker) |
| Feldbau der Tutorials | — | **nein** |

## Nicht-Ziele

- 250+ Guides 1:1 importieren oder nachbauen
- Tutorial-HTML/Code in `technologies/` oder `artifacts/` spiegeln
- RNT als Ersatz für TRM/IDF oder eigene Evidence
- Neue Sheets nur aus Tutorial-Titeln (G19)

## Quellenarten

| Art | Rolle hier |
|-----|------------|
| **sekundär** | RNT-Index / Artikel-URLs |
| **normativ** | nicht RNT — bei Vertiefung TRM/IDF nachziehen |
| **projektintern** | Match gegen `technologies/index.yaml` + eigene Apps |

## Prioritäten

1. Index → Match-Tabelle (Reuse vor neuem Slug)
2. Chip-Scope: „ESP32“ bei RNT oft Classic/Arduino — nicht still S3/C3
3. Lücken nur als FOLLOW-ON / observed, nicht als Sheet-Explosion
4. Evidence = Snapshot-Datum + URL, kein `reviewed_commit`

## Offene Scope-Fragen

- Welche 2–4 Artikel lohnen gezielte Vertiefung (CYD, FreeRTOS, I2S-Mic) ohne Katalog-Duplikat?
