# Project Application: bmw-nbt-evo in bmw-nbt-media-index

```yaml
project_id: bmw-nbt-media-index
tech_slug: bmw-nbt-evo
status: active
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../../audits/bmw-nbt-media-index-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W1
```

## Rolle

Bestehendes Sheet `bmw-nbt-evo` als Plattformanker für fünf voneinander
getrennte **Offline**-Quellen. Die Anwendung beschreibt Medienbackup-,
Container- und Forensikkontext; sie erweitert keine Host-Laufzeitclaims.

## A/B/C

| Ebene | Aussage |
|-------|---------|
| A | [`bmw-nbt-evo`](../../../technologies/bmw-nbt-evo/SHEET.md) bleibt der bestehende Plattform-Contract; kein neues Sheet. |
| B | `idrivetools`, BMC, BMWFirmwareExtractor und das Autopsy-Modul implementieren konkrete Offline-Verarbeitung; BMW_HU_Info liefert am Pin nur README-Kontext. |
| C | Es gibt keine eigene Host-/Lab-/Field-Beobachtung. Live-USB-Cache, Resume, Identity-Key und HU-Verhalten bleiben `UNKNOWN`. |

## Repositories

| Repo | Commit | Rolle | Lizenz am Snapshot |
|------|--------|-------|---------------------|
| `Centurix/idrivetools` | `08e0c43c63a64547b018d5c627f59d5453d9505b` | BMWData pack/unpack, Metadaten | keine Lizenzdatei / `UNKNOWN` |
| `sivu22/BMC` | `c22b27edaf4d5aba50fe66f7e005b272b71e5b35` | BRx → Medientypen | MIT |
| `superabiliter/BMWFirmwareExtractor` | `5cd2895bb92622ded6feb18b79325188e3ac9860` | NBT(EVO)/MGU Containerparser | keine Lizenzdatei / `UNKNOWN` |
| `Ricardo2192643/BMW-IVI-NBT-ingest-module` | `127fb15c420334dcc6dedf1010b902d8837c9144` | Autopsy/Jython für Offline-Datenquellen | GPL-3.0 |
| `Viaszx/BMW_HU_Info` | `c140b1d62ca59e0043a8c620eb390c96e6272c76` | README-only Varianten-/Capability-Kontrast | keine Lizenzdatei / `UNKNOWN` |

## Offline-Datenfluss

```text
autorisierte Backup-/Image-Kopie
  ├─ BMWData → idrivetools / BMC → Medien + Backup-Metadaten
  ├─ Upgrade-Container → FirmwareExtractor → Forschungsartefakte
  └─ gemountete QNX-Kopie / SQLite → Autopsy-Modul → Forensikartefakte

kein Pfad in dieser Kampagne → Live-NBT / Fahrzeug / USB-Verhalten
```

## Relevante Pfade

| Repo | Pfad | Desk-Beleg |
|------|------|------------|
| idrivetools | `README.rst` | BMWData-Hierarchie, unterstützte BRx-Typen |
| idrivetools | `idrivetools/file_tools/bmw_{backup,info,data_1}_file.py` | `NBTV2`, Info-/Zählmetadaten, `NBTevo_E15413A` als Codekonstante |
| BMC | `BMC/MediaConverter.cs` | BRx-Mapping und byteweise Transformregeln |
| FirmwareExtractor | `extractor.py` | Containerheader, zlib, Datei/Verzeichnis/Symlink-Ausgabe |
| NBT ingest | `IvibmwDataSourceIngestModule.py` | SQLite-Suche/Queries und Autopsy-Artefakte |
| BMW_HU_Info | `README.md` | Upstream nennt NBT/NBTEVO/ENAVEVO/MGU; kein prüfbarer Code |

## Ebene B — Offline-Implementierungsclaims

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| BMWData-Backups besitzen dokumentierte Medienhierarchie plus `data_1`, `data_1_count`, `info`, `BMWBackup.ver` | `EVID-BMWMEDIA-2026-10-13-001` | `FACT` |
| idrivetools erzeugt Metadaten aus Dateizahl/-größe, Verzeichnisliste, Zeit und Codekonstanten | `EVID-BMWMEDIA-2026-10-13-002` | `FACT` |
| BMC ordnet die im Code gelisteten BRx-Endungen Medientypen zu | `EVID-BMWMEDIA-2026-10-13-003` | `FACT` |
| BMC implementiert je BRx-Typ unterschiedliche Byte-Invertierungsgrenzen | `EVID-BMWMEDIA-2026-10-13-004` | `FACT` |
| BMC-README berichtet Tests mit CIC und NBT Evo ID4 | `EVID-BMWMEDIA-2026-10-13-005` | `FACT` (README-Aussage) |
| Die berichtete Kompatibilität wurde in dieser Kampagne nicht reproduziert | `EVID-BMWMEDIA-2026-10-13-014` | `UNKNOWN` |
| FirmwareExtractor parst Containerblöcke und schreibt dekomprimierte Artefakte | `EVID-BMWMEDIA-2026-10-13-006` | `FACT` |
| Autopsy-Modul fragt u. a. Medienquellen, Musikgruppen, USB-Details und Ordner aus Offline-SQLite ab | `EVID-BMWMEDIA-2026-10-13-007` | `FACT` |
| Offline-SQLite enthält Kandidatenfelder wie USB-Serial, `identifier`, `mountpath`, `basepath`, `lastseen` und `last_sync` | `EVID-BMWMEDIA-2026-10-13-015` | `FACT` |
| Forensikpfad kann hochsensible personenbezogene Artefakte verarbeiten | `EVID-BMWMEDIA-2026-10-13-008` | `FACT` |
| BMW_HU_Info enthält am Snapshot nur README-Claims, keinen prüfbaren Implementierungsbeleg | `EVID-BMWMEDIA-2026-10-13-009` | `FACT` |
| Kein Snapshot belegt Live-USB-Cache, Resume, Identity-Key oder HU-Laufzeitverhalten | `EVID-BMWMEDIA-2026-10-13-011` | `FACT` (Evidence-Abwesenheitsgrenze) |

## Ebene C — Host-/Lab-/Field-Evidenz

Keine eigene Beobachtung. Insbesondere bleiben Live-USB-Cache, Resume,
Identity-Key, Read-Reihenfolge und Timing `UNKNOWN`.

## Review-Grenzen

- Keine Kompatibilität aus Versionsstrings oder README allein ableiten.
- Backup-Metadaten sind Formatbeobachtung, kein Identity-Key-Beleg.
- Forensische `identifier`-/Serial-/Pfad-/Zeitfelder sind persistente
  Datenbankfelder, aber kein nachgewiesener Cache-Schlüssel oder
  Eviction-Mechanismus.
- Parser nur auf Kopien und in Isolation; Archivepfade, Symlinks,
  Dekompressionsgrößen und Ausgaben validieren.
- Keine sensiblen HU-Info-Capabilities in operative Schritte übersetzen.
