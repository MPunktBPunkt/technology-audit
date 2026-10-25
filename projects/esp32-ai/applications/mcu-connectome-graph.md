# Project Application: mcu-connectome-graph in esp32-ai

```yaml
project_id: esp32-ai
tech_slug: mcu-connectome-graph
status: active
sheet: ../../../technologies/mcu-connectome-graph/SHEET.md
audit: ../../../audits/esp32-ai-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle im Projekt

Subgraph der MaleCNS Fruit-Fly-Connectome (48 311 Neuronen, ~9.46M Verbindungen) auf ESP32-S3; Escape-Demo über verdrahtete Looming-/Giant-Fiber-Neuronen — **nichts trainiert**.

| Repo | Commit | Rolle |
|------|--------|-------|
| [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | `52ebcbb` | `esp32_fly` + connectome runtime |

## Architektur / Datenfluss

```text
connectome.fcl (flash `flymodel` @ 0x210000)
  + escape-circuit.json
  → host gold (graph steps + escape cases)
  → dual-core / SIMD step over edges
  → LC4/LPLC2 inputs ← spider size
  → DNp01/… escape outputs → OLED jump
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `runtime/connectome_codec.h`, `connectome_stream.h`, `connectome_fast.h` | Graph codec / stream |
| `firmware/esp32_fly/esp32_fly.ino` | Sketch |
| `firmware/esp32_fly/connectome_simd.S` | SIMD Kern |
| `firmware/esp32_fly/escape_*.h` | UI / World / App |
| `firmware/esp32_fly/MODEL_FORMATS.md`, `VERIFICATION.md` | Formate + Gates |
| `docs/fly-connectome/` | Attribution, Subgraph-Warum |

## Konfiguration und Parameter

| Parameter | Upstream (Desk) | Status |
|-----------|-----------------|--------|
| Neuronen / Kanten | 48 311 / 9 462 135 | `FACT` (README) |
| Graph in Flash | ~13.5 MiB compressed; PSRAM block cache | `FACT` (README) |
| Partition | `flymodel` @ `0x210000` | `FACT` (fly README) |
| Whole CNS | passt nicht (Upstream: ~24.49 MiB lossless vs. Restflash) | `FACT` (docs) |
| Training | none | `FACT` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Subgraph + Escape ohne Training; OLED Spider-Demo | `EVID-ESP32AI-2026-10-25-005` | `FACT` |
| Bundle/Gold vor Flash (`deploy.sh`, model_bundle.json) | `EVID-ESP32AI-2026-10-25-006` | `FACT` |
| Datenlizenz/Attribution dokumentiert | `EVID-ESP32AI-2026-10-25-007` | `FACT` |
| Eigene Lab-Escape-Timing-Messung | — | `UNKNOWN` |

## Offene Fragen

- C-Fallback vs. `connectome_simd.S` auf Non-S3?
