# Project Application: esp-hub-telemetry in esp32.bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: esp-hub-telemetry
status: draft
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
maturity:
  technology: R0
  implementation: R0
  field_evidence: R0
  reusability: W0
```

## Rolle im Projekt

Hub-Registration, Heartbeat, OTA (`bt-analyzer.<ver>.esp32s3.bin`) vor jedem Bluetooth-Capture (Gate BT0).

## Architektur / Datenfluss

```text
ESP AppCore  →  Hub :8093 register/heartbeat  →  OTA push / inventory
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/analyzer-node/src/core/` | vendored esp-hub-base v1.10.5 |
| `tools/flash_lab_ota.sh` | LocalWeb OTA |
| `docs/HUB-BASELINE.md` | Stufe A policy |
