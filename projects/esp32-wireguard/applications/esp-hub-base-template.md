# Project Application: esp-hub-base-template in esp32-wireguard

```yaml
project_id: esp32-wireguard
tech_slug: esp-hub-base-template
status: active
sheet: ../../../technologies/esp-hub-base-template/SHEET.md
maturity:
  technology: R4
  implementation: R2
  field_evidence: R1
  reusability: W4
```

## Rolle

Vendorierte `esp-hub-base` **1.12.0** (D-022 UiTab). Abgeleitete Firmware `fwType=wireguard`, OTA über Hub, Core-Tabs unverändert.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Base 1.12.0 auf .87/.88/.131 (OTA) | `EVID-WG-2026-11-27-003` | `FACT` (Lab) |
| Δ Base 1.11.1→1.12.0 ≈ +2.0 KiB Flash | `EVID-BASE-2026-11-27-022` | `FACT` (Build-Host) |
