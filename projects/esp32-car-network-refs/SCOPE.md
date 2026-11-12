# Project Scope: esp32-car-network-refs (Fremd)

```yaml
project_id: esp32-car-network-refs
title: ESP32 Car-Side Networking — Hotspot/NAT Outbound (Fremd)
updated: 2026-11-12
profile_hint: lab-tool
reviewed_commit: "esp_wireguard@9217c5b esp32_nat_router@08da293 microlink@216da33"
repos:
  - https://github.com/trombik/esp_wireguard
  - https://github.com/martin-ger/esp32_nat_router
  - https://github.com/CamM2325/microlink
status: active
```

## Zweck

Desk: wie ein ESP32 im Auto **outbound** über Phone-Hotspot/CGNAT erreichbar wird — Blocker für bt-analyzer car runbook **A6→B1**. Muster: WireGuard-Client-Komponente, SoftAP+STA NAT-Router (Lab), Tailscale-kompatibles Rendezvous (DERP/STUN).

## Systeme und Grenzen

| Quelle | Muster | Im Scope? |
|--------|--------|-----------|
| trombik/esp_wireguard @ 9217c5b | ESP-IDF WG Client: init/connect/set_default/disconnect; keepalive für NAT | ja |
| martin-ger/esp32_nat_router @ 08da293 | SoftAP+STA NAT; optional WG via `vpn_manager.c`; Portmap; UI `/vpn` | ja — Lab-AP, kein Car-Primärpfad |
| CamM2325/microlink @ 216da33 | Tailscale-compat: WG + DERP + STUN; failover; hotspot NAT traversal | ja — bevorzugtes A6/B1 Rendezvous |
| Espressif RF Coexistence (SoftAP+BT = C1) | SoftAP+BT/BLE performance unstable | ja — Gate/Hinweis; kein Sheet `esp-wifi-bt-coex` |
| bt-analyzer car A6/B1 | Reachability-Blocker-Kontext | Querverweis only |
| Offensive Bypass / Hotspot-Crack | — | **nein** |

## Nicht-Ziele

- Attack-/Bypass-How-tos (Hotspot, Carrier, VPN)
- Produktions-Firmware für bt-analyzer in diesem Desk
- SoftAP als alleiniges Car-Rendezvous (bewusst nachrangig)
- Host-Tailscale-Daemon-Betrieb (nur ESP-Client-Muster)
- USB↔WiFi Coex (`esp32-s3-usb-wifi-coex`) außer Abgrenzung

## Prioritäten

1. Sheets `esp-wireguard`, `esp-wifi-nat-router`, `esp-tailscale-client` (Primary **D**)  
2. Decision: Rendezvous (microlink) > SoftAP-Wait; WG allein braucht Endpoint/keepalive  
3. SoftAP+BT C1 Gate dokumentieren (kein `esp-wifi-bt-coex`-Sheet vorhanden)  
4. Evidence-Pins + C10–C13 in Audit

## Offene Scope-Fragen

- Lab: Hotspot STA + microlink DERP vs. reines WG keepalive — Messwerte offen  
- Coex-Matrix SoftAP+Classic BT auf Zielchip parallel zu Analyzer — FOLLOW-ON  
