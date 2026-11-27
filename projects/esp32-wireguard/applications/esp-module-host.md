# Project Application: esp-module-host in esp32-wireguard

```yaml
project_id: esp32-wireguard
tech_slug: esp-module-host
status: active
sheet: ../../../technologies/esp-module-host/SHEET.md
maturity:
  technology: R3
  implementation: R2
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

Optionaler WireGuard-Tab und -API über `BaseModule::uiTab()` + Shell `GET /api/ui/tabs` (esp-hub-base **1.12.0** / D-022). Kein WG-HTML in der Base-Shell.

## Architektur / Datenfluss

```text
WireGuardModule.uiTab() → ModuleManager.buildUiTabsJson()
  → GET /api/ui/tabs
Shell → /ui/tab/wg (+ .js)  [modul-owned PROGMEM]
Sketch: modules().add(&gWireGuard)  [Compile-Time Opt-in]
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp32.wireguard/src/wireguard/WireGuardModule.*` | Modul + Tab-Assets |
| `esp32.wireguard/src/core/UiTab.h` / `WebSend.h` | Base-Infra (vendored) |
| `ESP32.esp-hub/.../D022_MODULE_UI_TABS.md` | ADR |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| UiTab-Infra ≈ +2 KiB Flash vs 1.11.1 (esp32) | `EVID-WG-2026-11-27-001` | `FACT` (Build-Host) |
| WireGuard-Modul 0.2.0 ≈ +17.9 KiB / +312 B Globals vs Base-only | `EVID-WG-2026-11-27-002` | `FACT` (Build-Host) |
| OTA .87/.88/.131 liefern `/api/ui/tabs` mit `wg` | `EVID-WG-2026-11-27-003` / `EVID-WG-2026-11-27-010` | `FACT` (Lab) |
| Base 1.12.0 ohne WG: `tabs=[]`, kein `/api/wg` | `EVID-WG-2026-11-27-011` | `FACT` (Lab .131) |
| Modul-UI muss in Base-index hardcodiert sein | — | `REJECTED` |
| kMaxModules=6 erhöhen | — | `REJECTED` (kein Bedarf) |
| Multi-Tab pro Modul jetzt | — | `REJECTED` (kein Bedarf) |

Siehe `EVIDENCE-2026-11-27-phase1.md`.

## Offene Fragen

- Multi-Tab / kMaxModules: unverändert bis reales Modul begründet
