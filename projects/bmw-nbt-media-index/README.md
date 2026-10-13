# bmw-nbt-media-index (Fremd)

Desk-only-Aufnahme öffentlicher Werkzeuge zu BMW-iDrive-Medienbackups,
Backup-Metadaten, Firmwarecontainern und NBT-Forensik nach Standard **0.7.1**.

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Quellen, Grenzen, Security/Safety |
| [INVENTORY.md](INVENTORY.md) | Reuse von `bmw-nbt-evo` |
| [applications/bmw-nbt-evo.md](applications/bmw-nbt-evo.md) | A/B/C-getrennte Anwendung |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | sichere Desk-Folgeideen |
| Audit | [`bmw-nbt-media-index-2026-foreign`](../../audits/bmw-nbt-media-index-2026-foreign/) |

## Snapshots

| Repository | Commit | Desk-Rolle |
|------------|--------|------------|
| [Centurix/idrivetools](https://github.com/Centurix/idrivetools) | `08e0c43c63a64547b018d5c627f59d5453d9505b` | Backupstruktur und Metadaten |
| [sivu22/BMC](https://github.com/sivu22/BMC) | `c22b27edaf4d5aba50fe66f7e005b272b71e5b35` | BRx-Medienkonvertierung |
| [superabiliter/BMWFirmwareExtractor](https://github.com/superabiliter/BMWFirmwareExtractor) | `5cd2895bb92622ded6feb18b79325188e3ac9860` | Firmwarecontainer-Kontrast |
| [Ricardo2192643/BMW-IVI-NBT-ingest-module](https://github.com/Ricardo2192643/BMW-IVI-NBT-ingest-module) | `127fb15c420334dcc6dedf1010b902d8837c9144` | Offline-QNX-/Autopsy-Forensik |
| [Viaszx/BMW_HU_Info](https://github.com/Viaszx/BMW_HU_Info) | `c140b1d62ca59e0043a8c620eb390c96e6272c76` | README-only HU-Kontrast |

**Claim-Grenze:** Diese Kampagne enthält keine Fahrzeug-, USB- oder
Head-Unit-Messung. Sie ist kein Beleg für NBT-Live-USB-Cache, Resume,
Identity-Key oder konkretes HU-Verhalten.
