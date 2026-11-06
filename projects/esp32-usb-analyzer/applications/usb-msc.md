# Project Application: usb-msc in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-field-host-matrix/
related_audits:
  - ../../../audits/esp32-usb-analyzer-2026-0.0.50/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R2   # Fremd-Host-Matrix 2026-11-06; OTG-Loop bleibt Lab
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
| `tools/lab_baseline_campaign.py` | Volle MSC/TCP-Tabelle |
| `tools/lab_capability_audit.py` | Regressionstor inkl. MSC |
| `tools/lab_bot_class_hook_verify.py` | Gate-6 CBW/CSW |
| `tools/lab_usb_proxy_verify.py` | Proxy byte-exact |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| Media | 256 KiB gadget RAM; write-cache 64 LBA | `FACT` (B) |
| Peak READ (0.0.50) | **~917 kB/s** chunk=8 | `MEASURED` · `EVID-USBA-2026-11-02-001` |
| Sustained 3× | **907–914 kB/s**, failB=0 | `MEASURED` · `001` |
| Peak WRITE | ~250–460 kB/s (Pilot 0.0.18) | `MEASURED` · Pilot `005` |
| Multi-LBA fill bug | fixed Device 0.0.14 | `FACT` · Pilot `004` |
| Soft ceiling band | ~0.90–0.93 MB/s über 0.0.14→0.0.50 | `MEASURED` |
| Windows Feld WRITE | 31 ops / 54272 B (=106 Sektoren) vs Cache 64 | `MEASURED` Bytes; Eviction `UNKNOWN` · `EVID-USBA-2026-11-06-010` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| OTG-Loop Integrity-clean 0.0.50 | `EVID-USBA-2026-11-02-001` | `MEASURED` |
| Class-hook CBW/CSW sichtbar | `EVID-USBA-2026-11-02-005` (+ Pilot `012`) | `MEASURED` |
| Proxy byte-exact ≠ MITM | Pilot `013` / Observer `007` | `MEASURED` / claim limit |
| Fremd-Hosts mounten Lab-MSC (HU/TV/Soundbar/FRITZ/Windows) | `EVID-USBA-2026-11-06-002`…`005` | `MEASURED` |
| Write-Cache Eviction / 64 vs 106 Sektoren | `010` | `UNKNOWN` / Test Gap |
| Host-Fingerprints | siehe [`usb-msc-host-behaviour`](usb-msc-host-behaviour.md) | — |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-31 | False positive pattern_fail bei chunk>1 vor Fill-Fix |
| 2026-10-31 | WRITE ≪ READ expected on this stack |
| 2026-11-02 | Revalidation: Rate-Band stabil; Capability 7/7 |
| 2026-11-06 | Feldmatrix: Lab-MSC als Storage-Probe an Fremd-Hosts; Write-Cache Gap offen |

## Abweichungen vom „Lehrbuch“

App-inferred BOT decode existiert parallel zu class-hook — immer `source` lesen. Fremd-DUT (pidrive/hu-probe) beweist Visibility, nicht `lab_sector_v1`-Pattern-Rate. Pattern-Stick ≠ FAT-Media-UI.

## Verwandte Applications / Methods

- [`usb-otg-loop-baseline`](../../../methods/usb-otg-loop-baseline.md)
- [`usb-bot-command-observation`](../../../methods/usb-bot-command-observation.md)
- [`usb-msc-host-fingerprint`](../../../methods/usb-msc-host-fingerprint.md)
- [`usb-msc-host-behaviour`](usb-msc-host-behaviour.md) · [`bmw-nbt-evo`](bmw-nbt-evo.md)
- hu-probe / pidrive `usb-msc` Apps (Feld vs Lab)
