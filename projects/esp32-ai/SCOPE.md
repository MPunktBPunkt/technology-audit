# Project Scope: esp32-ai (Fremd)

```yaml
project_id: esp32-ai
title: esp32-ai — On-Device PLE LLM + Fly Connectome (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "52ebcbbd905270592c1d415efd1128d04d0fa365"
repos:
  - https://github.com/slvDev/esp32-ai
status: active
```

## Zweck

Fremdrepo als Desk-Quelle: **28.9M-Parameter PLE-LLM** und **Fruit-Fly-Connectome-Subgraph** auf ESP32-S3 (N16R8) — Memory-Hierarchy-Split (SRAM/PSRAM/Flash), Host-Verify-Gates, OLED-Demo. Wissen in wiederverwendbare Sheets + Applications überführen; **kein** Code-Import.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `runtime/llm.h` + TinyStories/Barista sketches | On-device PLE-Inference | ja (Desk) |
| `runtime/connectome_*.h` + `esp32_fly` | Connectome-Graph + Escape-Demo | ja (Desk) |
| `firmware/benchmarks/bandwidth` | Flash/PSRAM-Bandbreitenmessung | ja (Desk-Claims) |
| `src/` + `research/` (PyTorch Train/Export) | Host-Training/Ablation | angrenzend (nur Export-/Gate-Bezüge) |
| HuggingFace Model-Artefakte | Weights / Graph | Links only, nicht spiegeln |
| Eigene Lab-Messung auf Board | — | **nein** (FOLLOW-ON) |
| Cloud-/Server-Inference | — | **nein** (Repo: offline) |

## Nicht-Ziele

- Model-Weights, Connectome-Binaries oder Media in die KB kopieren
- Capability-Claims („Antwortqualität“) als A-FACT ohne Domain-Gate
- Classic-ESP32 / C3 ohne S3+PSRAM+Flash-Budget still übertragen
- Hub-/WiFi-/BT-Integration (Upstream: Connectivity none)

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| Code | https://github.com/slvDev/esp32-ai @ `52ebcbb` | Fremd, Desk |
| Results | `RESULTS.md` | Author MEASURED → Desk-`FACT`/`INFERRED` |
| Docs | `docs/fly-connectome/`, Firmware-READMEs | Attribution Connectome |
| Modelle | HF `slvDev/esp32-ai-{barista,tinystories,fly}` | Links only |

## Prioritäten für die Analyse

1. Neue Sheets: `mcu-ple-inference`, `mcu-connectome-graph` (A) + Applications
2. Reuse: `esp32-s3-silicon` (N16R8 / Tiering), `ssd1306-oled-ui` (SH1106/SSD1306)
3. Evidence an Commit `52ebcbb`; Host-Verify als Transfer-Muster
4. Eigene Board-Remessung = FOLLOW-ON, nicht Exit dieser Kampagne

## Offene Scope-Fragen

- Reicht ein gemeinsames „Flash-sparse-table“-Muster später als dritter Slug, oder bleiben PLE und Connectome getrennt? (vorerst getrennt)
- Barista asymmetrische Vocab/Head — eigenes A-Fallstrick-Muster oder nur Application?
