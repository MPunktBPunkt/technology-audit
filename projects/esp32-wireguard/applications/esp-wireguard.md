# Project Application: esp-wireguard in esp32-wireguard

```yaml
project_id: esp32-wireguard
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

Referenz-Client für trombik/esp_wireguard hinter Hub-Base. Stand **v0.4.9**: Transport-DoD im Lab geschlossen (selektives Routing, Guest/WAN/NAT, Reconnect, OTA-über-WG). Keine weitere Feature-Arbeit ohne neuen Anwendungsfall.

Consumer: **hu-probe 0.3.42** (Lab-validated), **bt-analyzer 0.3.21-wg** (build scaffold).

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| connect ESP_OK ≠ peer up | sheet | `REJECTED` (übernommen) |
| NAT ohne keepalive stabil | sheet | `REJECTED` |
| Library sync’t Zeit selbst | sheet | `REJECTED` |
| Stack gelinkt (nm + OTA 0.4.0) | `EVID-WG-2026-11-27-030`/`033` | `FACT` |
| Δ real stack esp32 ≈ +22.0 KiB / +1576 B Globals | `EVID-WG-2026-11-27-031` | `FACT` (Build-Host) |
| Peer AllowedIPs selektiv (patched + Lab) | `EVID-WG-2026-11-27-050` | `FACT` |
| Fritz Guest/WAN peer_up + Hub over WG | `EVID-WG-2026-11-27-051` | `FACT` |
| Reconnect + OTA-with-WG | `EVID-WG-2026-11-27-052` | `FACT` |
| v0.4.9 release closed | `EVID-WG-2026-11-27-049` | `FACT` |

Siehe `EVIDENCE-2026-11-27-storage-stack.md`, `EVIDENCE-2026-11-27-v049-closed.md`.
