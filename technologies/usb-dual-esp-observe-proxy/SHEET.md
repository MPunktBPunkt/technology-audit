# Technology Sheet: Dual-ESP USB Observe / Proxy Lab

```yaml
slug: usb-dual-esp-observe-proxy
title: Dual-ESP USB Observe / Proxy Lab
primary: H
tags: [usb, lab-only, esp32s3, capture, proxy]
type: pattern
status: active
seen_in: [esp32-usb-analyzer]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
  evidence_scope: [LAB]
pilot: audits/esp32-usb-analyzer-2026-pilot
```

Ebene **A** (Lab-Architektur). Board-IPs, Gate-Slices, konkrete Tools → Application B.  
HU/Feld → getrennt (C). Analog im BLE-Raum: [`ble-gatt-observe-proxy`](../ble-gatt-observe-proxy/SHEET.md) — **nicht** kopieren, nur Kontrast.

## Kurzfassung

Zwei ESP32-S3 teilen die USB-Rollen (**Host** und **Device**) und melden Ereignisse über WiFi/TCP an eine Control-Plane (Discovery, dual Timeline, Lab-API). Beobachtung und Proxy-Slices liegen auf **Class-/App-Ebene** (L1), nicht auf D+/D−. OTG-Kabel-Baseline und Mode-A Proxy sind getrennte Topologien mit getrennten Claims.

## Abgrenzung

- **Ist:** Dual-Node Lab für Enum/MSC/AOA/HID-Observation, Integrity-Messung, optionale Bulk/Control-Forward-Slices.
- **Ist nicht:** USB-IF Sniffer; Logic-Analyzer; hard clock-synced Wire Capture; produktives transparentes MITM.
- **Grenzt an:** [`esp-usb-host`](../esp-usb-host/SHEET.md) (Host-Rolle), [`usb-msc`](../usb-msc/SHEET.md) (Device/BOT), [`usb-aoa`](../usb-aoa/SHEET.md) (Vendor-Control), [`esp32-s3-usb-wifi-coex`](../esp32-s3-usb-wifi-coex/SHEET.md) (Mode-A Datenrate).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | USB OTG FS Host + Device | getrennte Chips — ein Chip ≠ dual role gleichzeitig |
| lateral | WiFi TCP event/proxy plane | oft Bottleneck vs USB cable |
| oben | Capture timeline + Lab REST | Timestamp-Domain pro Node labeln |
| lateral | Debian discovery / UI | optional Control; Datenplane kann peer-to-peer sein |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Dual-ESP Lab = transparent MITM | `REJECTED` still | Observer-effect Baseline fehlt bis belegt |
| Capture Events = D+/D− Packets | `REJECTED` | Class-hook / App-callback / inferred |
| Cross-node µs timestamps sync by default | `REJECTED` | Offset-Estimate ≠ hard lock |
| WiFi Mode-A rate ≥ USB MSC Nutzrate | oft `REJECTED` / lab-specific | Baseline Method erst messen |
| OTG-Loop Topologie = MITM Wiring | `REJECTED` | DUT↔Host und Device↔PC getrennt stecken |
| Phone HS-only auf S3 Host | `REJECTED` / Gate | FS-only Host |

### Projektstart-Checkliste

- [ ] Zwei Boards + Rollen (Host/Device) explizit
- [ ] Claim-Layer wählen: OTG-Loop Baseline vs Proxy Slice vs MITM
- [ ] Capture `source` Tags Pflicht (inferred / class_hook / …)
- [ ] Method [`usb-otg-loop-baseline`](../../methods/usb-otg-loop-baseline.md) vor Rate-Claims
- [ ] Coex-/PHY-Hygiene: [`esp32-s3-usb-wifi-coex`](../esp32-s3-usb-wifi-coex/SHEET.md)
- [ ] Application + `seen_in`; Feld/HU = anderes Audit

## Transfer

Nützlich für jedes Lab, das USB Host- und Device-Verhalten **gleichzeitig** instrumentieren will (Protokollforschung, Proxy-PoC, AOA/MSC Desk). Nicht als Ersatz für Hardware-Sniffer oder Fahrzeug-Feldmessung verkaufen.

## Referenzen

- Pilot: [`esp32-usb-analyzer-2026-pilot`](../../audits/esp32-usb-analyzer-2026-pilot/)
- Kontrast Methods: [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md), [`usb-wifi-coex-discrimination`](../../methods/usb-wifi-coex-discrimination.md)

## Offene Fragen

- Wann ist Mode-A + Windowing ausreichend vs. Store-and-Forward?
- Minimales Observer-effect Protokoll für „transparent genug“?
