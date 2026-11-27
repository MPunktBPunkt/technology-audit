# Project Application: esp-wireguard in esp32-wireguard

```yaml
project_id: esp32-wireguard
tech_slug: esp-wireguard
status: active
sheet: ../../../technologies/esp-wireguard/SHEET.md
maturity:
  technology: R3
  implementation: R1
  field_evidence: R0
  reusability: W3
```

## Rolle

Referenz-Client für trombik/esp_wireguard hinter Hub-Base. Stand **0.2.0**: Fassade + UiTab/NVS/Parser; Stack noch `stack_not_linked`.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| connect ESP_OK ≠ peer up | sheet | `REJECTED` (übernommen) |
| NAT ohne keepalive stabil | sheet | `REJECTED` |
| Library sync’t Zeit selbst | sheet | `REJECTED` |
| Echter Tunnel / peer_is_up Lab | — | `UNKNOWN` (Phase 11+) |

## Nächste Evidence

Fritz!Box Handshake + Hotspot + SNTP auf Lab-ESPs.
