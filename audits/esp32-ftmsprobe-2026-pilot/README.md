# Audit Campaign: esp32-ftmsprobe-2026-pilot

```yaml
id: esp32-ftmsprobe-2026-pilot
project_id: esp32-ftmsprobe
started: 2026-10-09
ended: null
status: active
reviewed_commit: 70c3c25
profile: lab-tool
standard_version: "0.6.0"
standard_gaps: ["0.6.1 Geschwister-Reuse / G9–G11 / Arduino-Layout — Kampagne vor Regelstand"]
```

## Ziel

Lab-Sonde und Method `ftms-capability-probe` in die Wissensbasis; FTMS/Varon-Evidence dem Wachstum zuordnen; Pattern `ble-http-gatt-probe` für künftige Projekte. Prozess-Test: Bootstrap mit Sheet-Match ([REUSE.md](../../docs/REUSE.md)).

## Scope

Siehe [SCOPE.md](../../projects/esp32-ftmsprobe/SCOPE.md).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SCOPE + INVENTORY mit Match auf bestehende Slugs | erfüllt |
| 2 | Method Note `ftms-capability-probe` | erfüllt |
| 3 | Sheet `ble-http-gatt-probe` + Applications | erfüllt |
| 4 | `bluetooth-ftms` / `hammer-varon-xtr` `seen_in` inkl. Probe | erfüllt |
| 5 | `ta-assist check` grün | erfüllt (lokal) |
| 6 | Zweiter Geräte-Lauf (Nicht-Varon) oder bewusst deferred | offen |

## Bezug

[INVENTORY](../../projects/esp32-ftmsprobe/INVENTORY.md) · [evidence](evidence.md) · Method [ftms-capability-probe](../../methods/ftms-capability-probe.md)

## Ergebnisse

| Artefakt | Pfad |
|----------|------|
| Neu | `ble-http-gatt-probe`, Method `ftms-capability-probe` |
| Gewachsen | `bluetooth-ftms` (W3), `hammer-varon-xtr` (W2), Hub/HR/Web `seen_in` |
| Prozess | `docs/REUSE.md`, Bootstrap-Katalog `existing_sheets` |

## Offene Punkte

- Exit 6: weiteres Bike oder deferred dokumentieren
- Optional: Application für Web/SSE der Sonde
