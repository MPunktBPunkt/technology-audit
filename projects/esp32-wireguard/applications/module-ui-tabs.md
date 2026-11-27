# Application: Module UI Tabs (esp-hub-base 1.12 + esp32.wireguard)

```yaml
project_id: esp32-wireguard
tech_slug: esp-module-host
status: active
related:
  - esp-hub-base-template
  - esp-wireguard
maturity:
  technology: R2
  implementation: R2
  field_evidence: R1
```

## Rolle

Optionale SPA-Tabs/API-Routen für Application-Module **ohne** WireGuard (oder andere Domain) in der Base-Shell zu hardcoden. WireGuard ist erster Consumer.

## Architektur (kurz)

```text
BaseModule::uiTab() → ModuleManager::buildUiTabsJson()
  → GET /api/ui/tabs
Shell lädt /ui/tab/<id> + /ui/tab/<id>.js (Modul-owned PROGMEM)
```

Define-Gate im Sketch (`ESPHUB_ENABLE_*` + `modules().add`) — nicht im Base-Linker allein.

## Evidenz (Build-Host 2026-11-27)

| Claim | Status | Zahl |
|-------|--------|------|
| UiTab-Infra vs 1.11.1 (esp32 sketch) | `FACT` | +2064 B Flash, +0 Globals |
| Testmodul vs Infra-only | `FACT` | +3340 B Flash, +0 Globals |
| WireGuard 0.2.0 vs Infra-only | `FACT` | +18284 B Flash, +312 B Globals |
| OTA lab .87/.88/.131 mit 0.1.0 | `FACT` | vor Tab-Refactor; 0.2.0 nachziehen |

Quelle Detail: `ESP32.esp-hub/docs/update/MODULE_UI_FLASH_BUDGET.md`, ADR D-022.

## Offene Punkte

- Keepalive/Tunnel-Stack (esp-wireguard) weiterhin Phase 2
- NVS-Encryption für WG-Secrets: UNKNOWN / später Lab
