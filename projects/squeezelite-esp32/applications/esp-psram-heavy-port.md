# Project Application: esp-psram-heavy-port in squeezelite-esp32

```yaml
project_id: squeezelite-esp32
tech_slug: esp-psram-heavy-port
status: active
sheet: ../../../technologies/esp-psram-heavy-port/SHEET.md
audit: ../../../audits/squeezelite-esp32-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle

Schwere Decode/Resample/EQ/Display-Last auf ESP32: **PSRAM Pflicht**, 240 MHz, internes 16-bit Core als Default-Budget; Display niedrigste Prio.

## Kontrast zu Doom-PoC

| | Doom PoC | Squeezelite |
|--|----------|-------------|
| Chip | Classic Wrover 2017 | Classic + S3 |
| Last | Game+FB | Decode+Net+UI |
| PSRAM | Game heap | Stream/decode buffers |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| ≥4 MB PSRAM; WROOM rejected; 240 MHz | `EVID-SQZ-2026-10-25-002` | `FACT` |
| Display can block high-rate FLAC | `EVID-SQZ-2026-10-25-005` | `FACT` |
