# Project Inventory: esp32-car-network-refs

```yaml
project_id: esp32-car-network-refs
updated: 2026-11-12
reviewed_commit: "esp_wireguard@9217c5b esp32_nat_router@08da293 microlink@216da33"
profile: lab-tool
pilot_order: [esp-tailscale-client, esp-wireguard, esp-wifi-nat-router]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel | Aktion |
|--------|------|--------|
| ESP-IDF WireGuard Client + NAT keepalive | `esp-wireguard` | **neu** |
| SoftAP+STA NAT Lab-Router (+ optional WG) | `esp-wifi-nat-router` | **neu** |
| Tailscale-compat Rendezvous (WG+DERP+STUN) | `esp-tailscale-client` | **neu** |
| SoftAP+BT Coex C1 | — | **kein** Sheet `esp-wifi-bt-coex`; Hinweis + Cross-Ref `bt-dual-mode-coex` / Espressif coexist |
| USB↔WiFi Coex | `esp32-s3-usb-wifi-coex` | Abgrenzung (nicht SoftAP+BT) |
| Host Fritz/WG Adapter | `iobroker-fritzwireguard-adapter` | Kontrast (Host, nicht ESP) |

Kampagne: [esp32-car-network-2026-foreign](../../audits/esp32-car-network-2026-foreign/).

## Muster × Quelle

| Quelle @ pin | Muster | Hotspot/NAT | Car A6/B1 Rolle |
|--------------|--------|-------------|-----------------|
| esp_wireguard @ 9217c5b | WG Client Component | `persistent_keepalive`; Peer muss Endpoint erreichen oder NAT-Mapping halten | Baustein; allein kein Rendezvous |
| esp32_nat_router @ 08da293 | SoftAP+STA NAT (+ WG via `vpn_manager`) | Lab: ESP = AP oder STA; Portmap | Lab-AP gut; SoftAP+BT = C1 |
| microlink @ 216da33 | Tailscale-compat Client | DERP relay + STUN hinter Hotspot/CGNAT | **bevorzugtes** Rendezvous |

## Übersicht Sheets

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `esp-wireguard` | ESP WireGuard (IDF Component) | D | applied | partial | [SHEET](../../technologies/esp-wireguard/SHEET.md) | [app](applications/esp-wireguard.md) |
| `esp-wifi-nat-router` | ESP WiFi NAT Router (SoftAP+STA) | D | applied | partial | [SHEET](../../technologies/esp-wifi-nat-router/SHEET.md) | [app](applications/esp-wifi-nat-router.md) |
| `esp-tailscale-client` | ESP Tailscale-Compatible Client | D | applied | partial | [SHEET](../../technologies/esp-tailscale-client/SHEET.md) | [app](applications/esp-tailscale-client.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Lab Hotspot STA + DERP | Desk only | Lab Gate G-HOTSPOT |
| SoftAP+Classic BT Coex messbar | kein `esp-wifi-bt-coex` Sheet; C1 Desk | FOLLOW-ON / optional neues Sheet |
| bt-analyzer Integration | Upstream A6/B1 runbook | nach Lab-Rendezvous |

## Signale ohne Eintrag

- `esp-wifi-bt-coex` als eigener Slug — absichtlich nicht angelegt; Espressif C1 + `bt-dual-mode-coex` reichen für Desk-Gate  
