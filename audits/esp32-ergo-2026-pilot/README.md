# Audit Campaign: esp32-ergo-2026-pilot

```yaml
id: esp32-ergo-2026-pilot
project_id: esp32-ergo
started: 2026-10-09
ended: null
status: active
reviewed_commit: edaeb19
```

## Ziel

Desk-Audit von `esp32.ergo`: neues FTMS-/Gerätewissen + **Wachstum** der bereits aus `esp32-heartrate` bekannten Sheets (kein Fork). Prozess-Test für „Wissen darf nur wachsen“.

## Scope

- Im Scope: siehe [SCOPE.md](../../projects/esp32-ergo/SCOPE.md)
- Nicht im Scope: Hub-Internals, MyWhoosh-Quellcode, medizinische Claims

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SCOPE + INVENTORY Status/Coverage A–J | erfüllt |
| 2 | Sheet `bluetooth-ftms` + Host-Sheet `hammer-varon-xtr` | erfüllt |
| 3 | Bestehende Slugs wiederverwendet (`seen_in` + Applications), keine Forks | erfüllt |
| 4 | `python3 tools/ta-assist check` grün | erfüllt (lokal) |
| 5 | Bridge MyWhoosh-Abnahme mit Evidence-IDs | offen (STATE) |
| 6 | Nachtest 6 Crash unter Last dokumentiert oder verworfen | offen |

## Bezug Inventar

Priorität: `bluetooth-ftms` → `hammer-varon-xtr` → shared HR/Hub/Web  
Details: [INVENTORY.md](../../projects/esp32-ergo/INVENTORY.md) · Evidence: [evidence.md](evidence.md)

## Ergebnisse

| Artefakt | Pfad |
|----------|------|
| Sheets neu | [`bluetooth-ftms`](../../technologies/bluetooth-ftms/SHEET.md), [`hammer-varon-xtr`](../../technologies/hammer-varon-xtr/SHEET.md) |
| Sheets gewachsen | `ble-hrm-gatt`, `ble-hr-relay`, `esp-hub-telemetry`, `esp-embedded-web-sse` |
| Applications | [applications/](../../projects/esp32-ergo/applications/) |

## Lokal prüfen

```bash
python3 tools/ta-assist check
python3 tools/ta-assist prepare bootstrap https://github.com/MPunktBPunkt/esp32.ergo
```

## Offene Punkte

- Evidence für Bridge-Abnahme und Nachtest 6
- Optional: Method-Note Capability-Probe (`esp32.ftmsprobe`)
- Sheet `ftms-erg-control` wenn Transferbedarf steigt
