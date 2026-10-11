# Project Application: bluetooth-ftms in esp32.ergo

```yaml
project_id: esp32-ergo
tech_slug: bluetooth-ftms
status: active
sheet: ../../../technologies/bluetooth-ftms/SHEET.md
audit: ../../../audits/esp32-ergo-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R3
  reusability: W2
```

## Rolle im Projekt

ESP als **FTMS-Central** am Varon (lesen IBD, schreiben Resistance) und als **FTMS-Peripheral-Bridge** zu Apps (MyWhoosh). Steuerstrategie kommt aus `ftms::Capabilities` zur Connect-Zeit — nicht aus Hardcode „Varon“.

## Architektur / Datenfluss

```text
Varon 0x1826 ──FtmsClient──▶ Limiter / PowerController / Coach
App (MyWhoosh) ◀──FtmsServer── ESP (Bridge Exclusive/Observer)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/ble/FtmsClient.cpp` | Central, Subscribe, Writes |
| `src/ble/FtmsCapabilities.*` | Ableitung Steuerstrategie |
| `src/ble/FtmsCodec.*` | Encode/Decode |
| `src/ble/FtmsServer.*` | Peripheral Bridge |
| `src/control/Limiter.*` | einziger Schreibpfad |
| `docs/ergometer/BRIDGE.md` | Betriebsregeln Exclusive/Observer |

## Konfiguration und Parameter

| Claim | Status |
|-------|--------|
| `MAX_CONNECTIONS=3` für Coach+Bridge | `FACT` (`platformio.ini`) |
| Capability-first: Power Target nur wenn Feature+Range belastbar | `FACT` (FtmsCapabilities + Docs) |
| Resistance wide sint16 Zehntel am Varon | `MEASURED` → siehe `hammer-varon-xtr` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Varon: kein Power Target / kein `0x2AD8` | `EVID-FTMS-2026-10-09-001` | `MEASURED` |
| Control-Point-Success ≠ Wirkung (`0x05`) | `EVID-FTMS-2026-10-09-002` | `MEASURED` |
| Bridge Exclusive: Coach-Last → HTTP 409 solange App controlling | `EVID-FTMS-2026-10-09-003` | `INFERRED` (BRIDGE.md + Code) |
| Produkt-Chip-Scope: ESP32-S3 Dual-Role (Central+Bridge) | `EVID-SCOPE-2026-10-11-001` | `FACT` |
| Formale MyWhoosh-Abnahme abgeschlossen | — | `UNKNOWN` (STATE offen) |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| GERAETEPROFIL / ftmsprobe 2026-09-10 | Caps, Stufenraster, Advertising-Lücken |
| BRIDGE.md 2026-09-14 | Observer/Controller, Resistance-Spam-Schutz |

## Abweichungen vom „Lehrbuch“

- ERG = Emulation über Stufe + Kennfläche, nie Opcode `0x05` ans Varon (produktiv).
- Bridge mappt App-Power auf lokalen Regler; Resistance-Spam nach SetPower wird verworfen.

## Offene Fragen

- Nachtest 6 Crash unter Last — Einfluss auf FTMS-Link?
- SIM-Passthrough Code nachziehen?

## Verwandte Applications / Methods

- [hammer-varon-xtr](hammer-varon-xtr.md)
- [ble-hrm-gatt](ble-hrm-gatt.md)
