# Audit Campaign: squeezelite-esp32-2026-foreign

```yaml
id: squeezelite-esp32-2026-foreign
project_id: squeezelite-esp32
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "ee1720c7556ffec5f43329aadd47c20546bdbb79"
reuse_outcomes:
  reused: [esp-i2s-audio, esp-psram-heavy-port, bluetooth-a2dp, webradio-browser-host]
  new: [lms-squeezelite]
  not_helped: []
  process: "Desk LMS-first Squeezelite; reuse I2S/PSRAM/A2DP; contrast browser webradio"
```

## Ziel

squeezelite-esp32 als Fremd-Upstream für **LMS/Squeezelite-Multi-Room-Player** auf ESP — mit klarer LMS-first-Epistemik und Reuse der Audio/PSRAM-Sheets.

## Scope

[SCOPE](../../projects/squeezelite-esp32/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + Commit | erfüllt |
| 2 | Sheet `lms-squeezelite` + 4 Apps | erfüllt |
| 3 | PSRAM/240 MHz/LMS-first Evidence | erfüllt |
| 4 | C10–C12 | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 6 | Sync Lab | offen |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Neues Sheet? | = webradio-browser? | `…-001` | Nein — neu LMS |
| PSRAM Sheet reuse? | Heavy decode? | `…-002` | reuse `esp-psram-heavy-port` |
| A2DP Sheet? | BT roles? | `…-006` | reuse + App |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-001` | BT-only Use-Case nicht als LMS-Reife verkaufen |
| `…-002` | WROOM ohne PSRAM = Gate |
| `…-006` | S3 ≠ Classic BT Audio |
| `…-007` | Spotify+SPDIF+stats Classic = disable stats |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Nur Browser-Audio-Host ohne Decode | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk; Sync Lab UNKNOWN ≠ STOP.
```

## Bezug

[INVENTORY](../../projects/squeezelite-esp32/INVENTORY.md) · [evidence](evidence.md)
