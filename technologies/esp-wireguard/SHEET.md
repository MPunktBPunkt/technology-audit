# Technology Sheet: ESP WireGuard (IDF Component)

```yaml
slug: esp-wireguard
title: ESP WireGuard (IDF Component)
primary: D
tags: [esp-idf, networking, vpn]
type: component
status: active
seen_in: [esp32-car-network-refs, esp32-wireguard, hu-probe, esp32-bt-analyzer]
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
  evidence_scope: [LAB, GENERAL]
pilot: audits/esp32-wireguard-2026-11-dod-close
```

Nur Ebene **A**. Projekt-/NAT-Lab → Application. Pin: trombik/esp_wireguard **v0.9.0**. Host-WG → `iobroker-fritzwireguard-adapter` (Kontrast).

Referenz-Firmware **esp32.wireguard v0.4.9** — **Lab Transport-DoD geschlossen** (Core, Data Plane, Recovery, OTA). Consumer Lab-E2E: hu-probe **0.3.42-wg**, bt-analyzer **0.3.21-wg**. Abschlussaudit: `audits/esp32-wireguard-2026-11-dod-close/`.

## Kurzfassung

ESP-IDF-/Arduino-vendored Client für einen **WireGuard-Tunnel** über lwIP/esp-netif: `esp_wireguard_init` → `connect` → selektives Routing (kein Full-Tunnel-Default) → `disconnect`. Hinter NAT: `persistent_keepalive`. `connect`/`ESP_OK` startet nur den Handshake — **Peer-up** ist separat (`peer_is_up`). Zeit: SNTP vor Handshake.

## Abgrenzung

- **Ist:** Embedded WG Client, selektive AllowedIPs, NAT-Keepalive, optionaler Overlay (keine harte App-Abhängigkeit).
- **Ist nicht:** SoftAP/NAT-Router (`esp-wifi-nat-router`); Tailscale/DERP (`esp-tailscale-client`); Host-`wg-quick`; automatischer WiFi-Failover (WLAN-Ebene).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | WiFi/ETH + esp-netif / lwIP | Working IF Voraussetzung |
| API | init / connect / disconnect / peer_is_up | Context `wireguard_ctx_t` |
| Config | keys, Address, AllowedIPs, Endpoint, keepalive | Full-tunnel `0.0.0.0/0` ablehnen |
| Status | peer_is_up + optional TX/RX | ≠ connect return |
| Zeit | SNTP | Library sync’t nicht |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| `esp_wireguard_connect` ESP_OK = Tunnel up | `REJECTED` | peer_is_up separat pollen |
| Hinter NAT ohne keepalive stabil | `REJECTED` | persistent_keepalive setzen |
| Component sync’t Zeit selbst | `REJECTED` | SNTP-Gate |
| WG allein = Rendezvous hinter CGNAT ohne Endpoint | `REJECTED` | Endpoint muss erreichbar sein |
| Same-LAN STA + AllowedIPs = sichere Default-Route | `REJECTED` | blackhole — route refuse |
| Port immer beliebig | `HYPOTHESIS` | Desk-Default oft 51820 |

## Transfer

Überall, wo ESP outbound einen festen WG-Peer braucht (selektives Heimnetz). Optionaler Overlay: Consumer-Funktion (MSC/BT) darf bei WG-DOWN weiterlaufen. Nächster Kandidat mit konkretem Use-Case: **esp32.pidrive** — erst Readiness-Audit (Verkehr/Ziele), nicht Copy-Paste.

### Projektstart-Checkliste

- [ ] Sheet gelesen (Abgrenzung + Fallstricke)
- [ ] Endpoint/NAT-Keepalive entschieden
- [ ] SNTP-Pfad geplant
- [ ] peer_is_up Observability
- [ ] Selective AllowedIPs; same-LAN refuse bedacht
- [ ] Compile-Gate + default-off
- [ ] Application + `seen_in`

## Referenzen

- https://github.com/trombik/esp_wireguard (pin v0.9.0)
- https://github.com/MPunktBPunkt/esp32.wireguard (v0.4.9)
- Related: `esp-wifi-nat-router`, `esp-tailscale-client`, `esp-hub-base-template`

## Offene Fragen

- Natürlicher WiFi-Failover (Multi-AP ohne Lab-Kommando) — Lab/Feld
- Keepalive vs. Carrier/Phone NAT timers (Feintuning)
- Feld: Langzeit / Roaming / Fahrzeug
