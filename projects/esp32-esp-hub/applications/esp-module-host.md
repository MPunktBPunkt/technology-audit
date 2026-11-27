# Project Application: esp-module-host in esp32-esp-hub

```yaml
project_id: esp32-esp-hub
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

Ab **esp-hub-base 1.12.0** (D-022): generische UiTab-Infrastruktur für optionale Application-Module. Erster Consumer außerhalb der Base: `esp32-wireguard`.

## Architektur

```text
BaseModule::uiTab() / registerRoutes / appendStatusJson
ModuleManager::buildUiTabsJson → GET /api/ui/tabs
Shell SPA lädt Panel/JS dynamisch
ESPHUB_ENABLE_TEST_MODULE — Referenz-Opt-in
```

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Infra vs 1.11.1 ≈ +2.0 KiB Flash, +0 Globals | `EVID-BASE-2026-11-27-022` | `FACT` (Build-Host) |
| Testmodul ≈ +3.3 KiB Flash | `EVID-BASE-2026-11-27-023` | `FACT` (Build-Host) |
| kMaxModules=6 / 1 Tab pro Modul bewusst unverändert | — | `INFERENCE` (kein realer Bedarf) |
