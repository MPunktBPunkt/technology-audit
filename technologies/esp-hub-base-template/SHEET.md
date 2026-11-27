# Technology Sheet: ESP-Hub Base Firmware Template

```yaml
slug: esp-hub-base-template
title: ESP-Hub Base Firmware Template
primary: J
tags: [arduino, esp-idf]
type: pattern
status: active
seen_in: [esp32-esp-hub]
maturity:
  technology: R4
  implementation: R0
  field_evidence: R0
  reusability: W4
```

## Kurzfassung

Ableitungsmuster für Hub-Nodes: gemeinsame Plattform (WiFiManager, Heartbeat, OTA, Status-Web/SSE, Lifecycle/`SystemState`, `Fsm<>`) **unverändert lassen**; nur markierte Abschnitte anfassen (`ProjectConfig`, Hardware/`ios`, optional BaseModule / eigene Web-Tabs). Ab **1.9+** ist die Vorlage ein **Ordner** (`esp-hub-base/` + `src/core/`), kein Einzel-`.ino`-Monolith. Ab **1.11** grober Infra-Lifecycle + FSM-Helper (Domain-Graphen bleiben lokal). Ergebnis: konsistente Familie + schneller Start; Derived A/B belegt Transfer.

## Abgrenzung

- **Ist:** Template-/Fork-Disziplin für Hub-Nodes inkl. A/B-Sync-Regel (HI/CpuLoad).
- **Ist nicht:** Modular-Host (`esp-module-host`); der HTTP-Contract (`esp-hub-telemetry`); der Adapter; Zwang, Diag/Recovery in jede Ableitung zu vendorn (Base-only bis Stufe C/D).

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Heartbeat-Kern für Features umbauen | `REJECTED` | Kern belassen; ios / Module erweitern |
| WLAN-Secrets im Repo | `REJECTED` | nur WiFiManager/NVS |
| Beliebige Bin-Namen | `REJECTED` | `{projekt}.{version}.esp32[.s3].bin` |
| Jede Ableitung braucht neues Hub-Sheet | `REJECTED` | Contract-Sheet wächst; Application neu |
| Ableitung = einzelne `.ino` ohne Ordner | `REJECTED` | ab 1.9 gesamten `esp-hub-base/`-Baum bauen |
| Diag/Recovery still in A/B nachziehen | `REJECTED` | bewusst Base-only; Stufe C/D Gate |
| `src/core/` für Sensorik umbauen | `REJECTED` | Plattform; Features in `.ino` / Module |

### Projektstart-Checkliste

- [ ] Ordner `esp-hub-base/` kopieren/forken (nicht nur `.ino`)
- [ ] `ProjectConfig.h`: DEVICE_NAME, FW_VERSION, Portal-SSID, Hub
- [ ] `.ino`: Hardware + ios + `updateIoValues()`; optional BaseModule
- [ ] `src/core/` belassen; HI/CpuLoad-Kopien bei Patch syncen
- [ ] Domain-FSM: `Fsm<>` / lokales Enum — nicht `SystemState` erweitern
- [ ] OTA-Policy nötig? `Lifecycle::setAllowOta` (nicht OtaService forken)
- [ ] Web: `web/` + `pack_ui.py` (gzip) wenn UI geändert
- [ ] Diag/Recovery nur bewusst (nicht still A/B); `Lifecycle`/`Fsm` sind A/B-fähig
- [ ] Contract-Checkliste `esp-hub-telemetry` (Status-Additive `sysState*`)
- [ ] Application + `seen_in`

## Referenzen

- [ESP32.esp-hub](https://github.com/MPunktBPunkt/ESP32.esp-hub) „Neue Firmware ableiten“ · `docs/update/`

## Offene Fragen

- Wann Template vs. `esp-module-host` (toolnode)?
- Stufe C/D: welche Diag-APIs gehören in Produkt-Nodes?
- M12 (Base **1.11.0** / D-021): `Lifecycle`/`SystemState` + `Fsm<>` — Sheet/Application/Evidence nachziehen (`sysState` additiv; Domain-FSMs bleiben lokal; `allowOta`-Hook)?
- **1.12.0 / D-022:** UiTab-Shell — Application `esp32-wireguard` / Sheet `esp-module-host` (Flash-Budget dokumentiert).
