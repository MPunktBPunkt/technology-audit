# Methodik

Vorgehen für ein Technologie-Audit. Jede Phase liefert Artefakte aus dem [Dokumentenstandard](DOCUMENT-STANDARD.md).

## Überblick

```
0 Signale → 1 Inventar → 2 Taxonomie → 3 Sheets → 4 Applications → 5 Transfer
```

Nicht linear erzwingen: Rücksprünge sind normal (neue Signale aus der Historie, Feldtests). Coverage im Inventar zeigt, was fehlt.

## Phase 0 — Signale sammeln

**Ziel:** Herausfinden, was überhaupt existiert — noch keine Bewertung.

**Zuerst:** bestehende Wissensbasis konsultieren — [`docs/REUSE.md`](REUSE.md) und [`technologies/README.md`](../technologies/README.md). Signale gegen bekannte Slugs matchen, bevor neue Sheets vorgeschlagen werden. **Profil wählen:** [`AUDIT-PROFILES.md`](AUDIT-PROFILES.md) (`firmware` / `lab-tool` / `planning` / `ops-field`).

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

## Operationalisierung (0.7.0)

Zwischen Evidence und Lab gehört die Brücke **Entscheidung + Engineering Action** — sonst bleibt Wissen dokumentiert, aber nicht handlungsleitend.

```text
bestehendes Wissen → Delta-Audit → Evidence
  → Decision Trace + Review Checks + Kill-Kriterien
  → Lab → Field → Evidence zurück in Application/Sheet
```

| Schritt | Wann | Artefakt |
|---------|------|----------|
| Decision Trace | Go/No-Go (Lab/Feld) | Kampagne: Entscheidung → Frage → Evidence → Konsequenz (+ opt. Wissenszeitpunkt) |
| Engineering Review Checks | Evidence betrifft Zielcode | Pre-Test-Checkliste (State, Re-Entry, Idempotenz) |
| Kill-Kriterien | vor erstem Messlauf | präregistrierte Widerlegung **oder** `NO JUSTIFIED KILL CRITERION` |
| Knowledge Feedback | nach Lab/Field | neue Evidence-IDs + Application/Sheet-Update |
| Retro-Impact | nur Revalidation / Counterfactual | optional; siehe Template |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact. Validierungsbeispiel: Busy-Retry-Desk [`tinyusb-msc-busy-retry-2026`](../audits/tinyusb-msc-busy-retry-2026/) → NBT-Feld [`pidrive-2026-bmw-hu`](../audits/pidrive-2026-bmw-hu/) (`EVID-BMWHU-2026-10-12-*`).

**`UNKNOWN` ist kein automatisches STOP-Kriterium.** Epistemisch bleibt `UNKNOWN` ungeklärt: es kann weitere Untersuchung rechtfertigen und zusammen mit anderer Evidence ein Gate oder Kill auslösen — allein erzeugt es kein STOP. Fehlt ein begründbares Falsifikationskriterium → `NO JUSTIFIED KILL CRITERION` (nicht: „alles bewiesen“).

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

## Chip-/SoC-Varianten und Transfer-Gates

Desk-Wissen darf **nicht** still von einer Chip-Variante auf eine andere springen.

| Stufe | Erlaubt | Nicht |
|-------|---------|-------|
| Belegte Variante (Code + Docs) | Sheet/Claims mit klarem Chip-Scope | „ESP32 kann X ⇒ S3 kann X“ |
| Verwandte Variante ohne Beleg | `UNKNOWN` / `HYPOTHESIS` + Gate benennen | neues Sheet als wäre es bewiesen |
| Architekturidee (Hub-Knoten, Netzwerk-TX) | FOLLOW-ON / Application-Skizze | Technology Sheet vor Lab-/Pfad-Evidence |

**Gate-Reihenfolge (RF/Clock, typisch):**

```text
E-0  Desk: TRM/IDF bis Register + Pin-Mux (kein RF nötig)
E-1  Lab: konstanter Träger messbar (Frequenz vorhanden)
E-2  Raster / Stabilität
E-3  Modulation (Teiler-/Frac-Updates → hörbarer/messbarer Hub)
```

Erst nach positivem Gate darf ein Varianten-Sheet (oder Sheet-Ausweitung) entstehen. Methode: [`methods/hw-path-gate.md`](../methods/hw-path-gate.md).

## KB-Cross-Check (Wissensqualität)

Um zu prüfen, ob Sheets als **Reasoning-Bausteine** taugen (nicht nur als Wiki):

1. Primärquelle = Audit-Repo (Sheets, Evidence, Applications).
2. Modell/Mensch muss FACT / INFERRED / HYPOTHESIS / UNKNOWN / REJECTED trennen.
3. Keine Zielarchitektur vorgeben beim **Blindtest** — nur Frage + erlaubte Pfade.
4. Ergebnis auswerten: Reproduzierbarkeit, Transfer-Bremse, erkannte Absolutismen.

Prompt: [`templates/prompts/kb-cross-check.md`](../templates/prompts/kb-cross-check.md) · Method: [`methods/kb-cross-check.md`](../methods/kb-cross-check.md).

## Werkzeuge

Methoden (Tracing, Korrelation, Replay, …) als eigene Notes unter `methods/` führen und aus Applications/Audits verlinken — nicht in jedem Sheet wiederholen.

## Assistenz-Prompts

Standardisierte Arbeitsaufträge (kein Schreib-Bot): [PROMPT-CONTRACT.md](PROMPT-CONTRACT.md), Prüfliste [REVIEW-CHECKS.md](REVIEW-CHECKS.md), Vorlagen [`templates/prompts/`](../templates/prompts/).

Typischer Ablauf: Befund/Prompt erzeugen → KI oder Mensch arbeitet den Auftrag ab → optional `quality-review` gegen den Standard.
