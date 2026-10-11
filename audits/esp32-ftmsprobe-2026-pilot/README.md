# Audit Campaign: esp32-ftmsprobe-2026-pilot

```yaml
id: esp32-ftmsprobe-2026-pilot
project_id: esp32-ftmsprobe
started: 2026-10-09
ended: null
status: active
reviewed_commit: 70c3c25
profile: lab-tool
standard_version: "0.6.6"
revalidated_from: "0.6.0"
revalidated: 2026-10-11
reuse_outcomes:
  - new: [ble-http-gatt-probe]
  - grown: [bluetooth-ftms, hammer-varon-xtr, ble-hrm-gatt, esp-hub-telemetry]
  - method: ftms-capability-probe
  - sharpened: "0.6.6 chip/build-scope probe vs probe-s3; dual-link budget"
  - process: "parity 0.6.0 → 0.6.6; DELTA"
  - siblings: [esp32-heartrate, esp32-ergo]
```

## Ziel

Lab-Sonde und Method `ftms-capability-probe` in die Wissensbasis; FTMS/Varon-Evidence dem Wachstum zuordnen; Pattern `ble-http-gatt-probe` für künftige Projekte. Prozess-Test: Bootstrap mit Sheet-Match ([REUSE.md](../../docs/REUSE.md)).

**Revalidation 2026-10-11:** Commit `70c3c25` unter **0.6.6** — Chip-/Build-Scope Dual-Env, Dual-Link-Budget, Gaps schließen. Historie: Git + [DELTA](DELTA.md).

## Scope

Siehe [SCOPE.md](../../projects/esp32-ftmsprobe/SCOPE.md). Revalidation = gleicher Commit, kein neuer Geräte-Lauf.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SCOPE + INVENTORY mit Match auf bestehende Slugs | erfüllt |
| 2 | Method Note `ftms-capability-probe` | erfüllt |
| 3 | Sheet `ble-http-gatt-probe` + Applications | erfüllt |
| 4 | `bluetooth-ftms` / `hammer-varon-xtr` `seen_in` inkl. Probe | erfüllt |
| 5 | `ta-assist check` grün | erfüllt (lokal) |
| 6 | Zweiter Geräte-Lauf (Nicht-Varon) oder bewusst deferred | offen |
| 7 | Revalidation 0.6.6: Chip-Scope Dual-Env + DELTA | erfüllt (2026-10-11) |

## Bezug

[INVENTORY](../../projects/esp32-ftmsprobe/INVENTORY.md) · [evidence](evidence.md) · **[DELTA](DELTA.md)** · Method [ftms-capability-probe](../../methods/ftms-capability-probe.md)

## Ergebnisse

| Artefakt | Pfad |
|----------|------|
| Neu | `ble-http-gatt-probe`, Method `ftms-capability-probe` |
| Gewachsen | `bluetooth-ftms` (W3), `hammer-varon-xtr` (W2), Hub/HR/Web `seen_in` |
| Prozess | `docs/REUSE.md`, Bootstrap-Katalog `existing_sheets` |

## Lessons (Revalidation)

- Dual-Env (`probe` / `probe-s3`) braucht expliziten Connection-Budget-Scope (G17), auch wenn beide Central-only sind.
- Method + Host-Sheet waren bereits die richtige Schicht — 0.6.6 bestätigt, kein neues Varianten-Sheet.

## Offene Punkte

- Exit 6: weiteres Bike oder deferred dokumentieren
- Optional: Application für Web/SSE der Sonde
