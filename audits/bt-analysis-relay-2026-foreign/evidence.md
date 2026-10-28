# Evidence — bt-analysis-relay-2026-foreign

Desk 2026-10-28 · **standard_version 0.7.1**. Offensive MITM nur Architektur.

## Observe / Transparent

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTAR-2026-10-28-001` | Chimera `relayNotify` + UART hex fields in `log.cpp` | `FACT` | ChimeraBLE@2330423 `mitm.cpp` / `log.cpp` |
| `EVID-BTAR-2026-10-28-002` | Host CCCD `onSubscribe` log-only; Target auto-subscribed in `wireRelays` | `FACT` | `mitm.cpp` |
| `EVID-BTAR-2026-10-28-010` | ble2mqtt publishes GATT values to MQTT (Central-only, GATTS off) | `FACT` | esp32-ble2mqtt@e66ec5a `ble2mqtt.c` / `sdkconfig.defaults` |
| `EVID-BTAR-2026-10-28-020` | uart-mx Dual-Role + Serial forward observability | `FACT` | esp32-ble-uart-mx@3451904 |
| `EVID-BTAR-2026-10-28-021` | btlejuice 2-HCI proxy architecture (Host-Kontrast) | `FACT` | btlejuice@981b2e3 `proxy.js`/`fake.js` |

## Endpoint

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BTAR-2026-10-28-030` | a2dpSinkHfpClient logs HFP call/audio as HF Endpoint | `FACT` | a2dpSinkHfpClient@df6c5f4 `bt_app_hf.c` |
| `EVID-BTAR-2026-10-28-031` | Classic-only + BLE mem_release — kein Dual-Link MITM | `FACT` | `a2dpSinkHfpHf.c` |
| `EVID-BTAR-2026-10-28-040` | EspBle Classic HFP/SPP/HID endpoint surface | `FACT` | EspBle@ef09bed |
| `EVID-BTAR-2026-10-28-050` | bthidbridge HOGP↔Classic forward (Cross-Transport) | `FACT` | esp32-bthidbridge@5d3a563 |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Lab Capture Phone↔Watch mit Observe-Proxy | `UNKNOWN` | FOLLOW-ON |
| Auto proprietäre SDP/GATT Extensions | `UNKNOWN` | |
| LE Secure Connections Relais mit eigenen Bonds stabil | `HYPOTHESIS` | Gate |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-28 | Bridge + Classic Gaps Desk → Analyse-Relais Synthese |
