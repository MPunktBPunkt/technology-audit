# Project Application: esp-wireguard in hu-probe

```yaml
project_id: hu-probe
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

Optionaler Overlay-Transport (`WireGuardTransport`) hinter compile-time Gate.
**MSC/Session dürfen nicht von WG abhängen.** Basis: esp32.wireguard **v0.4.9**.

| Env | FW | WG |
|-----|----|----|
| `huprobe-s3` | 0.3.41 | aus (`lib_ignore`) |
| `huprobe-s3-wg` | 0.3.42 | gelinkt, `wgEnable` default false |

## Ebene C (Lab 2026-11-27)

| Claim | Status |
|-------|--------|
| peer_up + Guest-WAN + selektive `/24` | `FACT` |
| Hub lastOk über WG | `FACT` |
| WG-Ausfall blockiert keine MSC-Session | `FACT` |
| Natürlicher WiFi-Failover | `UNKNOWN` |
| Feld Langzeit / Roaming | `UNKNOWN` |

Abschlussaudit: [`../../../audits/esp32-wireguard-2026-11-dod-close/`](../../../audits/esp32-wireguard-2026-11-dod-close/).
