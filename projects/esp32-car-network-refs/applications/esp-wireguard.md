# Project Application: esp-wireguard in esp32-car-network-refs

```yaml
project_id: esp32-car-network-refs
tech_slug: esp-wireguard
status: active
sheet: ../../../technologies/esp-wireguard/SHEET.md
audit: ../../../audits/esp32-car-network-2026-foreign/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt

ESP-IDF **WireGuard-Client-Baustein** hinter Phone-Hotspot/NAT: Tunnel aufbauen, Default-Route setzen, Keepalive gegen NAT-Timeout. Allein kein Car-Rendezvous — braucht erreichbaren Peer-Endpoint oder Mapping-Erhalt.

## Architektur / Datenfluss

```text
WiFi STA (Phone Hotspot)
  → lwIP / esp-netif
  → esp_wireguard_init / connect [/ set_default]
  → UDP :51820 → Peer Endpoint
  → peer_is_up? (≠ connect ESP_OK)
```

## Relevante Pfade

| Pfad (Ursprungsrepo @ 9217c5b) | Rolle |
|--------------------------------|------|
| `include/esp_wireguard.h` | API: init / connect / set_default / disconnect |
| `wireguard_config_t` | private_key, public_key, allowed_ip, endpoint, port, persistent_keepalive |
| README usage | NAT-Hinweis: keepalive setzen; peer_is_up separat pollen |

## Konfiguration und Parameter

| Key | Desk-Fakt | Hinweis |
|-----|-----------|---------|
| `port` | typ. 51820 | Peer-UDP |
| `persistent_keepalive` | default off; bei NAT setzen (z. B. 10 s) | `EVID-CARNET-2026-11-12-001` |
| `esp_wireguard_connect` ESP_OK | Start Handshake, nicht „Tunnel up“ | `…-002` |
| `esp_wireguardif_peer_is_up` / peer_is_up | separates Up-Kriterium | `…-002` |
| Zeit-Sync | beide Peers brauchen synchrone Zeit | Library sync’t nicht |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Component API init/connect/set_default/disconnect + config fields | `EVID-CARNET-2026-11-12-001` | `FACT` |
| connect ESP_OK ≠ peer up; peer_is_up separat | `EVID-CARNET-2026-11-12-002` | `FACT` |
| Keepalive nötig hinter Hotspot-NAT (Lab) | — | `UNKNOWN` (Lab) |

## Offene Fragen

- Welches Keepalive-Intervall stabil gegen typische Phone-NAT-Timeouts?
- set_default vs. selektive AllowedIPs für Analyzer-Traffic only?

## Verwandte Applications / Methods

- [esp-wifi-nat-router](esp-wifi-nat-router.md) — nutzt esp_wireguard unter der Haube  
- [esp-tailscale-client](esp-tailscale-client.md) — Rendezvous über DERP statt purem Endpoint  
