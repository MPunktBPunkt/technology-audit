# Methodik

Vorgehen für ein Technologie-Audit. Jede Phase liefert Artefakte aus dem [Dokumentenstandard](DOCUMENT-STANDARD.md).

## Überblick

```
0 Signale → 1 Inventar → 2 Taxonomie → 3 Sheets → 4 Applications → 5 Transfer
```

Nicht linear erzwingen: Rücksprünge sind normal (neue Signale aus der Historie, Feldtests). Coverage im Inventar zeigt, was fehlt.

## Phase 0 — Signale sammeln

**Ziel:** Herausfinden, was überhaupt existiert — noch keine Bewertung.

**Zuerst:** bestehende Wissensbasis konsultieren — [`docs/REUSE.md`](REUSE.md) und [`technologies/README.md`](../technologies/README.md). Signale gegen bekannte Slugs matchen, bevor neue Sheets vorgeschlagen werden.

Untersuchungsbereiche:

- Quellcode (Python, C/C++, Shell, JS, …)
- Firmware / Build-Konfiguration
- Systemintegration (systemd, udev, PipeWire, …)
- Hardware und Schnittstellen
- Protokolle und Datenformate
- Dienste und Steuerung (UI, CLI, Trigger)
- Tests und Feldberichte
- Git-Historie (inkl. verworfener Ansätze)

Drei Zustände unterscheiden:

| Zustand | Bedeutung |
|---------|-----------|
| Aktuell | Stand auf dem Analyse-Branch (meist `main`) |
| Historisch relevant | Frühere Implementierung mit bleibender Erkenntnis |
| Verworfen | Bewusst aufgegebener Weg (kurz notieren, warum) |

**Artefakt:** Rohnotizen / Arbeitsliste (noch kein formalisiertes Inventar nötig). Optional: Coverage-Skizze, welche Bäume angefasst wurden. Plus: Liste „Signal → bestehender Slug | neuer Slug-Kandidat“.

## Phase 1 — Inventar

**Ziel:** Alle Technologie-Kandidaten in `projects/<id>/INVENTORY.md`.

- Ein Eintrag pro Technologie (Slug festlegen).
- Status zunächst `candidate` oder `observed`.
- Coverage meist `none`.
- Scanner/Automatik darf nur **Kandidaten** liefern, keine endgültigen Aussagen.

**Artefakt:** [`templates/project-inventory.md`](../templates/project-inventory.md) ausgefüllt + [`SCOPE.md`](../templates/project-scope.md).

## Phase 2 — Taxonomie zuordnen

**Ziel:** Jeden Inventareintrag einer Primary-Kategorie und ggf. Secondary-Tags zuweisen ([TAXONOMY.md](TAXONOMY.md)).

Regeln:

- Genau eine Primary-Kategorie.
- Überlappungen (z. B. AVRCP = Protokoll *und* Steuerung) über Secondary-Tags lösen.
- Unklare Fälle im Inventar als offene Frage markieren, nicht erzwingen.

**Artefakt:** Aktualisierte Inventar-Spalten `primary` / `tags`.

## Phase 3 — Technology Sheets

**Ziel:** Wiederverwendbares Wissen in `technologies/<slug>/SHEET.md`.

Priorisierung: Technologien mit hohem Transferwert oder hohem Projektrisiko zuerst (bei PiDrive z. B. USB-MSC, AVRCP, DAB+-Pipeline).

**Wiederbegegnung:** Existiert der Slug schon, Sheet **erweitern** (nicht forken) — siehe [Wissenswachstum](DOCUMENT-STANDARD.md#wissenswachstum-wiederbegegnung-mit-bekannter-tech). Projektunterschiede → Phase 4.

**Artefakt:** Sheets nach [`templates/technology-sheet.md`](../templates/technology-sheet.md). Inventar-Status → `documented`.

## Phase 4 — Project Applications

**Ziel:** Projektspezifische Anwendung in `projects/<id>/applications/<slug>.md`.

Hier gehören Pfade, Datenflüsse, Konfigschlüssel, Feldbelege und „so hat es sich im Auto verhalten“.

**Artefakt:** Applications nach Vorlage. Inventar-Status → `applied`, Coverage → `partial`/`full`.

## Phase 5 — Transfer / Folgeprojekte

**Ziel:** Wissen für andere Projekte nutzbar machen.

- Sheet um Transfer-Hinweise ergänzen.
- Folgeideen unter `projects/<id>/FOLLOW-ON-IDEAS.md` oder neuem Projektordner.
- Optional: Audit-Kampagne abschließen (`audits/<id>/`).

**Artefakt:** Transfer-Abschnitte, Folgeprojekt-Skizzen; Status `transferred` wo greifbar.

## Exit-Kriterien (pro Projekt-Audit)

Ein Audit-Durchlauf gilt als belastbar, wenn:

1. Scope und Inventar existieren.
2. Coverage für Prioritäts-Techs nicht mehr `none` ohne Begründung.
3. Mindestens die priorisierten Sheets + Applications geschrieben sind.
4. Offene Fragen explizit gelistet sind (nicht implizit „fertig“).

## Pilot-Reihenfolge (Schema-Validation)

Nicht viele Sheets parallel öffnen. Zuerst einen **vollen Zyklus** durch das Framework:

```
Technology Sheet → Project Application → Evidence Review
  → Architecture/Dataflow → Maturity → Reusability → Lessons
```

| # | Pilot | Profil | Warum |
|---|-------|--------|-------|
| 1 | `usb-msc` | Protokoll + Streaming + Lab/Feld-Messkette | dichteste Evidenzlage in PiDrive |
| 2 | `bmw-nbt-evo` | Empirisches Host-Verhalten (USB, später BT) | erzwingt Ebene **C** getrennt von Spec |
| 3 | `avrcp` | BT-Protokoll / State Machine / Metadaten | anderes Profil als MSC |

Pilot 1 (closed): [`audits/pidrive-2026-msc/`](../audits/pidrive-2026-msc/). Pilot 2 (active): [`audits/pidrive-2026-bmw-hu/`](../audits/pidrive-2026-bmw-hu/).

## Werkzeuge

Methoden (Tracing, Korrelation, Replay, …) als eigene Notes unter `methods/` führen und aus Applications/Audits verlinken — nicht in jedem Sheet wiederholen.

## Assistenz-Prompts

Standardisierte Arbeitsaufträge (kein Schreib-Bot): [PROMPT-CONTRACT.md](PROMPT-CONTRACT.md), Prüfliste [REVIEW-CHECKS.md](REVIEW-CHECKS.md), Vorlagen [`templates/prompts/`](../templates/prompts/).

Typischer Ablauf: Befund/Prompt erzeugen → KI oder Mensch arbeitet den Auftrag ab → optional `quality-review` gegen den Standard.
