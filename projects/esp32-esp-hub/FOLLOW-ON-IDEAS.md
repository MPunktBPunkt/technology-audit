# Folgeprojekte

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Ableiten-Checkliste in `ta-assist` Bootstrap-Prompt | `esp-hub-base-template` | Prompt-Text |
| BOOT 3 s WLAN-Reset manuell an Base | `esp-hub-base-template` | Feld |
| Partition Minimal SPIFFS Evidence | `esp-hub-base-template` | Feld |
| Adapter-Nachzug Rename/`interval` (0.5.x) | `esp-hub-telemetry` · `iobroker-esp-hub-adapter` | Adapter-Kampagne |
| MeterMaster optional Hub-`interval`/`otaUrl` | `esp-hub-telemetry` | Derived ADR |
| Ergo `HwInfo` → `HardwareInfo` angleichen | `esp-hub-base-template` | Parallelspur |
| Stufe C/D: Diag/Recovery bewusst in Produkt-FWs | Base-only APIs | Gate |
| **M12 System Lifecycle + Fsm<>** (Base 1.11.0 / D-021): Sheet `esp-hub-base-template` + Application nachziehen; Status-Additive `sysState`/`sysStateAgeMs` in `esp-hub-telemetry`; Lab-Smoke `/api/status` nach Boot | `esp-hub-base-template` · `esp-hub-telemetry` | Desk + Lab |
| Derived A/B: `Lifecycle.h`/`Fsm.h` vendorn (ohne Diag-APIs); heartrate `BleCentral::setState` → `Fsm<BleState>` Pilot | `esp-hub-base-template` | Code-Transfer |
| bt-gateway: `Lifecycle::setAllowOta` an STREAMING/BMW-Connect koppeln (Pflichtenheft) | `esp-hub-base-template` · `esp-hub-telemetry` | Firmware noch offen |
