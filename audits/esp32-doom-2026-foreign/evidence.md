# Evidence — esp32-doom-2026-foreign

Desk 2026-10-25 · **standard_version 0.7.1** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/espressif/esp32-doom | `085f21b630f11adb69a3894db5a1efa39a7aa31a` (2017-07-04) |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-DOOM-2026-10-25-001` | PrBoom port; needs PSRAM; ESP-Wrover / 4 MiB flash+PSRAM; unsupported PoC | `FACT` | readme.rst, repo description |
| `EVID-DOOM-2026-10-25-002` | sdkconfig: SPIRAM enable+malloc 4 MiB, cache workaround, CPU 240 MHz | `FACT` | sdkconfig |
| `EVID-DOOM-2026-10-25-003` | `i_video.c`: screenbuf `MALLOC_CAP_INTERNAL` 320×240; not SPIRAM heap for FB | `FACT` | i_video.c |
| `EVID-DOOM-2026-10-25-004` | `wad` partition 3072K @ 0x100000; `esp_partition_mmap`; doom task pinned core 0 stack 22480 | `FACT` | partitions.csv, i_system.c, app_main.c |
| `EVID-DOOM-2026-10-25-005` | No sound/music; no savegames; most menus may crash | `FACT` | readme.rst |
| `EVID-DOOM-2026-10-25-006` | SPI LCD ILI9341/ST7789; DOUBLE_BUFFER in spi_lcd.c; PSX controller GPIOs | `FACT` | Kconfig, spi_lcd.c, readme |
| `EVID-DOOM-2026-10-25-007` | Commercial WAD needs larger flash/partition; cut shareware for 4 MiB | `FACT` | readme.rst |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-25 | Desk-Bootstrap Heavy-Port Sheet; FB-internal Nuance |
