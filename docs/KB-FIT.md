# Eignung der Wissensbasis für Neuentwicklung

Stand: **2026-10-11** · Audit-Standard [`0.6.6`](../VERSION) · inkl. KB-Cross-Check ESP-FM / Pi-TX.

## Kurzurteil

**Ja — Zweck erfüllt; Cross-Check zeigt Reasoning-Tauglichkeit, nicht nur Dokumentationsabdeckung.**
Geeignet als Referenz beim Projektstart über Index → Familie → 1–3 Sheets.
Nächster Hebel: Gate-Messungen (Desk≪Lab) und gezielte Signalpfad-Tiefe — nicht neue Dokumenttypen.

| Kriterium | Note | Kommentar |
|-----------|------|-----------|
| Struktur & Schichten A/B/C | sehr gut | Projekt ≠ Tech ≠ Evidence |
| Wiederverwendbarkeit | gut–sehr gut | Chip-Varianten-Bremse ab 0.6.6 |
| Auffindbarkeit | gut | Index + `index.yaml` + `ta-assist index` |
| Prozess & Tooling | sehr gut | Templates, Prompt-Contract, check, CI, `kb-cross-check` |
| Inhaltstiefe / Evidenz | gut (↑) | ESP-APLL-FM Desk belegt; S3-Pfad bewusst offen |
| Skalierung / Wartung | mittel–gut | SoT in [`MAINTENANCE.md`](MAINTENANCE.md) |
| Agenten-Nutzung | gut–sehr gut | Cross-Check 2026-10-11: FACT/UNKNOWN-Trennung reproduzierbar |
| Desk → Lab Validierung | mittel | Gates E-0…E-3 definiert; Messungen noch ausstehend |

## Cross-Check 2026-10-11 (Kurz)

Frage: ESP32-S3 als FM-Ausgabeknoten, Wissensquelle = Audit-Repo (+ Hub-Repo).

| Prüfaspekt | Ergebnis |
|------------|----------|
| Reproduzierbarkeit | sehr gut |
| FACT / UNKNOWN / HYPOTHESIS | sehr gut |
| Classic ESP32 → S3 gebremst | korrekt |
| Absolutismus „einziger Kandidat“ | erkannt → Prozess G18 |
| Architekturableitung | gut (Modell D), hinter Gate |
| Lab-Validierung | offen (bewusst) |

Einordnung: Extraktion ~9/10 · Engineering-Entscheidung ~8–8,5/10 · Validierung ~6/10 bis E-1 gemessen.

## Was trägt

1. Ebene-A-Disziplin + Claim-Status — Irrtümer bleiben sichtbar.
2. Contract-Sheets stack-neutral (z. B. Hub C++ ↔ Node).
3. `ta-assist check` (I4/I5, NAV-Index-Parität, S8 `seen_in`↔App).
4. Fremd-Repo-Tests: `pi-fm-tx`, `esp-fm-tx` — TX-Slugs getrennt (Pi ≠ ESP APLL).
5. Transfer-Gates + `kb-cross-check` statt stiller Varianten-Übertragung.
6. [`PROJECT-START.md`](PROJECT-START.md) als Permalink.

## Bewusst offene Baustellen

| Lücke | Haltung |
|-------|---------|
| Desk ≫ Feld | Reifegrade ehrlich; E-0/E-1 vor S3-Sheet |
| Viele aktive Kampagnen | desk-complete schließen oder Exit bewusst verwerfen |
| Method Notes | `hw-path-gate`, `kb-cross-check` neu; weitere nur bei Wiederholeinsatz |
| Harmonic-Pegel ungemessen | `UNKNOWN` in Pi- und ESP-TX-Sheets |

## Empfohlene Verweis-Formel

```text
Wissensbasis: https://github.com/MPunktBPunkt/technology-audit
Start: docs/PROJECT-START.md
Pflege: docs/MAINTENANCE.md
Familie: docs/FAMILIES.md
Bootstrap: python3 tools/ta-assist prepare bootstrap <repo>
Cross-Check: templates/prompts/kb-cross-check.md
Index: python3 tools/ta-assist index && python3 tools/ta-assist check
```

Nur 2–4 Sheet-URLs anhängen — nicht den ganzen Tree.
