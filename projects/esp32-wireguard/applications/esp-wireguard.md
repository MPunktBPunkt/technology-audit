# Project Application: esp-wireguard in esp32-wireguard

```yaml
project_id: esp32-wireguard
tech_slug: esp-wireguard
status: active
sheet: ../../../technologies/esp-wireguard/SHEET.md
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle

Referenz-Client für trombik/esp_wireguard hinter Hub-Base. Stand **v0.4.9**: Lab Transport-DoD **geschlossen** (selektives Routing, Guest/WAN/NAT, Reconnect, OTA-über-WG). Keine weitere Feature-Arbeit ohne neuen Anwendungsfall.

Consumer Lab-E2E: **hu-probe 0.3.42-wg**, **bt-analyzer 0.3.21-wg**.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| connect ESP_OK ≠ peer up | sheet | `REJECTED` (übernommen) |
| NAT ohne keepalive stabil | sheet | `REJECTED` |
| Library sync’t Zeit selbst | sheet | `REJECTED` |
| v0.4.9 release + Hub bins | `EVID-WG-2026-11-27-049` | `FACT` |
| Selective AllowedIPs + same-LAN refuse | `EVID-WG-2026-11-27-050` | `FACT` |
| Guest/WAN peer_up + Hub over WG | `EVID-WG-2026-11-27-051` | `FACT` |
| Reconnect + OTA-with-WG | `EVID-WG-2026-11-27-052` | `FACT` |
| Natürlicher WiFi-Failover | `EVID-WG-2026-11-27-066` | `UNKNOWN` |

Abschlussaudit: [`../../../audits/esp32-wireguard-2026-11-dod-close/`](../../../audits/esp32-wireguard-2026-11-dod-close/).  
Detail: [`EVIDENCE-2026-11-27-v049-closed.md`](EVIDENCE-2026-11-27-v049-closed.md).
