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
| Audit (Pfadvergleich) | [`usb-bot-observation-2026-foreign`](../../audits/usb-bot-observation-2026-foreign/) |
| Audit (Instrumentierung) | [`usb-bot-observation-2026-instrument-sources`](../../audits/usb-bot-observation-2026-instrument-sources/) |

**Stand:** Desk 2026-10-14. Hook-Karte und Host-eBPF-Decode sind Desk-`FACT`;
NBT-CDBs, Sense-Folgen, Timing und Transparenz bleiben `UNKNOWN`. Kein
Lab-/Feld- oder Fahrzeug-Capture.
