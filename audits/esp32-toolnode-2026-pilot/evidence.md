# Evidence — esp32-toolnode-2026-pilot

Desk-Audit 2026-10-09 @ `af4d973` · **standard_version 0.6.1**.

Basis: `https://github.com/MPunktBPunkt/esp32.toolnode/blob/af4d973/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-MOD-2026-10-09-001` | ModuleManager/BaseModule dokumentiert | `FACT` | [ARCHITECTURE.md](https://github.com/MPunktBPunkt/esp32.toolnode/blob/af4d973/docs/ARCHITECTURE.md) |
| `EVID-MOD-2026-10-09-002` | `TOOLNODE_ENABLE_*` Build-Flags | `FACT` | [BuildFlags.h](https://github.com/MPunktBPunkt/esp32.toolnode/blob/af4d973/include/BuildFlags.h) |
| `EVID-RF-2026-10-09-010` | Scanner + RfHealth Module | `FACT` | `src/modules/ScannerModule.*`, `RfHealthModule.*` |
| `EVID-RF-2026-10-09-011` | BLE default aus (`ENABLE_BLE=0`) | `FACT` | BuildFlags.h |
| `EVID-HUB-2026-10-09-010` | `fwType: toolnode` | `FACT` | AppCore.cpp / ARCHITECTURE |
| `EVID-HUB-2026-10-09-011` | Register inkl. enabledModules / rf_score | `FACT` | ARCHITECTURE Hub-Beispiel |
| `EVID-WEB-2026-10-09-010` | REST `/api/*` + SSE + Wizard | `FACT` | README API / WIZARD.md |
| `EVID-MQTT-2026-10-09-001` | MQTT Namespace toolnode | `FACT` | README MQTT |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| RF-Score-Formel identisch zu rfmonitor | `UNKNOWN` | Exit 5 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Pilot; Standard 0.6.1 Geschwister-Reuse |
