# Project Scope: esp32-spotify-remote (Fremd)

```yaml
project_id: esp32-spotify-remote
title: ESP32 Spotify Remote — Web API + PKCE (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "15259e6e31e15895829414ac50cb8e0c38133df9"
repos:
  - https://github.com/seichris/esp32-spotify-remote
status: active
```

## Zweck

Fremdrepo: **Spotify Web API Remote** auf ESP32-S3 (Touch-AMOLED) mit **PKCE** (kein Client-Secret in FW), verified HTTPS, NVS Refresh-Token, Touch-Controls + Cover-Art. Abgrenzung zu Spotify-Connect-/LMS-Decode-Playern.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `SpotifyClient` + PKCE/OAuth bridge | API Remote | ja |
| AMOLED/Touch/Orientation | Board UI | Application |
| Spotify Connect / cspot decode | — | **nein** (Kontrast LMS) |
| Client secret in firmware | — | **nein** (Upstream vermeidet) |

## Nicht-Ziele

- Spotify-Lizenz-/Account-Beratung
- AMOLED-Treiber als Universal-Sheet (Board-spezifisch)
- Secrets spiegeln

## Prioritäten

1. Sheet `spotify-web-api-remote` + App
2. Kontrast `lms-squeezelite` (Connect≠Web-API-Remote)
