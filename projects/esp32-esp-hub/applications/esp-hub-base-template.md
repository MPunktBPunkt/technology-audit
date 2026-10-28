# Project Application: esp-hub-base-template in esp32-esp-hub

```yaml
project_id: esp32-esp-hub
tech_slug: esp-hub-base-template
status: active
sheet: ../../../technologies/esp-hub-base-template/SHEET.md
audit: ../../../audits/esp32-esp-hub-2026-1.10-validation/
maturity:
  technology: R4
  implementation: R4
  field_evidence: R3
  reusability: W4
```

## Rolle im Projekt

Kanonische Vorlage `esp-hub-base` **v1.10.5**: AppCore-Plattform unter `src/core/`; Ableiten über `ProjectConfig.h`, `.ino`-Zonen und optional BaseModule. Derived A/B-Rollout belegt Transfer.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `esp-hub-base/ProjectConfig.h` | DEVICE_NAME, FW_VERSION, Hub, Portal |
| `esp-hub-base/esp-hub-base.ino` | Hardware / ios / `updateIoValues()` |
| `esp-hub-base/src/core/` | AppCore, Hub, Web, OTA, Lifecycle (Plattform) |
| `esp-hub-base/src/modules/` | BaseModule-Beispiel |
| `docs/update/ROLLOUT_DERIVED.md` | A/B-Matrix |
| `docs/update/AUDIT_BASE_A-B_2026-10-27.md` | Freeze-Grenze Base-only vs A/B |
| README „Neue Firmware ableiten“ | Prozess |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Ableiten-Zonen Ordner/Core | `EVID-BASE-2026-10-28-001` | `FACT` |
| M0–M11 + BaseModule | `EVID-BASE-2026-10-28-002` | `FACT` |
| Derived A/B Lab-Reuse | `EVID-BASE-2026-10-28-003` | `FACT` (Lab, Upstream) |
| Diag/Recovery ≠ A/B-Pflicht | `EVID-BASE-2026-10-28-004` | `FACT` |
| Bin-Namenskonvention | `EVID-BASE-2026-10-09-002` | `FACT` |
