# Project Application: iobroker-mbrepository-adapter

```yaml
project_id: iobroker-mbrepository
tech_slug: iobroker-mbrepository-adapter
status: active
sheet: ../../../technologies/iobroker-mbrepository-adapter/SHEET.md
audit: ../../../audits/iobroker-mbrepository-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R1
  reusability: W2
```

## Rolle

Scan GitHub-User auf Adapter-Repos; vergleicht installiert vs. Release/Tag/main; installiert via `iobroker url`/Shell; Self-Update; Debug-Konsole.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| webPort 8091, no auth | `EVID-MBR-2026-10-09-001` | `FACT` |
| /api/repos + /api/scan | `EVID-MBR-2026-10-09-002` | `FACT` |
| Version 0.5.5 | `EVID-MBR-2026-10-09-003` | `FACT` |
