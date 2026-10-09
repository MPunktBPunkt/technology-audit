# Project Scope: esp32.network

```yaml
project_id: esp32-network
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.network
reviewed_commit: 3b9b82d
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `esp32.network.ino`, README (Scan, SSE, TR-064, Hub) |
| **Nicht in scope** | RF-Monitor; ESP-NOW; Spektrumanalyse |
| **Hardware** | ESP32 (Wemos D1 Mini getestet) |
| **Version** | 1.6.6 |

## Systeme

```text
Subnet TCP-Port-Scan ──▶ Device Inventory (NVS)
optional FritzBox TR-064 HTTPS:49443 ──▶ Merge
Browser ◀── REST+SSE
ESP ──Hub ios devices/online──▶ esp-hub
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.2** (Hub ohne fwType, Scan-Schichten, Reuse).
