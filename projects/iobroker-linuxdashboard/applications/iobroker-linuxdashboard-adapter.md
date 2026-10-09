# Project Application: iobroker-linuxdashboard-adapter

```yaml
project_id: iobroker-linuxdashboard
tech_slug: iobroker-linuxdashboard-adapter
status: active
sheet: ../../../technologies/iobroker-linuxdashboard-adapter/SHEET.md
audit: ../../../audits/iobroker-linuxdashboard-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R1
  reusability: W2
```

## Rolle

Host-Verwaltung ohne SSH: Metriken, FS, Prozesse, journalctl, systemd, apt, cron, tar-Backups, Terminal; States für CPU/RAM/Uptime.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Default port 8090, no auth | `EVID-LXD-2026-10-09-001` | `FACT` |
| allowCommandExecution native | `EVID-LXD-2026-10-09-002` | `FACT` |
| Version 0.6.0 | `EVID-LXD-2026-10-09-003` | `FACT` |
