# Project Application: fm-rds in pi-fm-tx

```yaml
project_id: pi-fm-tx
tech_slug: fm-rds
status: active
sheet: ../../../technologies/fm-rds/SHEET.md
audit: ../../../audits/pi-fm-tx-2026-foreign/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

RDS-Encoder/Meta auf FM-MPX — **nicht** in reinem markondej/pifm/player.

| Quelle | Commit | RDS? |
|--------|--------|------|
| F5OEO/PiFmRds | `2707ecc` | ja — `rds.c`, Control-Pipe, CLI `-pi/-ps/-rt` |
| F5OEO/rpitx | `ee7ff57` | ja — `src/pifmrds`, `testfmrds.sh` (Untermenge der Plattform) |
| markondej / zoroxide / pifm / pi-fm-player | … | nein (nur Audio-FM) |

## Pfade

| Pfad | Rolle |
|------|-------|
| `PiFmRds/src/rds.c` | Gruppen, CRC, PS/RT |
| `PiFmRds/src/control_pipe.c` | Runtime PS/RT |
| `rpitx/src/pifmrds/` | RDS im rpitx-Tree |
| `rpitx/testfmrds.sh` | Demo-Launcher |

## Kontrast Meta

RDS PS/RT ≠ DAB-DLS ≠ AVRCP/MPRIS — gleicher Nutzerwunsch, andere Schicht.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| RDS-Gruppen/CRC in PiFmRds `rds.c` | `EVID-RDS-2026-10-10-001` | `FACT` |
| ~228 kHz Samplepfad / 57 kHz | `EVID-RDS-2026-10-10-002` | `FACT` |
| Control-Pipe PS/RT | `EVID-RDS-2026-10-10-003` | `FACT` |
| rpitx enthält pifmrds + testfmrds | `EVID-RPITX-2026-10-10-005` | `FACT` |
