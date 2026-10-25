# Project Inventory: esp32-spotify-remote (Fremd)

```yaml
project_id: esp32-spotify-remote
updated: 2026-10-25
reviewed_commit: "15259e6e31e15895829414ac50cb8e0c38133df9"
profile: lab-tool
pilot_order: [spotify-web-api-remote, lms-squeezelite]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Spotify Web API + PKCE + HTTPS remote control | `spotify-web-api-remote` | **neu** + App |
| Spotify Connect / on-device decode | `lms-squeezelite` | **Kontrast** |
| AMOLED CO5300 / FT3168 / QMI8658 | — | observed (Board-HAL) |
| LittleFS album art | — | observed |

Kampagne: [`esp32-spotify-remote-2026-foreign`](../../audits/esp32-spotify-remote-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `spotify-web-api-remote` | Spotify Web API Remote (PKCE) | F | applied | partial | [SHEET](../../technologies/spotify-web-api-remote/SHEET.md) | [app](applications/spotify-web-api-remote.md) |
| `lms-squeezelite` | LMS / Squeezelite | F | observed | none | [SHEET](../../technologies/lms-squeezelite/SHEET.md) | — (Kontrast) |

## Signale ohne Eintrag

- PlatformIO Cert-Bundle CI — Ops
