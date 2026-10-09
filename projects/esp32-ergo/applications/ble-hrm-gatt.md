# Project Application: ble-hrm-gatt in esp32.ergo

```yaml
project_id: esp32-ergo
tech_slug: ble-hrm-gatt
status: active
sheet: ../../../technologies/ble-hrm-gatt/SHEET.md
audit: ../../../audits/esp32-ergo-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

`HrClient` subscribed `0x180D` auf Gurt **oder** auf HR-Relay (sichtbar als normales HR-Gerät). Zusätzlich HR aus Bike-IBD (`HrSource::Machine`) — das ist **nicht** dieses Sheet, nur alternative Quelle.

## Architektur / Datenfluss

```text
Polar / Relay ──0x180D──▶ HrClient ──▶ Coach (HR_HOLD, Reha-Deckel, Bridge-HR-Limit)
Bike 0x2AD2 HR-Bit ──────────────────▶ HrSource::Machine (Fallback)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/ble/HrClient.*` | GATT HR Central |
| `src/ble/HrSource.h` | Strap / Relay / Machine |
| `src/app/App.cpp` | Quellenpriorität |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Relay und Strap laufen beide über HrClient/`0x180D` | `EVID-HRM-2026-10-09-001` | `FACT` (Code/README) |
| H9 single-link → Relay für parallele Consumer | `EVID-HRM-2026-10-08-001` (heartrate) + README ergo | `MEASURED` |

## Abweichungen vom Heartrate-Projekt

- Kein eigener Peripheral-HR-Server in ergo — Relay ist **externes** Gerät.
- Drei Quellen-Priorität inkl. Machine-HR.

## Offene Fragen

- Messprotokoll Machine-HR vs. Strap unter Last?

## Verwandte

- [ble-hr-relay](ble-hr-relay.md)
- Sheet-Wachstum: Varianten-Tabelle in `ble-hrm-gatt`
