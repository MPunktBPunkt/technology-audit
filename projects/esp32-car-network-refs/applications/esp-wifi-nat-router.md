# Project Application: esp-wifi-nat-router in esp32-car-network-refs

```yaml
project_id: esp32-car-network-refs
tech_slug: esp-wifi-nat-router
status: active
sheet: ../../../technologies/esp-wifi-nat-router/SHEET.md
audit: ../../../audits/esp32-car-network-2026-foreign/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

**Lab SoftAP+STA NAT-Router** (martin-ger): schnelles Bench-Uplink / Portmap / optional WireGuard über `vpn_manager.c` → `esp_wireguard_*`. Für Car-Analyzer **nicht** Primär-Rendezvous — SoftAP+BT/BLE ist Espressif **C1** (unstable). Gut als Lab-AP und WG-Integrationsreferenz.

## Architektur / Datenfluss

```text
[Clients] ↔ SoftAP ──NAT── STA/ETH uplink
                              │
                    optional vpn_manager
                              │
                    esp_wireguard_* → Peer :51820
```

## Relevante Pfade

| Pfad (Ursprungsrepo @ 08da293) | Rolle |
|--------------------------------|------|
| SoftAP + STA NAT core | Lab-Router |
| `main/vpn_manager.c` | WG connect/disconnect wrapper um esp_wireguard_* |
| Web UI `/vpn` | Config / import `.conf` |
| Portmap / multi-target firmware | Lab Port-Forward |

## Konfiguration und Parameter

| Key | Desk-Fakt | Hinweis |
|-----|-----------|---------|
| SoftAP + STA NAT | Kernfunktion | Lab-AP |
| Optional WireGuard | `vpn_manager` → esp_wireguard | `EVID-CARNET-2026-11-12-010` |
| Port default | 51820; keepalive CLI `-a` | Wiki/CLI |
| SoftAP+BT parallel | Espressif C1 unstable | `…-030`; kein Sheet `esp-wifi-bt-coex` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| SoftAP+STA NAT + optional WG via vpn_manager/esp_wireguard | `EVID-CARNET-2026-11-12-010` | `FACT` |
| SoftAP connecting/connected × BT/BLE = C1 (Espressif) | `EVID-CARNET-2026-11-12-030` | `FACT` |
| SoftAP als Car-Rendezvous für Analyzer stabil mit BT | — | `REJECTED` (Desk-Policy: nachrangig) |

## Offene Fragen

- Lab: SoftAP+Classic BT Coex-Messung auf Zielchip (FOLLOW-ON)?
- Portmap-only ohne SoftAP als Analyzer-Pfad?

## Verwandte Applications / Methods

- [esp-wireguard](esp-wireguard.md) — Component unter der Haube  
- [esp-tailscale-client](esp-tailscale-client.md) — bevorzugtes Car-Rendezvous  
- Cross-Ref: `bt-dual-mode-coex` (BTDM); **kein** `esp-wifi-bt-coex` Sheet  
