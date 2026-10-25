# Evidence — esp32-ai-2026-foreign

Desk 2026-10-25 · **standard_version 0.7.1** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/slvDev/esp32-ai | `52ebcbbd905270592c1d415efd1128d04d0fa365` |

Upstream-Author-Messungen werden als Desk-`FACT` zitiert (Quelle benannt), nicht als eigene Lab-`MEASURED`.

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-ESP32AI-2026-10-25-001` | `runtime/llm.h`: PLE TinyLM, Magic `PLE\0`, int4 QT, Flash-bind Weights; Host+Device gleicher Header | `FACT` | `runtime/llm.h` |
| `EVID-ESP32AI-2026-10-25-002` | README/RESULTS: ~9.5–9.88 tok/s e2e auf ESP32-S3 N16R8; 28.9M stored (25M flash table) | `FACT` | README, RESULTS.md |
| `EVID-ESP32AI-2026-10-25-003` | Bandwidth sketch: PSRAM ~60.7 MB/s; Flash random 512 B ~20.3 µs; Table ~0.12 ms/token; Head ~17.3 ms | `FACT` | RESULTS.md, `firmware/benchmarks/bandwidth/` |
| `EVID-ESP32AI-2026-10-25-004` | Barista: asym. Vocab (8057 in / 854 out), `out2in`, Boot-Guards gegen Table/Model-Mismatch | `FACT` | `firmware/esp32_barista/README.md` |
| `EVID-ESP32AI-2026-10-25-005` | Fly: 48311 Neuronen, 9462135 Verbindungen; Escape via LC4/LPLC2→DNp01…; nothing trained | `FACT` | README, `firmware/esp32_fly/README.md` |
| `EVID-ESP32AI-2026-10-25-006` | `deploy.sh` / `model_bundle.json`: Bundle-Hash + Host-Gold vor Compile/Flash; Compile before flash images | `FACT` | fly/tinystories READMEs, scripts |
| `EVID-ESP32AI-2026-10-25-007` | `docs/fly-connectome/` Attribution + LICENSE-DATA; Whole CNS passt nicht in Restflash | `FACT` | `docs/fly-connectome/` |
| `EVID-ESP32AI-2026-10-25-008` | Zielhardware ESP32-S3 512 KB SRAM / 8 MB PSRAM / 16 MB Flash; custom `model` partition @ 0x110000 | `FACT` | README, partitions.csv |
| `EVID-ESP32AI-2026-10-25-009` | Optional 128×64 I²C OLED; default SH1106; SSD1306 flag; SDA18/SCL46; absent = probe then no-op | `FACT` | `display.h`, barista/fly README |
| `EVID-ESP32AI-2026-10-25-010` | Connectivity none; alles on-device | `FACT` | README |
| `EVID-ESP32AI-2026-10-25-011` | Top-Level: firmware/{barista,tinystories,fly,benchmarks}, runtime/, src/, research/, scripts/, MIT | `FACT` | Repo tree @ `52ebcbb` |
| `EVID-ESP32AI-2026-10-25-012` | TinyStories: dual-core int8 Matvec (`xTaskCreatePinnedToCore`); RESULTS-Leiter dual-core exact head → int8-staged ~9.5 tok/s; Fly separat Dual-Core+SIMD | `FACT` | `esp32_tinystories.ino`, RESULTS.md, fly README |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-25 | Desk-Bootstrap + Sheets/Apps/Kampagne 0.7.1 |
