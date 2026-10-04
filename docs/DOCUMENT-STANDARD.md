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

## Was nicht hierhin gehört

- Vollständige Projekt-Quelltexte oder Firmware-Binaries
- Roh-Traces ohne Auswertung (nur Verweis auf Artefaktpfade im Ursprungsrepo)
- Geheimnisse, Tokens, private Fahrzeugdaten

## Abweichungen

Wenn ein Dokument vom Standard abweichen muss: Abschnitt `## Abweichungen` mit Begründung. Dauerhafte Regeländerungen gehören in dieses Dokument, nicht in Einzeldateien.
