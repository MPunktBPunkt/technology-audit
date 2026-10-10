# Eignung der Wissensbasis für Neuentwicklung

Stand: **2026-10-10** · Audit-Standard [`0.6.4`](../VERSION) · nach externen Reviews (Mistral / GPT / Claude) + Index-Prozess.

## Kurzurteil

**Ja — Zweck erfüllt, Architektur stärker als Abdeckung.** Geeignet als Referenz beim Projektstart über Index → Familie → 1–3 Sheets. Nächster Hebel ist **Wartung/Auffindbarkeit**, nicht neue Dokumenttypen.

| Kriterium | Note | Kommentar |
|-----------|------|-----------|
| Struktur & Schichten A/B/C | sehr gut | Projekt ≠ Tech ≠ Evidence |
| Wiederverwendbarkeit | gut–sehr gut | kein Stack-Fork; Geschwister-Regel |
| Auffindbarkeit | gut (↑) | Index nach Primary + `index.yaml` + `ta-assist index` |
| Prozess & Tooling | sehr gut | Templates, Prompt-Contract, check, CI |
| Inhaltstiefe / Evidenz | mittel | viele Desk-Pilots; Fallstricke oft stärker als „So geht’s“ |
| Skalierung / Wartung | mittel (↑) | SoT-Regeln in [`MAINTENANCE.md`](MAINTENANCE.md); weniger Status-Duplikate |
| Agenten-Nutzung | gut | Bootstrap; nicht ganze KB dump |

## Was trägt

1. Ebene-A-Disziplin + Claim-Status (`FACT`/`REJECTED`) — Irrtümer bleiben sichtbar.
2. Contract-Sheets stack-neutral (z. B. Hub C++ ↔ Node).
3. `ta-assist check` (I4/I5, NAV-Index-Parität, S8 `seen_in`↔App).
4. Fremd-Repo-Test (`pi-fm-tx`): Match schlägt fehl → neue TX-Slugs statt RX verbiegen.
5. [`PROJECT-START.md`](PROJECT-START.md) als Permalink.

## Bewusst offene Baustellen

| Lücke | Haltung |
|-------|---------|
| Desk ≫ Feld | Reifegrade ehrlich niedrig lassen; Evidence bei Nutzung nachziehen |
| Viele aktive Kampagnen | desk-complete schließen oder Exit bewusst verwerfen |
| Method Notes dünn | nur bei Wiederholeinsatz anlegen |
| Branch bündelt alles | später kleine PRs / main |
| Kein Volltext-Search | vorerst Index + FAMILIES + Bootstrap; kein Vektor-Store |

## Empfohlene Verweis-Formel

```text
Wissensbasis: https://github.com/MPunktBPunkt/technology-audit
Start: docs/PROJECT-START.md
Pflege: docs/MAINTENANCE.md
Familie: docs/FAMILIES.md
Bootstrap: python3 tools/ta-assist prepare bootstrap <repo>
Index: python3 tools/ta-assist index && python3 tools/ta-assist check
```

Nur 2–4 Sheet-URLs anhängen — nicht den ganzen Tree.
