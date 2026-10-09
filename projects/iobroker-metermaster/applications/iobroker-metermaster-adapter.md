# Project Application: iobroker-metermaster-adapter

```yaml
project_id: iobroker-metermaster
tech_slug: iobroker-metermaster-adapter
status: active
sheet: ../../../technologies/iobroker-metermaster-adapter/SHEET.md
audit: ../../../audits/iobroker-metermaster-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

**Node.js**-Adapter: HTTP-Empfänger für die Android-App (Readings/Import) und optionale ESP32-Display-Nodes (Register, Config-Poll, Cmd). WebUI auf demselben Port.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `main.js` | HTTP-Server, States, nodesCache |
| `admin/` | Admin-UI / jsonConfig |
| `README.md` | API-Tabelle Readings + Nodes |
| `io-package.json` | Version 0.9.12, native `port` default 8089 |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| Default-Port | 8089 | `FACT` |
| Write-Auth | Basic Auth optional | `FACT` |
| Readings | `POST /api/reading`, `/api/readings`, `/api/import` | `FACT` |
| Nodes | `POST /api/register`, `/api/nodes/{MAC}/config`, `configAck`, `cmd` | `FACT` |
| Discover | `GET /api/discover`, `/api/node-discover` | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Port 8089 + Readings/Nodes API | `EVID-MM-2026-10-09-001` | `FACT` |
| ESP-Register ≠ Hub :8093 | `EVID-MM-2026-10-09-002` | `FACT` |
| Nodes optional; App allein nutzbar | `EVID-MM-2026-10-09-003` | `FACT` |

## Verwandte

- Sheet: [`iobroker-metermaster-adapter`](../../../technologies/iobroker-metermaster-adapter/SHEET.md)
- Firmware: [`esp32-metermaster`](../../esp32-metermaster/)
- Abgrenzung Hub: [`esp-hub-telemetry`](../../../technologies/esp-hub-telemetry/SHEET.md)
