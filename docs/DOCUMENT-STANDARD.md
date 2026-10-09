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

## Wissenswachstum (Wiederbegegnung mit bekannter Tech)

Wissen darf **nur wachsen**, nie still überschrieben oder projektweise verdoppelt werden.

| Situation | Tun | Nicht tun |
|-----------|-----|-----------|
| Dieselbe Tech, zweites Projekt | Bestehendes Sheet (Slug) behalten; `seen_in` erweitern; nur **neue Ebene-A-Fakten** ergänzen | Neues Sheet `…-ergo` / `…-v2` anlegen |
| Andere Implementierung derselben Tech | Neue **Project Application** (B); Varianten im Sheet unter Fallstricke/Transfer als Alternativen | Sheet in „unseren Code-Pfad“ umschreiben |
| Anderes Host-/Geräteverhalten | Ebene **C** in Application oder eigenes Host-Sheet (wie `bmw-nbt-evo`); Evidence-IDs | C-Claims als allgemeines Spec-Wissen ins Sheet schieben |
| Früherer Irrtum | Claim behalten, Status → `REJECTED` (+ kurzer Hinweis) | Zeile löschen |
| Spec bestätigt / widerlegt | Epistemic-Status und Reifegrade anheben (`R*`, `W*`) | Maturity „schönrechnen“ ohne Evidence |

**Slug-Stabilität:** Ein Slug = eine Technologie. Ähnlichkeit allein reicht nicht für Merge — wenn Primary + Abgrenzung klar auseinanderfallen, neuer Slug; sonst bestehendes Sheet pflegen.

**Reusability:** `W2` = in einem Projekt beschrieben; erst ab **zweitem** unabhängigen `seen_in` mit Application typischerweise `W3` prüfen. Feld/Lab multi-host → `W4`/`W5` nach [Reifegrade](#reifegrade).

**Audit-Checkliste bei Treffer auf bestehenden Slug:**

1. Inventar: Status mindestens `observed`; Sheet-Link auf **bestehenden** Pfad.
2. Sheet: A-Delta (Fallstricke, Transfer, Referenzen) — oder bewusst „kein A-Delta“.
3. Application: nur B/C für *dieses* Projekt.
4. Evidence: neue IDs; Querverweis auf ältere Kampagne erlaubt.
5. `seen_in` + Indexes (`technologies/README.md`) aktualisieren.

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

### Reifegrade (Beispiele)

| Situation | Typische Werte |
|-----------|----------------|
| Inventareintrag, noch kein Sheet | Technology R0–R1 · Rest R0 · W0 |
| Sheet geschrieben, nur Spec/Abgrenzung | Technology R2 · Implementation/Field R0 (Details in Application) · W1 |
| Lab-Messungen reproduzierbar, Feld offen | Field evidence R3 · nicht R4 |
| Feld-Oracle/Ohr dokumentiert PASS | Field evidence R4 möglich |
| Mehrere Hosts/Projekte bestätigen dasselbe A-Muster | Technology R5 / W4–W5 prüfen |
| Wissen in Folgeprojekt übernommen | Reusability W5 · Status `transferred` |

**Regel:** Lab-PASS allein begründet kein R4. Offenes Exit-Kriterium „Feld-AV PASS“ und `field_evidence: R4` widersprechen sich — siehe [REVIEW-CHECKS.md](REVIEW-CHECKS.md) R1–R2.

**Negativbeispiele (nicht verwechseln):**

| Angabe | Falsch | Richtig |
|--------|--------|---------|
| Lab AV am Host-dd PASS | `field_evidence: R4` | R3 — Feld-Ohr/Exit noch offen |
| Einzelnes Feld-Oracle (z. B. C′) PASS | pauschal R4 für gesamtes AV | R3 mit Claim-Tabelle; R4 erst wenn Exit-Kriterium erfüllt |
| Sheet + Application existieren | `reusability: W4` | W1–W2 bis Transfer/Modul belegt |
| Nur im PiDrive-Repo beschrieben | `reusability: W5` | W2 projektgebunden; W5 nur mit Folgeprojekt-Nachweis |

Sheets dürfen `implementation`/`field_evidence` auf R0 lassen, wenn die Bewertung in der Application geführt wird.

## Assistenz / Prompts

- Reuse bei neuem Projekt: [REUSE.md](REUSE.md)
- Vertrag: [PROMPT-CONTRACT.md](PROMPT-CONTRACT.md)
- Prüffragen: [REVIEW-CHECKS.md](REVIEW-CHECKS.md)
- Vorlagen: [`templates/prompts/`](../templates/prompts/)
- Generierte Aufträge: [`artifacts/prompts/`](../artifacts/prompts/)

Assistenz darf Wissensdateien nicht autonom schreiben — nur strukturierte Arbeitsaufträge erzeugen. Bootstrap-Prompts müssen den bestehenden Sheet-Katalog einbinden.

## Externe Quellen

Kein Pflichtordner „Wiki/Google“. Referenzen gehören ins Technology Sheet (Abschnitt Referenzen). Optional später `technologies/<slug>/REFERENCES.md`, wenn die Quellenlage komplex ist.

Quellenarten kennzeichnen: **normativ** (Spec/Hersteller) · **projektintern** (Code/Evidence-Links) · **sekundär** (Wiki/Blog, sparsam).

## Was nicht hierhin gehört

- Vollständige Projekt-Quelltexte oder Firmware-Binaries
- Roh-Traces ohne Auswertung (nur Verweis auf Artefaktpfade im Ursprungsrepo)
- Geheimnisse, Tokens, private Fahrzeugdaten

## Abweichungen

Wenn ein Dokument vom Standard abweichen muss: Abschnitt `## Abweichungen` mit Begründung. Dauerhafte Regeländerungen gehören in dieses Dokument, nicht in Einzeldateien.
