# Project Scope: squeezelite-esp32 (Fremd)

```yaml
project_id: squeezelite-esp32
title: Squeezelite-ESP32 — LMS Multi-Room Player (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "ee1720c7556ffec5f43329aadd47c20546bdbb79"
repos:
  - https://github.com/sle118/squeezelite-esp32
status: active
```

## Zweck

Fremdrepo als Desk-Quelle für **Logitech Media Server (LMS) / Squeezelite**-Players auf ESP32(+S3): Multi-Room-Sync, schwere Decode-Last, PSRAM-Pflicht, I2S/SPDIF/BT-Ausgänge. Primär LMS-zentriert; AirPlay/BT/Spotify als Add-ons.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `components/squeezelite` + codecs | LMS player core | ja |
| I2S DAC / SPDIF outs | Audio sink path | ja (Reuse I2S) |
| BT sink/source, AirPlay, Spotify Connect | Add-ons | ja (Inventar; Teiltiefe) |
| Display / buttons / IR / Ethernet | Hardware extensions | observed |
| LMS server itself | Host | angrenzend Link |
| Browser-Webradio-Host | — | **nein** (Kontrast) |
| Eigene Sync-Lab-Messung | — | FOLLOW-ON |

## Nicht-Ziele

- Vollständige Codec-Matrix 1:1 in Sheets
- Spotify/cspot Lizenzberatung
- WROOM-ohne-PSRAM als unterstütztes Target

## Quellen

| Quelle | URL | Bemerkung |
|--------|-----|-----------|
| Code | https://github.com/sle118/squeezelite-esp32 @ `ee1720c` | branch `master-v4.3` |
| README | Performances, Hardware | Desk |

## Prioritäten

1. Sheet `lms-squeezelite` + Application
2. Reuse Apps: `esp-i2s-audio`, `esp-psram-heavy-port`, `bluetooth-a2dp`
3. Kontrast `webradio-browser-host`
4. 16-bit core / 240 MHz / PSRAM Fallstricke
