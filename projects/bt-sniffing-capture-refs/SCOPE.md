# Project Scope: bt-sniffing-capture-refs (Fremd)

```yaml
project_id: bt-sniffing-capture-refs
title: Bluetooth Sniffing & Capture-Pipelines (ESP → Host)
updated: 2026-10-28
profile_hint: lab-tool
reviewed_commit: "esp32-ble-scan-mqtt@ee096de BLESniffer@1bea2e8 classic_sniffer@0e174ca bsniffhub@29049d7 ble2mqtt@e66ec5a ChimeraBLE@2330423 a2dpSinkHfpClient@df6c5f4"
repos:
  - https://github.com/wiredlab/esp32-ble-scan-mqtt
  - https://github.com/CapibaraZero/BLESniffer
  - https://github.com/Matheus-Garbelini/esp32_bluetooth_classic_sniffer
  - https://github.com/homewsn/bsniffhub
  - https://github.com/shmuelzon/esp32-ble2mqtt
  - https://github.com/MatthewKuKanich/ChimeraBLE
  - https://github.com/walinsky/a2dpSinkHfpClient
status: active
```

## Zweck

Desk: Capture-Pipelines für Heimgeräte — **ESP Application-Level Endpoint → strukturierte Events → Debian** (TCP/JSONL bevorzugt). Abgrenzung zu nRF OTA und HCI-Snoop. Kein Universal-MITM.

## Systeme und Grenzen

| Quelle | Capture-Muster | Im Scope? |
|--------|----------------|-----------|
| esp32-ble-scan-mqtt | Adv → JSON → MQTT (+ Serial/SD), Queues/Drops | ja |
| CapibaraZero BLESniffer | Adv → synthetisches PCAP SD | ja |
| esp32_bluetooth_classic_sniffer | Classic aktiv → UART → Host PCAP | ja (Grenzfall Classic) |
| bsniffhub | Host: Dongle Serial → PCAP/Wireshark (+ optional Decrypt) | ja |
| ble2mqtt / Chimera / a2dpSinkHfpClient | GATT/Endpoint Logging-Muster | Querverweis |
| nRF Sniffer / Android HCI snoop | Passiv | Method `bt-passive-host-sniff` |
| Eidolon HFP TCP | — | **nicht gefunden** (öffentlich) |

## Nicht-Ziele

- ESP als nRF-Ersatz (Connection-Follow OTA)
- Attack/Decrypt fremder Bonds
- Pflicht-A2DP/SCO-Rohstream über TCP
- Ubertooth Classic OTA Schwerpunkt

## Prioritäten

1. Sheet `bt-endpoint-event-stream` (ESP→Host Event-Export)  
2. Method `bt-passive-host-sniff` um Pipeline-Vergleich erweitern  
3. `bt-analysis-endpoint` / observe-proxy Cross-Refs + JSONL-Schema  
4. Geräteklasse → Capture-Pfad  
