# Project Inventory: iobroker.kostalpiko

```yaml
project_id: iobroker-kostalpiko
updated: 2026-10-09
reviewed_commit: e90c650
profile: adapter
pilot_order: [kostal-piko-http]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.3](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| PIKO lokal HTTP scrape + LogDaten.dat | `kostal-piko-http` | **neu** |
| Adapter WebUI :8092 / States / Influx | — | Application B (kein zweites Sheet) |
| Fremd-Adapter `kostal-piko-ba` im Catalog | — | **kein Merge** — anderes Produkt |
| FritzWireGuard networkMode | `iobroker-fritzwireguard-adapter` | Projekt [`iobroker-fritzwireguard`](../iobroker-fritzwireguard/) |
| Open-Meteo Wetter | — | observed |

Ursprung: [ioBroker.kostalpiko](https://github.com/MPunktBPunkt/ioBroker.kostalpiko).  
Kampagne: [iobroker-kostalpiko-2026-pilot](../../audits/iobroker-kostalpiko-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `kostal-piko-http` | Kostal PIKO HTTP | C | `iot`, `http` | applied | partial | [SHEET](../../technologies/kostal-piko-http/SHEET.md) | [app](applications/kostal-piko-http.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Catalog latest/stable | `kostalpiko` nicht in Fork-`sources-dist` | Ops-Repositories |
| Multi-Modell Feldmatrix | Desk | Evidence pro Modell |

## Signale ohne Eintrag

- InfluxDB Sync mit historischen Timestamps
- HTML E-Mail Reports
- Chart.js History UI
