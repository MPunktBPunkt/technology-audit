# Project Application: esp-psram-heavy-port in esp32-doom

```yaml
project_id: esp32-doom
tech_slug: esp-psram-heavy-port
status: active
sheet: ../../../technologies/esp-psram-heavy-port/SHEET.md
audit: ../../../audits/esp32-doom-2026-foreign/
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
```

## Rolle im Projekt

Espressif-PoC: PrBoom auf Classic ESP32-Wrover — PSRAM als Heap, Doom-Logik+Renderer-Last, SPI-LCD-Ausgabe, WAD in eigener Flash-Partition. Unsupported; kein Sound/Save.

| Repo | Commit | Rolle |
|------|--------|-------|
| [espressif/esp32-doom](https://github.com/espressif/esp32-doom) | `085f21b` (2017-07-04) | PoC Firmware |

## Architektur / Datenfluss

```text
wad partition @ 0x100000 (mmap)
  + SPIRAM malloc heap (4 MiB)
  + doomEngineTask @ core 0 (stack ~22 KiB)
  → PrBoom render → screens[0] 320×240 INTERNAL
  → spi_lcd_send (ST7789/ILI9341, optional double-buffer)
  ← PSX pad GPIOs
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `readme.rst` | PSRAM Pflicht, unsupported, Flash-Hinweise |
| `sdkconfig` | SPIRAM malloc, 240 MHz, LCD pins |
| `partitions.csv` | `wad` 3072K @ 0x100000 |
| `main/app_main.c` | LCD init, pinned doom task |
| `components/prboom-esp32-compat/i_video.c` | Screenbuf internal 320×240 |
| `…/i_system.c` | Partition mmap for WAD |
| `…/spi_lcd.c` | SPI LCD + DOUBLE_BUFFER |
| `components/prboom/` | Engine |

## Konfiguration und Parameter

| Parameter | Upstream (Desk) | Status |
|-----------|-----------------|--------|
| PSRAM | `CONFIG_MEMMAP_SPIRAM_ENABLE_MALLOC`, size 4 194 304 | `FACT` |
| CPU | 240 MHz | `FACT` |
| Screenbuf | `pvPortMallocCaps(320*240, MALLOC_CAP_INTERNAL\|8BIT)` | `FACT` |
| Task | `xTaskCreatePinnedToCore(..., 22480, ..., 0)` | `FACT` |
| LCD | ST7789 default in checked sdkconfig; ILI option | `FACT` |
| Sound/Save | unsupported | `FACT` |
| 4 MiB flash | cut shareware WAD; commercial → 16 MiB + bigger wad part | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Needs PSRAM hardware; Classic Wrover | `EVID-DOOM-2026-10-25-001` | `FACT` |
| SPIRAM malloc + 240 MHz + cache workaround | `EVID-DOOM-2026-10-25-002` | `FACT` |
| FB internal; PSRAM = heap for engine | `EVID-DOOM-2026-10-25-003` | `FACT` |
| WAD partition mmap; heavy task on core 0 | `EVID-DOOM-2026-10-25-004` | `FACT` |
| No sound/music/save; menus may crash | `EVID-DOOM-2026-10-25-005` | `FACT` |
| Lab FPS | — | `UNKNOWN` |

## Offene Fragen

- Läuft der PoC noch auf aktuellem IDF/Wrover-KIT ohne Patch?
