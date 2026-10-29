# Project Scope: bimmergestalt-idrive-refs (Fremd)

```yaml
project_id: bimmergestalt-idrive-refs
title: BimmerGestalt — BMW iDrive / Connected-App Protocol Desk Sources
updated: 2026-10-29
profile_hint: lab-tool
reviewed_commit: "org-BimmerGestalt-2026-10-28+c1b-desk-continuation"
repos:
  - https://github.com/BimmerGestalt/AAIdrive
  - https://github.com/BimmerGestalt/BMWConnectedAnalysis
  - https://github.com/BimmerGestalt/BclCarLink
  - https://github.com/BimmerGestalt/BimmerGestalt.github.io
  - https://github.com/BimmerGestalt/HassGestalt
  - https://github.com/BimmerGestalt/IDriveConnectAddons
  - https://github.com/BimmerGestalt/IDriveConnectKit
  - https://github.com/BimmerGestalt/IDriveConnectKitAndroid
  - https://github.com/BimmerGestalt/IDriveExperiments
  - https://github.com/BimmerGestalt/ReadYou
  - https://github.com/BimmerGestalt/Simulator
  - https://github.com/BimmerGestalt/Simulator-kt
  - https://github.com/BimmerGestalt/breezy-weather
  - https://github.com/BimmerGestalt/wireshark_bmw_bcl
status: active
```

## Zweck

Desk-only External-Knowledge-Audit der öffentlichen Org **BimmerGestalt** (14 Repos).
Ziel: belastbares Wissen über BMW Connected-App-/iDrive-Protokollschichten
(**BCL → Etch/BMWRemoting → RHMI/AV/CDS/AM**) für `technology-audit`, Querverweise
zu `hu-probe` und `pidrive` — ohne fremde Claims als eigene Lab-/Field-FACTS zu
übernehmen.

Leitfrage: *Welches technische Wissen steckt in diesen Repos, das wir für eigenes
Reverse Engineering wiederverwenden können — mit Herkunft und Evidenzstärke?*

## Systeme und Grenzen

| Quelle | Rolle | Im Scope? |
|--------|-------|-----------|
| BclCarLink | BCL-Client-Implementierung (BT RFCOMM) | ja — P0 |
| wireshark_bmw_bcl | BCL-Dissector + Etch `.ewh` | ja — P0 |
| BMWConnectedAnalysis | RE-Doku (BCL/Etch/Auth/RHMI/CDS) | ja — P0 |
| IDriveConnectKit (+ Android) | Etch IDL, RHMI-Lib, Connection-Helper | ja — P0 |
| AAIdrive | Produktionsnahe Connected Apps (Music/AV/RHMI) | ja — P0 |
| Simulator / Simulator-kt | Fake-HU Etch-Server | ja — P1 Lab |
| IDriveConnectAddons / HassGestalt / IDriveExperiments | RHMI-/CDS-Muster | ja — P1/P2 |
| ReadYou / breezy-weather | Consumer-Forks mit BMW-App-Support | gesichtet — P2 / irrelevant für Protokollkern |
| BimmerGestalt.github.io | Pages-Hub | gesichtet — Link-Hub |

## Nicht-Ziele

- Code-/Firmware-Änderungen an `hu-probe`, `pidrive`, ESP-Projekten
- Übernahme von BimmerGestalt-Claims als eigene MEASURED-FACTS
- Attack-/Bypass-Anleitungen (SAS/Cert/Security-Service)
- Stillschweigender Transfer NBT Evo USB-MSC-Verhalten ↔ Connected-App-Protokoll
- Implementierungsempfehlung ohne eigene Evidence

## Epistemik

Externe Herkunft bleibt sichtbar. Klassifikation:
`FACT` (Code/Doc am Pin) · `INFERENCE` · `HYPOTHESIS` · `UNKNOWN` · `REJECTED`.
Evidence-Achse R getrennt von Knowledge-Value und Reuse.
W ≠ Evidenz.

## Prioritäten

1. BCL Framing / Handshake / Dest-Ports  
2. Etch `BMWRemoting` (SAS, RHMI, AV, CDS, AM)  
3. RHMI Lifecycle + Media/AV  
4. Connection/Transport (BT vs Doc-USB/ENET)  
5. hu-probe / PiDrive Cross-Reference  
