# Project Application: usb-msc-host-behaviour in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: usb-msc-host-behaviour
status: active
sheet: ../../../technologies/usb-msc-host-behaviour/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-field-host-matrix/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

Analyzer-Device `.89` als **MSC-Feldsonde** gegen Fremd-Hosts: Host-Fingerprints
(Opcode, READ/WRITE, Mount/Remount, AOA-Nebenkanal) messen — Storage-Probe, nicht
Connected-Apps-Probe.

## Architektur / Datenfluss

```text
USB Host (HU/TV/…/Windows) ──OTG──▶ Analyzer Device MSC (303a:1001)
                                         │
                                         ├─ status: reads/bytes/writes/mounts + aoa51..53
                                         └─ class-hook CBW/CSW ring / scsi_ops
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `docs/evidence/field_host_matrix_2026-11-06/` | Rohmatrix |
| `docs/evidence/LAB_FIELD_HOST_MATRIX_2026-11-06_MEASURED.md` | Claim-Dokument |
| `docs/reports/2026-11-06-field-host-matrix.md` | Feldbericht |
| Device CaptureLog / status APIs | Zähler + Ring |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Dimensionen messbar am Analyzer-Gadget | `EVID-USBA-2026-11-06-001` | `FACT` |
| BMW / Windows Referenzprofile | `002`/`003`/`006`/`007` | `MEASURED` |
| Ergometer Non-Host | `004` | `MEASURED` |
| TV/Soundbar/FRITZ n=1 | `005` | Project Evidence; GENERAL `REJECTED` |
| Write-Cache Eviction | `010` | `UNKNOWN` / Test Gap |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-11-06 @ `688a40b` | Fremd-Host-Messreihe lohnt sich; Fingerprint > „AOA=0“-Headline |
| Capture ring | Overflow `dropped≈2476` — Aggregate Counters P0 |

## Abweichungen vom „Lehrbuch“

Pattern-Stick erzeugt Mount ohne Media-UI. AOA-respond am MSC-Gadget ersetzt keine
phone-like Identity.

## Verwandte Applications / Methods

- [`usb-msc`](usb-msc.md) · [`usb-aoa`](usb-aoa.md) · [`bmw-nbt-evo`](bmw-nbt-evo.md)
- Method [`usb-msc-host-fingerprint`](../../../methods/usb-msc-host-fingerprint.md)
