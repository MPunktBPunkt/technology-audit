# AUDIT DELTA — esp32-ftmsprobe-2026-pilot

```yaml
campaign: esp32-ftmsprobe-2026-pilot
old_standard: "0.6.0"
new_standard: "0.6.6"
revalidated: 2026-10-11
method: desk revalidation (same commit 70c3c25) + 0.6.1–0.6.6 process rules
siblings: [esp32-heartrate, esp32-ergo]
```

## OLD AUDIT (0.6.0)

| Bereich | Stand |
|---------|--------|
| Claims | HTTP-GATT-Sonde; Varon Cap/Wirkung; Method `ftms-capability-probe`; Hub-Familien-OTA |
| UNKNOWNs | Zweites Nicht-Varon-Gerät; Sim `0x11` Wirkung vollständig |
| Sheets | neu `ble-http-gatt-probe`; Wachstum `bluetooth-ftms`, `hammer-varon-xtr` |
| Process gaps | `standard_gaps` nur 0.6.1; Chip-Scope Dual-Env/`MAX_CONNECTIONS` nicht formal |

## NEW AUDIT (0.6.6 Revalidation)

| Bereich | Delta |
|---------|--------|
| neue FACTs | Dual-Env `probe` (Classic) / `probe-s3`; Central-only Probe; Dual-Link-Budget als Chip-/Build-Claim |
| geschärft | Dual-Central (Bike+H9) nicht still von einem Env auf alle ESP32 übertragen (G17) |
| Gates | Zweites Bike = Method erneut, nicht Spec-Ausweiten; kein `ftms-erg-control`-Sheet (G19) |
| Reuse | Evidence-Ursprung für ergo bestätigt; Pattern W2→prüfbar für weitere GATT-Sonden |
| verworfene Transfers | Host-BlueZ ersetzt Sonde; Varon-Quirks → FTMS-Spec |

## Quantitativ

| Metrik | 0.6.0 | nach 0.6.6 | Δ |
|--------|-------|------------|---|
| Pilot-Sheets | 1 neu + Wachstum | unverändert | 0 |
| Evidence-IDs | 7 | 10 | +3 Scope |
| `standard_gaps` | [0.6.1…] | keine | Parität |

## Urteil

Stärkster 0.6.6-Hebel: **Chip-/Build-Scope am Dual-Link-Lab** (`probe` vs `probe-s3`, Connection-Budget) plus Bestätigung, dass Method + Host-Sheet die richtige Schichttrennung schon hatten — Parität schließt vor allem den Gap-Rückstand.

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Kampagne | [README.md](README.md) |
| Sheet | [`ble-http-gatt-probe`](../../technologies/ble-http-gatt-probe/SHEET.md) |
| Method | [`ftms-capability-probe`](../../methods/ftms-capability-probe.md) |
