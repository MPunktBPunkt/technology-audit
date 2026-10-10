# Pflege & Single Source of Truth

Antwort auf Skalierungs-/Redundanz-Risiken (externe Reviews 2026-10). Ziel: **weniger doppelte Statuspflege**, bessere Auffindbarkeit, Checks statt Erinnerung.

Verwandt: [`PROJECT-START.md`](PROJECT-START.md) · [`KB-FIT.md`](KB-FIT.md) · [`REVIEW-CHECKS.md`](REVIEW-CHECKS.md) · [`retrieval-tests.yaml`](retrieval-tests.yaml) · `ta-assist`

## Wahrheitsorte (nicht verdoppeln)

| Fakt | Quelle der Wahrheit | Abgeleitet / Index |
|------|---------------------|--------------------|
| Sheet-Slug, Primary, `seen_in`, Maturity A | `technologies/<slug>/SHEET.md` YAML | `technologies/index.yaml` + README via `ta-assist index` |
| Geplante Slugs ohne Sheet | `technologies/_planned.txt` | landet im Tech-Index |
| Projektkatalog (ID, Profil, Status) | `projects/<id>/SCOPE.md` YAML | `projects/index.yaml` + `projects/README.md` |
| Projekt-Status/Coverage einer Tech | `projects/<id>/INVENTORY.md` | nicht in Sheet-Maturity spiegeln |
| Kampagnen-Status / Exit | `audits/<id>/README.md` YAML + Exit-Tabelle | `audits/README.md` nur Kurzliste |
| Evidence-IDs | `audits/<id>/evidence.md` | Apps zitieren, nicht neu erfinden |
| Transfer-Nachweis | Kampagne YAML `reuse_outcomes` und/oder FOLLOW-ON | keine Schätzung von W* |
| Audit-Standard | [`VERSION`](../VERSION) + [`STANDARD-CHANGELOG`](STANDARD-CHANGELOG.md) | Kampagne `standard_version` |

**Regel:** Status nur an der Wahrheitsquelle ändern; Indizes neu generieren, nicht handkorrigieren.

### `seen_in` kanonisch

- Nur **project_id** (`pidrive`), niemals Pfad (`projects/pidrive`).
- Jede ID muss als `projects/<id>/` existieren (Check S9/S10).
- Bidirektional: Sheet↔Application (S8 / G2).

## Nach Sheet-/Scope-Änderung

```bash
python3 tools/ta-assist index
python3 tools/ta-assist check
```

CI failt bei Errors (NAV2/3, I5, S9/S10, RT1).

## Check-Stufen

| Stufe | Bedeutung | Beispiel |
|-------|-----------|----------|
| **error** | harte Parität | Sheet nicht im Index; unbekannte `seen_in`-ID |
| **warning** | nachziehen | Application ohne `seen_in`-Eintrag (G2) |
| **info** | Hinweis | `field_evidence=R0` trotz `seen_in` (R5); Kampagnen-Patch-Lag |

Fachliche Richtigkeit von Claims bleibt **menschlich**.

## Retrieval-Tests (Nutzbarkeit)

[`retrieval-tests.yaml`](retrieval-tests.yaml): reale Fragen + erwartete Pfade + Reject-Slugs.  
Strukturell: Check RT1 (Pfade existieren). Semantisch: Agenten/Reviews manuell gegen die Fixtures.

## Transfer-Nachweis (Pflicht am Kampagnen-/Projektende)

In Audit-YAML und/oder FOLLOW-ON:

```yaml
reuse_outcomes:
  reused: [ble-hrm-gatt, esp-hub-telemetry]
  new: [rpi-gpio-fm-tx]
  not_helped: ["bmw-nbt-evo — zu host-spezifisch ohne neues HU"]
```

Vorlage: [`templates/follow-on-ideas.md`](../templates/follow-on-ideas.md).

## Was wir bewusst nicht bauen

- Vektordatenbank / Auto-Schreib-Bot
- Zweite parallele Statustabellen
- Method Notes spekulativ
- Automatische fachliche Claim-Validierung

## Methoden

[`methods/`](../methods/) — anlegen bei ≥2 Einsätzen desselben Ablaufs.
