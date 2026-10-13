# Audit Campaign: bmw-nbt-media-index-2026-foreign

```yaml
id: bmw-nbt-media-index-2026-foreign
project_id: bmw-nbt-media-index
started: 2026-10-13
ended: 2026-10-13
status: closed
profile: lab-tool
standard_version: "0.7.1"
reuse_outcomes:
  reused: [bmw-nbt-evo]
  new: []
  not_helped: [live-usb-cache, resume, identity-key, hu-runtime-behavior]
  process: "Desk-only; five immutable snapshots; media/backup/forensics boundary"
```

## Ziel

Fünf Foreign-Snapshots auf belastbare Offline-Claims zu BMW-Medienbackups,
BRx-Konvertierung, Firmwarecontainern und NBT-Forensik prüfen. Das bestehende
Sheet `bmw-nbt-evo` wiederverwenden, ohne Host-Laufzeitverhalten zu behaupten.

## Scope

[SCOPE](../../projects/bmw-nbt-media-index/SCOPE.md) — desk only. Keine
Fahrzeug-/HU-Interaktion, kein Ausführen fremder Binärdateien und keine
Zugriffsanleitung.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1 und fünf vollständige SHAs | erfüllt |
| 2 | nur Projekt/Application/Audit-Artefakte | erfüllt |
| 3 | `bmw-nbt-evo` reuse; keine neue Host-Technology | erfüllt |
| 4 | A/B/C und Lizenzstatus getrennt | erfüllt |
| 5 | keine Live-Cache-/Resume-/Identity-/HU-Claims | erfüllt |
| 6 | Security-/Safety-/Privacy-Grenzen ohne Zugriffsanleitung | erfüllt |
| 7 | C10–C13 behandelt | erfüllt |

## Decision Trace (C10)

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neues Host-Sheet? | Neuer generischer Host-Contract belegt? | `EVID-BMWMEDIA-2026-10-13-010` | Nein; `bmw-nbt-evo` reuse | KNOWN BEFORE TEST |
| Backup-Claims übernehmen? | Code/README am SHA vorhanden? | `EVID-BMWMEDIA-2026-10-13-001`–`005` | Ja, nur offline und epistemisch getrennt | DISCOVERED DURING TEST |
| Forensikclaims übernehmen? | Konkrete Queries/Artefakte im Code? | `EVID-BMWMEDIA-2026-10-13-007`/`008`/`015` | Ja, mit Privacy-/Autorisierungsgate; persistente Felder sind kein Live-Key-Beweis | DISCOVERED DURING TEST |
| BMW_HU_Info als Implementierungsbeleg? | Liegt prüfbarer Code vor? | `EVID-BMWMEDIA-2026-10-13-009` | Nein; README-only candidate | DISCOVERED DURING TEST |
| Live-HU-Verhalten ableiten? | Enthält eine Quelle Live-Messungen? | `EVID-BMWMEDIA-2026-10-13-011` | Nein; explizit `UNKNOWN` | DISCOVERED AFTER TEST |
| Codeübernahme? | Lizenz eindeutig? | `EVID-BMWMEDIA-2026-10-13-010` | Nur BMC/GPL-Modul lizenzklar; sonst STOP | DISCOVERED DURING TEST |

## Engineering Review Checks (C11)

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-BMWMEDIA-2026-10-13-001`/`002` | Dateizahl, Größe, Zeit und Versionsstring nicht als HU-Identity-Key umdeuten | DISCOVERED DURING TEST |
| `EVID-BMWMEDIA-2026-10-13-003`/`004` | BRx-Mapping und Transformgrenze pro Typ testen; unbekannte Endung fail-closed | DISCOVERED DURING TEST |
| `EVID-BMWMEDIA-2026-10-13-006` | Zielpfade normalisieren; Traversal/Symlink-Escape und Dekompressionslimits prüfen | DISCOVERED DURING TEST |
| `EVID-BMWMEDIA-2026-10-13-007`/`008` | Nur read-only Kopien; Provenienz, Minimierung, Zugriff und Löschung prüfen | DISCOVERED DURING TEST |
| `EVID-BMWMEDIA-2026-10-13-015` | USB-Serial, `identifier`, Mount-/Basepath und Zeitfelder nur als Identity-Hypothesen führen; keine kausale Cache-Key-Aussage ohne HU-A2 | DISCOVERED AFTER TEST |
| `EVID-BMWMEDIA-2026-10-13-009` | README-Capability ohne Code/Lab nie als Implementierungs-FACT führen | DISCOVERED DURING TEST |
| `EVID-BMWMEDIA-2026-10-13-011` | Offline-Artefakt nie als Live-HU-/USB-Verhaltensbeleg verwenden | KNOWN BEFORE TEST |

## Kill-Kriterien (C12)

```text
NO JUSTIFIED KILL CRITERION
Begründung: Diese abgeschlossene Kampagne war eine statische Desk-
Korpusklassifikation ohne Messlauf oder freizugebenden Implementierungspfad.
Quellenmangel, fehlende Lizenz oder Scope-Verletzung sind Ausschluss- und
Qualitätsgates, aber kein präregistrierter Hypothesentest. Sie werden daher
nicht rückwirkend als vorab gesetzte Kill-Kriterien ausgegeben.
```

Für jede spätere praktische Nutzung gelten zusätzlich STOP-Gates bei fehlender
Autorisierung, personenbezogenen Daten ohne Schutzkonzept, ungeklärter Lizenz
oder unisolierter Verarbeitung untrusted Container.

## Bezug Inventar

- [INVENTORY](../../projects/bmw-nbt-media-index/INVENTORY.md)
- [Application](../../projects/bmw-nbt-media-index/applications/bmw-nbt-evo.md)
- [Evidence](evidence.md)

## Knowledge Feedback (C13)

Desk only — keine Lab-/Field-Ergebnisse, daher kein Rückkanal neuer
MEASURED-Claims. Die Desk-Evidence fließt ausschließlich in diese Application;
das bestehende Technology Sheet bleibt unverändert.

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact.

## Lessons → Transfer

- Backup-/Forensikartefakte können Plattformkontext liefern, aber kein
  Live-Hostverhalten beweisen.
- README-Testclaims, Code-FACT und eigene Messung müssen getrennt bleiben.
- Offline-Parser brauchen Security-, Provenienz- und Datenschutzgates, auch
  wenn die Kampagne selbst keinen Zugriff ausführt.
