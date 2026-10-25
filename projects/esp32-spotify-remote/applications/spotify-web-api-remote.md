# Project Application: spotify-web-api-remote in esp32-spotify-remote

```yaml
project_id: esp32-spotify-remote
tech_slug: spotify-web-api-remote
status: active
sheet: ../../../technologies/spotify-web-api-remote/SHEET.md
audit: ../../../audits/esp32-spotify-remote-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle

Standalone Spotify Remote auf Waveshare ESP32-S3-Touch-AMOLED-2.06: PKCE auth, Now-Playing + Controls + Cover, Auto-Rotate.

| Repo | Commit |
|------|--------|
| [seichris/esp32-spotify-remote](https://github.com/seichris/esp32-spotify-remote) | `15259e6` |

## Datenfluss

```text
Browser → OAuthPortal / spotify_oauth_bridge.py (127.0.0.1:4381)
  → SpotifyClient PKCE exchange → NVS refresh
  → HTTPS Web API (Mozilla bundle)
  → AppUi + BoardDisplay (CO5300) + Touch
```

## Pfade

| Pfad | Rolle |
|------|-------|
| `src/SpotifyClient.*` | PKCE, API, artwork |
| `src/OAuthPortal.*` | Setup page |
| `tools/spotify_oauth_bridge.py` | Loopback forward |
| `docs/ARCHITECTURE.md` | Layer split |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| PKCE; no client secret; verified HTTPS | `EVID-SPOTIFY-2026-10-25-001` | `FACT` |
| Clean-room vs ThingPulse inspiration | `EVID-SPOTIFY-2026-10-25-002` | `FACT` |
| AMOLED 410×502 + QMI8658 rotate | `EVID-SPOTIFY-2026-10-25-003` | `FACT` |
