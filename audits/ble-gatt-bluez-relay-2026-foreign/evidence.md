# Evidence — ble-gatt-bluez-relay-2026-foreign

Desk 2026-11-12 · **standard_version 0.7.1** · Pins: BluetoothInterceptor@`4a10bcf`, bluez_peripheral@`8174c15`.

Offensive Repo (BluetoothInterceptor): **nur Architektur-Claims**. Keine Attack-Schritte.

## BluetoothInterceptor @ `4a10bcf`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BZGATT-2026-11-12-001` | `connect_target(adapter, addr)` verbindet als **Central**; `build_clone(..., clone_adapter, ...)` registriert GATT Application + Advertisement auf **zweitem** Adapter als **Peripheral** | `FACT` | [`src/proxy.rs`](https://github.com/BrentWebEU/BluetoothInterceptor/blob/4a10bcf/src/proxy.rs) `connect_target` / `build_clone` · [`README.md`](https://github.com/BrentWebEU/BluetoothInterceptor/blob/4a10bcf/README.md) `--target-adapter` / `--clone-adapter` |
| `EVID-BZGATT-2026-11-12-002` | Per-Char: `CharacteristicRead` / `CharacteristicWriteMethod::Fun` / `CharacteristicNotifyMethod::Fun` forwarden zu remote; `pump_notify` subscribed upstream lazy und pusht Bytes downstream | `FACT` | `proxy.rs` Read/Write/Notify closures · `pump_notify` |
| `EVID-BZGATT-2026-11-12-003` | CCCD / Notify-Subscription lokal über BlueZ `CharacteristicNotify`; `--clone-descriptors` default **off** (optionale Descriptor-Read-Forward) | `FACT` | `proxy.rs` Notify Fun · [`README`](https://github.com/BrentWebEU/BluetoothInterceptor/blob/4a10bcf/README.md) CLI `--clone-descriptors` · [`main.rs`](https://github.com/BrentWebEU/BluetoothInterceptor/blob/4a10bcf/src/main.rs) `cli.clone_descriptors` |
| `EVID-BZGATT-2026-11-12-004` | Services `0x1800` (GAP) / `0x1801` (GATT) werden übersprungen — BlueZ reserved | `FACT` | `proxy.rs` skip `0x1800 \| 0x1801` |
| `EVID-BZGATT-2026-11-12-005` | Zwei Adapter stark empfohlen; Tool warnt wenn target==clone; Two-HCI ≠ on-chip Dual-Role | `FACT` | [`DESIGN.md`](https://github.com/BrentWebEU/BluetoothInterceptor/blob/4a10bcf/DESIGN.md) §4 · README „Two Bluetooth adapters strongly recommended“ |
| `EVID-BZGATT-2026-11-12-006` | bluer: beide Rollen existieren; Concurrent Central+Peripheral auf **einem** Controller = controller-dependent / unreliable in practice | `FACT` (DESIGN) | DESIGN.md §4 „Two adapters“ |
| `EVID-BZGATT-2026-11-12-007` | `EventBus` / `RelayEvent` loggt Read/Write/Notify mit **plaintext hex** (console + optional TCP stream) — Analyse-Observability | `FACT` | [`src/event.rs`](https://github.com/BrentWebEU/BluetoothInterceptor/blob/4a10bcf/src/event.rs) `Op::{Read,Write,Notify}` · `spawn_console_logger` · `serve_stream` |

## bluez_peripheral @ `8174c15`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BZGATT-2026-11-12-010` | Python BlueZ GATT **Peripheral** API: `Advertisement`, `Service`, `Characteristic`, `Agent` — Building Block, **kein** Central/Relay | `FACT` | [`README.md`](https://github.com/spacecheese/bluez_peripheral/blob/8174c15/README.md) · [`advert.py`](https://github.com/spacecheese/bluez_peripheral/blob/8174c15/bluez_peripheral/advert.py) · [`gatt/service.py`](https://github.com/spacecheese/bluez_peripheral/blob/8174c15/bluez_peripheral/gatt/service.py) · [`gatt/characteristic.py`](https://github.com/spacecheese/bluez_peripheral/blob/8174c15/bluez_peripheral/gatt/characteristic.py) · [`agent.py`](https://github.com/spacecheese/bluez_peripheral/blob/8174c15/bluez_peripheral/agent.py) |

## CROSSREF (nicht neu auditiert)

| Claim | Status | Quelle |
|-------|--------|--------|
| ifit Interceptor / FTMS semantic | Prior FACT | `EVID-BLEBR-2026-10-28-021`–`023` in [`ble-gatt-bridge-refs-2026-foreign`](../ble-gatt-bridge-refs-2026-foreign/evidence.md) |
| btlejuice 2-HCI transparent | Prior FACT | `EVID-BLEBR-2026-10-28-060`/`061` |
| Zwei-HCI = on-chip Dual-Role | Prior `REJECTED` | Sheet `ble-gatt-dual-role`; verstärkt durch 005/006 |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| bluer Concurrent Dual-Role auf spezifischem USB-Dongle stabil | `UNKNOWN` | DESIGN open Q1 → Lab |
| BD_ADDR Clone auf Clone-Adapter unter BlueZ | `UNKNOWN` hier | → Pack B `bt-bdaddr-rewrite` |
| Notify-Backpressure best practice (tokio) | `UNKNOWN` | DESIGN open Q3 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-11-12 | Desk BlueZ/bluer delta; Sheets Transparent/Dual-Role gewachsen |
