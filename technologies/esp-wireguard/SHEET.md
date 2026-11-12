# Technology Sheet: ESP WireGuard (IDF Component)

```yaml
slug: esp-wireguard
title: ESP WireGuard (IDF Component)
primary: D
tags: [esp-idf, networking, vpn]
type: component
status: active
seen_in: [esp32-car-network-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/esp32-car-network-2026-foreign
```

Nur Ebene **A**. Projekt-/NAT-Lab → Application. Pin-Referenz: trombik/esp_wireguard. Host-WG → `iobroker-fritzwireguard-adapter` (Kontrast).

## Kurzfassung

ESP-IDF-Komponente für einen **WireGuard-Client-Tunnel** über lwIP/esp-netif: `esp_wireguard_init` → `connect` → optional `set_default` → `disconnect`. Hinter NAT/`stateful firewall` ist `persistent_keepalive` erforderlich. `connect`/`ESP_OK` startet nur den Handshake — **Peer-up** ist separat (`peer_is_up`).

## Abgrenzung

- **Ist:** Embedded WG Client API, Config-Struct, NAT-Keepalive-Semantik.
- **Ist nicht:** SoftAP/NAT-Router (`esp-wifi-nat-router`); Tailscale/DERP-Rendezvous (`esp-tailscale-client`); Host-`wg-quick`; Krypto-Spec.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | WiFi/ETH + esp-netif / lwIP | Working IF Voraussetzung |
| API | init / connect / set_default / disconnect | Context `wireguard_ctx_t` |
| Config | `wireguard_config_t` | keys, allowed_ip, endpoint, port (51820), keepalive |
| Status | peer_is_up | ≠ connect return |
| Zeit | SNTP/Wall clock | beide Peers synced; Library sync’t nicht |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| `esp_wireguard_connect` ESP_OK = Tunnel up | `REJECTED` | peer_is_up separat pollen |
| Hinter NAT ohne keepalive stabil | `REJECTED` | README: persistent_keepalive setzen |
| Component sync’t Zeit selbst | `REJECTED` | Voraussetzung synced clocks |
| WG allein = Rendezvous hinter CGNAT ohne erreichbaren Endpoint | `REJECTED` | Endpoint muss erreichbar sein oder Mapping halten; sonst DERP-Muster |
| Port immer beliebig | `HYPOTHESIS` | Desk-Default 51820 |

## Transfer

Überall, wo ESP outbound einen festen WG-Peer braucht (Lab-VPN, selektive Tunnel-IP). Für Phone-Hotspot-Reachability ohne öffentlichen Endpoint → `esp-tailscale-client`. Für Lab SoftAP+NAT mit optionalem WG → `esp-wifi-nat-router`.

### Projektstart-Checkliste

- [ ] Sheet gelesen (Abgrenzung + Fallstricke)
- [ ] Endpoint-Erreichbarkeit / NAT-Keepalive entschieden
- [ ] Zeit-Sync-Pfad (SNTP) geplant
- [ ] peer_is_up Observability, nicht nur connect-Return
- [ ] Application + `seen_in`

## Referenzen

- https://github.com/trombik/esp_wireguard (pin in Audit)
- WireGuard protocol (wireguard.com)
- Related: `esp-wifi-nat-router`, `esp-tailscale-client`

## Offene Fragen

- Empfohlenes keepalive-Intervall vs. typische Carrier/Phone NAT timers (Lab)?
