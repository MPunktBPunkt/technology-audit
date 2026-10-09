# Project Inventory: iobroker.metermaster

```yaml
project_id: iobroker-metermaster
updated: 2026-10-09
reviewed_commit: be89348
profile: adapter
pilot_order: [iobroker-metermaster-adapter]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.3](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Adapter :8089 Readings + ESP node mgmt | `iobroker-metermaster-adapter` | **neu** (ersetzt observed `metermaster-adapter-http` in Firmware-Inventar) |
| `POST /api/register` auf 8089 | **nicht** `esp-hub-telemetry` | anderer Port/Contract (Produkt-Adapter) |
| Simple-API :8087 | `iobroker-simple-api` | nur Firmware-Client; hier kein Match |
| WebUI Tabs Data/Import/Logs/System/Nodes | — | observed (Adapter-B) |

Ursprung: [ioBroker.metermaster](https://github.com/MPunktBPunkt/ioBroker.metermaster).  
Kampagne: [iobroker-metermaster-2026-pilot](../../audits/iobroker-metermaster-2026-pilot/).  
Firmware: [esp32-metermaster](../esp32-metermaster/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `iobroker-metermaster-adapter` | MeterMaster Adapter | F | `iobroker`,`nodejs` | applied | partial | [SHEET](../../technologies/iobroker-metermaster-adapter/SHEET.md) | [app](applications/iobroker-metermaster-adapter.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Android↔Adapter Feldserie | Desk | App-Evidence bei Bedarf |
| Katalog stable vs latest Version | Ops | [`iobroker-repositories`](../iobroker-repositories/) |

## Signale ohne Eintrag

- Backup-Import Schema 2.0
- Charts/CSV Export (WebUI)
