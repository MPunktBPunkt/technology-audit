# Evidence — ble-gatt-bridge-refs-2026-foreign

Desk 2026-10-28 · **standard_version 0.7.1** · Pins siehe Kampagne YAML.

Offensive Repos (ChimeraBLE, btlejuice, ifit Interceptor): **nur Architektur-Claims**. Keine Attack-Schritte.

## ChimeraBLE @ `2330423`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BLEBR-2026-10-28-001` | Dual-Role MITM; NimBLE MAX_CONNECTIONS=3 Kommentar | `FACT` | [`platformio.ini`](https://github.com/MatthewKuKanich/ChimeraBLE/blob/2330423/platformio.ini) · [`mitm.cpp`](https://github.com/MatthewKuKanich/ChimeraBLE/blob/2330423/src/mitm.cpp) |
| `EVID-BLEBR-2026-10-28-002` | `wireRelays` subscribed **alle** Notify/Indicate am Target; Host `onSubscribe` loggt nur | `FACT` | `mitm.cpp` `wireRelays` / `MirrorCharCb::onSubscribe` |
| `EVID-BLEBR-2026-10-28-003` | `relayNotify` Byte-Passthrough Target→Mirror `notify()` | `FACT` | `mitm.cpp` `relayNotify` |
| `EVID-BLEBR-2026-10-28-004` | Target-Reconnect + re-`wireRelays` in `loopTick` | `FACT` | `mitm.cpp` `loopTick` |

## iFitnessProxy @ `1c24f58`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BLEBR-2026-10-28-010` | Dual-Role; `CONFIG_BT_NIMBLE_MAX_CONNECTIONS=2` | `FACT` | [`platformio.ini`](https://github.com/jesusbotella/iFitnessProxy/blob/1c24f58/platformio.ini) |
| `EVID-BLEBR-2026-10-28-011` | Semantic: parse FTMS `0x2AD2` → `sendCpsMeasurement` CPS `0x1818` | `FACT` | [`main.cpp`](https://github.com/jesusbotella/iFitnessProxy/blob/1c24f58/src/main.cpp) `parseFtmsIndoorBikeData` / `sendCpsMeasurement` |
| `EVID-BLEBR-2026-10-28-012` | Bike-Subscribe einmalig; Watch-Notify gated `watchConnected` | `FACT` | `main.cpp` subscribe + `sendCpsMeasurement` |

## ifit @ `d29ca88`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BLEBR-2026-10-28-021` | FTMS Control Point Write + Indicate Result; Opcode-Handler | `FACT` | [`_server.py`](https://github.com/ianchi/ifit/blob/d29ca88/ifit/ftms/_server.py) ControlPoint handlers |
| `EVID-BLEBR-2026-10-28-022` | `_notify_loop` pollt iFit Reads → FTMS Notify (kein Upstream-Notify-Zwang) | `FACT` | `_server.py` `_notify_loop` |
| `EVID-BLEBR-2026-10-28-023` | Interceptor: custom RX notify passthrough + TX framing (Architektur) | `FACT` | `ifit/interceptor/_discovery.py` |

## esp32-ble2mqtt @ `e66ec5a`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BLEBR-2026-10-28-030` | GATTS disabled — Central-only | `FACT` | [`sdkconfig.defaults`](https://github.com/shmuelzon/esp32-ble2mqtt/blob/e66ec5a/sdkconfig.defaults) |
| `EVID-BLEBR-2026-10-28-031` | Notify-Register + CCCD-Write queued; MTU req on connect | `FACT` | [`ble.c`](https://github.com/shmuelzon/esp32-ble2mqtt/blob/e66ec5a/main/ble.c) |

## BleRemoteBrideg @ `958da7c`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BLEBR-2026-10-28-040` | Dual-Role + FSM `IDLE…DISCOVERING…READY…BACKOFF` | `FACT` | [`rc003_client.cpp`](https://github.com/QYHHHH/BleRemoteBrideg/blob/958da7c/firmware/MiRemoteBridge/rc003_client.cpp) `enum class St` |
| `EVID-BLEBR-2026-10-28-041` | Semantic HID map + `subscribeNative` CCCD | `FACT` | `bridge.cpp` · `native_subscription.cpp` · `rc003_client.cpp` |

## esp32-ble-uart-mx @ `3451904`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BLEBR-2026-10-28-050` | Dual-Role + `MAX_PEERS` Multi-Connection | `FACT` | [`README`](https://github.com/olegv142/esp32-ble-uart-mx/blob/3451904/README.md) · [`mx_config.h`](https://github.com/olegv142/esp32-ble-uart-mx/blob/3451904/src/mx_config.h) |
| `EVID-BLEBR-2026-10-28-051` | Transparent Service `FFE0` | `FACT` | `mx_config.h` `SERVICE_UUID` |

## btlejuice @ `981b2e3`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BLEBR-2026-10-28-060` | Proxy (noble Central) + FakeDevice (bleno Peripheral) — 2 HCI | `FACT` | [`proxy.js`](https://github.com/DigitalSecurity/btlejuice/blob/981b2e3/proxy.js) · [`fake.js`](https://github.com/DigitalSecurity/btlejuice/blob/981b2e3/fake.js) |
| `EVID-BLEBR-2026-10-28-061` | `setGattHandlers` read/write/notify relay; optional `keepHandles` | `FACT` | `proxy.js` · `fake.js` |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Classic ESP32 Dual-Role ≥2 Peripheral stabil | `UNKNOWN` | Gate |
| CPS Watch-Akzeptanz synthetischer Crank-Felder | `HYPOTHESIS` | iFitnessProxy ungetestet hier |
| Notify-Congestion-Policy best practice | `UNKNOWN` | kein Fremd-Vorbild stark |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-28 | Multi-Repo Desk; Pattern-Sheets Dual/Transparent/Semantic |
