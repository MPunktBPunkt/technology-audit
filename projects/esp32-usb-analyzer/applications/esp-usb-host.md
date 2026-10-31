# Project Application: esp-usb-host in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: esp-usb-host
status: active
sheet: ../../../technologies/esp-usb-host/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-pilot/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

ESP-A (`analyzer-s3-host`): USB OTG **Host** — DUT-Enum, MSC Host-Probe, AOA Accessory-Rolle, HID Observe, Capture.

## Architektur / Datenfluss

```text
DUT FS Device ──OTG──▶ EspUsbHost callbacks ──▶ CaptureLog / Lab APIs
                              │
                     optional TCP peer (.89)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/analyzer-node` env `analyzer-s3-host` | Host FW |
| `/api/lab/usb-host-probe`, `usb-enum-observe`, `hid-observe`, `aoa-*` | Lab REST |
| `tools/lab_usb_enum_observe.py`, `lab_hid_interrupt_verify.py` | Verify |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| Stack | EspUsbHost 2.x + Arduino-ESP32 ≥3.2 (Upstream Gate1) | `FACT` (B) |
| Speed | FS only | `FACT` · Sheet |
| Enum outcome | address/config ≠0 MEASURED | `MEASURED` · `EVID-USBA-2026-10-31-010` |
| HID observe | keyboard report via callback | `MEASURED` · `011` |
| HS Phone as DUT | often FAIL | `FACT` Gate4 notes |

## Ebene C — Host- / Feld-Evidenz

Lab-only (OTG peer als DUT). Kein Fahrzeug-Host.

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| FS DUT enum + MSC I/O | `EVID-USBA-2026-10-31-001`/`010` | `MEASURED` |
| HID interrupt observe | `EVID-USBA-2026-10-31-011` | `MEASURED` |
| Mid-enum SETUP on wire | `010` | `UNKNOWN` |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| Lab inventory | `.88` Host YD-ESP32-S3 N8R2; Serial via CH343 COM |

## Verwandte Applications / Methods

- `usb-aoa` (Host treibt 51→53)
- Sheet Fallstricke VBUS / FS-only
