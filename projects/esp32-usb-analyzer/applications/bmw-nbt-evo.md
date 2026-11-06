# Project Application: bmw-nbt-evo in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: bmw-nbt-evo
status: active
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-field-host-matrix/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R2   # P-MOUNT / Soft-Reenum / AOA-neg under MSC identity; Prefetch/Media-UI out of scope here
  reusability: W1
```

## Rolle im Projekt

**Feld-Host** für Analyzer-MSC-Gadget: NBT Evo als Storage-Host gegen Lab-Identity
`303a:1001`. Kein Prefetch-/Media-Leiter-Audit (das bleibt hu-probe/pidrive). Hier:
P-MOUNT-Sequenz, Remount, AOA-Negativ unter MSC-Identity.

## Architektur / Datenfluss

```text
BMW NBT Evo USB Host ──MSC──▶ Analyzer .89 (303a:1001 lab_sector_v1)
         │
         ├─ P-MOUNT SCSI (TUR / MS6 / PREVENT / RCAP10 / READ10)
         ├─ Soft-Reenum → remount + more READs
         └─ aoa51/52/53 = 0
```

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| HU mountet Analyzer MSC `303a:1001` | `EVID-USBA-2026-11-06-002` | `MEASURED` |
| P-MOUNT inkl. **MODE_SENSE(6)** + **PREVENT/ALLOW** am F20 | `006` | `MEASURED` |
| Soft-Reenum → Remount + READ-Anstieg | `007` | `MEASURED` |
| AOA 51/52/53 absent under MSC identity | `008` | `FACT` / `MEASURED` |
| Prefetch / Media-UI / Eager | — | out of scope (hu-probe) |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-11-06 | MODE_SENSE6 + PREVENT nicht mehr nur „erwartete MSC-Kommandos“, sondern feldbeobachtet |
| Pattern-Stick | kein Media/Zubehör auf HU-Display — Content-Gap (C0) |

## Verwandte Applications / Methods

- hu-probe / pidrive `bmw-nbt-evo` Apps (Prefetch/Media)
- Analyzer [`usb-msc-host-behaviour`](usb-msc-host-behaviour.md) · [`usb-aoa`](usb-aoa.md)
