# Project Scope: espargos-espsdr (Fremd)

```yaml
project_id: espargos-espsdr
title: ESPARGOS ESP-SDR — Multi-Chip Undocumented I/Q RX (Fremd)
updated: 2026-10-11
profile_hint: lab-tool
reviewed_commit: "esp-sdr@e74f2a4 SoapyESPSDR@6f2cc72 CardputerADV-SDR@aa4737d"
reviewed_commit_note: Desk; Site Snapshot 2026-10-11
repos:
  - https://github.com/ESPARGOS/esp-sdr
  - https://github.com/ESPARGOS/SoapyESPSDR
  - https://github.com/fedaykinofdune/CardputerADV-SDR
sources:
  - https://espargos.net/espsdr
status: active
```

## Zweck

Primärquelle **Chip-Capability-Matrix** für undokumentierten I/Q-RX-Dump; G7 Host-Backends (WebSDR / Soapy / Bridges). Kein TX-Public-Code.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESPARGOS/esp-sdr | Multi-target Firmware | ja |
| SoapyESPSDR | S31 continuous stream Host | ja |
| CardputerADV-SDR | Downstream Board-Port | ja (Portabilität) |
| espargos.net/espsdr | Flasher / WebSDR | ja (Snapshot) |
| Public TX firmware | — | **nein** (withheld) |
| Eigene Array-Phasenmessung | — | FOLLOW-ON |

## Nicht-Ziele

- TX-Claims aus Site-Marketing als Implementierungs-FACT
- Sheet pro Board-Port
- 100–6000 MHz Tuning-Marketing als Performance-FACT

## Prioritäten

1. Sheet `esp32-undoc-iq-rx` mit Matrix inkl. C5/S31  
2. Applications / Ports ohne PHY-Fork  
3. Abgrenzung zu polar-TX und APLL
