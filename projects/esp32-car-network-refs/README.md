# Project: esp32-car-network-refs

Fremd-Desk: ESP32 **car-side networking** — outbound connectivity via phone hotspot/NAT (A6/B1 blocker for bt-analyzer car reachability).

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Grenzen |
| [INVENTORY.md](INVENTORY.md) | Inventar + Muster-Matrix |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | Folge |
| [applications/](applications/) | Applications |
| Audit | [`esp32-car-network-2026-foreign`](../../audits/esp32-car-network-2026-foreign/) (`0.7.1`) |

**Entscheidung (Desk):** Für Analyzer-Reachability hinter Hotspot/NAT → **microlink / Tailscale-style rendezvous** (WG + DERP + STUN) bevorzugen vor reinem SoftAP-Wait. Reines WireGuard braucht erreichbaren Endpoint oder `persistent_keepalive` durch NAT. `esp32_nat_router` ist guter Lab-AP; SoftAP+BT Coex ist Espressif **C1** (unstable).
