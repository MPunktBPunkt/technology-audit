# Evidence — esp32.wireguard 0.2.0 Phase-1 Lab (2026-11-27)

Evidence categories only; no new technical claims beyond what was measured.

## EVID-WG-2026-11-27-010 — With WireGuard module (0.2.0)

**FACT** (Lab `.87` ESP32, `.88` ESP32-S3, `.131` ESP32):

| Probe | Result |
|-------|--------|
| `GET /api/status` → `version` | `0.2.0` |
| `modules` | `["wireguard"]` |
| `GET /api/ui/tabs` | `[{"id":"wg","title":"WireGuard","order":50,"panel":"/ui/tab/wg","script":"/ui/tab/wg.js"}]` |
| `GET /ui/tab/wg` | HTTP 200, 1382 B |
| `GET /ui/tab/wg.js` | HTTP 200, 1670 B (contains `/api/wg`) |
| `GET /api/wg/status` | HTTP 200; `wgState=unconfigured`; no PrivateKey/PresharedKey in JSON |
| `POST /api/wg/clear` (.87) | `{"ok":true,"cleared":true}`; device stayed reachable; `wdtFire` observed 0 on contemporaneous status |
| Secret leak scan on status/wg status | no `privatekey` / `preshared` material |

## EVID-WG-2026-11-27-011 — Without WireGuard (Base 1.12.0)

**FACT** (Lab `.131` after Hub OTA `esp-hub-base.1.12.0.esp32.bin`):

| Probe | Result |
|-------|--------|
| `version` | `1.12.0` |
| `modules` | absent / null |
| `GET /api/ui/tabs` | `[]` |
| `GET /api/wg/status` | HTTP 302 (no WG routes) |
| `GET /ui/tab/wg` | HTTP 302 |
| `wdtFire` | `0` |

## EVID-WG-2026-11-27-012 — Restore 0.2.0 after Base compare

**FACT** (`.131`): Hub OTA `wireguard.0.2.0.esp32.bin` → `version=0.2.0`, `modules=["wireguard"]`, tabs again contain `wg`.

## Architecture boundaries (Phase 2)

| Decision | Status |
|----------|--------|
| `kMaxModules = 6` | **INFERENCE**: ausreichend für aktuelle Apps; kein realer Bedarf — unverändert |
| 1 Modul → 0\|1 Tab | **INFERENCE**: WireGuard braucht einen Tab; unverändert |

Raw capture: `/tmp/wg-phase1-evid/phase1.json` on build host (session).
