# Technology Sheet: MCU PLE LLM Inference

```yaml
slug: mcu-ple-inference
title: MCU PLE / Memory-Tiered LLM Inference
primary: D
tags: [esp32s3, arduino, lab-only, fragile]
type: pattern
status: active
seen_in: [esp32-ai]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/esp32-ai-2026-foreign
```

Nur Ebene **A**. Board-Pins, Sketch-Namen, HF-Artefakte → Application B/C.  
Chip-Scope: brauchbare **externe Flash-Partition** + oft **PSRAM**; Classic ohne PSRAM = Gate.

## Kurzfassung

On-Device-Sprachmodell-Inference auf einem MCU, bei der die meisten Parameter als **selten gelesene Lookup-Tabelle** in Flash liegen (Per-Layer Embeddings / PLE-Idee) und nur heiße Tensoren in SRAM/PSRAM wohnen. Große Matvecs (oft Output-Head) können über **beide Kerne** gesplittet werden. Ziel: große *gespeicherte* Parametermenge bei kleinem Fast-Memory-Budget — nicht Desktop-Capability.

## Abgrenzung

- **Ist:** Memory-Hierarchy-Split für LLM-Weights (Flash-sparse table + dichter Kern/Head); quantisierte Matvecs; Host-Golden vor Flash.
- **Ist nicht:** Cloud-/Server-Inference; Connectome-/Graph-Simulation (`mcu-connectome-graph`); generisches ML-Training; Hub/WiFi-Telemetrie.
- **Grenzt an:** Chip-/PSRAM-/Flash-Limits (`esp32-s3-silicon`); kleine OLED-UI (`ssd1306-oled-ui`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Prompt / Serial / optional Display | Token- oder Klassen-Stream |
| unten | Flash mmap / Custom Partition, PSRAM, SRAM | Tier nach Zugriffsfrequenz |
| lateral | Tokenizer / Vocab-Tabellen | oft generate Headers aus Artefakten |
| parallel | Dual-Core Matvec (große Zeilenblöcke) | kleine Tensoren oft Single-Core |
| parallel | Host-Verify gegen Golden | vor Deploy |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| „28.9M Parameter“ = 28.9M Dense-Compute-äquivalent | `REJECTED` | stored params; sparse table ≠ denser core |
| Flash-Tabelle dominiert per-token Zeit | `REJECTED` / Gate | Upstream-Bandbreite: wenige Random-Rows ≈ billig; Head-Scan teurer |
| Dual-Core ist optional Deko | `REJECTED` / Gate | Upstream: Head-Matvec Dual-Core war messbarer Hebel vor int8-Staging |
| Dual-Core ≡ SIMD-Assembly | `REJECTED` | Row-Split über Kerne ≠ Vector-SIMD; beides getrennt budgetieren |
| PLE ohne große Vocab-/Tabellen-Rows lohnt immer | `REJECTED` | Ablation: kleine Vocab → geringer/negativer Gain |
| Classic ESP32 ohne PSRAM = gleicher Port | `REJECTED` | Head/Core-Placement braucht Fast-Memory-Budget |
| Weights flashen ohne Host-Golden | `REJECTED` | Drift FW vs. Model → falsche Outputs |
| Asym. Output-Vocab (Klassen ≠ Input-IDs) ohne Mapping | `REJECTED` | Feedback braucht out→in; Boot-Guards |
| OLED/Connectivity nötig für Inference | `REJECTED` | Serial-only möglich; Display optional |

### Projektstart-Checkliste

- [ ] Flash-Budget für Table + App-Partition
- [ ] SRAM vs PSRAM: was ist hot (Acts/Norms) vs einmal/Token (Head)
- [ ] Große Matvecs: Dual-Core Row-Split vs. Single-Core-Fallback
- [ ] Quantisierungspfad (z. B. int4 + Scales) + Host-Verify
- [ ] Tokenizer/Vocab: tied Head vs. separate Output-Klassen
- [ ] Application + `seen_in`; keine Capability-Marketing-FACTs als A

## Transfer

Relevant für Edge-Demos, die **Flash als Parameter-Lager** nutzen und Fast-RAM nur für heiße Tensoren. Nicht still auf Server-LLM oder Connectome-Graph übertragen.

## Referenzen

- Google Gemma 3n — Per-Layer Embeddings (Konzept; externe Spec)
- Upstream-Pilot: [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) (`runtime/llm.h`, `RESULTS.md`)

## Offene Fragen

- Wann int8-Staging des Heads die Numerics/Latency-Tradeoffs rechtfertigt (zweites Upstream)?
- Welche Flash-Random-Latenz-Budgets andere MCUs brauchen?
