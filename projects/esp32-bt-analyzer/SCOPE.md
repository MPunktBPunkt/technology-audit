# Project Scope: esp32.bt-analyzer

```yaml
project_id: esp32-bt-analyzer
title: ESP32 Bluetooth USB/HCI Analyzer
updated: 2026-11-03
source_repo: https://github.com/MPunktBPunkt/esp32.bt-analyzer
reviewed_commit: pending
profile_hint: lab-tool
status: active
repos:
  - https://github.com/MPunktBPunkt/esp32.bt-analyzer
```

## Zweck

Lab-Instrument: ESP32-S3 als USB Host gegenüber einem kommerziellen Bluetooth-USB-Dongle; Capture des **USB-HCI**-Verkehrs mit Timestamp/Richtung; Export nach Debian (Collector / JSONL / PCAPNG).  

**Nicht** RF-/Air-Sniffer, **nicht** Universal-MITM, **nicht** on-chip Classic-BR/EDR-Analyzer auf dem S3.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESP32-S3 N8R2 USB Host | Enum + HCI capture + TCP | ja (V1) |
| USB Bluetooth Dongle (BLE / Classic) | External controller (HCI) | ja |
| Debian Collector | Decode / PCAPNG / Wireshark | ja |
| esp-hub OTA / Heartbeat | FW-Verteilung | ja |
| ESP #2 USB Device HCI stimulus | synthetische Tests | später (BT11) |
| nRF / RF Air sniffer | L0 | **nein** — separates Gate BT15 |
| S3 on-chip Classic stack | BR/EDR | **REJECTED** |
| Endpoint GATT/HFP as HCI substitute | App-Ebene | **nein** als SoT |

## Nicht-Ziele (V1)

- Bluetooth RF / channel-hopping sniffer
- Universal Phone↔Device MITM
- Fremde Bond-Decryption
- Profile-Analyse (A2DP/HFP/GATT) auf dem ESP
- Eigene Bluetooth-Host-Stack-Implementierung auf dem Capture-Node

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| Code | `firmware/`, `controller/`, `tools/` | Upstream esp32.bt-analyzer |
| Gates / Architektur | `docs/GATES.md`, `ARCHITECTURE.md`, `EVIDENCE.md` | Claim-Grenzen |
| Method | [`bt-passive-host-sniff`](../../methods/bt-passive-host-sniff.md) | HCI-Semantik |
| Capture family | [`bt-sniffing-capture-refs`](../bt-sniffing-capture-refs/) | ESP vs HCI vs nRF |
| USB Host | [`esp-usb-host`](../../technologies/esp-usb-host/SHEET.md) | Dongle enum |
| Classic S3 | [`bluetooth-a2dp`](../../technologies/bluetooth-a2dp/SHEET.md) | REJECTED on-chip |

## Prioritäten für die Analyse

1. Epistemische Matrix HCI ≠ Endpoint ≠ Air fest verankern
2. BT0 Hub/OTA Bring-up
3. Erste USB-BT-Dongle-Enumeration (BT1) → erste HCI-Frames (BT3)
4. Keine neuen Technology-Sheets, solange vorhandene reichen

## Offene Scope-Fragen

- Welcher Dongle (VID/PID) als Lab-Referenz für BLE vs Classic?
- BTAC-Framing final vs. Anleihe an usb-analyzer BCL?
- Wann WiFi-Coex-Messung Pflicht vor „lossless“-Claim (BT6/BT13)?
