# Project Inventory: bmw-nbt-media-index (Fremd)

```yaml
project_id: bmw-nbt-media-index
updated: 2026-10-13
profile: lab-tool
pilot_order: [bmw-nbt-evo]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard
[0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| NBT/NBT Evo Medienbackup und BRx-Dateien | `bmw-nbt-evo` | reuse + Application |
| Offline-NBT-Forensik | `bmw-nbt-evo` | begrenzter Kontext, kein Runtime-Transfer |
| NBT(EVO)/MGU Firmwarecontainer | `bmw-nbt-evo` | Research-Kontrast; Varianten nicht gleichsetzen |
| HU-Info README | `bmw-nbt-evo` | candidate/README-only; keine Zugriffsdetails |
| Live-USB-Cache / Resume / Identity-Key | — | **kein Match; UNKNOWN** |

Kampagne:
[`bmw-nbt-media-index-2026-foreign`](../../audits/bmw-nbt-media-index-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `bmw-nbt-evo` | BMW NBT Evo Host-Plattform | I | applied | partial | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | [app](applications/bmw-nbt-evo.md) |

## A/B/C-Zuordnung

| Ebene | Inhalt dieser Kampagne |
|-------|-------------------------|
| A | bestehendes Sheet `bmw-nbt-evo`; unverändert |
| B | konkrete Offline-Parser/Konverter an fünf gepinnten Repos |
| C | keine eigene Host-/Lab-/Field-Beobachtung; Live-HU-Verhalten `UNKNOWN` |

## Coverage-Lücken

| Bereich | Status | Nächster sicherer Schritt |
|---------|--------|--------------------------|
| Backup-Roundtrip | `UNKNOWN` | synthetischer, nicht personenbezogener Fixture-Lab |
| BRx-Mapping je HU-Variante | `UNKNOWN` | synthetische/autorisiert bereitgestellte Fixtures |
| Firmwareparser-Härtung | partial | isoliertes Review gegen Path Traversal/Symlinks |
| Forensik-Schemaabdeckung | partial | Schema-/Query-Tests auf redigierten Fixtures |
| Live-HU-Verhalten | außerhalb Scope | keine Ableitung aus diesen Quellen |
