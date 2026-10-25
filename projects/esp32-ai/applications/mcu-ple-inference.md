# Project Application: mcu-ple-inference in esp32-ai

```yaml
project_id: esp32-ai
tech_slug: mcu-ple-inference
status: active
sheet: ../../../technologies/mcu-ple-inference/SHEET.md
audit: ../../../audits/esp32-ai-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle im Projekt

On-Chip-Inference für TinyStories (28.9M stored PLE) und Barista (asym. Vocab/Head); Host-Verify; Deploy über Custom-`model`-Partition.

| Repo | Commit | Rolle |
|------|--------|-------|
| [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | `52ebcbb` | Firmware + `runtime/llm.h` |

## Architektur / Datenfluss

```text
artifacts/model.bin (HF)
  → host_verify (golden / staging)
  → flash partition `model` @ 0x110000
  → llm.h forward
       SRAM: activations / norms
       PSRAM: dense core / output head (staged)
       FLASH mmap: PLE table (sparse rows/token)
       Dual-Core: große int8-Matvecs (Head) row-split; Worker pinned
  → Serial (+ optional OLED)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `runtime/llm.h` | Portable int4/PLE Inference; row-range Matvec für Parallel |
| `runtime/bpe_tokenizer.h` | On-device BPE |
| `firmware/esp32_tinystories/esp32_tinystories.ino` | Dual-Core Worker (`xTaskCreatePinnedToCore`) + int8 stage |
| `firmware/esp32_tinystories/` | 28.9M TinyStories sketch |
| `firmware/esp32_barista/` | Asym. Vocab QA sketch |
| `src/model.py`, `src/quantize.py` | Train/Export (Host) |
| `scripts/deploy.sh`, `scripts/fetch_model.sh` | Gates + Flash-Ordnung |
| `RESULTS.md` | Ablation + Bandwidth-Zahlen |

## Konfiguration und Parameter

| Parameter | Upstream (Desk) | Status |
|-----------|-----------------|--------|
| Chip-Ziel | ESP32-S3 N16R8 | `FACT` |
| Deploy TinyStories | vocab 32768, ~559K core, 25M PLE table, d_model=96, 6 layers | `FACT` (RESULTS) |
| Model partition | `0x110000`, size `0xEE0000` | `FACT` (partitions.csv) |
| Quant | group-wise int4 + fp16 scales; optional int8 head staging | `FACT` (`llm.h`) |
| Connectivity | none | `FACT` (README) |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| PLE TinyLM Header/Magic; Flash-bind Weights | `EVID-ESP32AI-2026-10-25-001` | `FACT` |
| Author: ~9.5–9.88 tok/s e2e auf S3 N16R8 | `EVID-ESP32AI-2026-10-25-002` | `FACT` (Upstream MEASURED → Desk) |
| Flash-Table ~0.12 ms/token vs Head ~17.3 ms (Bandwidth sketch) | `EVID-ESP32AI-2026-10-25-003` | `FACT` (Upstream MEASURED → Desk) |
| Dual-Core Head-Matvec + int8 staging als tok/s-Hebel (RESULTS-Leiter) | `EVID-ESP32AI-2026-10-25-012` | `FACT` (Upstream MEASURED → Desk) |
| Barista out2in + Boot-Guards gegen Vocab-Mismatch | `EVID-ESP32AI-2026-10-25-004` | `FACT` |
| Eigene Lab-Remessung | — | `UNKNOWN` |

## Abweichungen vom „Lehrbuch“

- „28.9M“ ist *stored* (Table-lastig), nicht Dense-äquivalent — Sheet-Fallstrick.
- Barista: Output-Klassen ≠ Input-Token-IDs (`out2in`).

## Offene Fragen

- Remessung tok/s und Flash-Random unter Arduino-Core 3.3.x?
