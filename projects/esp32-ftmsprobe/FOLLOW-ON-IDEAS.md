# Folgeprojekte (aus esp32.ftmsprobe)

```yaml
reuse_outcomes:
  - sheet: ble-http-gatt-probe
    note: 0.6.6 Revalidation — Chip-/Build-Scope Dual-Env
  - process: "parity 0.6.0 → 0.6.6; DELTA in audits/esp32-ftmsprobe-2026-pilot/"
```

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Zweites Bike mit gleicher Method | `ftms-capability-probe` | neuer scan-<datum> Ordner; kein Host-Sheet-Ausweiten |
| Dual-Link-Budget Classic vs S3 belegen | `ble-http-gatt-probe` | Env-Vergleich `probe` / `probe-s3` |
| Generische Probe für Nicht-FTMS-GATT | `ble-http-gatt-probe` | Profil-Plugins |
| Host-BlueZ-Gegencheck automatisieren | `ble-host-precheck.sh` | oft unmöglich im LXC |
