# Project Application: esp-tailscale-client in esp32-car-network-refs

```yaml
project_id: esp32-car-network-refs
tech_slug: esp-tailscale-client
status: active
sheet: ../../../technologies/esp-tailscale-client/SHEET.md
audit: ../../../audits/esp32-car-network-2026-foreign/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt

**Bevorzugtes A6/B1-Rendezvous:** Tailscale-kompatibler ESP-Client (CamM2325/microlink) — WireGuard-Datenpfad plus DERP-Relay und STUN/DISCO hinter Phone-Hotspot/CGNAT. Analyzer/Host erreicht ESP über Tailnet, ohne SoftAP-Wait und ohne öffentlich erreichbaren WG-Endpoint.

## Architektur / Datenfluss

```text
Phone Hotspot → ESP WiFi STA
  → microlink coord (ts2021 / MapResponse)
  → STUN / DISCO path check
  → Direct WG UDP  ODER  DERP relay (TLS)
  → Peer (Lab Host / Tailnet)
```

## Relevante Pfade

| Pfad (Ursprungsrepo @ 216da33) | Rolle |
|--------------------------------|------|
| `docs/ARCHITECTURE.md` | Task-Modell: coord / derp_tx / net_io / wg_mgr |
| `docs/TAILSCALE_REFERENCE.md` | Mapping zu Tailscale Go (DERP/STUN/MagicSock) |
| `examples/basic_connect` | Minimal connect |
| `examples/cellular_*`, failover | CGNAT / uplink failover Muster |

## Konfiguration und Parameter

| Key | Desk-Fakt | Hinweis |
|-----|-----------|---------|
| Control plane | ts2021 + DERPMap | dynamische Region |
| Data plane | WG encrypt; direct UDP oder DERP | Hotspot → oft DERP |
| PreferredDERP match | ESP muss gleiche Region connecten wie advertisen | sonst DISCO miss |
| SoftAP | nicht erforderlich für Rendezvous | Decision Trace |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| microlink = WG + DERP + STUN/DISCO; ARCHITECTURE + TAILSCALE_REFERENCE | `EVID-CARNET-2026-11-12-020` | `FACT` |
| Examples basic_connect / cellular_* / failover vorhanden | `EVID-CARNET-2026-11-12-021` | `FACT` |
| Muster geeignet für NAT hinter Phone-Hotspot (Rendezvous) | `EVID-CARNET-2026-11-12-022` | `FACT` (Desk-Architektur) |
| Lab: Hotspot STA → Peer erreichbar via DERP | — | `UNKNOWN` |

## Offene Fragen

- SRAM/Task-Budget parallel zu bt-analyzer Classic stack?
- Headscale vs. Tailscale control plane für Lab?

## Verwandte Applications / Methods

- [esp-wireguard](esp-wireguard.md) — reiner WG-Baustein ohne DERP  
- [esp-wifi-nat-router](esp-wifi-nat-router.md) — Lab SoftAP Kontrast  
