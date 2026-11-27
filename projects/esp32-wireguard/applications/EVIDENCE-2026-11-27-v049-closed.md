# Evidence: esp32.wireguard v0.4.9 transport closed + consumers

```yaml
date: 2026-11-27
project_id: esp32-wireguard
tech_slug: esp-wireguard
```

## FACT — Transportbasis abgeschlossen (esp32.wireguard 0.4.9)

| ID | Claim | Status |
|----|-------|--------|
| EVID-WG-2026-11-27-049 | Release v0.4.9; Hub bins `wireguard.0.4.9.esp32{,s3}.bin` | `FACT` |
| EVID-WG-2026-11-27-050 | Selective AllowedIPs + same-LAN route refuse | `FACT` (Lab) |
| EVID-WG-2026-11-27-051 | Guest/WAN/NAT → peer_is_up + Hub HTTP over WG | `FACT` (Lab) |
| EVID-WG-2026-11-27-052 | Reconnect + OTA-with-WG-config | `FACT` (Lab) |

## FACT — First consumer: hu-probe 0.3.42 (`feat/wireguard-transport`)

| ID | Claim | Status |
|----|-------|--------|
| EVID-HP-WG-2026-11-27-001 | `huprobe-s3` stub 0.3.41 vs `huprobe-s3-wg` 0.3.42 | `FACT` |
| EVID-HP-WG-2026-11-27-002 | WG default-off; MSC/session ohne WG OK | `FACT` |
| EVID-HP-WG-2026-11-27-003 | Guest → Fritz WAN → WG peer_up + Hub lastOk=1 | `FACT` |
| EVID-HP-WG-2026-11-27-004 | WG-Ausfall mid-session: Session bleibt aktiv | `FACT` |
| EVID-HP-WG-2026-11-27-005 | SNTP-Deferral + LOCK_TCPIP_CORE (kein Boot-Hang) | `FACT` |

Hub artifacts: `hu-probe.0.3.41.esp32s3.bin`, `hu-probe.0.3.42-wg.esp32s3.bin`.

## FACT — Second consumer scaffold: bt-analyzer 0.3.21-wg

| ID | Claim | Status |
|----|-------|--------|
| EVID-BT-WG-2026-11-27-001 | `analyzer-s3-wg` links stack; default `analyzer-s3` WG=0 / 0.3.20 | `FACT` (build) |
| EVID-BT-WG-2026-11-27-002 | Lab peer_up / guest E2E on analyzer | `UNKNOWN` (compile-only so far) |

Hub artifact: `bt-analyzer.0.3.21-wg.esp32s3.bin`.

## UNKNOWN (field)

- Langzeit im Fahrzeug / Mobilfunk-Roaming / reale HU-Bedingungen.
