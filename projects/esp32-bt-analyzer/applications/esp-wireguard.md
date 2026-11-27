# Project Application: esp-wireguard in esp32-bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: esp-wireguard
status: active
sheet: ../../../technologies/esp-wireguard/SHEET.md
maturity:
  technology: R3
  implementation: R2
  field_evidence: R1
  reusability: W3
```

## Rolle

Optionaler Overlay-Transport (`WireGuardTransport` + `WgConfigStore`) hinter compile-time Gate.
**BT-Capture darf nicht von WG abhängen.** Basis: esp32.wireguard **v0.4.9**.

| Env | FW | WG |
|-----|----|----|
| `analyzer-s3` | 0.3.20 | aus (`lib_ignore`) |
| `analyzer-s3-wg` | 0.3.21 | gelinkt, `wgEnable` default false |

## Ebene C (Lab 2026-11-27, DUT `.88`)

| Claim | Status |
|-------|--------|
| Guest-WAN → Fritz → `peer_up` + selektive `/24` | `FACT` |
| Hub heartbeat über WG | `FACT` |
| Natürlicher WiFi-Failover | `UNKNOWN` |
| Feld | `UNKNOWN` |

Abschlussaudit: [`../../../audits/esp32-wireguard-2026-11-dod-close/`](../../../audits/esp32-wireguard-2026-11-dod-close/).
