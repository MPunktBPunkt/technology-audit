# Audit Campaign: esp32-ergo-2026-pilot

```yaml
id: esp32-ergo-2026-pilot
project_id: esp32-ergo
started: 2026-10-09
ended: null
status: active
reviewed_commit: edaeb19
profile: firmware
standard_version: "0.6.6"
revalidated_from: "0.6.0"
revalidated: 2026-10-11
reuse_outcomes:
  - new: [bluetooth-ftms, hammer-varon-xtr]
  - grown: [ble-hrm-gatt, ble-hr-relay, esp-hub-telemetry, esp-embedded-web-sse]
  - sharpened: "0.6.6 product chip-scope ESP32-S3; relay = sibling deploy"
  - process: "parity 0.6.0 → 0.6.6; DELTA; knowledge-growth control case"
  - not_created: [ftms-erg-control]
  - siblings: [esp32-heartrate, esp32-ftmsprobe]
```

## Ziel

Desk-Audit von `esp32.ergo`: neues FTMS-/Gerätewissen + **Wachstum** der bereits aus `esp32-heartrate` bekannten Sheets (kein Fork). Prozess-Test für „Wissen darf nur wachsen“.

**Revalidation 2026-10-11:** Commit `edaeb19` unter **0.6.6** — S3-Produkt-Scope, Geschwister-Relay-Grenze, Gaps schließen. Historie: Git + [DELTA](DELTA.md).

## Scope

- Im Scope: siehe [SCOPE.md](../../projects/esp32-ergo/SCOPE.md)
- Nicht im Scope: Hub-Internals, MyWhoosh-Quellcode, medizinische Claims
- Revalidation: gleicher Commit, keine neuen Lab-PASSes

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SCOPE + INVENTORY Status/Coverage A–J | erfüllt |
| 2 | Sheet `bluetooth-ftms` + Host-Sheet `hammer-varon-xtr` | erfüllt |
| 3 | Bestehende Slugs wiederverwendet (`seen_in` + Applications), keine Forks | erfüllt |
| 4 | `python3 tools/ta-assist check` grün | erfüllt (lokal) |
| 5 | Bridge MyWhoosh-Abnahme mit Evidence-IDs | offen (STATE) |
| 6 | Nachtest 6 Crash unter Last dokumentiert oder verworfen | offen |
| 7 | Revalidation 0.6.6: S3-Chip-Scope + Geschwister + DELTA | erfüllt (2026-10-11) |

## Bezug Inventar

Priorität: `bluetooth-ftms` → `hammer-varon-xtr` → shared HR/Hub/Web  
Details: [INVENTORY.md](../../projects/esp32-ergo/INVENTORY.md) · Evidence: [evidence.md](evidence.md) · **[DELTA](DELTA.md)**

## Ergebnisse

| Artefakt | Pfad |
|----------|------|
| Sheets neu | [`bluetooth-ftms`](../../technologies/bluetooth-ftms/SHEET.md), [`hammer-varon-xtr`](../../technologies/hammer-varon-xtr/SHEET.md) |
| Sheets gewachsen | `ble-hrm-gatt`, `ble-hr-relay`, `esp-hub-telemetry`, `esp-embedded-web-sse` |
| Applications | [applications/](../../projects/esp32-ergo/applications/) |

## Lessons (Revalidation)

- Geschwister-Reuse (heartrate → ergo) war der Original-Prozess-Test — 0.6.6 formalisiert zusätzlich **S3-only** und Relay-als-Deploy.
- `ftms-erg-control` bleibt observed: kein Sheet aus Architekturidee (G19).

## Lokal prüfen

```bash
python3 tools/ta-assist check
python3 tools/ta-assist prepare bootstrap https://github.com/MPunktBPunkt/esp32.ergo
```

## Offene Punkte

- Evidence für Bridge-Abnahme und Nachtest 6
- Sheet `ftms-erg-control` nur bei Transferbedarf + Gate
