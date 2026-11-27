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

Referenz-Client für trombik/esp_wireguard hinter Hub-Base. Stand **0.4.0**: Stack gelinkt; Storage-Blob+Obfuscation; Tunnel-Lab (Handshake/Hotspot) offen.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| connect ESP_OK ≠ peer up | sheet | `REJECTED` (übernommen) |
| NAT ohne keepalive stabil | sheet | `REJECTED` |
| Library sync’t Zeit selbst | sheet | `REJECTED` |
| Stack gelinkt (nm + OTA 0.4.0) | `EVID-WG-2026-11-27-030`/`033` | `FACT` |
| Δ real stack esp32 ≈ +22.0 KiB / +1576 B Globals | `EVID-WG-2026-11-27-031` | `FACT` (Build-Host) |
| Peer AllowedIPs selektiv via High-Level-API | — | `CONSTRAINT` (upstream 0.0.0.0/0) |
| Fritz!Box peer_is_up / Heimnetz / Hotspot | — | `UNKNOWN` |

Siehe `EVIDENCE-2026-11-27-storage-stack.md`.
