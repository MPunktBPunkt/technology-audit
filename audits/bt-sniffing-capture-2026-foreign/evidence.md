# Evidence — bt-sniffing-capture-2026-foreign

Desk 2026-10-28 · **standard_version 0.7.1**.

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTSC-2026-10-28-001` | Adv→JSON; MQTT/Serial queues size 16; `dropped_mqtt`/`dropped_adv` status | `FACT` | [esp32-ble-scan-mqtt@ee096de](https://github.com/wiredlab/esp32-ble-scan-mqtt/tree/ee096de) `formatAdvertisementJson`, `pub_status_mqtt` |
| `EVID-BTSC-2026-10-28-010` | GATT→MQTT publish (Central-only) | `FACT` | esp32-ble2mqtt@e66ec5a |
| `EVID-BTSC-2026-10-28-020` | Adv→synthetic PCAP SD DLT 251; no TCP | `FACT` | CapibaraZero/BLESniffer@1bea2e8 |
| `EVID-BTSC-2026-10-28-030` | Classic active sniffer UART→Host PCAPNG | `FACT` | Matheus-Garbelini/esp32_bluetooth_classic_sniffer@0e174ca |
| `EVID-BTSC-2026-10-28-040` | Host hub Serial→PCAP/Wireshark pipe; optional LTK decrypt | `FACT` | homewsn/bsniffhub@29049d7 |
| `EVID-BTSC-2026-10-28-050` | Chimera Serial hex GATT dump/notify log | `FACT` | ChimeraBLE@2330423 |
| `EVID-BTSC-2026-10-28-060` | a2dpSink HFP/A2DP endpoint logs; no TCP export SoT | `FACT` | a2dpSinkHfpClient@df6c5f4 |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Eidolon öffentliches HFP-TCP-Repo | `UNKNOWN` | Search leer |
| Lab ESP→TCP:9000→Debian JSONL | `UNKNOWN` | FOLLOW-ON |
| A2DP Media-Frames über TCP sinnvoll | `HYPOTHESIS` | Metadata priorisieren |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-28 | Analyse-Relais Desk → Capture-Pipeline Nachzug |
