# Project Application: usb-msc in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-pilot/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt

Device-Node MSC Gadget (Lab-Media 512×512 B) + Host-Node MSC Probe; BOT Class-Hooks für CBW/CSW Capture; optional MSC Bulk-Proxy über WiFi.

## Architektur / Datenfluss

```text
Host usb-host-probe READ/WRITE ──OTG──▶ Device TinyUSB MSC (lab_sector_v1)
Device class-hook mscd_xfer_cb/send_csw ──▶ CaptureLog (source=class_hook_…)
Proxy: Device MscReq ──TCP──▶ Host READ DUT ──payload──▶ Device
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/…` MSC gadget / probe APIs | Device + Host |
| `firmware/common/.../UsbLabPattern.h` | `lab_sector_v1` |
| `tools/lab_usb_loop_probe.py` | OTG MSC sweep |
| `tools/lab_bot_class_hook_verify.py` | Gate-6 CBW/CSW |
| `tools/lab_usb_proxy_verify.py` | Proxy byte-exact |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| Media | 256 KiB gadget RAM; write-cache 64 LBA | `FACT` (B) |
| Peak READ | ~934 kB/s chunk=8 | `MEASURED` · `EVID-USBA-2026-10-31-001` |
| Peak WRITE | ~250–460 kB/s | `MEASURED` · `005` |
| Multi-LBA fill bug | fixed Device 0.0.14 | `FACT` · `004` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| OTG-Loop Integrity-clean | `EVID-USBA-2026-10-31-001` | `MEASURED` |
| Class-hook CBW/CSW sichtbar | `EVID-USBA-2026-10-31-012` | `MEASURED` |
| Proxy byte-exact ≠ MITM | `EVID-USBA-2026-10-31-013` | `MEASURED` / claim limit |
| NBT/HU MSC | — | out of scope |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-31 | False positive pattern_fail bei chunk>1 vor Fill-Fix |
| 2026-10-31 | WRITE ≪ READ expected on this stack |

## Abweichungen vom „Lehrbuch“

App-inferred BOT decode existiert parallel zu class-hook — immer `source` lesen.

## Verwandte Applications / Methods

- [`usb-otg-loop-baseline`](../../../methods/usb-otg-loop-baseline.md)
- [`usb-bot-command-observation`](../../../methods/usb-bot-command-observation.md)
- hu-probe / pidrive `usb-msc` Apps (Feld vs Lab)
