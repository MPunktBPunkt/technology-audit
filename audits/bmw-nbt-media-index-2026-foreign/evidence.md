# Evidence — bmw-nbt-media-index-2026-foreign

Desk 2026-10-13 · **standard_version 0.7.1** · Profile `lab-tool`.
Keine Repos ausgeführt; statische Analyse der gepinnten Snapshots.

## Quellen

| Repo | Commit | Lizenzbefund |
|------|--------|---------------|
| https://github.com/Centurix/idrivetools | `08e0c43c63a64547b018d5c627f59d5453d9505b` | keine Lizenzdatei / `UNKNOWN` |
| https://github.com/sivu22/BMC | `c22b27edaf4d5aba50fe66f7e005b272b71e5b35` | MIT (`LICENSE`) |
| https://github.com/superabiliter/BMWFirmwareExtractor | `5cd2895bb92622ded6feb18b79325188e3ac9860` | keine Lizenzdatei / `UNKNOWN` |
| https://github.com/Ricardo2192643/BMW-IVI-NBT-ingest-module | `127fb15c420334dcc6dedf1010b902d8837c9144` | GPL-3.0 (`LICENSE`, Source Header) |
| https://github.com/Viaszx/BMW_HU_Info | `c140b1d62ca59e0043a8c620eb390c96e6272c76` | keine Lizenzdatei / `UNKNOWN` |

## Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-BMWMEDIA-2026-10-13-001` | idrivetools dokumentiert `BMWData/Music/USB*` plus `data_1`, `data_1_count`, `info`, `BMWBackup.ver` und BRx-Medientypen | `FACT` | `idrivetools/README.rst` |
| `EVID-BMWMEDIA-2026-10-13-002` | idrivetools-Code erzeugt `NBTV2`, Verzeichnis-/Zeitdaten sowie Info aus BR-Dateizahl, Größe, Prüfsumme und Konstante `NBTevo_E15413A` | `FACT` | `bmw_backup_file.py`, `bmw_data_1_file.py`, `bmw_info_file.py` |
| `EVID-BMWMEDIA-2026-10-13-003` | BMC-Code mappt BR1/25/27/28/29/3/30/34/48/4/5/67 auf AAC/M4A/MP3/MP4/WMA/M3U/FLAC/JPG | `FACT` | `BMC/MediaConverter.cs` Enums und `GetMediaType` |
| `EVID-BMWMEDIA-2026-10-13-004` | BMC invertiert je BRx-Typ alle, begrenzte oder bis auf letzte Bytes des Inhalts; CIC-Zweig bei BR25/BR4 | `FACT` | `BMC/MediaConverter.cs::Convert` |
| `EVID-BMWMEDIA-2026-10-13-005` | Das BMC-README sagt, das Tool sei mit CIC und NBT Evo ID4 getestet | `FACT` | `BMC/README.md` |
| `EVID-BMWMEDIA-2026-10-13-006` | FirmwareExtractor parst 9-Byte-/Blockheader, Konfigurationsfelder, zlib-Daten und erzeugt Dateien/Verzeichnisse/Symlinks unter festem Ziel | `FACT` | `BMWFirmwareExtractor/extractor.py` |
| `EVID-BMWMEDIA-2026-10-13-007` | Autopsy-Modul sucht Offline-Dateien/SQLite und fragt u. a. `mediastores`, `categorydata_custom`, `usbdevicedetails`, `folders`, `library_albums`, `library_artists` ab | `FACT` | `IvibmwDataSourceIngestModule.py` |
| `EVID-BMWMEDIA-2026-10-13-008` | Dasselbe Modul verarbeitet Kontakte, Telefon/E-Mail/Adresse, Bluetooth, IMEI/IMSI, Anrufe, Nachrichten, Browser/Cookies und Medienhistorie | `FACT` | `IvibmwDataSourceIngestModule.py` Queries/Blackboard-Artefakte |
| `EVID-BMWMEDIA-2026-10-13-009` | BMW_HU_Info nennt NBT/NBTEVO/ENAVEVO/MGU und sensible Capabilities, enthält am Pin aber nur `README.md` | `FACT` | Repo-Baum + `BMW_HU_Info/README.md` |
| `EVID-BMWMEDIA-2026-10-13-010` | BMC hat MIT, NBT-ingest GPL-3.0; idrivetools, FirmwareExtractor und BMW_HU_Info haben am Pin keine Lizenzdatei | `FACT` | Snapshot-Bäume, `LICENSE`, `pyproject.toml` |
| `EVID-BMWMEDIA-2026-10-13-011` | Keine der fünf Quellen enthält eine Live-NBT-USB-Messung oder einen Beleg für Cache, Resume, Identity-Key oder konkretes HU-Laufzeitverhalten | `FACT` | vollständige Dateibäume und relevante Quellen an allen fünf SHAs; Korpusgrenze |
| `EVID-BMWMEDIA-2026-10-13-012` | Alle positiven Claims passen als Projektkontext unter bestehendes `bmw-nbt-evo`; kein neuer generischer Host-Contract wurde gefunden | `INFERRED` | `001`–`011` + bestehendes Sheet |
| `EVID-BMWMEDIA-2026-10-13-013` | Offline-Verarbeitung erfordert Autorisierung, Isolation, untrusted-input-Härtung und Schutz personenbezogener Daten | `INFERRED` | `006`–`010`; Scope-/Review-Analyse |
| `EVID-BMWMEDIA-2026-10-13-014` | Die im BMC-README genannte CIC-/NBT-Evo-ID4-Kompatibilität wurde in dieser Kampagne nicht reproduziert | `UNKNOWN` | Desk-only Scope; keine eigene Ausführung |
| `EVID-BMWMEDIA-2026-10-13-015` | Das NBT-Ingest-Modul liest aus Offline-SQLite unter anderem `mediastores` mit `msid`, `lastseen`, Name, `identifier` und `mountpath`, `usbdevicedetails` mit `deviceserialno`/`lastseen` sowie `folders` mit `basepath`/`last_sync` | `FACT` | `IvibmwDataSourceIngestModule.py`; gepinnter Snapshot |

## Claim-Grenzen

| Nicht belegter Claim | Status | Begründung |
|----------------------|--------|------------|
| NBT Live-USB-Cache oder Cache-Key | `UNKNOWN` | keine Live-Messung; Backup-/DB-Felder sind kein Laufzeitbeleg |
| Resume-Verhalten | `UNKNOWN` | keine Auswahl-/Wiedergabesession |
| Identity-Key der HU | `UNKNOWN` | Versions-, Serial- und Identifier-Felder zeigen keine kausale Schlüsselnutzung |
| Indexierungsdauer oder Read-Reihenfolge | `UNKNOWN` | keine USB-Traces oder Zeitmessungen |
| NBT-Evo-Kompatibilität aller Tools/Varianten | `UNKNOWN` | Upstream-README bzw. Versionsstrings ersetzen keine Reproduktion |
| BMW_HU_Info-Funktionalität | `UNKNOWN` | README-only am gepinnten Snapshot |

## Security-/Safety-Befund

- Keine Zugriffs- oder Bediensequenzen werden aus README-Capabilities
  übernommen.
- Firmware-/Archivpfade, Symlinks und Dekompressionsgrößen sind untrusted
  input; praktische Prüfung nur isoliert und auf Kopien.
- Forensikdaten können unmittelbar personenbezogen sein; rechtliche
  Grundlage, Zweckbindung, Minimierung und Zugriffsschutz sind Gates.
- Fehlende Lizenzdatei bedeutet nicht Public Domain; keine Übernahme oder
  Distribution bis zur Klärung.

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | fünf SHAs verifiziert; statische Desk-Analyse |
| 2026-10-13 | `bmw-nbt-evo` reuse; kein neues Sheet |
| 2026-10-13 | Live-Cache/Resume/Identity/HU-Verhalten explizit ausgeschlossen |
