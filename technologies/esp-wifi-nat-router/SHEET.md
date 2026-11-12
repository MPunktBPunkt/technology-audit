# Technology Sheet: ESP WiFi NAT Router (SoftAP+STA)

```yaml
slug: esp-wifi-nat-router
title: ESP WiFi NAT Router (SoftAP+STA)
primary: D
tags: [esp-idf, networking, vpn]
type: implementation
status: active
seen_in: [esp32-car-network-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/esp32-car-network-2026-foreign
```

Nur Ebene **A**. Lab-Firmware-Muster (martin-ger/esp32_nat_router). WG-Baustein → `esp-wireguard`. SoftAP+BT Coex: Espressif **C1** — **kein** Sheet `esp-wifi-bt-coex` in der KB; siehe `bt-dual-mode-coex` + Espressif coexist docs.

## Kurzfassung

Firmware-Muster: ESP32 als **WiFi NAT-Router** zwischen SoftAP-Clients und STA/ETH-Uplink, optional mit WireGuard-Upstream (`vpn_manager` → `esp_wireguard_*`), Portmap und Web-UI. Primär **Lab-AP / Bench-Uplink**, nicht Car-Rendezvous hinter Hotspot.

## Abgrenzung

- **Ist:** SoftAP+STA NAT, Portmap, optional WG-Client-Uplink, Multi-Target-Firmware.
- **Ist nicht:** Tailscale/DERP (`esp-tailscale-client`); reiner WG-Component ohne SoftAP (`esp-wireguard`); USB↔WiFi Coex (`esp32-s3-usb-wifi-coex`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| AP-Seite | SoftAP + DHCP/NAT | Clients hinter ESP |
| Uplink | STA oder ETH | Internet / Lab-LAN |
| optional VPN | `vpn_manager` → esp_wireguard | UI `/vpn`, keepalive, port 51820 |
| lateral RF | SoftAP + BT/BLE | Espressif C1 unstable |
| Ops | Portmap, CLI, Web UI | Lab-Convenience |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| SoftAP+BT/BLE connecting/connected = stabil | `REJECTED` | Espressif coexist: **C1** |
| SoftAP-Wait = bestes Car-Rendezvous | `REJECTED` | Desk: microlink/DERP bevorzugen |
| Optional WG ersetzt NAT-Traversal-Rendezvous | `REJECTED` | WG braucht Endpoint/keepalive; SoftAP ändert Hotspot-Problem nicht |
| nat_router = esp_wireguard API selbst | `REJECTED` | Wrapper; Component darunter |
| USB-WiFi-Coex-Sheet deckt SoftAP+BT ab | `REJECTED` | anderes Problem (`esp32-s3-usb-wifi-coex`) |

## Transfer

Lab: schnelles NAT-AP + Portmap + optional WG. Car/Analyzer: SoftAP+BT nur mit C1-Gate; Reachability → `esp-tailscale-client`.

### Projektstart-Checkliste

- [ ] Lab vs. Car-Rolle klar (Lab-AP ≠ Rendezvous)
- [ ] SoftAP+BT nötig? → C1 Gate / Coex-Plan
- [ ] WG optional: `esp-wireguard` Sheet + keepalive
- [ ] Application + `seen_in`

## Referenzen

- https://github.com/martin-ger/esp32_nat_router (pin in Audit)
- Espressif RF Coexistence: SoftAP × BT/BLE = C1
- Related: `esp-wireguard`, `bt-dual-mode-coex`

## Offene Fragen

- Eigenes Sheet `esp-wifi-bt-coex` lohnt sich erst bei SoftAP+BT Produktivpfad?
