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

## FACT — Second consumer: bt-analyzer 0.3.21-wg (Lab E2E 2026-11-27)

| ID | Claim | Status |
|----|-------|--------|
| EVID-BT-WG-2026-11-27-001 | `analyzer-s3-wg` links stack; default `analyzer-s3` WG=0 / 0.3.20 | `FACT` (build) |
| EVID-BT-WG-2026-11-27-002 | Lab `.88` guest WAN → Fritz → WG `peer_up=1` | `FACT` |
| EVID-BT-WG-2026-11-27-003 | Selective `/24` route on guest (`192.168.179.3`) | `FACT` |
| EVID-BT-WG-2026-11-27-004 | Hub heartbeat over WG from guest (`[HB] -> …113:8093`) | `FACT` |

Hub artifact: `bt-analyzer.0.3.21-wg.esp32s3.bin`.

Two independent consumers of esp32.wireguard **0.4.9** now Lab-validated: hu-probe **0.3.42**, bt-analyzer **0.3.21**.

## UNKNOWN (bewusst)

- Natürlicher WiFi-Failover (unattended Multi-AP) — `EVID-WG-2026-11-27-066`
- Feld: Langzeit / Mobilfunk-Roaming / reale Fahrzeug-Bedingungen
- Carrier/Phone NAT keepalive-Feintuning jenseits Keepalive=25 Lab

Abschlussaudit: [`../../../audits/esp32-wireguard-2026-11-dod-close/`](../../../audits/esp32-wireguard-2026-11-dod-close/).
