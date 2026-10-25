# Technology Sheet: MCU Connectome Graph

```yaml
slug: mcu-connectome-graph
title: MCU Connectome / Sparse Neural Graph
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

Nur Ebene **A**. Welche Neuronen/Escape-Regel, Board-Pins, Datenlizenz → Application B/C.  
Chip-Scope: große **Flash-Partition** + oft **PSRAM-Cache**; Ganzhirn oft **nicht** fit → Subgraph-Gate.

## Kurzfassung

Simulation eines **dünn besetzten neuronalen Graphs** (Connectome) auf einem MCU: Graph komprimiert in Flash, Blöcke in PSRAM gecacht, Schritt über alle Kanten (oft Dual-Core / SIMD). Verhalten kann aus verdrahteten Input-/Output-Neuronen kommen — ohne gelerntes Modell.

## Abgrenzung

- **Ist:** Sparse-Graph-Laufzeit + Kompression/Streaming auf MCU; feste Circuit-Maps (Inputs/Outputs/Thresholds).
- **Ist nicht:** LLM/PLE-Inference (`mcu-ple-inference`); Trainiertes RL/Policy-Netz; vollständige Organismus-Emulation ohne Budget-Gate.
- **Grenzt an:** Flash/PSRAM-Limits (`esp32-s3-silicon`); Demo-UI (`ssd1306-oled-ui`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Escape-/Demo-App, Serial | Sensor→Neuron→Motor-Mapping |
| unten | Flash-Partition (Graph), PSRAM-Cache, CPU SIMD | Blockweise Dekompression |
| lateral | Host Gold (Graph-Steps, Escape-Cases) | vor Flash |
| parallel | Attribution / Datenlizenz Upstream | Desk dokumentieren |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Ganzes Nervous System passt immer in 16 MB Flash | `REJECTED` | Upstream: lossless Whole > Restflash → Subgraph nötig |
| Demo-Verhalten = trainiertes Modell | `REJECTED` | Wiring + Threshold; nichts gelernt |
| Graph ohne Host-Gold flashen | `REJECTED` | Bundle-Hash / Gold-Gates |
| LLM-Runtime deckt Connectome ab | `REJECTED` | anderer Datenpfad / anderer Slug |
| Single-Core reicht „immer“ für Full-Step | `HYPOTHESIS` / Gate | Upstream nutzt Dual-Core + SIMD; Budget messen |

### Projektstart-Checkliste

- [ ] Flash-Rest vs. komprimierte Graph-Größe (Subgraph-Gate)
- [ ] Cache-Strategie PSRAM vs. Random-Flash
- [ ] Circuit-Datei: Inputs, Escape-Outputs, Thresholds
- [ ] Host-Verify / Gold vor Deploy
- [ ] Datenlizenz/Attribution der Connectome-Quelle
- [ ] Application + `seen_in`

## Transfer

Für Edge-Neuroscience-Demos und sparse Graph-Engines auf MCUs mit Flash-Lager. Nicht mit PLE-LLM-Inference vermischen.

## Referenzen

- Upstream-Pilot: [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) (`runtime/connectome_*.h`, `docs/fly-connectome/`)
- MaleCNS / fruit fly connectome — externe Datenquelle (Attribution im Projekt)

## Offene Fragen

- Welche Kompressions-/Blockgrößen auf anderen Flash-Controllern stabil sind?
- Wann SIMD-Assembly portabel vs. C-Fallback Pflicht ist?
