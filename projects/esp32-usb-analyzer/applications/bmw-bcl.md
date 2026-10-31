# Project Application: bmw-bcl in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: bmw-bcl
status: active
sheet: ../../../technologies/bmw-bcl/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-pilot/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

**Desk/Lab Framing only:** 8-byte BE BCL-Header + init über AOA Vendor-Bulk-Echo. Host-Unit-Tests + Lab-Serie. Beweist **nicht** Connected auf HU-Wire.

## Architektur / Datenfluss

```text
Host BclLabFrame ──AOA vendor bulk──▶ Device echo ──▶ Host RX parse
                 (HANDSHAKE / DATA / empty)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/common/.../BclLabFrame.h` | Framing |
| `tests/host/` | Host units (no hardware) |
| `tools/lab_aoa_bcl_verify.py` | `--series` / `--unit-only` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Lab BCL framing echo over AOA bulk | `EVID-USBA-2026-10-31-009` | `MEASURED` (lab Rohr) |
| BCL on HU bulk / RFCOMM | — | `UNKNOWN` / not claimed |
| Etch/RHMI | — | out of scope |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 0.0.33/34 | Framing + RX-parse + unit negatives |

## Abweichungen vom „Lehrbuch“

Sheet beschreibt oft BT RFCOMM als beobachteten Träger; hier absichtlich **USB AOA lab Rohr** als Transport-Kandidat — gleicher Framing-Contract, anderer Pipe.

## Verwandte Applications / Methods

- `usb-aoa` Application
- Kampagne `usb-aoa-bmw-connected-2026-desk` / BimmerGestalt Desk
