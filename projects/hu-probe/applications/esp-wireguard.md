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
| peer_up + Guest-WAN + selective /24 | `FACT` |
| Hub lastOk über WG | `FACT` |
| WG-Ausfall blockiert keine MSC-Session | `FACT` |
| Feld Langzeit / Roaming | `UNKNOWN` |

Siehe `../../esp32-wireguard/applications/EVIDENCE-2026-11-27-v049-closed.md`.
