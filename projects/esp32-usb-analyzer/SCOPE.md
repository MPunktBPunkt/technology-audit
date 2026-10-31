# Project Scope: esp32.usb-analyzer

```yaml
project_id: esp32-usb-analyzer
title: Dual ESP32-S3 USB Protocol Analyzer / MITM Lab
updated: 2026-10-31
source_repo: https://github.com/MPunktBPunkt/esp32.usb-analyzer
reviewed_commit: b2c9987
profile_hint: lab-tool
status: active
repos:
  - https://github.com/MPunktBPunkt/esp32.usb-analyzer
```

## Zweck

Lab-Instrument: zwei ESP32-S3 (OTG Host + OTG Device) und Debian (Discovery `:9750`, Lab-UI `:8080`) für Capture, Proxy-Slices und Protokoll-Lab (MSC/AOA/BCL-Framing/HID) — **ohne** USB-IF-Compliance oder transparente MITM-Claims.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESP-A `.88` Host OTG | Enum / MSC Host-Probe / AOA Host / Capture | ja |
| ESP-B `.89` Device OTG | MSC(+Vendor+HID) Gadget / Responder / Capture | ja |
| Debian Control | Discovery, dual Capture-Proxy, Lab-UI | ja |
| WiFi TCP `:9752` Mode A | Integrity / MSC-proxy / EP0-forward slices | ja (lab) |
| OTG-Kabel Host↔Device | Baseline MSC READ/WRITE + Pattern | ja — MEASURED |
| PC als Device-Host | Enum Device-Gadget | ja (lab) |
| BMW NBT / HU Wire | Feld-Host | **nein** — kein HU-Lauf in diesem Audit |
| D+/D− / DATA0/1 | L0 Wire | **nein** — Gate 10 UNKNOWN |
| Transparent MITM PC↔Stick | Observer-effect Baseline | **noch nicht** claimed |

## Nicht-Ziele

- Hard µs-Clock-Lock zwischen beiden ESPs (nur Offset-Estimate)
- High-Speed USB
- HU Connected / BCL-on-Bulk als Feld-FACT
- Gleichsetzung App-Callback / Class-Hook mit Wire-Packets

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| Code | `firmware/`, `controller/`, `web/`, `tools/` | Upstream @ `b2c9987` |
| Gates / Architektur | `docs/GATES.md`, `ARCHITECTURE.md`, `CAPTURE.md` | Claim-Grenzen |
| Lab Evidence | `docs/evidence/LAB_*_MEASURED.md` + JSON | MEASURED 2026-10-31 |
| KB-Digest | Upstream `docs/EVIDENCE.md` | Gate-0 Extrakt aus technology-audit |

## Prioritäten für die Analyse

1. Lab-Baseline (MSC/TCP) und Claim-Boundaries in Evidence-IDs
2. Match auf bestehende Sheets (`usb-msc`, `esp-usb-host`, `usb-aoa`, …)
3. Dual-Node Observe/Proxy als wiederverwendbares Pattern + Method
4. Offene Gates (transparent MITM, L0, HU) als UNKNOWN/REJECTED belassen

## Offene Scope-Fragen

- Wann Mode-A Datenrate (WiFi) für MSC-Proxy unter Last ausreicht vs. Store-and-Forward?
- Observer-effect Baseline: welcher Kontroll-Host vor erstem „transparent“-Claim?
