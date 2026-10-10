# Pflege & Single Source of Truth

Antwort auf Skalierungs-/Redundanz-Risiken (externe Reviews 2026-10). Ziel: **weniger doppelte Statuspflege**, bessere Auffindbarkeit, Checks statt Erinnerung.

Verwandt: [`PROJECT-START.md`](PROJECT-START.md) · [`KB-FIT.md`](KB-FIT.md) · [`REVIEW-CHECKS.md`](REVIEW-CHECKS.md) · `ta-assist`

## Wahrheitsorte (nicht verdoppeln)

| Fakt | Quelle der Wahrheit | Abgeleitet / Index |
|------|---------------------|--------------------|
| Sheet-Slug, Primary, `seen_in`, Maturity A | `technologies/<slug>/SHEET.md` YAML | `technologies/index.yaml` + `technologies/README.md` via `ta-assist index` |
| Geplante Slugs ohne Sheet | `technologies/_planned.txt` | landet im Index/README |
| Projekt-Status/Coverage einer Tech | `projects/<id>/INVENTORY.md` | nicht in Sheet-Maturity spiegeln |
| Kampagnen-Status / Exit | `audits/<id>/README.md` YAML + Exit-Tabelle | `audits/README.md` nur Kurzliste |
| Evidence-IDs | `audits/<id>/evidence.md` | Apps zitieren, nicht neu erfinden |
| Audit-Standard | [`VERSION`](../VERSION) + [`STANDARD-CHANGELOG`](STANDARD-CHANGELOG.md) | Kampagne `standard_version` |

**Regel:** Status nur an der Wahrheitsquelle ändern; Indizes neu generieren, nicht handkorrigieren.

## Nach Sheet-Änderung

```bash
python3 tools/ta-assist index
python3 tools/ta-assist check
```

CI (`audit-structure-check`) failt bei Errors — u. a. wenn `index.yaml` hinter den Sheets zurückbleibt (NAV2/NAV3).

## Check-Stufen (bewusst)

| Stufe | Bedeutung | Beispiel |
|-------|-----------|----------|
| **error** | harte Parität / Pflichtfelder | `applied` ohne App (I5); Sheet nicht im Index (NAV2) |
| **warning** | fachlich/pflegetechnisch prüfen | `seen_in` ohne App (S8); Standard-Lag (C8) |
| **info** | Hinweis, kein Blocker | aktive Kampagnen-Anzahl (PILOT) |

Fachliche Richtigkeit von Claims bleibt **menschlich** — `check` ersetzt kein Lab/Feld.

## Was wir bewusst nicht bauen

- Vektordatenbank / Auto-Schreib-Bot für Sheets
- Zweite parallele Statustabellen „fürs Dashboard“
- Method Notes spekulativ (nur bei konkretem Lab-Wiederholeinsatz)

## Methoden

[`methods/`](../methods/) sind die transferierbarsten Lab-Pfade — dünn halten ist ok. Anlegen wenn derselbe Messablauf in ≥2 Kontexten gebraucht wird (siehe `methods/README.md`).

## Erfolg messen (nicht Sheet-Zählung)

Bei Folgeprojekten kurz notieren (Kampagne oder FOLLOW-ON):

1. Welche Sheets/Fallstricke wurden **übernommen**?
2. Was war **neu** vs. schon gelöst?
3. Wo hat die KB **nicht** geholfen?

Ein Sheet mit nachgewiesenem Transfer schlägt zehn ungenutzte.
