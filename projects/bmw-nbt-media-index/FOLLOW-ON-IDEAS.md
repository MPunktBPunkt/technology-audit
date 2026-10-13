# Follow-on ideas (aus bmw-nbt-media-index)

```yaml
reuse_outcomes:
  reused: [bmw-nbt-evo]
  new: []
  not_helped: [live-usb-cache, resume, identity-key, hu-runtime-behavior]
```

Nur sichere Offline-Ideen; keine Zugriffs-, Fahrzeug- oder
Schutzumgehungsanleitung.

| Idee | Baut auf | Gate |
|------|----------|------|
| Synthetischer BMWData-Fixture-Korpus | `idrivetools`, BMC | keine realen Nutzerdaten |
| Roundtrip-/Metadaten-Konsistenztest | `idrivetools` | isoliert; Ergebnis bleibt Backup-Format-Claim |
| BRx-Header-/Transform-Testvektoren | BMC | nur autorisierte/synthetische Dateien |
| Parser-Härtungsreview | FirmwareExtractor | keine Firmwareverteilung; Pfade/Symlinks begrenzen |
| Forensik-Query-Vertragstests | NBT ingest module | redigierte SQLite-Fixtures; Datenschutzreview |
| Provenienzmanifest für Offline-Images | Forensik-Kontext | Hashes, read-only source, Chain of Custody |
| Lizenzklärung | drei Repos ohne Lizenzdatei | bis dahin keine Codeübernahme/Distribution |

## Kill-/Stop-Grenzen für Folgearbeit

- STOP bei fehlender Autorisierung oder unklarer Datenherkunft.
- STOP bei personenbezogenen Echtdaten ohne Zweck, Zugriffskontrolle und
  Löschkonzept.
- STOP bei Versuch, aus Offline-Formaten Live-Cache, Resume, Identity-Key oder
  HU-Verhalten als belegt abzuleiten.
- STOP vor Integration von Code mit ungeklärter Lizenz.
