# Evidence — esp32-car-network-2026-foreign

Desk 2026-11-12 · **standard_version 0.7.1** · Profile `lab-tool`. Keine Attack-/Bypass-Inhalte.

## WireGuard Component (trombik/esp_wireguard @ 9217c5b)

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-CARNET-2026-11-12-001` | API `esp_wireguard_init` / `connect` / `set_default` / `disconnect`; `wireguard_config_t` mit private_key, public_key, allowed_ip, endpoint, port (typ. 51820), `persistent_keepalive` für NAT | `FACT` | esp_wireguard@9217c5b README / headers |
| `EVID-CARNET-2026-11-12-002` | `esp_wireguard_connect` ESP_OK startet Handshake; Peer-up separat (`esp_wireguardif_peer_is_up` / peer_is_up); Zeit-Sync Voraussetzung | `FACT` | README usage |

## NAT Router (martin-ger/esp32_nat_router @ 08da293)

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-CARNET-2026-11-12-010` | SoftAP+STA NAT-Router; optional WireGuard via `vpn_manager.c` → `esp_wireguard_*`; Portmap; multi-target firmware; UI `/vpn` | `FACT` | esp32_nat_router@08da293 main/vpn_manager + wiki |

## Tailscale-Compatible Client (CamM2325/microlink @ 216da33)

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-CARNET-2026-11-12-020` | Tailscale-compat Client: WireGuard + DERP + STUN/DISCO; Docs `ARCHITECTURE.md`, `TAILSCALE_REFERENCE` | `FACT` | microlink@216da33 docs/ |
| `EVID-CARNET-2026-11-12-021` | Examples: `basic_connect`, `cellular_*`, failover | `FACT` | microlink@216da33 examples/ |
| `EVID-CARNET-2026-11-12-022` | Architektur geeignet für NAT-Traversal hinter Phone-Hotspot (Rendezvous via DERP wenn direct UDP blockiert) | `FACT` | ARCHITECTURE cellular/CGNAT + WiFi path |

## SoftAP + BT Coex Gate

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-CARNET-2026-11-12-030` | SoftAP connecting/connected × BT/BLE = Espressif **C1** (supported but unstable). KB hat **kein** Sheet `esp-wifi-bt-coex`; Cross-Ref `bt-dual-mode-coex` + Espressif RF Coexistence | `FACT` | Espressif coexist docs; KB inventory gap |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Lab: Hotspot STA + microlink → Peer erreichbar | `UNKNOWN` | G-HOTSPOT FOLLOW-ON |
| Lab: WG keepalive Intervall vs. Phone NAT | `UNKNOWN` | G-WG-KA |
| SoftAP+Classic BT messbar auf Zielchip | `UNKNOWN` | C1 Desk; Lab optional |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-11-12 | Fremd-Desk Pins → Sheets/Apps; Decision Rendezvous > SoftAP; Audit closed |
