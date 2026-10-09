# Project Application: esp-module-host in esp32.toolnode

```yaml
project_id: esp32-toolnode
tech_slug: esp-module-host
status: active
sheet: ../../../technologies/esp-module-host/SHEET.md
audit: ../../../audits/esp32-toolnode-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R1
  reusability: W2
```

## Rolle im Projekt

`ModuleManager` + `BaseModule`: aktivierbare Module (Scanner, RfHealth, Lab, …) hinter gemeinsamen Lifecycle; Build-Flags `TOOLNODE_ENABLE_*`; Setup-Wizard Profile RF/Lab/Presence/Custom.

## Architektur / Datenfluss

```text
BuildFlags ──▶ Module register ──▶ ModuleManager.loop
Config/Wizard ──▶ enable/pins ──▶ PinGuard
Module status/IO ──▶ HubClient + Web/SSE (+ MQTT)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/core/BaseModule.h` | Interface |
| `src/core/ModuleManager.*` | Host |
| `src/core/SetupManager.*` | Wizard |
| `include/BuildFlags.h` | Defaults |
| `docs/ARCHITECTURE.md` / `docs/WIZARD.md` | Spec |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Modul-Interface + Manager dokumentiert | `EVID-MOD-2026-10-09-001` | `FACT` |
| Build-Flags `TOOLNODE_ENABLE_*` | `EVID-MOD-2026-10-09-002` | `FACT` |

## Verwandte

- [rf-environment-monitor](rf-environment-monitor.md) · [mqtt-node-telemetry](mqtt-node-telemetry.md)
