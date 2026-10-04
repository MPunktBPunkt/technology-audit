# Dokumentenstandard

Verbindliche Regeln für alle Dokumente in diesem Repository. Abweichungen nur mit Begründung in der jeweiligen Datei (Abschnitt `Abweichungen`).

## Schichtenmodell

| Schicht | Pfad | Lebensdauer | Wiederverwendbar? |
|---------|------|-------------|-------------------|
| Projekt | `projects/<id>/` | solange das Projekt relevant ist | nein (projektspezifisch) |
| Technologie | `technologies/<slug>/` | dauerhaft | ja (über Projekte hinweg) |
| Methode | `methods/<slug>.md` | dauerhaft | ja |
| Audit | `audits/<id>/` | Kampagne / Zeitpunkt | teilweise (Lessons → Sheets) |

**Kernregel:** Projektwissen gehört nicht in Technology Sheets. Technology Sheets beschreiben die Technologie selbst; Project Applications beschreiben den Einsatz *in einem Projekt*.

## Dokumenttypen

### 1. Technology Sheet

| | |
|--|--|
| **Pfad** | `technologies/<slug>/SHEET.md` |
| **Vorlage** | [`templates/technology-sheet.md`](../templates/technology-sheet.md) |
| **Zweck** | Wiederverwendbares Wissen: Definition, Schnittstellen, Fallstricke, Transfer |

- Genau **eine** Primary-Kategorie aus der [Taxonomie](TAXONOMY.md).
- Beliebig viele Secondary-Tags.
- Verweise auf Projekte nur als Liste „gesehen in“, ohne Projektdetails.

### 2. Project Scope

| | |
|--|--|
| **Pfad** | `projects/<id>/SCOPE.md` |
| **Vorlage** | [`templates/project-scope.md`](../templates/project-scope.md) |
| **Zweck** | Grenzen, Systeme, Nicht-Ziele, Quellen-Repos |

### 3. Project Inventory

| | |
|--|--|
| **Pfad** | `projects/<id>/INVENTORY.md` |
| **Vorlage** | [`templates/project-inventory.md`](../templates/project-inventory.md) |
| **Zweck** | Alle erkannten Technologien mit Status, Taxonomie, Coverage |

Statuswerte:

| Status | Bedeutung |
|--------|-----------|
| `candidate` | Signal gefunden (Name, Datei, Doku), noch nicht verifiziert |
| `observed` | im Code/Betrieb bestätigt |
| `documented` | Technology Sheet existiert |
| `applied` | Project Application existiert |
| `transferred` | Wissen in Folgeprojekt übernommen |

Coverage-Spalte: `none` · `partial` · `full` — verhindert die Illusion „fertig“, wenn nur ein Inventareintrag existiert.

### 4. Project Application

| | |
|--|--|
| **Pfad** | `projects/<id>/applications/<slug>.md` |
| **Vorlage** | [`templates/project-application.md`](../templates/project-application.md) |
| **Zweck** | *Wie* die Technologie *in diesem Projekt* sitzt |

Enthält: relevante Pfade, Datenflüsse, Konfiguration, Feldbelege, offene Fragen. Kein generisches Technologie-Lehrbuch — das gehört ins Sheet.

### 5. Method Note

| | |
|--|--|
| **Pfad** | `methods/<slug>.md` |
| **Vorlage** | [`templates/method-note.md`](../templates/method-note.md) |
| **Zweck** | Analyseverfahren (Tracing, Replay, Korrelation, Hardware-Validierung, …) |

### 6. Audit Campaign

| | |
|--|--|
| **Pfad** | `audits/<id>/README.md` |
| **Vorlage** | [`templates/audit-campaign.md`](../templates/audit-campaign.md) |
| **Zweck** | Zeitlich begrenzter Analyselauf mit Exit-Kriterien und Ergebnislinks |

ID-Schema: `<project>-<YYYY>` oder `<project>-<YYYY>-<kurzname>` (z. B. `pidrive-2026`, `pidrive-2026-msc`).

## Namenskonventionen

| Element | Regel | Beispiele |
|---------|-------|-----------|
| Projekt-ID | `kebab-case`, kurz | `pidrive`, `esp-hub` |
| Tech-Slug | `kebab-case`, stabil | `usb-msc`, `avrcp`, `dab-plus` |
| Method-Slug | `kebab-case` | `msc-trace-correlation` |
| Audit-ID | siehe oben | `pidrive-2026` |

Slugs ändern sich selten. Umbenennung = Redirect-Hinweis in alter Datei oder Inventar aktualisieren.

## Verknüpfungsregeln

1. Inventar verlinkt auf `technologies/<slug>/SHEET.md` (auch wenn die Datei noch fehlt — Zielpfad steht fest).
2. Application verlinkt auf dasselbe Sheet und auf den Inventareintrag.
3. Audit verlinkt auf Inventar-Zeilen und genutzte Methoden.
4. Keine zyklischen Detailkopien: eine Faktenquelle pro Aspekt.

## Wissens-Ebenen (A / B / C)

Jede Aussage in Sheets und Applications gehört in genau eine Ebene:

| Ebene | Name | Inhalt | Typischer Ort |
|-------|------|--------|---------------|
| **A** | Allgemein | Spec-/domänenweite Fakten (gilt unabhängig vom Projekt) | Technology Sheet |
| **B** | Projekt-Implementierung | Wie *dieses* Projekt die Tech baut | Project Application |
| **C** | Host-/Feld-Evidenz | Empirisches Verhalten eines konkreten Hosts (z. B. BMW HU) | Application (Abschnitt C) oder später Sheet `bmw-nbt-evo` |

**Harte Regel:** Aus „die HU macht X“ darf nicht still „USB-MSC macht X“ werden. Ebene-C-Claims brauchen Evidence-ID und Epistemic-Status.

## Epistemic-Status

| Status | Bedeutung |
|--------|-----------|
| `FACT` | Allgemein akzeptiertes Spec-/Domänenwissen (A) |
| `MEASURED` | Gemessen, reproduzierbar (Lab/Feld) |
| `INFERRED` | Aus Messungen abgeleitet, nicht direkt beobachtet |
| `HYPOTHESIS` | Arbeitshypothese, noch offen |
| `UNKNOWN` | Bewusst ungeklärt |
| `REJECTED` | Früher angenommen, später widerlegt (behalten!) |

## Evidence-IDs

Format: `EVID-<AREA>-<YYYY-MM-DD>-<nnn>`  
Beispiel: `EVID-USBMSC-2026-10-04-001`

- Kurzregister unter `audits/<kampagne>/evidence.md` oder im Application-Abschnitt.
- Rohdaten bleiben im Ursprungsrepo; hier nur ID + Claim + Link + Status.

## Reifegrade

Pro Technology/Application-Paar mitführen:

| Dimension | Skala | Bedeutung (kurz) |
|-----------|-------|------------------|
| Technology | R0–R5 | Wie gut die *allgemeine* Tech verstanden ist |
| Implementation | R0–R5 | Wie klar die *Projekt*-Implementierung beschrieben/stabil ist |
| Field evidence | R0–R5 | Stärke der Lab/Feld-Belege |
| Reusability | W0–W5 | Wie weit als generische Komponente übertragbar |

Orientierung: R0 unbekannt · R1 Signale · R2 beschrieben · R3 Lab · R4 Feld · R5 mehrfach validiert.  
W0 kein Transfer · W2 projektgebunden nutzbar · W4 eigenständiges Modul denkbar · W5 in Folgeprojekt belegt.

## Was nicht hierhin gehört

- Vollständige Projekt-Quelltexte oder Firmware-Binaries
- Roh-Traces ohne Auswertung (nur Verweis auf Artefaktpfade im Ursprungsrepo)
- Geheimnisse, Tokens, private Fahrzeugdaten

## Abweichungen

Wenn ein Dokument vom Standard abweichen muss: Abschnitt `## Abweichungen` mit Begründung. Dauerhafte Regeländerungen gehören in dieses Dokument, nicht in Einzeldateien.
