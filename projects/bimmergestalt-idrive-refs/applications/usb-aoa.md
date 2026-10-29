# Project Application: usb-aoa in bimmergestalt-idrive-refs

```yaml
project_id: bimmergestalt-idrive-refs
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

Desk-Ergänzung zum Connected-App-Stack: **USB AOA als möglicher physischer Transport**
unter BCL — getrennt vom BCL-Sheet. Pins: AAIdrive@`3e93419`, BclCarLink@`7cfd959`,
BMWConnectedAnalysis@`9e96ac6`.

## Evidenz (Transport nur)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Doc USB Accessory als BCL-Weg | `EVID-AOA-2026-10-28-011` | `FACT` Doc |
| BclCarLink nur BT | `EVID-AOA-2026-10-28-012` | `FACT` Code |
| USB-Impl in BclCarLink | `EVID-AOA-2026-10-28-013` | Contradiction / REJECTED |
| AAIdrive UsbAccessory / BMW manufacturer | `EVID-AOA-2026-10-28-015` | `FACT` Code |
| BCL-Ready inkl. USB Accessory | `EVID-AOA-2026-10-28-016` | `FACT` Code |
| USB_STATE: charging / mtp / accessory getrennt | `EVID-AOA-2026-10-29-027` | `FACT` Code |
| Connected: USB Acc **oder** BT → BCL → ATTACHED | `EVID-AOA-2026-10-29-028` | `FACT` Doc |
| BCL stream-agnostisch; Wire nur RFCOMM in BclCarLink | `EVID-AOA-2026-10-29-029` | `FACT` Code |
| Doc: File Transfer oft vor Apps-USB | `EVID-AOA-2026-10-29-033` | `FACT` Doc |
| Feld: Enum Zubehör ja; 51/52/53=0; Bulk=0 | `EVID-AOA-2026-10-29-030` | `MEASURED` C (hu-probe) |

## Abgrenzung

Keine RHMI/Etch/SAS-Analyse in diesem Application-File. Siehe `bmw-bcl` /
`bmw-etch-rpc` / `bmw-rhmi` Applications und Kampagne
`bimmergestalt-idrive-2026-foreign`. C1b-Messplan:
[`C1b-PLAN.md`](../../../audits/usb-aoa-bmw-connected-2026-desk/C1b-PLAN.md).
