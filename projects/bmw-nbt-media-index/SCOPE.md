# Project Scope: bmw-nbt-media-index (Fremd)

```yaml
project_id: bmw-nbt-media-index
title: BMW NBT Media/Backup/Forensics Desk Sources
updated: 2026-10-13
profile_hint: lab-tool
status: active
reviewed_commits:
  Centurix/idrivetools: 08e0c43c63a64547b018d5c627f59d5453d9505b
  sivu22/BMC: c22b27edaf4d5aba50fe66f7e005b272b71e5b35
  superabiliter/BMWFirmwareExtractor: 5cd2895bb92622ded6feb18b79325188e3ac9860
  Ricardo2192643/BMW-IVI-NBT-ingest-module: 127fb15c420334dcc6dedf1010b902d8837c9144
  Viaszx/BMW_HU_Info: c140b1d62ca59e0043a8c620eb390c96e6272c76
```

## Zweck

Fünf immutable Snapshots ausschließlich als Desk-Quellen für
Medienbackup-Strukturen, BRx-Dateikonvertierung, Firmwarecontainer und
forensische Artefaktklassen prüfen. Bestehende Host-Technologie
[`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md) wiederverwenden.

## Im Scope

- statische README-, Lizenz- und Codeanalyse an den genannten SHAs
- BMWData-/BRx-Formate und deren Offline-Verarbeitung
- Firmwareextraktion nur als defensiver Analysekontext
- Offline-Forensik bereits rechtmäßig erhobener Images und Datenbanken
- Privacy-, Provenienz-, Lizenz- und Parser-Sicherheitsgrenzen

## Nicht im Scope

- Fahrzeugzugriff, Head-Unit-Verbindung, Diagnose, Codierung oder Änderung
- Authentisierung, Schlüssel, SSH, FSC oder Umgehung von Schutzmaßnahmen
- Ausführen fremder Binärdateien oder Parser auf produktiven Systemen
- Beschaffung oder Extraktion von Daten ohne Eigentümerfreigabe
- neue Host-Technology, Technology Sheets, Methods oder Shared Indexe
- Aussagen zu Live-USB-Cache, Resume, Identity-Key, Indexierungszeit,
  Host-Reads, Prefetch, Wiedergabe oder anderem HU-Laufzeitverhalten

## Security-/Safety-Grenzen

Die Kampagne dokumentiert **keine Zugriffsanleitung**. Firmware- und
Forensikwerkzeuge dürfen nur offline, auf autorisierten Kopien, in isolierter
Umgebung und mit unveränderter Beweismittelquelle bewertet werden. Extrahierte
Pfade, Symlinks und Dateigrößen sind als untrusted input zu behandeln.
Personenbezogene Daten wie Kontakte, Nachrichten, Gerätekennungen und
Medienhistorie unterliegen Zugriffskontrolle, Minimierung und Löschkonzept.

## Epistemische Grenze

`FACT` bedeutet hier ausschließlich: im gepinnten Quelltext oder README
vorhanden. README-Kompatibilitätsaussagen sind als Upstream-Aussage
dokumentiert, nicht als eigene Messung. Desk-FACT ≠ Lab-FACT ≠ Field-FACT.
