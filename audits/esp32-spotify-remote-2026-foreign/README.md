# Audit Campaign: esp32-spotify-remote-2026-foreign

```yaml
id: esp32-spotify-remote-2026-foreign
project_id: esp32-spotify-remote
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "15259e6e31e15895829414ac50cb8e0c38133df9"
reuse_outcomes:
  reused: [lms-squeezelite]
  new: [spotify-web-api-remote]
  not_helped: []
  process: "Desk Spotify Web API + PKCE remote; contrast LMS/Connect decode"
```

## Ziel

esp32-spotify-remote als Fremd-Upstream für **Spotify Web-API Remote (PKCE)** — Control ohne On-Device-Decode, klar getrennt von LMS/Connect.

## Scope

[SCOPE](../../projects/esp32-spotify-remote/SCOPE.md) — Desk; kein Spotify-Account-Feldtest.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + Commit | erfüllt |
| 2 | Sheet `spotify-web-api-remote` + App; Kontrast LMS | erfüllt |
| 3 | PKCE / no-secret / verified HTTPS Evidence | erfüllt |
| 4 | C10–C12 | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 6 | Account-Feldtest | offen |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neues Sheet vs LMS? | Control oder Decode? | `…-001` | Neu Web-API-Remote | KNOWN BEFORE |
| Secret in FW? | PKCE? | `…-001` | Nein | KNOWN BEFORE |
| Board in Sheet? | AMOLED general? | `…-003` | Application only | KNOWN BEFORE |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-001` | Kein Client-Secret und kein insecure TLS als Pattern |
| `…-001` | Web-API-Remote ≠ Spotify Connect Player |
| `…-003` | Board-HAL nicht in Sheet-Schnittstellen |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Nur Connect-Decode ohne Web-API | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk; Account-Feldtest UNKNOWN ≠ STOP.
```

## Bezug

[INVENTORY](../../projects/esp32-spotify-remote/INVENTORY.md) · [evidence](evidence.md)
