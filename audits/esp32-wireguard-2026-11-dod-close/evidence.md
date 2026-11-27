# Evidence: WireGuard DoD close-out (Lab 2026-11-27)

```yaml
audit_id: esp32-wireguard-2026-11-dod-close
environment: lab
dut:
  - esp32 .131 / .87 (referenz wireguard FW)
  - esp32-s3 .88 (hu-probe 0.3.42-wg; bt-analyzer 0.3.21-wg)
endpoint: "Fritz!Box WAN 84.164.233.124:58187"
```

## 1. Core — esp32.wireguard v0.4.9

| ID | Claim | Status |
|----|-------|--------|
| EVID-WG-2026-11-27-049 | Release v0.4.9; Hub bins esp32 + esp32s3 | `FACT` |
| EVID-WG-2026-11-27-060 | Vendored trombik/esp_wireguard **v0.9.0** (nicht Stub) | `FACT` |
| EVID-WG-2026-11-27-061 | NVS/Storage-Blob + Config API | `FACT` |
| EVID-WG-2026-11-27-062 | SNTP/Zeit-Gate vor Handshake | `FACT` |
| EVID-WG-2026-11-27-063 | `connect` ESP_OK ≠ `peer_is_up` (separat pollen) | `FACT` / sheet `REJECTED` opposite |

## 2. Data Plane

| ID | Claim | Status |
|----|-------|--------|
| EVID-WG-2026-11-27-050 | Selektive AllowedIPs; same-LAN route refuse | `FACT` |
| EVID-WG-2026-11-27-051 | Guest/WAN/NAT → peer_is_up + Hub HTTP über WG | `FACT` |
| EVID-WG-2026-11-27-064 | TX/RX-Counter bewegen sich unter Traffic | `FACT` |
| EVID-WG-2026-11-27-065 | Full-tunnel `0.0.0.0/0` abgelehnt | `FACT` (policy) |

## 3. Recovery

| ID | Claim | Status |
|----|-------|--------|
| EVID-WG-2026-11-27-052a | WLAN-Wechsel (Heim↔Gast/Hotspot) + WG reconnect | `FACT` |
| EVID-WG-2026-11-27-066 | Natürlicher WiFi-Failover (unattended Multi-AP) | **`UNKNOWN`** |
| EVID-HP-WG-2026-11-27-004 | WG-Ausfall mid-session: MSC/Session bleibt aktiv | `FACT` (hu-probe) |

## 4. OTA

| ID | Claim | Status |
|----|-------|--------|
| EVID-WG-2026-11-27-052 | OTA über aktiven WG-Tunnel | `FACT` |
| EVID-WG-2026-11-27-067 | WG-NVS/Config nach OTA erhalten | `FACT` |

## 5. Consumer — hu-probe 0.3.42-wg

| ID | Claim | Status |
|----|-------|--------|
| EVID-HP-WG-2026-11-27-001 | Stub 0.3.41 vs WG-Build 0.3.42 | `FACT` |
| EVID-HP-WG-2026-11-27-002 | WG default-off; MSC ohne WG OK | `FACT` |
| EVID-HP-WG-2026-11-27-003 | Guest → Fritz → WG → Hub lastOk=1 | `FACT` |
| EVID-HP-WG-2026-11-27-005 | SNTP-Deferral + LOCK_TCPIP_CORE | `FACT` |

## 6. Consumer — bt-analyzer 0.3.21-wg

| ID | Claim | Status |
|----|-------|--------|
| EVID-BT-WG-2026-11-27-001 | `analyzer-s3` WG-off 0.3.20; `analyzer-s3-wg` 0.3.21 | `FACT` |
| EVID-BT-WG-2026-11-27-002 | Guest → WAN → `peer_up=1` | `FACT` |
| EVID-BT-WG-2026-11-27-003 | Selektive `/24` auf Gast-STA | `FACT` |
| EVID-BT-WG-2026-11-27-004 | Hub HB über WG (`[HB] → .113:8093`) | `FACT` |

## Nicht mehr offen (Lab)

AllowedIPs · WAN · NAT · Handshake · peer_is_up · echter Tunnel-Traffic · Consumer-E2E (beide).

## UNKNOWN (bewusst)

- Natürlicher WiFi-Failover (ohne Lab-`LAB WIFI`)
- Feld: Langzeit, Mobilfunk-Roaming, reale Fahrzeug-Bedingungen
- Carrier/Phone NAT keepalive-Feintuning jenseits Keepalive=25 Lab
