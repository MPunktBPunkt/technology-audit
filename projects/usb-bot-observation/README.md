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
| Audit (Control/Stall/Enum) | [`usb-control-stall-recovery-2026`](../../audits/usb-control-stall-recovery-2026/) |

**Stand:** Desk 2026-10-14. BOT-Hooks, Control/Enum-Epochs und Host-eBPF-Decode
sind Desk-`FACT`; NBT-CDBs, Sense-Folgen, Timing/S1–S3 und Transparenz bleiben
`UNKNOWN`. WiFi↔USB nur `HYPOTHESIS`. Kein Lab-/Feld- oder Fahrzeug-Capture.
