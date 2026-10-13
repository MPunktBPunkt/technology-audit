# Project: USB BOT Observation

Desk-only Vergleichsprojekt für Beobachtungspfade an USB Mass Storage Bulk-Only
Transport (BOT). Ziel ist eine belastbare Trennung von **CBW**, eingebetteter
**SCSI-CDB**, Datenphase und **CSW** — ohne einen realen NBT-Mitschnitt zu
behaupten.

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Quellen-Snapshots, Systemgrenzen und Nicht-Ziele |
| [INVENTORY.md](INVENTORY.md) | Reuse-Inventar mit `usb-msc` |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | kontrollierte nächste Schritte |
| [applications/usb-msc.md](applications/usb-msc.md) | BOT-Beobachtung als Anwendung von `usb-msc` |
| Audit | [`usb-bot-observation-2026-foreign`](../../audits/usb-bot-observation-2026-foreign/) |

**Stand:** Desk 2026-10-13. NBT-CDBs, Sense-Folgen und Timing bleiben
`UNKNOWN`; es existiert in dieser Kampagne kein Lab-/Feld- oder
Fahrzeug-Capture.
