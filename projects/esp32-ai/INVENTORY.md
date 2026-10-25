# Project Inventory: esp32-ai (Fremd)

```yaml
project_id: esp32-ai
updated: 2026-10-25
reviewed_commit: "52ebcbbd905270592c1d415efd1128d04d0fa365"
profile: lab-tool
pilot_order: [mcu-ple-inference, mcu-connectome-graph, esp32-s3-silicon, ssd1306-oled-ui]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| PLE TinyLM, int4, flash table / PSRAM head / SRAM acts, dual-core Matvec | `mcu-ple-inference` | **neu** + App |
| Fruit-fly connectome subgraph, LZ4 flash, dual-core SIMD | `mcu-connectome-graph` | **neu** + App |
| ESP32-S3 N16R8, PSRAM/Flash mmap, bandwidth bench | `esp32-s3-silicon` | **reuse** + App |
| 128×64 I²C OLED SH1106/SSD1306, probe-or-noop | `ssd1306-oled-ui` | **reuse** + App (Controller-Variante) |
| Hub / WiFi / BT / USB-MSC | — | out of scope (Connectivity none) |
| BPE tokenizer on-device | `mcu-ple-inference` | A-Fallstrick / App (kein eigener Slug) |

Kampagne: [`esp32-ai-2026-foreign`](../../audits/esp32-ai-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `mcu-ple-inference` | MCU PLE LLM Inference | D | applied | partial | [SHEET](../../technologies/mcu-ple-inference/SHEET.md) | [app](applications/mcu-ple-inference.md) |
| `mcu-connectome-graph` | MCU Connectome Graph | D | applied | partial | [SHEET](../../technologies/mcu-connectome-graph/SHEET.md) | [app](applications/mcu-connectome-graph.md) |
| `esp32-s3-silicon` | ESP32-S3 Silicon / HW Limits | D | applied | partial | [SHEET](../../technologies/esp32-s3-silicon/SHEET.md) | [app](applications/esp32-s3-silicon.md) |
| `ssd1306-oled-ui` | SSD1306 OLED UI (small) | G | applied | partial | [SHEET](../../technologies/ssd1306-oled-ui/SHEET.md) | [app](applications/ssd1306-oled-ui.md) |

## Nach Kategorie

### D — Embedded

- `mcu-ple-inference`, `mcu-connectome-graph`, `esp32-s3-silicon`

### G — Steuerung / UI

- `ssd1306-oled-ui`

### Sonstige

—

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Eigene tok/s / Bandwidth auf Board | Desk only; Upstream-Zahlen | Lab FOLLOW-ON |
| Barista out2in / asym. Vocab als A | nur App-Pfad | Sheet-Fallstrick nach 2. Upstream |
| Whole-CNS Connectome | Upstream: passt nicht in 16 MB | observed gap, kein Sheet |
| Classic ESP32 ohne PSRAM | nicht im Repo | Gate in Sheets |

## Signale ohne Eintrag

- PyTorch Train/Ablation (`research/tinystories`) — Host-ML, nicht MCU-A
- LZ4 block codec internals — Implementierungsdetail Connectome-App
- `scripts/deploy.sh` Flash-Ordnung — Ops-Muster in Apps, kein Slug
