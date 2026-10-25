# Project Scope: esp32-doom (Fremd)

```yaml
project_id: esp32-doom
title: ESP32-DOOM — PrBoom PoC + PSRAM (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "085f21b630f11adb69a3894db5a1efa39a7aa31a"
repos:
  - https://github.com/espressif/esp32-doom
status: active
```

## Zweck

Fremdrepo als Desk-Quelle für **schwere Legacy-C-Ports auf ESP32 mit PSRAM-Heap**: PrBoom/Doom, SPI-LCD-Framebuffer, WAD-Partition-mmap, hohe CPU-Last. Wissen generalisieren als Sheet — **Chip-Scope Classic Wrover**; S3-Transfer nur mit Gate.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `components/prboom` | Game Engine | ja (Desk, Last-Muster) |
| `prboom-esp32-compat` | Video/LCD/System/WAD mmap | ja |
| SPIRAM malloc / 240 MHz | Memory+CPU Contract | ja |
| PS1/PS2 Gamepad | Input | Application |
| Sound / Savegames | — | **nein** (Upstream unsupported) |
| Commercial WAD Rights | — | out of KB (nur Size-Gate) |
| Moderne IDF/S3-Remessung | — | FOLLOW-ON |

## Nicht-Ziele

- Doom als Produkt-/Lizenzberatung
- Sound-Stack nachrüsten in der KB
- `esp32-s3-silicon` still als Chip-SoT dieses Repos (Classic ≠ S3)
- Tiny-OLED-UI mit Game-Framebuffer vermischen

## Quellen

| Quelle | URL / Pfad | Bemerkung |
|--------|------------|-----------|
| Code | https://github.com/espressif/esp32-doom @ `085f21b` | letzter Code-Commit 2017-07-04 |
| Readme | `readme.rst` | PSRAM Pflicht, unsupported |
| sdkconfig | SPIRAM + 240 MHz + LCD | Desk |

## Prioritäten

1. Sheet `esp-psram-heavy-port` (PSRAM-Heap + schwere Grafik/Logik)
2. Nuance: Framebuffer **internal**, Game-Heap **PSRAM**
3. Kontrast S3-PSRAM-Sheets / OLED-UI
4. Historical PoC / IDF-Lag sichtbar halten

## Offene Scope-Fragen

- Eigenes SPI-LCD-Framebuffer-Sheet später, oder reicht dieses Port-Muster?
