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
| AOA am F20/NBT Evo erreichbar | `EVID-AOA-2026-10-28-025` | `UNKNOWN` → C1b **B1** |
| BCL-ähnliche Frames auf Bulk | `EVID-AOA-2026-10-28-026` | `UNKNOWN` → C1b **B2** |

## Empfehlung C1b-0

1. Transport-Interface **agnostisch** halten (`ITransport`).
2. Keine AOA-/SAS-/Etch-/RHMI-Implementierung in hu-probe aus diesem Desk.
3. MSC-Instrumentierung und bestehende Gates unangetastet.
4. Nächste Engineering-Arbeit = Messplan B1/B2, nicht Code.

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-28 Desk | Sheet + Kampagne `usb-aoa-bmw-connected-2026-desk` closed; R0 Field |
