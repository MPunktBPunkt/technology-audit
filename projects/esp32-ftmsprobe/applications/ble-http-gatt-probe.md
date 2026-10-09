# Project Application: ble-http-gatt-probe in esp32.ftmsprobe

```yaml
project_id: esp32-ftmsprobe
tech_slug: ble-http-gatt-probe
status: active
sheet: ../../../technologies/ble-http-gatt-probe/SHEET.md
audit: ../../../audits/esp32-ftmsprobe-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R3
  reusability: W2
```

## Rolle im Projekt

Firmware ist die Sonde: `BleProbe` + HTTP-API + `tools/probe-run.py` automatisieren Scan→GATT→Read→BikeData→Control. Kein Coach — reines Lab.

## Architektur / Datenfluss

```text
probe-run.py ──HTTP /api/probe/*──▶ App / BleProbe ──NimBLE──▶ Bike/Gurt
                                      │
                                 ProbeLog NDJSON · ProbeGuard Deadman
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/ble/BleProbe.*` | Central-Explorer |
| `src/ble/ProbeGuard.*` | Deadman / Link-Schutz |
| `src/app/App.cpp` | HTTP-Routen |
| `tools/probe-run.py` | Orchestrierung Schritte 1–4+ |
| `tools/ftms.py` | Codec-Referenz (Host) |
| `docs/ergometer/TESTS.md` | API/Abruf |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Varon-Lauf 2026-09-10 vollständig mit Rohordner | `EVID-PROBE-2026-10-09-001` | `MEASURED` |
| OTA abgelehnt solange BLE-Links offen (Deploy-Pfad) | `EVID-PROBE-2026-10-09-002` | `INFERRED` (README) |
| Panic `08 01` + Disconnect | `EVID-PROBE-2026-10-09-003` | `FACT` (API/README) |

## Abweichungen vom „Lehrbuch“

- Peripheral-Rollen bewusst disabled (reiner Central) — für Ergo-Bridge später anders.
- NimBLE 1.4.x gepinnt wegen Transfer nach ergo/heartrate.

## Offene Fragen

- Probe-API Versionierung für Nicht-FTMS-Profile?

## Verwandte

- Method [ftms-capability-probe](../../../methods/ftms-capability-probe.md)
- [bluetooth-ftms](bluetooth-ftms.md)
