# Technology Sheet: ESP Tailscale-Compatible Client

```yaml
slug: esp-tailscale-client
title: ESP Tailscale-Compatible Client (WG + DERP + STUN)
primary: D
tags: [esp-idf, networking, vpn]
type: pattern
status: active
seen_in: [esp32-car-network-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/esp32-car-network-2026-foreign
```

Nur Ebene **A**. Referenzimplementierung: CamM2325/microlink. Reiner WG-Tunnel → `esp-wireguard`. SoftAP-NAT → `esp-wifi-nat-router`. Primary **D** (Embedded-Muster); Tailscale-Ökosystem wäre F — hier ESP-Client-Pattern.

## Kurzfassung

**Rendezvous-Muster** für ESP hinter NAT/Hotspot/CGNAT: Tailscale-kompatibler Client mit WireGuard-Datenpfad, **DERP-Relay**, STUN und DISCO-Pfadfindung. Ermöglicht Erreichbarkeit ohne öffentlichen WG-Endpoint und ohne SoftAP-Wait — bevorzugtes Muster für car-side Analyzer-Reachability (A6/B1).

## Abgrenzung

- **Ist:** Embedded Tailscale-compat Client (control plane + MagicSock-ähnlich: WG/DERP/STUN/DISCO).
- **Ist nicht:** Host Tailscaled; reines `esp_wireguard` ohne DERP; SoftAP NAT-Router; Attack/Bypass von Fremdnetzen.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Uplink | WiFi STA (Hotspot) / optional Cellular | Outbound first |
| Control | ts2021 / MapResponse / DERPMap | Region discovery |
| Data | WG UDP direct **oder** DERP TLS relay | hinter CGNAT oft DERP |
| Discovery | STUN + DISCO | NAT type / peer path |
| Tasks | coord / derp_tx / net_io / wg_mgr | Queue-IPC (microlink v2) |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| SoftAP nötig für Car-Reachability | `REJECTED` | STA + rendezvous reicht architektonisch |
| PreferredDERP advertise ≠ connected region | `REJECTED` | DISCO/Relay miss |
| = esp_wireguard drop-in | `REJECTED` | Control plane + DERP/STUN fehlen dort |
| Cellular/CGNAT: direct UDP immer möglich | `REJECTED` | oft force DERP |
| Desk-Architektur = Lab MEASURED hinter Hotspot | `REJECTED` | Lab Gate offen |

## Transfer

Car/Lab-Geräte hinter Phone-Hotspot: zuerst dieses Muster evaluieren; WG-only nur wenn Endpoint erreichbar + keepalive. SoftAP nur Lab/Provisioning, nicht als Analyzer-Rendezvous.

### Projektstart-Checkliste

- [ ] Control plane: Tailscale vs Headscale
- [ ] Hotspot STA + DERP Failover geplant
- [ ] SRAM/Task-Budget vs. paralleler BT-Stack
- [ ] SoftAP bewusst **nicht** als Reachability-Plan
- [ ] Application + `seen_in`

## Referenzen

- https://github.com/CamM2325/microlink — `docs/ARCHITECTURE.md`, `docs/TAILSCALE_REFERENCE.md`
- Related: `esp-wireguard`, `esp-wifi-nat-router`

## Offene Fragen

- Minimales Task-/Heap-Budget parallel zu Classic BT Analyzer?
