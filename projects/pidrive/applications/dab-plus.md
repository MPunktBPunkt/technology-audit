# Project Application: dab-plus in PiDrive

```yaml
project_id: pidrive
tech_slug: dab-plus
status: active
sheet: ../../../technologies/dab-plus/SHEET.md
audit: ../../../audits/pidrive-2026-radio-bt/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle

DAB+ über **welle-cli** + RTL-SDR: Scan → `dab_stations.json`, Play/DLS, CLI/`pidrivectl dab`. Gain über Index-Tabelle (`dab_helpers._get_dab_gain`) — nicht dB wie `rtl_fm`.

## Pfade

| Pfad | Rolle |
|------|-------|
| `pidrive/modules/radio/dab*.py` | Facade Scan/Play/DLS |
| `docs/referenz/WELLE-CLI.md` | Tool-Referenz |
| `docs/archiv/auftraege/AUFTRAG-DAB-AUDIOWEG.md` | Audio-Route-Befunde |
| `pidrive/config/dab_stations.json` | Senderliste |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| welle-cli + Gain-Index (nicht dB) | `EVID-DAB-2026-10-09-001` | `FACT` |
| welle-/spectrum nur DAB-Kanäle | `EVID-DAB-2026-10-09-002` | `FACT` |
| Audio-Route kann BT-Politik umgehen | `EVID-DAB-2026-10-09-003` | `FACT` (Auftrag DA*) |
