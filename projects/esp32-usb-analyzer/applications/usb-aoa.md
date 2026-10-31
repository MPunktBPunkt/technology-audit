# Project Application: usb-aoa in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: usb-aoa
status: active
sheet: ../../../technologies/usb-aoa/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-pilot/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

**Lab-Validierung** des AOA Control-Handshake und Vendor-Bulk-Rohrs auf OTG Host↔Device — Desk-FACTS aus dem Sheet operationalisieren. **Nicht** HU Connected.

## Architektur / Datenfluss

```text
Host AOA Accessory ──EP0 51→52×6→53──▶ Device AoaLabResponder
        │ soft re-enum → 18d1:2d00
        └── Vendor Bulk OUT/IN echo (lab Rohr)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/.../AoaLabResponder.*` | Device EP0 + bulk echo |
| `tools/lab_aoa_handshake_verify.py` | Lab A/B + `--bulk` |
| Capture `decoded.protocol=aoa` | Host markers |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| Lab A duration 51…reenum | ~553 ms | `MEASURED` · `EVID-USBA-2026-10-31-006` |
| Protocol | AOA 1.0 (GET_PROTOCOL=1) | `MEASURED` |
| Lab B responder OFF | Host fail/STALL | `MEASURED` · `007` |
| Bulk echo | TinyUSB FIFO poll (nicht nur Arduino RX queue) | `MEASURED` · `008` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| ESP↔ESP AOA control + accessory VID/PID | `EVID-USBA-2026-10-31-006` | `MEASURED` (lab) |
| Vendor bulk echo | `008` | `MEASURED` (lab) |
| HU/Phone AOA wire | — | `UNKNOWN` / deferred (hu-probe C1b) |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 0.0.31→0.0.32 | Arduino USBVendor RX allein missingt OUT — FIFO-Poll Fix |
| Timing | Band passt zu hu-probe Phone lab ~0,5–0,6 s (Desk note) |

## Abweichungen vom „Lehrbuch“

Soft-composite bleibt MSC+Vendor(+HID); AOA Switch ändert Identität — MSC-Gates der Produkt-Sonden unangetastet lassen.

## Verwandte Applications / Methods

- hu-probe `usb-aoa` Application (Feld-Gaps)
- `bmw-bcl` Lab-Framing über AOA bulk
