# Evidence — bmw-bcl-rfcomm-role-2026-desk

Desk 2026-11-12 · **standard_version 0.7.1** · Pin: BimmerGestalt/BclCarLink @ `7cfd959`.

Focused RFCOMM-role delta. Framing/Handshake/SAS: CROSSREF only.

## BclCarLink @ `7cfd959`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BCLRF-2026-11-12-001` | Phone-App öffnet Bluetooth-Socket als RFCOMM **Client**: `device.createRfcommSocketToServiceRecord(SDP_BCL)` dann `socket.connect()` | `FACT` | [`BtConnection.kt`](https://github.com/BimmerGestalt/BclCarLink/blob/7cfd959/app/src/main/java/io/bimmergestalt/bcl/android/BtConnection.kt) `run` / `connectSocket` |
| `EVID-BCLRF-2026-11-12-002` | `SDP_BCL` = UUID `00001101-0000-1000-8000-00805F9B34FB` — Kommentar „Generic Serial Port“ (SPP) | `FACT` | `BtConnection.kt` companion `SDP_BCL` |
| `EVID-BCLRF-2026-11-12-003` | HU ist SDP-Provider / RFCOMM **Server**: aus Client-Connect-Pattern abgeleitet (App verbindet *zu* Device mit SPP UUID; kein Server-Listen-Code in BclCarLink) | `INFERENCE` | `BtConnection.kt` Client-only; `BtClientService.hasBCL` prüft Remote-UUIDs |
| `EVID-BCLRF-2026-11-12-004` | Watchdog: dest/port **5001**; Payload `0x13 0x37 0x13 0x37` (`0x13371337`); Interval **5000** ms; Timeout **20000** ms → `transport.shutdown()` | `FACT` | [`WatchdogProtocol.kt`](https://github.com/BimmerGestalt/BclCarLink/blob/7cfd959/app/src/main/java/io/bimmergestalt/bcl/protocols/WatchdogProtocol.kt) `WATCHDOG_PORT` / `WATCHDOG_DATA` / `WATCHDOG_INTERVAL` / `WATCHDOG_TIMEOUT` |
| `EVID-BCLRF-2026-11-12-005` | `BtClientService` nutzt **A2DP**-ProfileProxy Connected-Devices als Discovery-Hint; filtert `hasBCL()` (SPP UUID); startet `BtConnection` Threads | `FACT` | [`BtClientService.kt`](https://github.com/BimmerGestalt/BclCarLink/blob/7cfd959/app/src/main/java/io/bimmergestalt/bcl/android/BtClientService.kt) `a2dpListener` / `tryConnections` |

## CROSSREF (nicht neu)

| Thema | IDs / Ort |
|-------|-----------|
| BCL 8-Byte Header, dest 0x0FA4 Etch, Handshake | `EVID-BG-2026-10-28-*` · [`bimmergestalt-idrive-2026-foreign`](../bimmergestalt-idrive-2026-foreign/) |
| Watchdog dest 0x1389 / 5001 (Framing-Ebene) | `EVID-BG-2026-10-28-007` — Timing/Ping-Bytes hier vertieft (004) |
| SAS Auth Challenge/Response | [`bmw-connected-sas-auth-2026-11-06`](../bmw-connected-sas-auth-2026-11-06/) — **nicht duplizieren** |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| HU RFCOMM Server Channel-Nummer (z. B. 5) = OEM fest | `UNKNOWN` | Lab Dummy ≠ Field |
| HU Watchdog-Pong Byte-Layout | `UNKNOWN` | Client liest nur als Stream-Activity |
| A2DP Pflicht für BCL-Discovery auf allen HUs | `HYPOTHESIS` | Code-Pfad; Alternativen möglich |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-11-12 | Focused RFCOMM-role desk; Sheet `bmw-bcl` Fallstrick/FACT gewachsen |
