# Project Application: usb-aoa in hu-probe

```yaml
project_id: hu-probe
tech_slug: usb-aoa
status: active
sheet: ../../../technologies/usb-aoa/SHEET.md
audit: ../../../audits/usb-aoa-bmw-connected-2026-desk/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

**Nur Transport-Sicht / Desk.** AOA ist ein Kandidat für ein künftiges Byte-Rohr unter
einer Connected-App-Control-Plane (`… → ITransport → BclFramer`).  
hu-probe bleibt vorerst **USB-MSC-Messsonde**; dieser Application-Eintrag legt **keine**
Firmware-Architektur „wir bauen AOA“ fest und ändert **keine** MSC-Gates.

## Architektur / Datenfluss (Zielbild — nicht implementiert)

```text
[HU NBT Evo?] --USB AOA Bulk--> [ITransport / AoaTransport?] --> BclFramer --> …
                                        ^
                                        optional später: SppTransport (BT)
```

Heute gemessen: MSC Device-Pfad. AOA wäre eine **andere** USB-Rolle/Klasse am OTG.

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| AOA Handshake/PIDs allgemein | `EVID-AOA-2026-10-28-001`…`010` | `FACT` A (Desk) |
| AAIdrive USB-Accessory / BMW manufacturer | `EVID-AOA-2026-10-28-014`…`016` | `FACT` B fremd |
| Feld Enum Zubehör `0x18D1:0x2D00` (aoa_observe) | `EVID-AOA-2026-10-29-030` | `MEASURED` (P0-A/C) |
| AOA Control 51/52/53 am Wire | `EVID-AOA-2026-10-29-030` | **absent** diese Session → C1b **B1** |
| BCL-ähnliche Frames auf Bulk | `EVID-AOA-2026-10-28-026` | `UNKNOWN` / absent → C1b **B2** |
| Vendor-Tap sieht Standard/Class nicht vollständig | `EVID-AOA-2026-10-29-031` | `FACT` Impl-Gap |
| Post-53 Re-Enum | `EVID-AOA-2026-10-29-032` | NOT IMPLEMENTED |

## Empfehlung C1b (Desk 2026-10-29)

1. Transport-Interface **agnostisch** halten (`ITransport`).
2. Messplan B1/B2 aus [`C1b-PLAN.md`](../../../audits/usb-aoa-bmw-connected-2026-desk/C1b-PLAN.md) — **Plan only**, kein Code in diesem Audit.
3. MSC-Instrumentierung und bestehende Gates unangetastet; kein Soft-Composite.
4. Already-Accessory-Boot: Kill „kein Switch zu 0x18D1“ ersetzen durch „kein Bulk/Connected nach Enum“.

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-28 Desk | Sheet + Kampagne `usb-aoa-bmw-connected-2026-desk` closed; R0 Field |
| 2026-10-29 Feld (Quellrepo) | `aoa_observe` Enum+UI ja; 51/52/53=0; Bulk=0 — Evidence `030` |
| 2026-10-29 Desk continuation | Gap A/B + C1b-PLAN B1/B2; Applications aktualisiert |
