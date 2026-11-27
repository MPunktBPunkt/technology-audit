# Evidence — Storage 0.3.0 + Stack 0.4.0 (2026-11-27)

## Storage / Obfuscation / OTA persistence

| ID | Claim | Status |
|----|-------|--------|
| EVID-WG-2026-11-27-020 | Config save via POST `/api/wg/config` → `wgState=configured`; PrivateKey/PresharedKey only as `configured`/`missing`; no key material in status/config JSON | `FACT` (.87) |
| EVID-WG-2026-11-27-021 | After OTA 0.3.0→0.3.0 (bootGen 4→5) config remained (`wgConfigured`, endpoint/address/allowedIps, keys configured) | `FACT` (.87) |
| — | Obfuscation is cryptography / encryption | `REJECTED` (by design wording) |
| — | Flash Encryption / Secure Boot required for V1 threat model | `REJECTED` (deferred) |

## Module limits

| Claim | Status |
|-------|--------|
| Raise `kMaxModules` beyond 6 now | `REJECTED` (no real need) |
| Multi-tab per module now | `REJECTED` (no real need) |

## Real WireGuard stack (trombik v0.9.0) — Build-Host

| ID | Claim | Status |
|----|-------|--------|
| EVID-WG-2026-11-27-030 | `esp_wireguard_init` / `connect` / `peer_is_up` symbols present in 0.4.0 ELF | `FACT` (nm) |
| EVID-WG-2026-11-27-031 | Δ Flash Sketch E→F (0.3.0→0.4.0) esp32 = **+22528 B (~22.0 KiB)**; Globals **+1576 B** | `FACT` (arduino-cli) |
| EVID-WG-2026-11-27-032 | esp32s3 Sketch 0.4.0 = 1251891 B; Globals 54020 B | `FACT` |
| EVID-WG-2026-11-27-033 | OTA 0.4.0 on .87/.88/.131; `version=0.4.0`; enable without config → non-fatal; app stays up (`wdtFire` observed 0) | `FACT` (Lab) |

## CONSTRAINT / UNKNOWN (routing)

| Claim | Status |
|-------|--------|
| High-level trombik API encodes peer AllowedIPs selectively | `CONSTRAINT` — upstream `esp_wireguard.c` sets peer allowed to `0.0.0.0/0` (“Allow all IPs through tunnel”) |
| Selective routing without `set_default` / without full peer allow | `UNKNOWN` until Phase 19 lab with lower-level `wireguardif` or fork |

## Not yet FACT

- SNTP gate, Fritz!Box handshake, peer_is_up in field, hotspot, reconnect times, Heimnetz TCP
