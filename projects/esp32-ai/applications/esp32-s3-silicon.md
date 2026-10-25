# Project Application: esp32-s3-silicon in esp32-ai

```yaml
project_id: esp32-ai
tech_slug: esp32-s3-silicon
status: active
sheet: ../../../technologies/esp32-s3-silicon/SHEET.md
audit: ../../../audits/esp32-ai-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

ESP32-S3 **N16R8** (16 MB Flash, 8 MB PSRAM) als Memory-Hierarchy-Träger für PLE-Table (Flash mmap), Head/Core (PSRAM) und Activations (SRAM). Bandwidth-Sketch misst PSRAM/SRAM/Flash-Random.

## Architektur / Datenfluss

```text
SRAM (hot acts/norms)
PSRAM (head / dense)
Flash mmap custom partition (PLE table / connectome)
  ← firmware/benchmarks/bandwidth (cycle counter)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/benchmarks/bandwidth/bandwidth.ino` | Hierarchy bandwidth |
| `firmware/*/partitions.csv` | Custom `model` / `flymodel` |
| README / RESULTS.md | N16R8 + Author-Messwerte |

## Konfiguration und Parameter

| Parameter | Upstream | Status |
|-----------|----------|--------|
| Board | ESP32-S3, 512 KB SRAM, 8 MB PSRAM, 16 MB Flash | `FACT` |
| Author PSRAM seq read | 60.7 MB/s | `FACT` (Desk, Upstream MEASURED) |
| Author Flash random 512 B row | 20.3 µs | `FACT` (Desk) |
| Sleep/USB-OTG Fokus | nicht genutzt (offline Demo) | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| N16R8 + three-tier accounting | `EVID-ESP32AI-2026-10-25-008` | `FACT` |
| Bandwidth sketch = Design-Gate für PLE | `EVID-ESP32AI-2026-10-25-003` | `FACT` |
| Eigene Remessung | — | `UNKNOWN` |

## Offene Fragen

- Octal-PSRAM Timing vs. hu-probe N8R2 (andere Modulklasse) — nur kontrastieren, nicht vermischen.
