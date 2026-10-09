# Eignung der Wissensbasis für Neuentwicklung

Stand: **2026-10-09** · Audit-Standard [`0.6.3`](../VERSION) · nach Hub-Paar (Firmware + ioBroker-Adapter).

## Kurzurteil

**Geeignet als Referenz beim Projektstart** — wenn der Einstieg über Index → Familie → 1–3 Sheets läuft, nicht über „alles lesen“. Die Struktur (A/B/C, Reuse, Profile) trägt Stack-Wechsel (C++ ↔ Node) und wachsende Projektzahl; die **Navigationsschicht** muss bewusst mitwachsen.

| Kriterium | Note | Kommentar |
|-----------|------|-----------|
| Wiederverwendbarkeit (kein Fork) | gut | Geschwister-Regel, Contract vs. Adapter getrennt |
| Auffindbarkeit | mittel–gut | Index + FAMILIES + PROJECT-START; noch kein Volltext-Search im Repo |
| Kontrakt-Klarheit Hub | gut | Spec jetzt von Server+Client belegt |
| Feld-/Lab-Tiefe | mittel | viele Desk-Pilots; Coverage oft `partial` |
| Skalierung >30 Sheets | Risiko | Primary-Gruppierung + Familienkarte pflegen |
| Agenten-/Prompt-Nutzung | gut | Bootstrap + Checklisten; nicht ganze KB dump |

## Was schon trägt

1. **Ein Wahrheitsort** für Hub-HTTP (`esp-hub-telemetry`) — Node und Adapter teilen den Slug.
2. **Ableitungsrezept** (`esp-hub-base-template`) für neue ESP-Nodes der Familie.
3. **Schichten** (RF / LAN / ESP-NOW / Lab) verhindern falsche Matches.
4. **`ta-assist check`** hält Parität; `standard_version` macht Regel-Lag sichtbar.
5. **PROJECT-START** ist der Permalink, den du in neuen Chats/Issues verlinken kannst.

## Was noch fehlt für „immer zurechtfinden“

| Lücke | Wirkung | Nächster Schritt |
|-------|---------|------------------|
| Sheet-Index nur alphabetisch | Scannen dauert | nach TAXONOMY Primary gruppieren |
| Viele `observed` ohne Sheet | Rauschen | bewusst lassen oder Quartals-Triage |
| Wenig Method Notes | Lab-Wiederholung schwer | bei Bedarf `methods/` nachziehen |
| Desk > Feld | Reifegrade R* oft niedrig | Evidence bei Nutzung nachtragen |
| PR-Branch bündelt alles | große Review-Diffs | später kleine PRs / main mergen |

## Empfohlene Verweis-Formel (neues Projekt)

In Issue / Chat / README:

```text
Wissensbasis: https://github.com/MPunktBPunkt/technology-audit
Start: docs/PROJECT-START.md
Familie: docs/FAMILIES.md → ESP-Hub
Bootstrap: python3 tools/ta-assist prepare bootstrap <repo>
```

Dann nur die 2–4 relevanten Sheet-URLs anhängen — nicht den ganzen Tree.
